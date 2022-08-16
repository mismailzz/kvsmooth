#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Written by JM Lopez
# GitHub: https://github.com/jm66
# Email: jm@jmll.me
# Website: http://jose-manuel.me
#
# Note: Example code For testing purposes only
#
# This code has been released under the terms of the Apache-2.0 license
# http://opensource.org/licenses/Apache-2.0
#

import requests
from pyVmomi import vim
from tools import cli, tasks, pchelper, service_instance

# disable  urllib3 warnings
requests.packages.urllib3.disable_warnings(
    requests.packages.urllib3.exceptions.InsecureRequestWarning)


def get_hdd_prefix_label(language):
    language_prefix_label_mapper = {
        'English': 'Hard disk ',
        'Chinese': u'硬盘 '
    }
    return language_prefix_label_mapper.get(language)


def delete_virtual_disk(si, vm_obj, disk_number, language):
    """ Deletes virtual Disk based on disk number
    :param si: Service Instance
    :param vm_obj: Virtual Machine Object
    :param disk_number: Hard Disk Unit Number
    :param language: Vcenter API language
    :return: True if success
    """
    hdd_prefix_label = get_hdd_prefix_label(language)
    if not hdd_prefix_label:
        raise RuntimeError('Hdd prefix label could not be found')

    hdd_label = hdd_prefix_label + str(disk_number)
    virtual_hdd_device = None
    for dev in vm_obj.config.hardware.device:
        if isinstance(dev, vim.vm.device.VirtualDisk) \
                and dev.deviceInfo.label == hdd_label:
            virtual_hdd_device = dev
    if not virtual_hdd_device:
        raise RuntimeError('Virtual {} could not '
                           'be found.'.format(virtual_hdd_device))

    virtual_hdd_spec = vim.vm.device.VirtualDeviceSpec()
    virtual_hdd_spec.operation = \
        vim.vm.device.VirtualDeviceSpec.Operation.remove
    virtual_hdd_spec.device = virtual_hdd_device

    spec = vim.vm.ConfigSpec()
    spec.deviceChange = [virtual_hdd_spec]
    task = vm_obj.ReconfigVM_Task(spec=spec)
    tasks.wait_for_tasks(si, [task])
    return True


def main():
    parser = cli.Parser()
    parser.add_required_arguments(cli.Argument.VM_NAME)
    parser.add_custom_argument('--unitnumber', required=True,
                               help='HDD number to delete.', type=int)
    parser.add_custom_argument('--yes', help='Confirm disk deletion.', action='store_true')
    parser.add_custom_argument('--language', default='English', help='Language your vcenter used.')
    args = parser.get_args()
    si = service_instance.connect(args)

    content = si.RetrieveContent()
    print('Searching for VM {}'.format(args.vm_name))
    vm_obj = pchelper.get_obj(content, [vim.VirtualMachine], args.vm_name)

    if vm_obj:
        if not args.yes:
            cli.prompt_y_n_question("Are you sure you want "
                                    "to delete HDD "
                                    "{}?".format(args.unitnumber),
                                    default='no')
        delete_virtual_disk(si, vm_obj, args.unitnumber, args.language)
        print('VM HDD "{}" successfully deleted.'.format(args.unitnumber))
    else:
        print('VM not found')


# start
if __name__ == "__main__":
    main()


<br>

![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)
![forthebadge](https://forthebadge.com/images/badges/for-you.svg)
![](https://img.shields.io/badge/Excitement-High-red)
![](https://img.shields.io/badge/Maintained-Yes-indigo)
![](https://img.shields.io/badge/Pull_Requests-Accepting-yellow)
![](https://img.shields.io/badge/Contributions-Accepting-pink)

<br>



<br />
<p align="center">

  <h3 align="center">KvSmooth</h3>

  <p align="center">
    Patch Deployemnt for Linux Machines on ESXi VMware!
    <br />
    <a href="https://github.com/krvaibhaw/best-readme-template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/krvaibhaw/best-readme-template/issues">Report Bug</a>
    ·
    <a href="https://github.com/krvaibhaw/best-readme-template/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With Tools and Technologies</a></li>
      </ul>
    </li>
    <li><a href="#live-demo">Live Demo</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites/Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## About The Project

[![Product Name Screen Shot](preview/preview.png)](https://example.com)

KvSmooth comes to end with the idea of automating the tasks and getting the development knowledge of three-tier architechure applications. We also covered how the RESTFUL API framework works when we have to design the microservices architecture. Due to this, in the first place, the development was in the direction of Monolithic architecture and then gradually we move towards the Microservices architecture.

The problem that was selected for this learning is based on the real-world problem when we have to execute the script like bash etc on the Linux servers that are running over VMware ESXi hosts. We do have the solution of ansible or might be another CLI approach but it becomes user-friendly when we have the User Interface to deal with such tasks. By making the process smooth, we have given the name of KvSmooth.

We always appreciate your contribution and feedback.:smile: 

### Built With Tools and Technologies

* [Django](https://www.djangoproject.com/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)
* [Python](https://www.python.org)
* [VMware vSphere API Python Bindings](https://github.com/vmware/pyvmomi)
* [Python](https://www.python.org)
* [Bash](https://www.gnu.org/software/bash/)
* [Celery](https://docs.celeryq.dev/en/stable/)
* [Flower](https://flower.readthedocs.io/en/latest/)
* [Redis](https://redis.io/)
* [Docker](https://www.docker.com/)
* [Linux](https://www.linux.org/)


<!-- LIVE DEMO -->

## Live Demo

Added Soon - Inshallah

[Live Demo Link](https://example.com)


<!-- GETTING STARTED -->

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites/Installation

1. Clone the repo
   ```sh
   git clone https://github.com/mismailzz/kvsmooth.git
   ```
2. Build from docker-compose
   ```sh
   docker-compose build
   ```
3. Run the docker-compose file
   ```sh
   docker-compose up
   ```
   
<!-- ROADMAP -->

## Roadmap

    1. Created the CLI-based solution using Ansible
        1. It's able to resolve the problem as its run at once and ideally executes the patch over all VMs incrementally
        2. Limitations
            a. As it was not user friendly
            b. Tasks don't run async for multiple VMs on a single host
            c. Become hard to manage when multiple users want to use the Ansible playbook for different hosts
            d. There is no database for data persistency
            e. It's not time efficient
            f. Can't able to track the tasks they executed successfully or failed as we have to wait till the end for complete or partial execution of the script
    2. We learned the Django framework fundamentals
    3. Created the dashboard and run Ansible playbook in the backend
    4. Limitations of Monolithic architecture and Ansible playbook
    5. Learned the REST API Framework and 3-Tier Architecture
    6. Modified the "VMware vSphere API Python Bindings" scripts based on requirements
    7. Created the main and patch panel dashboard
    8. Integrated the Redis, Celery, and Flower - Asynchronous tasks and Monitoring
    9. Created Docker Compose file
    10. The final execution of the application based on microservices 3-tier architecture



<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->

## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

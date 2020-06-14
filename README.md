# SFIA2

The practical project for QA consulting.

## Index

1. [Brief](#Brief)
2. [Architecture](#Architecture)
3. [Risk Assessment](#Risk-Assessment)
4. [Deployment Activities](#Deployment)
5. [Testing](#Testing)
6. [Front End Design/Result](#Front-End-Design/Result)
7. [Workflow and Tools](#Workflow-and-Tools-Used)
8. [Future Improvements](#Improvements-to-Make-in-the-Future)
9. [Acknowledgements](#Acknowledgements)



## Brief

This project requires a set of 4 microservices which work with eachother using HTTP requests to achieve a single outcome on the front-end. The output data needs to be persisted and retrieved from the database onto a page so that previous outcomes can be viewed even after new ones are made. 

Docker needs to be used for containersiation with swarm and stack to load balance on another virtual machine(s). Jenkins must be used to perform Ansible configuration and deployment. 

## Architecture

I have used a simple database hosted on GCP which stores the outputs of my app each time the generate button is clicked. The data is then queried from this database and shown on the home page underneath the generator.

![Data Table](https://github.com/oskar951/SFIA2/blob/master/Images/Table.jpg)

The application consists of 4 services which break down the funcionality of the app.

**Service 1 -** This is the service which houses the HTML page that delivers the content and queries the database. It collects the data from service 4 and outputs the information to the user.  
  
**Service 2 -** Generates a random beginning for the username from a select list.  
  
**Service 3 -** Generates a random ending for the username from a select list.  
  
**service 4 -** Here is where the data from service 2 and 3 is requested and put together. Each ending of the username from service 3 corresponds to a certain group so this service follows rules to assign the usernames to those groups.


[Back to top](#Index)

### CI Pipeline
Here is my continuous integration and deployment pipeline 

![CI Pipeline](https://github.com/oskar951/Game-Review-Library/blob/master/Images/.jpg)

### Trello Project Tracking

Using Trello, I tracked my project along the way with a Kanban style board which allowed me to see my progress and things that need to be done. Here is the inital board:


![Trello Board](https://github.com/oskar951/SFIA2/blob/master/Images/Trello1.jpg)

This is my board throughout the project when some things were in progress and others ocmpleted. I also added bugs that I encountered.
![Trello Board](https://github.com/oskar951/SFIA2/blob/master/Images/Trello2.jpg)

In the final board everything is complete apart from the documentation to which I was adding finishing touches. The bugs have been solved and solutions were added to the description of the cards.
![Trello Board](https://github.com/oskar951/SFIA2/blob/master/Images/Trello3.jpg)

## Risk Assessment

In my risk assessment I have listed possible risks with the project. I added the risks cause and effect as well as the likelihood of it happening, this is then followed by a control measure which can help negate the risk and give it a lower likelihood and consequence. 

![Risk Assessment](https://github.com/oskar951/SFIA2/blob/master/Images/RiskAssessment1.jpg)

I then reviewed my risks towards the end of the project to see which control measures are implemented and whether I avoided those risks or not.

Here is my Risk Matrix with some of them added in:

![Risk Matrix](https://github.com/oskar951/SFIA2/blob/master/Images/RiskMatrix.jpg)

## Deployment

## Testing

I tested each service separately and made coverage reports for each one. I did not manage do do mock testing therefore service 1 and 4 is not up to 100%. Service 2 and 3 were covered to 100%, next time I would like to inlcude mock testing to allow for the responses from these services to be tested within service 4 and 1 so that they could also be fully covered.

### Service 1
![Service1 Test](https://github.com/oskar951/SFIA2/blob/master/Images/Cov0.jpg)

### Service 2
![Service2 Test](https://github.com/oskar951/SFIA2/blob/master/Images/Cov1.jpg)

### Service 3
![Service3 Test](https://github.com/oskar951/SFIA2/blob/master/Images/Cov2.jpg)

### Service 4
![Service4 Test](https://github.com/oskar951/SFIA2/blob/master/Images/Cov3.jpg)



## Front End Design/Result


![Home page wireframe](https://github.com/oskar951/Game-Review-Library/blob/master/Images/.jpg)
![Add review wireframe](https://github.com/oskar951/Game-Review-Library/blob/master/Images/.jpg)

### Front End Result


![Frontend](https://github.com/oskar951/SFIA2/blob/master/Images/Frontend.jpg)

[Back to top](#Index)

## Workflow and Tools Used

Here is a workflow for creating the app:

![WorkFlow](https://github.com/oskar951/Game-Review-Library/blob/master/Images/WorkFlow.jpg)

* SQL - Database service
* Python - Logic
* Flask - Front End (HTML)
* Jenkins - Continues Integration and Deployment server
* PyTest - Testing
* Git - Versions Control System
* Trello - Project Tracking
* GCP - Cloud Server
* Docker - Containerisation tool
* Docker Swarm - Container orchestration tool
* Ansible - Configuration and deployment tool
* NGINX - Reverse proxy web server

## Improvements to Make in the Future


## Acknowledgements

Thanks to the Trainers for the knowledge used to build and document this project.

Also thanks to my cohort for all learning together and being a great group.


**Written and Produced by** - *Oskaras Ceremnovas* 

##### Copyright (c)
*2020 QA Academy Training - All rights reserved*

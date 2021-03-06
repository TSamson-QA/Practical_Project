# Fundamental Project

## Table of Contents

 - [Brief](https://github.com/TSamson-QA/Practical_Project#brief)
 - [Scope](https://github.com/TSamson-QA/Practical_Project#scope)
 - [My Approach](https://github.com/TSamson-QA/Practical_Project#my-approach)
 - [CI/CD](https://github.com/TSamson-QA/Practical_Project#continuous-integration-and-deployment)
 - [Risk Assessment](https://github.com/TSamson-QA/Practical_Project/blob/main/README.md#risk-assessment)
 - [Jira Board](https://github.com/TSamson-QA/Practical_Project#jira-board)
 - [First Working Build](https://github.com/TSamson-QA/Practical_Project/blob/main/README.md#first-working-build)
 - [Second Working Build](https://github.com/TSamson-QA/Practical_Project/blob/main/README.md#second-working-build)
 - [Final Build](https://github.com/TSamson-QA/Practical_Project/blob/main/README.md#final-build)
 - [Test Results](https://github.com/TSamson-QA/Practical_Project/blob/main/README.md#test-results)
 - [Front-End Application](https://github.com/TSamson-QA/Practical_Project/blob/main/README.md#front-end-application)



## Brief: 
This project revolves around creating an application that generates “Objects” upon a set of predefined rules.
These “Objects” can be from whatever domain you wish. The project will utilise several different connected services and will require them to work together. 


## Scope:
The requirements of the project are as follows:

- An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.
- This could also provide a record of any issues or risks that you faced creating your project.
- An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
- If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
- The project must follow the Service-oriented architecture that has been asked for.
- The project must be deployed using containerisation and an orchestration tool.
- As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.
- The project must make use of a reverse proxy to make your application accessible to the user.

## My Approach:
For my approach, I decided to create an application to generate a D&D character, randomly generating a 'Class' and 'Race,' based on the Core rules. 
From these two Objects, a suggested Alignment will be generated. To achieve this, I have considered assigning numerical values to the Classes and Races and placing them in an Array.
Service 2 will select a random Class (and its assigned value). Service 3 will select a random Race (and its assigned value.)
Service 4 will then collect the values, and calculate an average, and output a suggested Alignment for your character based on the values assigned and the average of them.

## Continuous Integration and Deployment

The below diagram shows the implementation of a CI-CD pipeline, used to allow the automation of testing and building.

![CI-CD](https://github.com/TSamson-QA/Practical_Project/blob/main/images/CI-CD.png)

In order to follow this planned pipeline, a Jenkins pipeline was set up.

![Jenkins-Pipeline](https://github.com/TSamson-QA/Practical_Project/blob/main/images/Pipeline-Jenkins.PNG)

As the image shows, there are several key steps in the pipeline:
 1. Checkout SCM: Pulls the GitHub Repo.
 2. Requirements: Installs requirements.
 3. Test: Tests are completed and reports are generated in Jenkins.
 4. Build: Compiles and builds files into docker images.
 5. Push: Images are pushed on to docker swarm machines
 6. Configuration Management: Configures docker machines to ensure they are all capable of running application.
 7. Deploy: Environmental variables are set and the stack is deployed with the Docker-compose file.

## Risk Assessment

![Risk Assessment](https://github.com/TSamson-QA/Practical_Project/blob/main/images/risk-assessment.PNG)

## Jira Board
My first draft of my Jira board has the first issues that need to be addressed, as well as issues that will need to be worked on through the project.
You can find the link to the Jira Board [here.](https://ajcacademyproject.atlassian.net/jira/software/projects/PP/boards/7)

![Initial_Jira](https://github.com/TSamson-QA/Practical_Project/blob/main/images/jira-1.PNG)

## First Working Build
Version 1.0.0 contains all working services, all created on different branches and merged into my Dev branch for testing, and eventual deployment to Main when completed.
Service 2 and 3 use random.choice to select a random class and race, respectively, both using different ports, which is accessed by service 4. Service 4 collects the
random selections and from these, calculates a suggested Alignment. The class, race and alignment are then displayed on HTML. When the user refreshes the page,
a different selection of objects are visible.

![FWB Image](https://github.com/TSamson-QA/Practical_Project/blob/main/images/FWB_image.PNG)

All services are successfully deployed via Docker and Docker Compose on a virtual machine.
For the next build. I am planning to fully integrate SQL services to display a number of previous object sets that have been generated randomly. I have updated my jira board
based on this.

![FWB Jira](https://github.com/TSamson-QA/Practical_Project/blob/main/images/jira-2.PNG)

## Second Working Build
Version 1.1.0 fully integrates an SQL database in order to have data persistence. An ID number is generated, and a class, race and alignment is attached to the ID. This allows the user to view the previous 5 generated characters.

![WB2 image](https://github.com/TSamson-QA/Practical_Project/blob/main/images/WB2_image.PNG)

Now that SQL has been fully integrated, the Jira board has been updated in accordance to this. Next to be added is Jenkins.

![Jira3](https://github.com/TSamson-QA/Practical_Project/blob/main/images/jira-3.PNG)

## Final Build
The final version of my application has fully integrated Jenkins, NGINX, Ansible, and Docker Swarm into it. The application is fully built, tested and deployed within Jenkins, as previously shown [here](https://github.com/TSamson-QA/Practical_Project#continuous-integration-and-deployment).

While I am able to have the application deployed through Jenkins, there are, however, issues connecting to Service-4 through port 5003.

![ConnectionError](https://github.com/TSamson-QA/Practical_Project/blob/main/images/error.PNG)

Due to this error, which I was unable to fix, the application cannot be used as intended, as the final service cannot be ran this way, despite previously being ran on a local machine. For this reason, I do not think it is a problem within the logic of the program. I believe this is the line that is causing an issue:

![Error-Line](https://github.com/TSamson-QA/Practical_Project/blob/main/images/error-line.PNG)

The marked line causes the failure, despite me ensuring that all elements were names correctly, including the requests HTTP. Due to this, I ensure that there was a backup I could use, as seen commented. This line sets the alignment manually, allowing the application to run, generating a random class and race as expected, but setting the alignment as True Neutral.

Below are images showing the status of NGINX and Docker services, showing that all services are running.

![Docker-Service](https://github.com/TSamson-QA/Practical_Project/blob/main/images/docker-service.png)

Through Jenkins, The server, class_api, race_api and alignment_api have all been started and are running correctly.

![NGINX-Service](https://github.com/TSamson-QA/Practical_Project/blob/main/images/nginx-service.PNG)

The NGINX service, used for load balancing has been started and is running as planned.

![Swarm-Nodes](https://github.com/TSamson-QA/Practical_Project/blob/main/images/swarm-nodes.PNG)

Here, you can see the Manager and Worker-1 nodes running properly in Swarm.

## Test Results

Through Jenkins, I was able to automate testing of the different APIs using Pytest.

![Class-test](https://github.com/TSamson-QA/Practical_Project/blob/main/images/class-test.PNG)

The class test chooses one of the classes from the selection and tests the output of it. I used a for loop to iterate this test 20 times for increased accuracy.

![race-test](https://github.com/TSamson-QA/Practical_Project/blob/main/images/race_test.PNG)

Just like the class testing, a race is selected and the output of it is tested. This test is again repeated 20 times.

![align-test](https://github.com/TSamson-QA/Practical_Project/blob/main/images/align-test.PNG)

In the alignment test, an error is thrown. This may be related to the application not working as intended and the test may be failing for the same reason. There is 100% coverage for all the tests, but only the alignment one fails.

## Front-End Application

![Front-end](https://github.com/TSamson-QA/Practical_Project/blob/main/images/final_app.PNG)

The front end of the app works as planned (except the problem with the alignment.) A race and class is randomly selected and output. A alignment would usually be calculated here, but due to the error previously mentioned, I manually set it to "True Neutral" in order for the application to function. All of these results are then stored in a database, and the previous 5 results are displayed, being pulled from the database.



# Fundamental Project

## Table of Contents

 - [Brief](https://github.com/TSamson-QA/Practical_Project#brief)
 - [Scope](https://github.com/TSamson-QA/Practical_Project#scope)
 - [My Approach](https://github.com/TSamson-QA/Practical_Project#my-approach)
 - [Jira Board](https://github.com/TSamson-QA/Practical_Project#jira-board)
 - [First Working Build](https://github.com/TSamson-QA/Practical_Project/blob/main/README.md#first-working-build)



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

## Jira Board
My first draft of my Jira board has the first issues that need to be addressed, as well as issues that will need to be worked on through the project.
You can find the link to the Jira Board [here.](https://ajcacademyproject.atlassian.net/jira/software/projects/PP/boards/7)




![Initial_Jira](https://github.com/TSamson-QA/Practical_Project/blob/main/images/jira-1.PNG)



## First Working Build
Version 1.0.0 contains all working services, all created on different branches and merged into my Dev branch for testing, and eventual deployment to Main when completed.
Service 2 and 3 use random.choice to select a random class and race, respectively, both using different ports, which is accessed by service 4. Service 4 collects the
random selections and from these, calculates a suggested Alignment. The class, race and alignment are then displayed on HTML. When the user refreshes the page,
a different selection of objects are visible.

All services are successfully deployed via Docker and Docker Compose on a virtual machine.
For the next build. I am planning to fully integrate SQL services to display a number of previous object sets that have been generated randomly. I have updated my jira board
based on this.



![FWD Jira](https://github.com/TSamson-QA/Practical_Project/blob/main/images/jira-2.PNG)



# INTEGRATE SQL



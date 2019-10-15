# School of Computing &mdash; Year 4 Project Proposal Form

## SECTION A

|                     |                   |
|---------------------|-------------------|
|Project Title:       | IOT Smart Garden  |
|Student 1 Name:      | Jacob Byrne       |
|Student 1 ID:        | 15492172          |
|Student 2 Name:      | Daniel Pereira    |
|Student 2 ID:        | 15364491          |
|Project Supervisor:  | xxxxxx            |

> Ensure that the Supervisor formally agrees to supervise your project; this is only recognised once the
> Supervisor assigns herself/himself via the project Dashboard.
>
> Project proposals without an assigned
> Supervisor will not be accepted for presentation to the Approval Panel.

## SECTION B

> Guidance: This document is expected to be approximately 3 pages in length, but it can exceed this page limit.
> It is also permissible to carry forward content from this proposal to your later documents (e.g. functional
> specification) as appropriate.
>
> Your proposal must include *at least* the following sections.


### Introduction

> Describe the general area covered by the project.

Our idea for our Final Year Project is to create a Smart Garden. This will allow us to create an environment for plants to grow without any need to look after them.
Users will have the option to take full control at any time or leave the garden as is without any input as the garden will maintain as ideal conditions as possible for the plant to survive. 
Our Final year project will involve monitoring the conditions of potted plants and then remotely supplying the plants with whatever they need. 
For monitoring the plants we will install sensors that pick up on the different elements of the environment. 
The data will be pushed to our database where It can be displayed to a user. The info the user sees can be up to date and can also show the history from the stored data. 

Along with monitoring the plants we are going to add remotely controlled heat; light & water sources. These environment altering sources will be controlled from the server. 
A user can choose to push a command, or alternatively a user can leave it up to the server to make a calculated decision based on data, to then send commands.

### Outline

> Outline the proposed project.
Our idea for our Final Year Project is to create a Smart Garden. This will allow us to create an environment for plants to grow without any need to look after them.
Users will have the option to take full control at any time or leave the garden as is without any input as the garden will maintain as ideal conditions as possible for the plant to survive. 

In order to do this we will have 2 sides to the project. One which encompasses controlling the environment through a web based UI, with the other side being the mechanism through which we can get data about the plant environment and alter the plant environment by the application of heat, light etc. 

The front end will be hosted on an AWS EC2 instance, here the user will be able to sign in to the UI and see various parameters about the plant on a custom Dashboard as well as view historical data, alter the plant environment and switch from automated plant monitoring to manual. 

This same server will be able to communicate with the mechanism for monitoring the plant and getting feedback from the plant environment, a network enabled raspberry pi that takes readings from light, heat, soil PH and moisture sensors placed in the plants environment. 
This data will be viewable on the dashboard as well as looking at historical data. 


### Background

> Where did the ideas come from?

We had the idea over our INTRA placement. The idea came from a project seen during work experience and noting that a house plant had died during the summer when we were away. 
The idea came to us as we wanted a way to be able to be away from home for extended periods of time and not need to worry about house plants. 

### Achievements

> What functions will the project provide? Who will the users be?

The project will allow users to ensure house plants to be looked after without the need for constant maintenance. 
Users will be anyone who is interested in maintaining house plants. The nature of the project is to be able to scale to multiple plants with the possibility of using larger water pumps, multiple sensors etc. to be enabled for much larger environments such as green houses. 


### Justification

> Why/when/where/how will it be useful?

This project will be extremely useful to anyone who likes to maintain house plants that are interested in travelling for example or who are away from home for extended periods of time. 
As the nature of this project is a Proof of Concept, the system will have the potential to scale to support multiple plants in a larger environment if necessary. 
This project also has implications for users with disabilities that impact motor skills for example. With this system users who are interested in keeping house plants that don't 
necessarily have the means to perform maintenance on said plants, the system we plan to build will be ideal. 

### Programming language(s)

> List the proposed language(s) to be used.

1. Python
2. Javascript(Node) 
3. Bash 
4. AWS SDK for Python and Node 

### Programming tools / Tech stack

> Describe the compiler, database, web server, etc., and any other software tools you plan to use.

We are hoping to use the following to implement our project. 
1. AWS EC2 for server running nginx with a custom-built UI to interface with the Smart Garden
2. Python to implement backend and aws greengrass to communicate with raspberry pi
3. AWS SDK for Python, Javascript, CLI 
4. Apache/Flask/Nginx
5. Database


### Hardware
> Describe any non-standard hardware components which will be required.

1. Servo to turn on/off pump
2. Temperature sensor in soil 
3. PH level sensor for soil
4. Soil moisture level 


### Learning Challenges

> List the main new things (technologies, languages, tools, etc) that you will have to learn.

1. Working with IOT 
    IOT is something we haven’t touched off during our time in University, it will be a steep learning curve getting the network PI up and running and getting it to communicate with EC2 server.
2. Dashboard building 
    Our project will involve graphically displaying a certain portion of historical data as well as analysing current data visually. This will involve core web-design principles as well as accessibility as the user base 
    may include users with impacted motor skills for example as mentioned in the 'Justificion' portion of our proposal. 


### Breakdown of work

> Clearly identify who will undertake which parts of the project.
>
> It must be clear from the explanation of this breakdown of work both that each student is responsible for
> separate, clearly-defined tasks, and that those responsibilities substantially cover all of the work required
> for the project.

#### Student 1

> *Student 1 should complete this section.*

#### Student 2

> *Student 2 should complete this section.

Daniel will be assembling and coding the Raspberry Pi. This includes how the pi gathers data from each of it’s sensors and then sends them off to the EC2 server. He will also be responsible for how the pi receives server commands and outputs them to different accessories (light, heat, water)....

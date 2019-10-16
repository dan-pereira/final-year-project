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

## SECTION B

### Introduction

Our idea for our Final Year Project is to create an IOT based Smart Garden. This will allow us to monitor and influence an environment for plants to grow in without the high maintenance normally associated with plant care.
Users will have the option to take full control at any time or leave the garden as is without any input as the Smart  Garden will maintain as close to ideal conditions as possible for the plant to survive.
Our Final year project will involve monitoring the conditions of potted plants and then remotely supplying the plants with what they need.
For monitoring the plants we will install sensors that pick up on the different elements of the environment.
The data will be pushed to our database where It can be displayed to a user. The info the user sees can be up to date and can also show the history from the stored data.

Along with monitoring the plants we are going to add remotely controlled heat; light & water sources. These environment altering sources will be controlled from the server.
A user can choose to push a command which will manually change the environment, or alternatively a user can leave it up to the server to make a calculated decision based on data, to then send commands.

### Outline

Our idea for our Final Year Project is to create a Smart Garden. This will allow us to create an environment for plants to grow without any need to look after them.
Users will have the option to take full control at any time or leave the garden as is without any input as the garden will maintain as ideal conditions as possible for the plant to survive.

In order to do this we will have 2 sides to the project. One which encompasses controlling the environment behind a web based UI, with the other side being the mechanism through which we can get data about the plant environment and alter the plant environment by the application of heat, light etc.

The front end will be hosted on an AWS EC2 instance, here the user will be able to sign in to the UI and see various parameters about the plant on a custom Dashboard as well as view historical data, alter the plant environment and switch from automated plant monitoring to manual.

This same server will be able to communicate with the mechanism for monitoring the plant and getting feedback from the plant environment, a network enabled raspberry pi that takes readings from light, heat, soil PH and moisture sensors placed in the plants environment.
This data will be viewable on the dashboard as well as looking at historical data.


### Background

We had the idea over our INTRA placement. The idea came from a project seen during work experience and noting that a house plant had died during the summer when we were away.
The idea came to us as we wanted a way to be able to be away from home for extended periods of time (travelling, working etc.) and not need to worry about plants at home. 


### Achievements

The project will allow users to ensure house plants to be looked after without the need for constant maintenance.
Our array of sensors (heat, light, soil temp/moisture, humidity etc.) will ensure that the plants are kept in the ideal range of conditions for successful growth. The proof of concept will show that it is feasible for larger environments. A project of this scale could also have massive applications for motor impaired users who are interested in maintaining house plants but may not necessarily have the means to do so. 
Users will be anyone who is interested in maintaining house plants. The nature of the project is to be able to scale to multiple plants with the possibility of using larger water pumps, multiple sensors etc. to be enabled for much larger environments such as green houses.


### Justification

This project will be extremely useful to anyone who likes to maintain house plants that are interested in travelling, for example or who are away from home for extended periods of time.
As the nature of this project is a Proof of Concept, the system will have the potential to scale to support multiple plants in a larger environment if necessary.
This project also has implications for users with disabilities that impact motor skills for example. With this system users who are interested in keeping house plants that don't
necessarily have the means to perform maintenance on said plants, the system we plan to build will be ideal.
The Botanic Gardens in Glasnevin have also expressed interest in the project and even gone as far as to offer us a place to work for the duration of our project. Our market research with the greenhouse team on the botanic garden campus lead us to believe that while there are mechanisms in place of monitoring certain parameters there is scope for what we plan to implement on a small and large scale as the system will allow them to bring this monitoring into one package rather than correlating multiple, disjointed sources of information on the plants they keep. 

### Programming language(s)

1. Python
2. Javascript(Node)
3. Bash
4. AWS SDK for Python and Node

### Programming tools / Tech stack

We are hoping to use the following to implement our project.
1. AWS EC2 for server running nginx with a custom-built UI to interface with the Smart Garden
2. Python to implement backend and aws greengrass to communicate with raspberry pi
3. AWS SDK for Python, Javascript, CLI
4. Apache/Flask/Nginx
5. Database


### Hardware

1. Raspberry Pi
2. Servo to turn on/off pump
3. Temperature sensor in soil
4. PH level sensor for soil
5. Soil moisture level


### Learning Challenges

> List the main new things (technologies, languages, tools, etc) that you will have to learn.

1. Working with IOT
   * IOT is something we haven’t touched off during our time in University, it will be a steep learning curve getting the network PI up and running and getting it to communicate with EC2 server.
2. Dashboard building
   * Our project will involve graphically displaying a certain portion of historical data as well as analysing current data visually. This will involve core web-design principles as well as accessibility as the user base
   may include users with impacted motor skills for example as mentioned in the 'Justificion' portion of our proposal.


### Breakdown of work

#### Student 1

Due to familiarity with AWS and design Jacob will be taking the building, configuration and deployment of our host server as well as configuring how the host server for the front end(dashboard) will interact with the raspberry pi and grab information from it accordingly through a custom API built by both students allowing communication between the two platforms. He will also be responsible for the deployment of our dashboard. This will encompass the security of sign-in and out for our end users as well as the design and implementation of the display of historical plant data. For the purposes of testing this will be pre-populated in the beginning and will be replaced with real data once we have had sufficient time to gather appropriate data from various sensors throwing information from the back end.
Jacob will also build the notification system we plan to implement. This feature will let the user know (when automated mode is off) whether the plant needs attention and if so what attention is required to bring the plant back to acceptable levels as defined for each plant. 

#### Student 2

Daniel will be assembling and coding the Raspberry Pi. There are 2 main functions of the pi from a software perspective, the first being fetching data from the environment. Each of the individual sensors will have to be accounted, interpreted and restructured into a suitable format. Using web requests the pi will then be programmed to push this data to the EC2 server. 
The second function of the pi will be to perform as a restful server waiting for inputs from the EC2 server. Daniel will program the pi to receive any information from the server … will be converted to send commands to the individual controllers (water light, heat). 

#### Collaboration

Due to the nature of the user interface dashboard work it involves. Both students have decided to work on this part together. While all of our project will need lots of communication to accomplish, we feel that collaborating on this specific section of the project will allow us to overcome the task with greater efficiency. This will also entail the development of the Analytics side of the dashboard where users will be able to graphically view historical data in graph form. This data will be retrieved from a SQL/NoSQL database and collected/updated in real time. 

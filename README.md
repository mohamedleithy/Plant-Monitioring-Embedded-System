# Plant-Monitioring-Embedded-System

## Table of contents

* [Introduction ](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#-introduction)
* [Background and Motivation](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#Background-and-Motivation)
* [Problem Statement](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#problem-statement)
* [Solution](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#solution)
* [Features](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#features)
* [Scale of the project](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#scale-of-the-project)
* [Architecture](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#architecture)
* [Iterations](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#Iterations)
* [Benefits](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#benefits)
* [Dashboard](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#dashboard)
* [Conclusion and Future Work](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#Conclusion-and-Future-Work)
* [Demo video](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#Demo-video)
* [Authors](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#authors)
* [Limitations](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#limitations)
* [Supervisor](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#supervisor)

# Introduction

Plant monitoring is a fundamental component of agriculture industries since it allows for controlling the growth of plants for the best possible output. Automating the process of plant monitoring and managing the environmental factors will ease the complexity of such process and will influence the growth of the plant and, consequently, its output. In this proposal a plant monitoring system is presented to provide feedback for the user on a web app. The proposal includes a detailed description of the problem, architecture of the system and the components used.

# Background and Motivation

After skimming through the past projects, we found a past project that used sensors to record the temperature,humidty and soil mositure. We then decided we can improve on this project by actuating on these sensor readings in negative feedback loop. By doing so, we would provide a given plant with the optimial needed conditions (soil mositure) and automate the process of watering. 


# Problem Statement

We are addressing two problems:

* The water waste introduced by the classical agricultural techniques.
* The high running cost of the agricultural sites workers.

# Solution

Designing an embedded system with a negative feedback loop to efficiently monitor and control agricultural sites. The system will monitor the environment by deploying sensors that keep track of the temperature, humidity, and soil moisture level, to regulate the soil water level using an electronically controlled water valve. An online dashboard will be integrated into the system to report updates on the agricultural site.

# Requirmenets and Features

* The user will be able to select his/her plant type through the web interface, and the soil moisture level is specified accordingly
* The system will be able to monitor the temperature and soil moisture level.
* The system will be able to control the water level in the soil.
* The system will be able to modify the soil moisture level, based on the temprature. 
* The system will be able to report updates on the environment to the user.

# Scale of the project

* The system will be able to monitor indoor plants on a small scale, prototype is made on two average sized plant pots.


# Architecture

## Software architecture design

For the STM board:
We designed our embedded system to used FreeRTOS to coordinate its different tasks. The use of FreeRTOS was essential to allow parallel execution of the tasks in a real-time fashion. Moreover, the use of interrupts opened the door for handling aperiodic tasks in the system, and data racing conditions were handled using semaphores. 

For the raspberry pi pico:
Here we used a multithreaded architecture to allow the blocking of synchronous receiving and sending of the server. The python _thread library was used to generate a couple of threads that separately handle the sockets operations and the UART communication with the STM board.

## Hardware architecture design

### Block Diagram

<img src = "https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System/blob/main/docs/images/Block_Diagram.png" alt="Block Diagram" width="700"/>

### System Components

 * NUCLEO LC432K 
 * Raspberry pi pico 
 * Water Valve
 * Humidity Sensor
 * Temperature Sensor (DS3231 RTC)
 * Mositure Sensor 


#### NUCLEO LC432K
<img src = "https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System/blob/main/docs/images/NUCLEO_LC432K.PNG" alt="NUCLEO LC432K" width="300"/>

#### Raspberry pi pico

<img src = "https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System/blob/main/docs/images/raspberry_pi_pico.png" alt="ESP32" width="300"/>

#### Water Valve

<img src = "https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System/blob/main/docs/images/Water_valve.PNG" alt="Water Valve" width="300"/>


#### Relay

<img src = "https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System/blob/main/docs/images/relay.jpg" alt="Relay" width="300"/>

#### Temperature Sensor


<img src = "https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System/blob/main/docs/images/Temperature_Sensor.PNG" alt="Temperature Sensor" width="300"/>

#### Mositure Sensor

<img src = "https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System/blob/main/docs/images/Mositure_Sensor.PNG" alt="Mositure Sensor" width="300"/>

### Connections:

* Deploy the STM board on the breadboard
* Deploy the Raspberry Pi Pico board on the breadboard
* Connect the two microcontrollers together via UART serial connection
* Connect the temprature sensor to the STM board using i2c synchronous connection
* Connect the 2 moisture sensor to the STM board using built in ADC on two seperate channels
* Connect each 12V supply to relay, connect relay output to the water valves
* Connect GPIO Pins to designated relay.


<img src = "https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System/blob/main/docs/images/Breadboard.jpg" alt="Breadboard Image" width="600"/>


<img src = "https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System/blob/main/docs/images/Connections.jpg" alt="Connection Image" width="600"/>



# Iterations

## First phase

Deployed STM and connected it to soil moisture and temperature sensor. 
Deployed ESP32 and connected it to humidty sensor.
Displayed Readings on Dashboard via Build-in Arudino APIs.

## Second phase

Removed ESP32 and deployed Raspberry Pico Pi.
Implemented User Interface via HTML, and intergrated front-end with Raspberry Pico Pi python back-end.

# Benefits

## Automation 
This embedded system would automate the process of watering plants, thus removing the need for human intervention on a daily basis resulting in error-free result in comparison to human labor, increasing consistency and reducing costs. 
## Real Time Display
With the use of the dashboard the user would be able to view the the real-time temperature, humidity and moisture directly through his/her phone/Desktop and get notified through telegram mobile application when any of the parameters approaches its threshold. 
## Set Optimal Conditions 
Given the monitored parameters, the system is able to water the plant and provide it with its optimal ecosystem that are predefined for a certain plant species to allow maximizing the plants’ growth and yield.

# Conlusion and Future Work

## Conclusion

it can be concluded that the system implemented successfully reads the soil moisture of plants and waters the plants accordingly. This system can be an effective solution for maintaining optimal soil moisture levels for plants, which is important for their health and growth. It can potentially save time and effort for gardeners and farmers by automating the watering process, and it may also help to conserve water by avoiding over-watering or under-watering. Overall, the implementation of this system appears to be a useful tool for the care and maintenance of plants.

## Future Work
* Adding additional sensors: The system could be enhanced with additional sensors to monitor other factors that may impact plant growth and health, such as light levels or nutrient levels in the soil.
* Expanding the watering capabilities: The system could be designed to support larger water bottles or to incorporate additional watering methods, such as a drip irrigation system or a spray system. This could allow the system to water plants more efficiently and effectively, particularly for larger grow areas or for plants with different watering needs.
* Improving the water bottle filling process: The system could be enhanced to make the process of filling the water bottles more efficient and convenient, potentially through the use of a water pump or other automation techniques.

# Dashboard

<img src = "https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System/blob/main/docs/images/dashboard.png" alt="Dashboard Image" width="600"/>

<img src = "https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System/blob/main/docs/images/dashboard2.png" alt="Dashboard Image 2" width="600"/>

# Project Progress and Demo video

The system is now able to monitor the soil moisture level in two average sized plant pots, along with the temperature, and accordingly switch on/off the relay that controls the water solenoids attached to the water source. 

[Demo1 video link](https://drive.google.com/file/d/1defMuau6kGnW1_lsAHdz8Dkl8jO6r3im/view?usp=sharing)




# Limitations

* Our system handles no more than 6 pots.
* Distance limitation because the digital signal received by the ADC will catch a lot of noise
* The system is very expensive due to the cost of the components compared to the scale
* The system does not handle failures
    * Over-watering 
    * Does not troubleshoot technical issues in sensors
    * Force quit the system when a technical issue happens


# Model of the system


<img src = "https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System/blob/main/docs/images/Base.JPG" alt="Dashboard Image" width="600"/>

<img src = "https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System/blob/main/docs/images/Cap.JPG" alt="Dashboard Image" width="600"/>

<img src = "https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System/blob/main/docs/images/rod.JPG" alt="Dashboard Image" width="600"/>

<img src = "https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System/blob/main/docs/images/Bottle.JPG" alt="Dashboard Image" width="600"/>


# Authors

* [Mohamed Nasr](https://github.com/mnassr1658)
* [Mohamed Eleithy](https://github.com/mohamedleithy)
* [Abdullah Nashat](https://github.com/n42at)
* [Youssef Kandil](https://github.com/kanndil)


# Supervisor

* [Mohamed Shalan](https://github.com/shalan)
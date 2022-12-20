# Plant-Monitioring-Embedded-System



## Table of contents

* [Introduction ](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#-introduction)
* [Background-and-Motivation](https://github.com/mohamedleithy/  Plant-Monitioring-Embedded-System#Background-and-Motivation)
* [Problem Statement](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#problem-statement)
* [Solution](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#solution)
* [Features](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#features)
* [Scale of the project](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#scale-of-the-project)
* [Architecture and Components](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#architecture-and-components)
* [Iterations](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#Iterations)
* [Benefits](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#benefits)
* [Dashboard](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#dashboard)
* [Connections](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#connections)
* [Demo video](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#Demo-video)
* [Authors](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#authors)
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

# Features

* The system will be able to monitor the temperature, humidity, and soil moisture level.
* The system will be able to control the water level in the soil.
* The system will be able to report updates on the environment to the user.

# Scale of the project

* The system will be able to monitor indoor plants on a small scale.









# Architecture and Components

## Required System Components

 * NUCLEO LC432K 
 * ESP32 
 * Water Valve
 * Humidity Sensor
 * Temperature Sensor (DS3231 RTC)
 * Mositure Sensor 


#### NUCLEO LC432K
<img src = "https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System/blob/93f90ed9ca5239e1ea5cceff654c46a319e15414/docs/images/NUCLEO_LC432K.PNG" alt="NUCLEO LC432K" width="300"/>

#### ESP32

<img src = "https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System/blob/afb314276207133cf847639b5021b7976e6eaa1d/docs/images/ESP32.PNG" alt="ESP32" width="300"/>

#### Water Valve

<img src = "https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System/blob/afb314276207133cf847639b5021b7976e6eaa1d/docs/images/Water_valve.PNG" alt="Water Valve" width="300"/>


#### Relay

<img src = "https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System/blob/afb314276207133cf847639b5021b7976e6eaa1d/docs/images/relay.jpg" alt="Water Valve" width="300"/>

#### Temperature Sensor


<img src = "https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System/blob/348df613407bbbb6691643846078791d8085499f/docs/images/Temperature_Sensor.PNG" alt="Temperature Sensor" width="300"/>

#### Mositure Sensor

<img src = "https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System/blob/d4f8a01b7df9d3efa0aec967675b00e0a9128026/docs/images/Mositure_Sensor.PNG" alt="Mositure Sensor" width="300"/>


## Architecture

#### Block Diagram

<img src = "https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System/blob/348df613407bbbb6691643846078791d8085499f/docs/images/Block_diagram_updated.png" alt="Block Diagram" width="700"/>


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
# Dashboard

<img src = "https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System/blob/main/docs/images/dashboard.png" alt="Dashboard Image" width="600"/>


# Connections:

* Deploy the STM board on the breadboard
* Deploy the Raspberry Pi Pico board on the breadboard
* Connect the two microcontrollers together via UART serial connection
* Connect the temprature sensor to the STM board using i2c synchronous connection
* Connect the 2 moisture sensor to the STM board using built in ADC on two seperate channels
* Connect each 12V supply to relay, connect relay output to the water valves
* Connect GPIO Pins to designated relay.


<img src = "https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System/blob/main/docs/images/Breadboard.png" alt="Breadboard Image" width="600"/>


<img src = "https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System/blob/main/docs/images/Connections.png" alt="Connection Image" width="600"/>




# Demo video

[Demo1 video link](https://drive.google.com/file/d/1defMuau6kGnW1_lsAHdz8Dkl8jO6r3im/view?usp=sharing)



# Authors

* [Mohamed Nasr](https://github.com/mnassr1658)
* [Mohamed Eleithy](https://github.com/mohamedleithy)
* [Abdullah Nashat](https://github.com/n42at)
* [Youssef Kandil](https://github.com/kanndil)


# Supervisor

* [Mohamed Shalan](https://github.com/shalan)
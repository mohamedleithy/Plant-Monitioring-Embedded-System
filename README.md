# Plant-Monitioring-Embedded-System



## Table of contents

* [Introduction ](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#-introduction)
* [Problem Statement](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#-file-structure)
* [Solution](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#-file-structure)
* [Architecture and Components ](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#--dependencies)
* [Benefits ](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#-how-it-works)
* [Dashboard ](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#-how-to-use)

* [Authors](https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System#-authors)
<!--* [Copyright and Licensing](https://github.com/kanndil/Lighter#%EF%B8%8F-copyright-and-licensing)-->

# 📖 Introduction

Plant monitoring is a crucial component of agriculture industries since it allows for the controlled climatic growth of plants for the best possible output. Automating a plant's monitoring and management of the environmental factors that either directly or indirectly influence the growth of the plant and, consequently, its output will ease the complexity of the process. In this proposal a plant monitoring system technology system is presented to provide feedback on a web app the proposal includes a detailed description of the problem, architecture of the system and the components used.

# Problem Statement

We are addressing two problems:

* The water waste introduced by the classical agricultural techniques.
* The high running cost of the agricultural sites workers.

# Solution

Designing an embedded system with a negative feedback loop to efficiently monitor and control agricultural sites. The system will monitor the environment by deploying sensors that keep track of the temperature, humidity, and soil moisture level, to regulate the soil water level using an electronically controlled water valve. An online dashboard will be integrated into the system to report updates on the agricultural site.


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

#### Humidity Sensor

<img src = "https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System/blob/d4f8a01b7df9d3efa0aec967675b00e0a9128026/docs/images/Humidity_Sensor.PNG" alt="Humidity Sensor" width="300"/>

#### Temperature Sensor


<img src = "https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System/blob/348df613407bbbb6691643846078791d8085499f/docs/images/Temperature_Sensor.PNG" alt="Temperature Sensor" width="300"/>

#### Mositure Sensor

<img src = "https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System/blob/d4f8a01b7df9d3efa0aec967675b00e0a9128026/docs/images/Mositure_Sensor.PNG" alt="Mositure Sensor" width="300"/>


## Architecture

#### Block Diagram

<img src = "https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System/blob/348df613407bbbb6691643846078791d8085499f/docs/images/Block_Diagram.png" alt="Block Diagram" width="700"/>





# Benefits

## Automation 
This embedded system would automate the process of watering plants, thus removing the need for human intervention on a daily basis resulting in error-free result in comparison to human labor, increasing consistency and reducing costs. 
## Real Time Display
With the use of the dashboard the user would be able to view the the real-time temperature, humidity and moisture directly through his/her phone/Desktop and get notified through telegram mobile application when any of the parameters approaches its threshold. 
## Set Optimal Conditions 
Given the monitored parameters, the system is able to water the plant and provide it with its optimal ecosystem that are predefined for a certain plant species to allow maximizing the plants’ growth and yield.
# Dashboard

<img src = "https://github.com/mohamedleithy/Plant-Monitioring-Embedded-System/blob/main/docs/images/dashboard.png" alt="Dashboard Image" width="600"/>

# Authors

* [Mohamed Nasr](https://github.com/mnassr1658)
* [Mohamed Eleithy](https://github.com/mohamedleithy)
* [Abdullah Nashat](https://github.com/n42at)
* [Youssef Kandil](https://github.com/kanndil)


# Supervisor

* [Mohamed Shalan](https://github.com/shalan)
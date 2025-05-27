
## Overview
This repo contains the work for a traffic management system designed to classify and detect traffic levels in real-time using machine learning and computer vision techniques, tested and validated through simulations in SUMO (Simulation of Urban Mobility). The repo contains the code for the EfficientNetB0 model which is used for classifying traffic into high, low, and medium categories, achieving superior performance with a macro-averaged F1-score of 0.91 and accuracy of 0.91. For vehicle detection and counting, the YOLOv8x model was used because of its high inference speed up to 100 Frames Per Second and accuracy, as demonstrated by consistent car counts with confidence scores ranging from 0.49 to 0.95 across diverse traffic scenes. The solution was tested in SUMO, simulating dynamic urban traffic scenarios, where it effectively optimized traffic flow by adapting to varying densities and conditions. Optimized for deployment on a hardware microcontrollers which use the serial peripheral communication protocol to share this data, analyze it using the models and then manage traffic. This approach highlights the ability to manage traffic in a real world setting while offering a scalable and efficient solution to urban congestion challenges.

## Datasets
The datasets are quite big. For this reason we could not directly push them to this repo. However they can be accessed from the links below

Vehicle Detection dataset -> https://www.kaggle.com/datasets/ssalijoshua/vehicle-detection

Traffic Density dataset -> https://www.kaggle.com/datasets/ssalijoshua/ssalis-traffic-density

## Running the Simulation
- Follow the directions to install SUMO basing on the operating system you are using at https://sumo.dlr.de/docs/Installing/index.html

- Run the script `Simulations/06_traci/simulation.py`, this opens a map of a city which shows how our algorithms will manage the traffic in the city. You should also be able to scale the traffic to see how dense traffic is handled.  
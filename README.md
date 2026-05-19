# Vehicle Sensor Simulation

Vehicle Sensor Simulation is a beginner-friendly Python project that simulates vehicle sensor data.  
The project generates speed, engine temperature, and fuel level values, detects warning conditions, saves sensor logs to a CSV file, and creates graphs from the collected data.

## Features

- Simulate vehicle speed data
- Simulate engine temperature data
- Simulate fuel level data
- Detect warning conditions
- Save sensor data logs to a CSV file
- Generate graphs from sensor data
- Create separate graphs for speed, engine temperature, and fuel level
- Beginner-friendly Python structure

## Technologies Used

- Python
- CSV
- Matplotlib
- Git
- GitHub

## How to Run

First, make sure Python is installed on your computer.

Install the required library:

```bash
pip install matplotlib
```

Run the project:

```bash
python main.py
```

## Outputs

When the program runs, it creates:

```text
sensor_logs.csv
```

and graph files inside:

```text
outputs/graphs/
```

Generated graph examples:

```text
outputs/graphs/speed_graph.png
outputs/graphs/temperature_graph.png
outputs/graphs/fuel_level_graph.png
```

## Warning Conditions

The project generates warning messages when:

- Speed is greater than 120 km/h
- Engine temperature is greater than 100 °C
- Fuel level is lower than 15%

## Project Purpose

The purpose of this project is to practice Python programming with a simple automotive-related simulation.  
It focuses on:

- Random sensor data generation
- Conditional warning logic
- CSV file handling
- Data logging
- Data visualization with Matplotlib
- Basic automotive sensor simulation

## Future Improvements

- Add real-time graph visualization
- Add battery level simulation
- Add dashboard interface
- Add more sensor types
- Improve warning system logic
- Add unit tests

## Author

Created by **Silan Karabulut**  
Computer Engineering Student
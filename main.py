import csv
import random
import time


def generate_sensor_data():
    speed = random.randint(0, 180)
    engine_temperature = random.randint(60, 130)
    fuel_level = random.randint(0, 100)

    return speed, engine_temperature, fuel_level


def check_warnings(speed, engine_temperature, fuel_level):
    warnings = []

    if speed > 120:
        warnings.append("High speed warning")

    if engine_temperature > 100:
        warnings.append("Engine temperature warning")

    if fuel_level < 15:
        warnings.append("Low fuel warning")

    return warnings


def display_sensor_data(speed, engine_temperature, fuel_level, warnings):
    print("\nVehicle Sensor Data")
    print(f"Speed: {speed} km/h")
    print(f"Engine Temperature: {engine_temperature} °C")
    print(f"Fuel Level: {fuel_level}%")

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")
    else:
        print("Status: All systems normal")


def initialize_log_file():
    with open("sensor_logs.csv", mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["speed", "engine_temperature", "fuel_level", "warnings"])


def save_sensor_log(speed, engine_temperature, fuel_level, warnings):
    if warnings:
        warning_text = ";".join(warnings)
    else:
        warning_text = "None"

    with open("sensor_logs.csv", mode="a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([speed, engine_temperature, fuel_level, warning_text])


def main():
    print("Vehicle Sensor Simulation Started")
    initialize_log_file()

    for _ in range(5):
        speed, engine_temperature, fuel_level = generate_sensor_data()
        warnings = check_warnings(speed, engine_temperature, fuel_level)
        display_sensor_data(speed, engine_temperature, fuel_level, warnings)
        save_sensor_log(speed, engine_temperature, fuel_level, warnings)
        time.sleep(1)

    print("\nSimulation finished.")


if __name__ == "__main__":
    main()
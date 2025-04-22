import random
import time
from enum import nonmember


class WeatherStation:
    def __init__(self):
        self.data = []

    def collect_data(self):
        reading = {
            'temperature': round(random.uniform(15.0, 30.0), 2),
            'humidity': round(random.uniform(30.0, 70.0), 2),
            'pressure': round(random.uniform(1000, 1025), 2)
        }
        self.data.append(reading)
        return reading

    def store_data(self, reading):
        self.data.append(reading)

    def transmit_data(self, reading):
        print(f"Transmitting: {reading}")

    def analyze_data(self):
        if not self.data:
            return None
        avg_temp = sum(d['temperature'] for d in self.data) / len(self.data)
        return {
            'average_temperature': round(avg_temp, 2),
            'data_points': len(self.data)
        }
    def run(self):
        for _ in range(5):
            reading = self.collect_data()
            self.store_data(reading)
            self.transmit_data(reading)
            time.sleep(1)
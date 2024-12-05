class EnergyManager:
    def __init__(self, battery_capacity, solar_efficiency):
        self.battery_capacity = battery_capacity
        self.solar_efficiency = solar_efficiency

    def schedule_energy(self, load):
        if load > self.battery_capacity * self.solar_efficiency:
            return "Warning: Insufficient energy!"
        return f"Energy allocated: {load} units."

if __name__ == "__main__":
    manager = EnergyManager(1000, 0.85)
    print(manager.schedule_energy(800))

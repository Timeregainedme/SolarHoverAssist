import unittest
from src.energy_management.energy_scheduler import EnergyManager

class TestEnergyManager(unittest.TestCase):
    def setUp(self):
        self.manager = EnergyManager(battery_capacity=1000, solar_efficiency=0.85)

    def test_energy_allocation(self):
        result = self.manager.schedule_energy(load=800)
        self.assertIn("allocated", result)
        print("Energy allocation test passed.")

    def test_insufficient_energy(self):
        result = self.manager.schedule_energy(load=1200)
        self.assertIn("Warning", result)
        print("Insufficient energy test passed.")

if __name__ == "__main__":
    unittest.main()

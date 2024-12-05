import unittest
from src.path_planning.algorithms import AntColony

class TestPathPlanning(unittest.TestCase):
    def setUp(self):
        self.graph = [
            [0, 1, 2],
            [1, 0, 1],
            [2, 1, 0]
        ]
        self.colony = AntColony(graph=self.graph, alpha=1, beta=2, evaporation_rate=0.1, num_ants=3)

    def test_path_optimization(self):
        self.colony.optimize(start=0, end=2, iterations=10)
        self.assertIsNotNone(self.colony.pheromone)
        print("Path optimization test passed.")

if __name__ == "__main__":
    unittest.main()

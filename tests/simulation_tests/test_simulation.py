import unittest
import os

class TestSimulation(unittest.TestCase):
    def test_gazebo_simulation(self):
        result = os.system("gazebo --version")
        self.assertEqual(result, 0, "Gazebo simulation environment not found.")
        print("Gazebo simulation test passed.")

    def test_matlab_simulation(self):
        # 假设 MATLAB 已配置环境变量
        result = os.system("matlab -batch 'disp(\"MATLAB running\")'")
        self.assertEqual(result, 0, "MATLAB simulation environment not found.")
        print("MATLAB simulation test passed.")

if __name__ == "__main__":
    unittest.main()

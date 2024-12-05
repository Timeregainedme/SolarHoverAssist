import os

def create_structure():
    structure = {
        "SolarHoverAssist": [
            "docs/requirements.md",
            "docs/technical_design.md",
            "docs/user_manual.md",
            "docs/roadmap.md",
            "docs/references.md",
            "src/flight_control/px4/",
            "src/flight_control/rtos/",
            "src/path_planning/ai_models/",
            "src/path_planning/algorithms.py",
            "src/energy_management/energy_scheduler.py",
            "src/energy_management/solar_simulation.m",
            "src/communication/mqtt_handler.py",
            "src/communication/grpc_manager.py",
            "src/3d_printing/slicer.py",
            "src/3d_printing/printer_control.py",
            "simulation/gazebo/models/",
            "simulation/gazebo/worlds/",
            "simulation/matlab/energy_analysis.m",
            "simulation/matlab/test_scenarios.m",
            "tests/unit_tests/test_path_planning.py",
            "tests/unit_tests/test_energy.py",
            "tests/integration_tests/test_communication.py",
            "tests/integration_tests/test_uav_system.py",
            "tests/simulation_tests/test_simulation.py",
            "tools/data_preprocessing.py",
            "tools/log_analysis.py",
            "tools/visualization/energy_usage_plot.py",
            "tools/visualization/path_plotter.py",
            ".gitignore",
            "README.md",
            "LICENSE",
            "CONTRIBUTING.md"
        ]
    }

    for root, files in structure.items():
        for file in files:
            path = os.path.join(root, file)
            if path.endswith("/"):
                os.makedirs(path, exist_ok=True)
            else:
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, "w") as f:
                    pass
    print("Project structure created successfully!")

if __name__ == "__main__":
    create_structure()

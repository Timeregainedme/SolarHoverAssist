import matplotlib.pyplot as plt

def plot_energy_usage(times, energy_levels):
    """Plot energy usage over time."""
    plt.figure(figsize=(10, 5))
    plt.plot(times, energy_levels, label="Energy Usage", color="blue", marker="o")
    plt.title("Energy Usage Over Time")
    plt.xlabel("Time")
    plt.ylabel("Energy Level (%)")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    times = ["10:00", "11:00", "12:00", "13:00", "14:00"]
    energy_levels = [90, 85, 80, 75, 70]
    plot_energy_usage(times, energy_levels)

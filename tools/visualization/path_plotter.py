import matplotlib.pyplot as plt

def plot_path(obstacles, path):
    """Visualize the planned path with obstacles."""
    plt.figure(figsize=(8, 8))
    
    # Plot obstacles
    for obstacle in obstacles:
        plt.scatter(obstacle[0], obstacle[1], color='red', label='Obstacle' if obstacle == obstacles[0] else "")

    # Plot path
    path_x, path_y = zip(*path)
    plt.plot(path_x, path_y, color='green', label='Planned Path', linewidth=2, marker='o')
    
    plt.title("Path Planning Visualization")
    plt.xlabel("X-coordinate")
    plt.ylabel("Y-coordinate")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    obstacles = [(2, 2), (4, 5), (6, 1)]
    path = [(0, 0), (1, 1), (3, 4), (5, 5), (7, 6)]
    plot_path(obstacles, path)

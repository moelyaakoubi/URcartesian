import csv
import matplotlib.pyplot as plt

# Function to read the log data
def read_log_data(file_path):
    timestamps = []
    joint_positions = [[] for _ in range(6)]
    cartesian_positions = [[], [], []]  # x, y, z
    current_data = []
    force_data = [[] for _ in range(6)]  # fx, fy, fz, tx, ty, tz

    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row

        for row in reader:
            timestamp = float(row[0])
            timestamps.append(timestamp)

            for i in range(6):
                joint_positions[i].append(float(row[i + 1]))

            for i, axis in enumerate(["x", "y", "z"]):
                cartesian_positions[i].append(float(row[i + 7]))

            current_data.append(float(row[13]))  # Current in amperes

            for i in range(6):
                force_data[i].append(float(row[14 + i]))  # Forces

    return timestamps, joint_positions, cartesian_positions, current_data, force_data

# Function to plot Cartesian positions (x, y, z) over time
def plot_cartesian_positions(timestamps, cartesian_positions):
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(timestamps, cartesian_positions[0], label="X position", color='r')
    plt.plot(timestamps, cartesian_positions[1], label="Y position", color='g')
    plt.plot(timestamps, cartesian_positions[2], label="Z position", color='b')
    plt.xlabel("Time (seconds)")
    plt.ylabel("Position (meters)")
    plt.title("Cartesian Positions Over Time")
    plt.legend()

# Function to plot joint positions over time
def plot_joint_positions(timestamps, joint_positions):
    plt.subplot(2, 1, 2)
    for i, joint in enumerate(joint_positions):
        plt.plot(timestamps, joint, label=f"Joint {i + 1}")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Joint Position (radians)")
    plt.title("Joint Positions Over Time")
    plt.legend()

# Function to plot current consumption over time
def plot_current_consumption(timestamps, current_data):
    plt.figure(figsize=(12, 6))
    plt.plot(timestamps, current_data, label="Current Consumption", color='m')
    plt.xlabel("Time (seconds)")
    plt.ylabel("Current (Amps)")
    plt.title("Robot Current Consumption Over Time")
    plt.legend()

# Function to plot forces (fx, fy, fz, tx, ty, tz) over time
def plot_forces(timestamps, force_data):
    force_labels = ["fx", "fy", "fz", "tx", "ty", "tz"]
    plt.figure(figsize=(12, 6))
    for i, force in enumerate(force_data):
        plt.plot(timestamps, force, label=force_labels[i])
    plt.xlabel("Time (seconds)")
    plt.ylabel("Force (N / Nm)")
    plt.title("TCP Forces Over Time")
    plt.legend()

# Main function to read the log data and plot the results
def plot_robot_data(log_file):
    timestamps, joint_positions, cartesian_positions, current_data, force_data = read_log_data(log_file)

    # Plot Cartesian positions (x, y, z)
    #plot_cartesian_positions(timestamps, cartesian_positions)

    # Plot joint positions
    #plot_joint_positions(timestamps, joint_positions)

    # Plot current consumption
    plot_current_consumption(timestamps, current_data)

    # Plot forces
    #plot_forces(timestamps, force_data)

    # Show all plots
    plt.tight_layout()
    plt.show()

# Call the plotting function with the log file
plot_robot_data('robot_data_current.csv')

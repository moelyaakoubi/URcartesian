import socket
import time

# Robot IP and port
ROBOT_IP = '192.168.56.101'
PORT = 30002

# Define Cartesian points (position + orientation)
point1 = [-0.0668, -0.23245, -0.03823, 1.2, 2.867, -0.109]
point2 = [-0.44918, -0.12638, -0.17823, 1.28, 2.991, 0.019]
point3 = [0.51036, 0.13778, -0.35977, 1.273, 2.878, 0.087]
points = [point1, point2, point3]

# Function to format the movel command
def movel_command(pose, a=1.2, v=0.25):
    return f"movel(p[{', '.join(map(str, pose))}], a={a}, v={v})\n"

try:
    # Connect to the robot
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ROBOT_IP, PORT))
        print("Connected to the robot")

        # Send movel commands for each point
        for i, point in enumerate(points):
            command = movel_command(point)
            print(f"Sending command to move to Cartesian point {i+1}: {command}")
            s.sendall(command.encode('utf-8'))

            # Wait for the robot to reach the point
            time.sleep(5)  # Adjust based on the expected motion duration

    print("Motion complete")
except Exception as e:
    print(f"An error occurred: {e}")

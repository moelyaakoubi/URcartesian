import socket
import time

# Robot IP address and port
ROBOT_IP = '192.168.56.101'  # Replace with your robot’s IP address
PORT = 30002              # Port for primary interface

# Define three points in Cartesian coordinates (X, Y, Z) and orientation (roll, pitch, yaw)
# Replace these values with your desired Cartesian positions
# The orientation is represented by Euler angles [roll, pitch, yaw]
point1 = [0.4, -0.2, 0.5, 0, 0, 0]   # Position: (X=0.4, Y=-0.2, Z=0.5), Orientation: (roll=0, pitch=0, yaw=0)
point2 = [0.5, -0.3, 0.6, 0, 0, 0]   # Position: (X=0.5, Y=-0.3, Z=0.6), Orientation: (roll=0, pitch=0, yaw=0)
point3 = [0.6, -0.4, 0.7, 0, 0, 0]   # Position: (X=0.6, Y=-0.4, Z=0.7), Orientation: (roll=0, pitch=0, yaw=0)
point4 = [0.7, -0.5, 0.8, 0, 0, 0]   # Position: (X=0.7, Y=-0.5, Z=0.8), Orientation: (roll=0, pitch=0, yaw=0)
point5 = [0.8, -0.6, 0.9, 0, 0, 0]   # Position: (X=0.8, Y=-0.6, Z=0.9), Orientation: (roll=0, pitch=0, yaw=0)

# Create a list of the points to loop over
points = [point1, point2, point3, point4, point5]

# Function to format Cartesian positions into a URScript command
def movel_command(cartesian, a=1.4, v=1.05):
    # URScript format for movel command with Cartesian positions (position and orientation)
    x, y, z, roll, pitch, yaw = cartesian
    return f"movel(p[{x}, {y}, {z}, {roll}, {pitch}, {yaw}], a={a}, v={v})\n"

# Connect to the robot
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((ROBOT_IP, PORT))
    print("Connected to the robot")

    # Loop through each point and send the move command
    for i, point in enumerate(points):
        # Create the move command for the current Cartesian position
        command = movel_command(point)
        print(f"Sending command to move to point {i+1}: {command}")

        # Send the command to the robot
        s.sendall(command.encode('utf-8'))

        # Wait a bit to ensure the robot has time to reach the target position
        time.sleep(9)  # Adjust the sleep time as needed for your application

    print("Motion complete")

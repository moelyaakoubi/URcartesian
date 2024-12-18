import socket
import time

# Robot IP address and port
ROBOT_IP = '192.168.0.1'  # Replace with your robot’s IP address
PORT = 30002              # Port for primary interface

# Define three points in Cartesian coordinates (X, Y, Z) and orientation (roll, pitch, yaw)
# Replace these values with your desired Cartesian positions
# The orientation is represented by Euler angles [roll, pitch, yaw]
point1 = [-0.05247, -0.2361, 0.36177, 1.111, 2.9, -0.107]
point2 = [-0.44061, -0.1536, 0.22177, 1.188, 3.029, 0.013]
point3 = [-0.50093,-0.16878 , 0.04021, 1.185, 2.917, 0.087]
point4 = [-0.45639, -0.16748, 0.16421, 1.212, 2.920, 0.007]
point5 = [-0.16163, -0.27849, 0.26036, 0.924, 3.082, -0.048]
point6 = [0.02844, -0.39761, 0.19901, 0.562, 3.021, -0.084]
point7 = [-0.00672, -0.44786, 0.04548, 1.088, 2.917, -0.001]
point8 = [0.04738,-0.34733,0.35249,0.693,3.001,-0.322]

points = [ point1,point2, point3,point4,point5,point6,point7,point8]

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
        time.sleep(3)  # Adjust the sleep time as needed for your application

    print("Motion complete")

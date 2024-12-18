import socket
import time

ROBOT_IP = '192.168.0.1'
PORT = 30002

point1= [0.704240353,-1.534144413,0.386590429,-0.469493569,-1.502553953,-0.13840461]
point2= [0.078365283, -0.853291471, 0.31503193, -1.132718685, -1.619840079, -0.748571716]
point3= [0.096691241, -0.429176463, 0.330216294, -1.455604596, -1.616174887, -0.700749695]
point4= [0.083775804, -0.720646448, 0.320791517, -1.188918286, -1.576206847, -0.700924228]
point5= [0.660258056, -1.554564765, 1.114392727, -1.201833723, -1.609368103, -0.331438025]
point6= [1.260651319, -1.303586418, 1.11456726, -1.429773723, -1.490685714, 0.058992129]
point7= [1.24284896, -0.956614963, 1.30550628, -1.922131105, -1.537286005, 0,388161226]


points = [ point1,point2, point3,point4,point5,point6,point7]

def movej_command(joints, a=1.4, v=1.05):
    return f"movej([{', '.join(map(str, joints))}], a={a}, v={v})\n"

def calculate_motion_time(joint_start, joint_end, speed):
    joint_distances = [abs(end - start) for start, end in zip(joint_start, joint_end)]
    return max(joint_distances) / speed

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ROBOT_IP, PORT))
        print("Connected to the robot")

        for i, (start, end) in enumerate(zip(points[:-1], points[1:])):
            command = movej_command(end)
            print(f"Sending command to move to point {i+2}: {command}")
            s.sendall(command.encode('utf-8'))

            motion_time = calculate_motion_time(start, end, speed=1.05)
            time.sleep(motion_time)  # Add buffer time

    print("Motion complete")
except Exception as e:
    print(f"An error occurred: {e}")

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
point8=[1,27984994,-1,286307659,0,309446876,-0,800931594,-1,506044612,0,166504411]


points = [point1,point2, point3,point4,point5,point6,point7,point8]

# Function to format the movej command with joint values
def movej_command_joint(joints, a=1.4, v=1.05):
    return f"movej([{', '.join(map(str, joints))}], a={a}, v={v})\n"


# Function to format the movej command with pose (Cartesian point)
def movej_command_cart(pose,a=1.4, v=1.05):
    return f"movej(p[{', '.join(map(str, pose))}], a={a}, v={v})\n"


def calculate_motion_time(start, target, speed=1.05):
    #start= [0.704240353,-1.534144413,0.386590429,-0.469493569,-1.502553953,-0.13840461]
    #target= [0.078365283, -0.853291471, 0.31503193, -1.132718685, -1.619840079, -0.748571716]
    distances = [abs(target - start) for start, target in zip(start, target)]
    #distances = [abs(0.078365283-0.704240353), abs(-0.853291471-(-1.534144413)), abs(0.31503193-0.386590429), abs(-1.132718685-(-0.469493569)), abs(-1.619840079-(-1.502553953)), abs(-0.748571716-(-0.13840461))]
    return max(distances) / speed


try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ROBOT_IP, PORT))
        print("Connected to the robot")


        for i, point in enumerate(points):
            start=points[i]
            print("start",start)
            if i+1<len(points):
                target=points[i+1]
                print("target",target)
            
            command = movej_command_cart(start)
            print(f"Sending command to move to point {i}: {command}")
            s.sendall(command.encode('utf-8'))

            motion_time = calculate_motion_time(start, target)
            time.sleep(motion_time+2)  # Add buffer time

    print("Motion complete")
except Exception as e:
    print(f"An error occurred: {e}")

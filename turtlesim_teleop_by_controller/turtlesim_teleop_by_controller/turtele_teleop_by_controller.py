import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy

class TurtleteleopBycontroller(Node):
    def __init__(self):
        super().__init__('turtle_teleop_by_controller')
        self.joy_sub=self.create_subscription(Joy,'turtle1/cmd_vel',self.joy_sub_callback,10)

def main():
    rclpy.init()
    node=TurtleteleopBycontroller(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

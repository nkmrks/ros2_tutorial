import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

class TurtleSimJoySubscriber(Node):
    def __init__(self):
        super().__init__('joy_node_subscriber')
        self.joy_node_sub_=self.create_subscription(Twist,'turtle1/cmd_vel',self.joy_node_sub_callback,10)

    def joy_node_sub_callback(self,twist_msg):
        subscribed_msg=twist_msg.data
        self.joy_node_sub_.subscribe(subscribed_msg)

def main():
    rclpy.init()
    node=TurtleSimJoySubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
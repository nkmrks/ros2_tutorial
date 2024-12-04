import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TwistPublisherNode(Node):
    def __init__(self):
        super().__init__('twist_subscriber_node')
        self.twist_sub_=self.create_subscription(Twist,'turtle1/cmd_vel',self.twist_sub_callback,10)

    def twist_sub_callback(self,twist_msg):
        subscribed_msg=twist_msg.data
        self.get_logger().info(subscribed_msg)

def main():
    rclpy.init()
    node=TwistPublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

    if __name__=='__main__':
        main()
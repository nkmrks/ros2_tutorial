import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TwistPublisherNode(Node):
    def __init__(self):
        super().__init__('twist_publisher_node')
        self.twist_pub_=self.create_publisher(Twist,'turtle1/cmd_vel',10)
        self.timer_=self.create_timer(0.5,self.timer_callback)

    def timer_callback(self):
        twist_msg=Twist()
        twist_msg.linear.x=0.5
        twist_msg.angular.z=0.5
        self.twist_pub_.publish(twist_msg)

def main():
    rclpy.init()
    node=TwistPublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

    if __name__=='__main__':
        main()
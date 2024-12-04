import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class StringPublisherNode(Node):
    def __init__(self):
        super().__init__('string_publisher_node')
        self.str_pub_=self.create_publisher(String,'string_message',10)
        self.timer_=self.create_timer(0.5,self.timer_callback)

    def timer_callback(self):
        str_msg=String()
        str_msg.data='Hello from string_publisher_node'
        self.str_pub_.publish(str_msg)

def main():
    rclpy.init()
    node=StringPublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

    if __name__=='__main__':
        main()

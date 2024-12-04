import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class StringSubscriberNode(Node):
    def __init__(self):
        super().__init__('string_subscriber_node')
        self.str_sub_=self.create_subscription(String,'string_message',self.str_sub_callback,10)

    def str_sub_callback(self,str_msg):
        subscribed_msg=str_msg.data
        self.get_logger().info(subscribed_msg)
def main():
    rclpy.init()
    node=StringSubscriberNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()

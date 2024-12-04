import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy

class JoySubscriberNode(Node):
    def __init__(self):
        super().__init__('joy_subscriber_node')
        self.joy_sub_=self.create_subscription(Joy,'joy',self.joy_sub_callback,10)

    def joy_sub_callback(self,joy_msg):
        joy_axes=joy_msg.axes
        joy_axes0 = joy_axes[0]
        joy_axes1 = joy_axes[1]
        # self.get_logger().info('Axes[0]:,%sAxes[1]:%s'%(str(joy_axes[0]),str(joy_axes[1])))
        self.get_logger().info('Axes[0]:%f, Axes[1]:%f' % (joy_axes0, joy_axes1))

def main():
    rclpy.init()
    node=JoySubscriberNode()
    rclpy.spin(node)
    node.destory_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()


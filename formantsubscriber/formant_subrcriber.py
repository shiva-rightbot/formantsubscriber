import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32
from std_msgs.msg import Bool

from rightbot_interfaces.msg import PickTask
import os


class FormantSubscriber(Node):
    task_id = 1
    

    def __init__(self):
        self.top_high = (1.4,-0.6,1.6,0.945,-0.029,0.324,0.026)
        self.top_low = (1.4,-0.6,1.3,0.945,-0.029,0.324,0.026)
        self.front_high =(1.0,-0.6,1.6,0.707,0.0,0.707,0.0)
        self.front_mid =(1.0,-0.6,1.0,0.707,0.0,0.707,0.0)
        self.front_low =(1.0,-0.6,0.8,0.707,0.0,0.707,0.0)
        self.lower =(1.0,-0.6,0.5,0.707,0.0,0.707,0.0)

        super().__init__('formant_subscriber')
       
       
        self.subscription_Top_high = self.create_subscription(
            Bool,
            'Top_high',
            self.listener_Top_high,
            10)
        self.subscription_Top_high  # prevent unused variable warning

        self.subscription_Top_low = self.create_subscription(
            Bool,
            'Top_low',
            self.listener_Top_low,
            10)
        self.subscription_Top_low 


        self.subscription_Front_high = self.create_subscription(
            Bool,
            'Front_high',
            self.listener_Front_high,
            10)
        self.subscription_Front_high  

        self.subscription_Front_mid = self.create_subscription(
            Bool,
            'Front_mid',
            self.listener_Front_mid,
            10)
        self.subscription_Front_mid  

        self.subscription_Front_low = self.create_subscription(
            Bool,
            'Front_low',
            self.listener_Front_low,
            10)
        self.subscription_Front_low  

        self.subscription_Lower = self.create_subscription(
            Bool,
            'Lower',
            self.listener_Lower,
            10)
        self.subscription_Lower 

        self.subscription_local = self.create_subscription(
            Int32,
            '/local_test_ip',
            self.Local_interface,
            10)
        self.subscription_Lower 

        self.publisher_ = self.create_publisher(PickTask, 'pick_task', 10)

          # camera left align
        self.subscription_camera_align_right = self.create_subscription(
            Bool,
            'camera_align_right',
            self.camera_align_right,
            10)
        self.subscription_camera_align_right

        # camera right align
        self.subscription_camera_align_left = self.create_subscription(
            Bool,
            'camera_align_left',
            self.camera_align_left,
            10)
        self.subscription_camera_align_left



    def listener_Top_high(self, msg):
        
        if(msg.data):
            self.get_logger().info("listener_top_high "+str(msg.data))
            self.publish_position(self.top_high)

    def listener_Top_low(self, msg):
        
        if(msg.data):
            self.get_logger().info("listener_top_low "+str(msg.data))
            self.publish_position(self.top_low)

    def listener_Front_high(self, msg):
        
        if(msg.data):
            self.get_logger().info("listener_front_high "+str(msg.data))
            self.publish_position(self.front_high)

    def listener_Front_mid(self, msg):
        if(msg.data):
            self.get_logger().info("listener_front_mid "+str(msg.data))
            self.publish_position(self.front_mid)

    def listener_Front_low(self, msg):
        
        if(msg.data):
            self.get_logger().info("listener_front_low "+str(msg.data))
            self.publish_position(self.front_low)

    def listener_Lower(self, msg):
        if(msg.data):
            self.get_logger().info("listener_Lower "+str(msg.data))
            self.publish_position(self.lower)

    def camera_align_right(self, msg):
        if(msg.data):
            self.get_logger().info("camera_align_right "+str(msg.data))
            os.system("""ros2 service call camera_align rightbot_interfaces/srv/CameraAlign "{auto_align: true, camera_name: 'right_camera'}" """)

    def camera_align_left(self, msg):
        if(msg.data):
            self.get_logger().info("camera_align_left "+str(msg.data))
            os.system("""ros2 service call camera_align rightbot_interfaces/srv/CameraAlign "{auto_align: true, camera_name: 'left_camera'}" """)


    def Local_interface(self, msg):
        if(msg.data == 1):
            self.listener_Front_high
            self.get_logger().info("front top")

        if(msg.data == 2):
            self.listener_Front_mid
            self.get_logger().info("front mid")

        if(msg.data == 3):
            self.listener_Front_low
            self.get_logger().info("front low")

        if(msg.data == 4):
            self.camera_align_left
            self.get_logger().info("camera align left")

        if(msg.data == 5):
            self.camera_align_right
            self.get_logger().info("camera align right")

        if(msg.data == 6):
            os.system("""ros2 service call /gripper_pump_control rightbot_interfaces/srv/Gripper""")
            self.get_logger().info("pump off")
            
        if(msg.data == 7):
            os.system("""ros2 service call /task_manager/clear_octomap std_srvs/srv/Empty""")
            self.get_logger().info("clear cost map")


    def publish_position(self, positions):
        pick_task = PickTask()
        self.task_id = self.task_id + 1
        pick_task.task_id = self.task_id
        pick_task.task_type = 'move'
        pick_task.data = positions
        self.publisher_.publish(pick_task)



def main(args=None):
    rclpy.init(args=args)

    formant_subscriber = FormantSubscriber()

    rclpy.spin(formant_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    formant_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
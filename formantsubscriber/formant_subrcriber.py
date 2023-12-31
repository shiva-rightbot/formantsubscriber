import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool
from rightbot_interfaces.msg import PickTask


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

        self.publisher_ = self.create_publisher(PickTask, 'pick_task', 10)

        #######################################################################
        ########### subscriber for bot sate ready and clear cost map ###########

        self.subscription_state_ready = self.create_subscription(
            Bool,
            'state_ready',
            self.stateReady(),
            10)
        self.subscription_state_ready


################# for clear cost map ###############
        self.subscription_clearCostMap = self.create_subscription(
            Bool,
            'ClearCostMap',
            self.clearCostMap(),
            10)
        self.subscription_clearCostMap




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

    
        
        
    def publish_position(self, positions):
        pick_task = PickTask()
        self.task_id = self.task_id + 1
        pick_task.task_id = self.task_id
        pick_task.task_type = 'move'
        pick_task.data = positions
        self.publisher_.publish(pick_task)



    # this fn handles the bot state command



    def stateReady(self, msg):
        


    def clearCostMap(self, msg):




    




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
import launch
import time

def generate_launch_description():
    topics_to_record = [
        '/scan',
        '/scan_echo',
        '/scan_image',
    ]

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    bag_name = f'recorded_rosbag_ping360_{timestamp}'
    
    return launch.LaunchDescription([
        launch.actions.ExecuteProcess(
            cmd=['ros2', 'bag', 'record'] + topics_to_record + ['-o', f'./share/rosbag_record/{bag_name}'],
            output='screen'
        )
    ])
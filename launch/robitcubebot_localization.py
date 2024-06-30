from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='slam_toolbox',
            executable='async_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            parameters=[
                {'use_sim_time': True},
                '/home/omar/robit_cube_bot_ws_/src/robitcubebot_localization/config/mapper_params_online_async.yaml'
            ],
            remappings=[
                ('/scan', '/scan')
            ]
        )
    ])

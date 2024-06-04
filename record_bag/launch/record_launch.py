import launch
from launch import LaunchDescription
from launch.actions import ExecuteProcess
import os

def generate_launch_description():
    package_path = os.path.dirname(os.path.realpath(__file__))
    script_path = os.path.join(package_path, 'record_bag.py')

    return LaunchDescription([
        ExecuteProcess(
            cmd=['python3', script_path],
            output='screen'
        ),
    ])


# import launch
# from launch import LaunchDescription
# from launch.actions import ExecuteProcess

# def generate_launch_description():
#     return LaunchDescription([
#         ExecuteProcess(
#             cmd=['python3', '/home/hayashi/bunker_ws_ros2/src/record_bag/launch/record_bag.py'],

#             output='screen'
#         ),
#     ])
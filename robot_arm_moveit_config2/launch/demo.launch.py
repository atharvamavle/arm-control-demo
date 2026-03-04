from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution


def generate_launch_description():
    pkg_share = FindPackageShare("robot_arm_moveit_config2")

    rsp_launch = PathJoinSubstitution(
        [pkg_share, "launch", "rsp.launch.py"]
    )

    move_group_launch = PathJoinSubstitution(
        [pkg_share, "launch", "move_group.launch.py"]
    )

    return LaunchDescription(
        [
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(rsp_launch)
            ),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(move_group_launch)
            ),
        ]
    )

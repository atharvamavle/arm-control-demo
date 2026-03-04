from launch import LaunchDescription
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    pkg_name = "your_robot_description"
    pkg_share = FindPackageShare(pkg_name).find(pkg_name)

    urdf_path = PathJoinSubstitution([pkg_share, "urdf", "arm.urdf"])

    params = {"robot_description": Command(["xacro ", urdf_path])}

    robot_state_pub = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[params],
    )

    joint_state_pub = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
    )

    return LaunchDescription([robot_state_pub, joint_state_pub, rviz_node])

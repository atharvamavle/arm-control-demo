from launch import LaunchDescription
from launch_ros.actions import Node
from moveit_configs_utils import MoveItConfigsBuilder


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder(
        "robot_arm", package_name="robot_arm_moveit_config2"
    ).to_moveit_configs()

    robot_description = moveit_config.robot_description
    robot_description_semantic = moveit_config.robot_description_semantic
    planning_pipelines = moveit_config.planning_pipelines
    trajectory_execution = moveit_config.trajectory_execution
    planning_scene_monitor = moveit_config.planning_scene_monitor

    return LaunchDescription(
        [
            Node(
                package="moveit_ros_move_group",
                executable="move_group",
                output="screen",
                parameters=[
                    robot_description,
                    robot_description_semantic,
                    planning_pipelines,
                    trajectory_execution,
                    planning_scene_monitor,
                ],
            ),
            Node(
                package="rviz2",
                executable="rviz2",
                name="moveit_rviz",
                output="screen",
                parameters=[robot_description, robot_description_semantic],
            ),
        ]
    )

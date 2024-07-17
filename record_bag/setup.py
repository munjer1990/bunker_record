from setuptools import setup

package_name = 'record_bag'

setup(
    name=package_name,
    version='0.0.0',
    packages=[],
    py_modules=[
        'record_ros2_bag'
    ],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/record_launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hayashi',
    maintainer_email='hayashi@todo.todo',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'record_ros2_bag = record_bag:main'
            'record_selected = record_bag.selected_topic:main'
        ],
    },
)

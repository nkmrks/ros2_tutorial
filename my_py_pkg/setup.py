from setuptools import find_packages, setup

package_name = 'my_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='keisoku',
    maintainer_email='keisoku@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_first_node = my_py_pkg.my_first_node:main',
            'my_second_node=my_py_pkg.my_second_node:main',
            'string_publisher_node=my_py_pkg.string_publisher_node:main',
            'twist_publisher_node=my_py_pkg.twist_publisher_node:main',
            'string_subscriber_node=my_py_pkg.string_subscriber_node:main',
            'joy_subscriber_node=my_py_pkg.joy_subscriber_node:main',
            'joy_node=my_py_pkg.joy_node:main',
            'joy_node_subscriber=my_py_pkg.joy_node_subscriber:main',
            'twist_subscriber_node=my_py_pkg.twist_subscriber_node:main',
        ],
    },
)

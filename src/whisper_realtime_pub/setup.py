from setuptools import setup

package_name = 'whisper_realtime_pub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='allen',
    maintainer_email='allen327lin2@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['go = whisper_realtime_pub.teleop_realtime_pub:main',
                            'test = whisper_realtime_pub.hello_world:main'
        ],
    },
)

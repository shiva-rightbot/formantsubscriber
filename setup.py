from setuptools import setup

package_name = 'formantsubscriber'

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
    maintainer='rightbot',
    maintainer_email='shiva.kumara@rightbot.in',
    description='TODO: Package description',
    license='license',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [ 'formantsubscriber = formantsubscriber.formant_subrcriber:main',
        ],
    },
)

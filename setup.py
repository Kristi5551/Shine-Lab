from setuptools import setup, find_packages

setup(
    name='beauty_salon',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
    ],
)

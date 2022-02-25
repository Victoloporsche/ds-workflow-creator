from setuptools import setup, find_packages
from os import path

path.abspath(path.dirname(__file__))

setup(
    name='ds_workflow',
    version='0.1',
    description='Data Science end-to-end Workflow',
    author='Victor Uwaje',
    packages=find_packages(),
    license='MIT'
)

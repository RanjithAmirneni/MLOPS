""" Inside setup.py we need to write this below code which i taken from the documentation of python
They are telling us that if you want to install some folder as a local package 
you need to use this  below piece of code
 """

from setuptools import setup, find_packages

setup(
    name="us_visa",
    version="0.0.0",
    author="Ranjith Kumar",
    author_email="ranjithamirneni@gmail.com",
    packages=find_packages()
)
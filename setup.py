from setuptools import setup, find_packages

setup(
    name='awesomefunctions',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description= "Tiego's EDSA python package",
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/tiego1/awesomefunctions.git',
    author='Tiego',
    author_email='somwhr80@gmail.com'
)

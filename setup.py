from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='hhtps://github.com/sensei01/mypackage',
    author='Ahmad Barde',
    author_email='ahmadsanibarde@gmail.com'
)
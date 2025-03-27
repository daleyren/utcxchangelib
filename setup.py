from setuptools import setup, find_packages

setup(
    name='utcxchangelib',
    version='0.1.1',
    author='Ian Magnell',
    author_email='ianmm3203@gmail.com',
    description='Client for xchangeV3',
    packages=['utcxchangelib'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'protobuf==5.29.0',
        'grpcio==1.71.0',
    ]
)


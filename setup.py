# from distutils.core import setup
from setuptools import setup, find_packages
import os
import glob

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()
    
setup(
    name='PLambda',
    version='1.0',
    description='The PLambda language',
    long_description=long_description,
    url='https://github.com/SRI-CSL/PLambda',
    author='Ian A. Mason',
    author_email='iam@csl.sri.com',
    

    packages=find_packages(exclude=['tests']),
    
    entry_points = {
        'console_scripts': [
            'plamparse = plam.visitor.Parser:main',
            'plambda = plambda.eval.rep:main',
            'pyactor = plambda.actors.pyactor:main',
        ],
    },
    
    license='MIT',
    
    install_requires=[
        "antlr4-python2-runtime" >= "4.5.3"
    ],
    
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Actor Programming',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Operating System :: OS Independent'
    ],
)

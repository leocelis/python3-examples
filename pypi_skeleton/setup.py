from codecs import open
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# long description
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='testlib',
    version='0.0.1',
    description='Test Lib',
    long_description=long_description,
    url='https://github.com/leocelis/testlib',
    author='Leo Celis',
    author_email='leo@leocelis.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='enterprise python framework',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    python_requires='>=3',
)

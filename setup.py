import os
from setuptools import setup, find_packages
import imp

REQUIREMENTS = ["offset"]

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Topic :: Software Development :: Libraries']


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
    long_description = f.read()

DATA_FILES = [('libchan', ["LICENSE", "MANIFEST.in", "README.rst"])]


def load_module(name, path):
    f, pathname, description = imp.find_module(name, [path])
    return imp.load_module(name, f, pathname, description)


VERSION = load_module('version', './libchan').__version__

setup(name='libchan',
      version=VERSION,
      description='',
      long_description=long_description,
      classifiers=CLASSIFIERS,
      license='MIT',
      url='http://github.com/benoitc/offset',
      author='Gijs Molenaar',
      author_email='gijs@pythonic.nl',
      packages=find_packages(),
      install_requires=REQUIREMENTS,
      setup_requires=REQUIREMENTS,
      tests_require=['pytest'],
      data_files=DATA_FILES)
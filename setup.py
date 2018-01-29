
import os
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

version = '0.1.0'


class PyTest(TestCommand):

    user_options = [('pytest-args=', 'a', "Arguments to pass into py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(name='protoc-gen-swagger',
      version=version,
      description=" A python package for swagger annotation proto files.",
      long_description=open(
          os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
      classifiers=(
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: Implementation :: CPython',
      ),
      keywords='proto swagger protobuf gRPC',
      author='universe-proton',
      url='https://github.com/universe-proton/protoc-gen-swagger',
      license='Apache 2.0',
      packages=find_packages(
          exclude=['ez_setup', 'examples', 'tests', 'gen.sh']),
      include_package_data=True,
      zip_safe=True,
      cmdclass={'test': PyTest},
      tests_require=('pytest==3.0.7',),
      install_requires=[
          # -*- Extra requirements: -*-
          'protobuf>=3.0.0'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
)

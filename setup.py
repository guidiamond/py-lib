from setuptools import setup

setup(name='dev_aberto_guilhermetb1',
      version='0.1',
      packages=['dev_aberto'],
      author="guilhemetb1",
      license="MIT",
      install_requires=[
          "requests",
      ],
      scripts=['scripts/hello.py']
      )


from setuptools import setup

setup(
    name='PyIsEven',
    version='0.3.1',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'requests>=2.14.0',
        'retry>=0.9.2',
    ],
)

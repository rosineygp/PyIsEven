from setuptools import setup

setup(
    name='PyIsEven',
    packages=['is_even'],
    version='0.4.0',
    license='MIT',
    description='Check is a integer is even',
    author='Rosiney Gomes Pereira',
    url='https://github.com/rosineygp/PyIsEven',
    keywords=['even'],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'requests>=2.14.0',
        'retry>=0.9.2',
    ],
)

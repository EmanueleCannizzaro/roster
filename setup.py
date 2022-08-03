from setuptools import find_packages, setup

setup(
    name='roster',
    version='0.1.0',
    packages=find_packages(
        where='.',
        include=['roster'],  # ["*"] by default
        exclude=['tests'],  # empty by default
    ),
    install_requires=[
        'pandas',
        'importlib-metadata; python_version >= "3.5"',
        'Autologging'
    ],
)

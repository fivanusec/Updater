from setuptools import setup, find_packages

local_packages = ['file:///lib/Updater/']

setup(
    name="Updater",
    author="Filip Ivanusec",
    author_email="fivanusec@gmail.com",
    version="1.0.0",
    packages=[
        'Updater',
        'Updater.updater'
    ],
    entry_points={
        'console_scripts': [
            'updater = Updater:main'
        ],
    },
    dependency_links=local_packages
)

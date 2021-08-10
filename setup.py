from setuptools import setup

setup(
    name="Updater",
    author="Filip Ivanusec",
    author_email="fivanusec@gmail.com",
    platforms=['linux'],
    install_requires=['distro'],
    scripts=['updater.py'],
    zip_safe=True
)

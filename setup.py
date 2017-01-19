from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name="monsoon-backup-mysql",
    version="0.1.0",
    description="Monsoon plug-in for MySQL backups.",
    long_description=long_description,
    url="https://github.ibm.com/apset/monsoon-backup-mysql",
    author="Luiz Aoqui",
    author_email="laoqui@ca.ibm.com",
    license="IBM",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 2 :: Only",
        "Topic :: Database",
        "Topic :: System :: Archiving :: Backup",
        "Topic :: Utilities"
    ],
    packages=find_packages(),
    install_requires=[
        "monsoon>=0.1.0"
    ],
    entry_points={
        "monsoon.backups": [
            "mysql=mysql:MySQLBackup"
        ]
    }
)

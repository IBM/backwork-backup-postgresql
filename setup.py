"""Add support for PostgreSQL backups
"""

from os import path

from setuptools import find_packages, setup

HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, "README.md")) as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="backwork-backup-postgresql",
    version="0.2.2",
    description="Backwork plug-in for PostgreSQL backups.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/ibm/backwork-backup-postgresql",
    author="Luiz Aoqui",
    author_email="laoqui@ca.ibm.com",
    license="Apache 2",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 2 :: Only",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Database",
        "Topic :: System :: Archiving :: Backup",
        "Topic :: Utilities",
    ],
    packages=find_packages(),
    install_requires=["backwork"],
    entry_points={"backwork.backups": ["postgresql=postgresql:PostgreSQLBackup"]},
)

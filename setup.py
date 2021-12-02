"""Python setup.py for filesproxy_service package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("filesproxy_service", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="filesproxy_service",
    version=read("filesproxy_service", "VERSION"),
    description="Awesome filesproxy_service created by michaelnurenberg",
    url="https://github.com/michaelnurenberg/filesproxy-service/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="michaelnurenberg",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["filesproxy_service = filesproxy_service.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)

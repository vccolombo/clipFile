from setuptools import setup
import setuptools

setup(
    name="clipFile",
    version="0.1.0",
    description="Copy your files content to clipboard from terminal",
    url="https://github.com/vccolombo/clipFile",
    author="Víctor Cora Colombo",
    author_email="victorcora98@gmail.com",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=["pyperclip==1.7.0"],
    entry_points={
        "console_scripts": [
            "clip=clipFile.main:main"
        ],
    },
    classifiers=[
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.7",
)

from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="optivision",
    version="0.1.0",
    author="Preet Sojitra",
    author_email="preet.dev373@gmail.com",
    description="A simple image processing library",
    long_description=long_description,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

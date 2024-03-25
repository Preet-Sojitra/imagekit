from setuptools import setup, find_packages

setup(
    name="optivision",
    version="0.2.0",
    author="Preet Sojitra",
    author_email="preet.dev373@gmail.com",
    description="A simple package to perform image processing operations.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Preet-Sojitra/optivision",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy",
    ],
)

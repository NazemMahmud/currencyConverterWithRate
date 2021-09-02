import io
import os
from setuptools import setup, find_packages, find_namespace_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="currency-converter-with-rate",    # This is the name of the package
    version="1.0.1",                        # The initial release version
    author="Nazem Mahmud Piash",            # Full name of the author
    author_email='nazem.piash10@gmail.com',
    url='https://github.com/NazemMahmud/currencyConverterWithRate',
    description="Currency conversion between any two or to multiple and currency rates based on some parameters",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=['currency-converter-with-rate'],    # List of all python modules to be installed
    classifiers=[
        'Intended Audience :: Developers',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Topic :: Software Development :: Internationalization',
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.5',                # Minimum version requirement of the package
    install_requires=['requests','simplejson'],  # Install other dependencies if any
)

import setuptools
from py_zillow.zillow._version import __version__

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name = 'py-zillow',
    version = __version__,
    license = "MIT",
    author = 'Alexander Dewhirst',
    author_email = 'alex@freightroll.com',
    description = 'A Zillow API wrapper',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/AlexanderDewhirst/py-zillow',
    keywords = ['zillow', 'api', 'real estate', 'python'],
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3"
    ],
)
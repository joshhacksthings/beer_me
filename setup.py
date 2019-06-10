import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="beer_me_setup_tools",
    version="0.0.1",
    author="Joshua Nowak",
    author_email="",
    description="Setup for beer_me",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/joshhacksthings/beer_me",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
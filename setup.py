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
    install_requires=[
        "Flask>=1.0.3",
        "Flask-Cors>=3.0.8",
        "flask_sqlalchemy==2.4.0",
        "flask_script==2.0.6",
        "flask_migrate==2.5.2",
        "flask_wtf==0.14.2",
        "psycopg2==2.8.3"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
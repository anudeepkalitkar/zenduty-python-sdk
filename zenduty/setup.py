from setuptools import setup, find_packages

setup(
    name="zenduty-api",
    version="0.9",
    description="Python SDK wrapper for the Zenduty API",
    long_description="Python SDK wrapper for the Zenduty API",
    long_description_content_type="text/x-rst",
    author="Anudeep Kalitkar",
    author_email="anudeep.kalitkar@gmail.com",
    packages=find_packages(),
    install_requires=[
        "urllib3==2.3.0",
        "certifi==2024.7.4"
    ]
)
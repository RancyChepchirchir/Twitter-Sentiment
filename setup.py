import os
import setuptools

current_dir = os.path.abspath(os.path.dirname(__file__))

## requirements
with open(os.path.join(current_dir, "README.md"), "r") as fh:
    long_description = fh.read()


# What packages are required for this module to be executed?
try:
    with open(os.path.join(current_dir, "requirements.txt"), encoding="utf-8") as f:
        required = f.read().split("\n")
except FileNotFoundError:
    required = []

setuptools.setup(
    name="shahules786",  # Replace with your own username
    version="0.0.1",
    author="Shahul ES",
    author_email="shahules786@gmail.com",
    description="A python package for sentiment analysis written using pytorch framework",
    long_description_content_type=long_description,
    url="https://github.com/shahules786/Twitter-Sentiment",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=required,
)
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="helpers",  # Replace with your own username
    version="0.0.1",
    author="Oxel40",
    # author_email="author@example.com",
    description="Some helper functions and classes I've developed and used in some of my personal projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Oxel40/python-helpers",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

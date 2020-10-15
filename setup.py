import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NIF-validator-spamz23", # Replace with your own username
    version="0.0.1",
    author="Diogo Silva",
    author_email="diogo_silva30@hotmail.com",
    description="A small Python package to validate Portuguese taxpayer numbers (NIFs)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/spamz23/NIF-validator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
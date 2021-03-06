import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NIF-validator",  # Replace with your own username
    version="0.0.6",
    author="Diogo Silva",
    author_email="diogo_silva30@hotmail.com",
    description="A small Python package to validate Portuguese taxpayer numbers (NIFs)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/spamz23/NIF-validator",
    install_requires=open("requirements.txt").readlines(),
    include_package_data=True,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)

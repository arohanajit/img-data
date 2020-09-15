import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="img-data",
    version="0.0.1",
    author="Arohan Ajit",
    author_email="arohanajit232@gmail.com",
    description="Use Stock Images APIs to make image dataset",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arohanajit/img-data",
    keywords='data api images photos',
    install_requires=['requests','urllib','os','warnings'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
)
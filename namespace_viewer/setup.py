import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-spencer-park"
    version="0.0.1",
    author="Spencer Park ",
    author_email="soorte214@gmail.com",
    description="python namespace viewer html",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/spencer-park/namespace-viewer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
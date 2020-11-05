import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="pytorch-vision-utils", # Replace with your own username
    version="0.0.1",
    scripts=['Utilities.py'],
    author="Nicole Guo",
    author_email="nicoleguob@gmail.com",
    description="PyTorch training and data visualization utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nguobadia/PyTorch-Utilities",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
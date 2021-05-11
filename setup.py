import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="latex-plot-utils", # Replace with your own username
    version="1.2.0",
    author="Bruce Collie",
    author_email="brucecollie82@gmail.com",
    description="Helpers for Matplotlib plots in LaTeX",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Baltoli/latex-plot-utils",
    packages=setuptools.find_packages(),
    install_requires=[
        'matplotlib'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

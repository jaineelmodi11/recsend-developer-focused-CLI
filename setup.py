# setup.py
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="recsend",                        # what you’ll publish on PyPI
    version="0.1.0",                       # start with your initial version
    author="Jaineel Modi",
    author_email="your.email@example.com",
    description="Developer-focused CLI for testing movie recommendation backends",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jaineelmodi11/recsend-developer-focused-CLI",
    packages=setuptools.find_packages(),   # assumes your code is in a module folder
    install_requires=[                     # your dependencies
        "requests>=2.0",
        "PyYAML>=5.0",
    ],
    entry_points={
        "console_scripts": [
            "recsend=recsend.cli:main",    # adjust to your CLI entry-point
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)

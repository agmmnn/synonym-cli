from setuptools import setup
from synonym_cli import __version__ as VERSION

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as file:
    requires = [line.strip() for line in file.readlines()]

DESCRIPTION = "Synonyms and antonyms of words from Thesaurus are now in your terminal, with rich output."

setup(
    name="synonym-cli",
    version=VERSION,
    url="https://github.com/agmmnn/synonym-cli",
    project_urls={
        "Changelog": "https://github.com/agmmnn/synonym-cli/releases",
        "Source": "https://github.com/agmmnn/synonym-cli",
    },
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="agmmnn",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Utilities",
    ],
    packages=["synonym_cli"],
    install_requires=requires,
    include_package_data=True,
    package_data={"synonym_cli": ["synonym_cli/*"]},
    python_requires=">=3.5",
    entry_points={"console_scripts": ["syn = synonym_cli.__main__:cli"]},
)

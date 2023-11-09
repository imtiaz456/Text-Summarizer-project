# here we will code the logic for the libraries we wrote in requirements.txt

import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-project"  # project name
AUTHOR_USER_NAME = "imtiaz456"     # github user name
SRC_REPO = "textSummarizer"   # source repository
AUTHOR_EMAIL = "sweet.lemon.12333@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small project for NLP app",
    long_description=long_description,
    long_description_content ="text/markdown",
    url=f"https://github.com/imtiaz456/Text-Summarizer-project",
    project_urls={
        "Bug Tracker": f"https://github.com/imtiaz456/Text-Summarizer-project/issues",
        },
        package_dir = {"":"src"},
        packages = setuptools.find_packages(where="src")
)
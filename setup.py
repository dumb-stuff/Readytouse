import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="Readytousebot",
    version="1.0.0",
    description="All purpose discord.py in one package",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/dumb-stuff/Readytouse/",
    author="python_mooping",
    author_email="imooping3roblox@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["Readytouse"],
    include_package_data=True,
    install_requires=["discord", "discord-ext-alternatives","aiofiles","asyncio","youtube_dl","functools","itertools"],
    entry_points={
        "console_scripts": [
            "realpython=reader.__main__:startthebot",
        ]
    },
)

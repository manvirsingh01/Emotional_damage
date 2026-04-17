from setuptools import setup, find_packages

setup(
    name="emotional-damage",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "edamage=Emotional_damage.cli:main"
        ]
    },
)
from setuptools import setup, find_packages

setup(
    name="analyze-auth0",
    version="0.4.0",
    description="Meltano project file bundle of Matatika datasets for tap-auth0",
    packages=find_packages(),
    package_data={
        "bundle": [
            "analyze/datasets/tap-auth0/*.yml",
        ]
    },
)

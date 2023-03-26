from setuptools import find_packages, setup

setup(
    name="mikita",
    packages=find_packages(exclude=["mikita_tests"]),
    install_requires=["dagster","duckdb","pandas","sqlescapy","lxml","html5lib"],
    extras_require={"dev": ["dagit", "pytest", "localstack", "awscli", "awscli-local"]},
)

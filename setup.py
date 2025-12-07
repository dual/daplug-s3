import os
from pathlib import Path

from setuptools import find_packages, setup


def read_long_description() -> str:
    readme_path = Path(__file__).parent / "README.md"
    with readme_path.open(encoding="utf-8") as fh:
        return fh.read()


setup(
    name="daplug-s3",
    version=os.getenv("CIRCLE_TAG", "0.1.0"),
    url="https://github.com/dual/daplug-s3",
    author="Paul Cruse III",
    author_email="paulcruse3@gmail.com",
    description="Schema-aware DynamoDB adapter with prefixing, SNS hooks, and batching.",
    long_description=read_long_description(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "boto3==1.40.69; python_version >= '3.9'",
        "botocore==1.40.75; python_version >= '3.9'",
        "daplug-core==1.0.0b5; python_version >= '3.9'",
    ],
    keywords=[
        "dynamodb",
        "aws",
        "ddb",
        "normalizer",
        "schema",
        "sns",
        "event-driven",
        "database",
        "adapter",
        "python-library",
    ],
    project_urls={
        "Homepage": "https://github.com/dual/daplug-s3",
        "Documentation": "https://github.com/dual/daplug-s3#readme",
        "Source Code": "https://github.com/dual/daplug-s3",
        "Bug Reports": "https://github.com/dual/daplug-s3/issues",
        "CI/CD": "https://circleci.com/gh/dual/daplug-s3",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Database :: Front-Ends",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3 :: Only",
    ],
    license="Apache License 2.0",
    platforms=["any"],
    zip_safe=False,
)

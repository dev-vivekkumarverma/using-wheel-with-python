from setuptools import setup, find_packages
from pathlib import Path

# Read requirements.txt
def get_requirements(requirement_dir:str):
    requirements=[]
    with open(requirement_dir) as rd:
        for line in rd.readlines():
            if not line.startswith("#"):
                requirements.append(line.strip())
    return requirements

setup(
    name="test_lib_test",
    version="1.0.1",
    description="this is a test for using wheel",
    author="vivek kumar verma",
    author_email="vivekkumarverma332@gmail.com",
    maintainer="dev-vivekkumarverma",
    maintainer_email="vivekkumarverma332@gmail.com",
    packages=find_packages(),
    include_dirs=[],
    install_requires=get_requirements('./requirement.txt'),
    entry_points={
        'console_scripts':[
            'analyze-data=test_lib.analyser:main'
        ],
    },
)
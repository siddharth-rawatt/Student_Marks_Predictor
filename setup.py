# Automatically find out all the ML packages required in the setup
from setuptools import find_packages, setup
from typing import List

Hyphen_e_dot = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requiremnts
    """

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # To remove the extra next line space
        requirements = [req.replace("\n", "") for req in requirements]

        if Hyphen_e_dot in requirements:
            requirements = requirements.remove(Hyphen_e_dot)

        return requirements


# metadata for the full project
setup(
    name="mlprojectendtoend",
    version="0.0.1",
    author="Siddharth",
    author_email="siddharth.rawatt@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)

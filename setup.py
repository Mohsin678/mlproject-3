from setuptools import find_packages,setup
from typing import List

Hypen_E_Dot = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    This function returns list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]

        if Hypen_E_Dot in requirements:
            requirements.remove(Hypen_E_Dot)

    return requirements

setup(
    name = "mlproject3",
    version = "1.81.1",
    author = "Mohsin678",
    author_email = "mohsin79.kh@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
)
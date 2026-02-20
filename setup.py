from setuptools import find_packages , setup
from typing import List
HYPEN_E_DOT='E'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements
setup (
    name = "Fault detection" , 
    version = '3.10.11' , 
    author = 'Kapil' , 
    author_mail = 'kplchhmp@gmail.com',
    install_requirements = get_requirements('requirements.txt'), 
    packages= find_packages()
) 
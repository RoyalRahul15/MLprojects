from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path)->List[str]:
    """ 
    This function will return the list of requirements
    mentioned in the requirements.txt file
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

    if '-e .' in requirements:
        requirements.remove('-e .')
setup(
    name='ml_projects',
    version='0.1.0',
    author='Royal Rahul',
    author_email='royal.rahulcse@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    description='A collection of machine learning projects and experiments.',

)
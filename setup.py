from setuptools import find_packages, setup

def get_requirements(file_path):
	requirements = []
	with open(file_path, mode= 'r') as file_obj:
		requirements = file_obj.readlines()
		requirements = [req.replace("\n", "") for req in requirements]

	return requirements

setup(
	name = "MLProject",
	version = "0.0.1",
	author = "R-NIRMALKUMAR",
	author_email = "nirmalkumarprojects@gmail.com",
	packages = find_packages(),
	install_requires = get_requirements("requirements.txt")
)
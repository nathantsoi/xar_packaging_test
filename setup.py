import setuptools

from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip

pfile = Project(chdir=False).parsed_pipfile
requirements = convert_deps_to_pip(pfile['packages'], r=False)

setuptools.setup(
    name='Test',
    version='0.1',
    packages=setuptools.find_packages(),
    install_requires=requirements,
    entry_points={'console_scripts':['test=test:main']}
)

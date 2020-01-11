import setuptools
import re
import ast

# https://packaging.python.org/tutorials/packaging-projects/

with open("README.md", "r") as fh:
    long_description = fh.read()

version_file = 'version/__init__.py'
tmp_version_file = 'temp/_tmp_version.tmp'

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open(version_file, 'rb') as f:
    for line in f:
        line=line.strip()
        if line:
            line=line.decode('utf-8')
            reg_comment = re.compile(r'^#.*')
            m = reg_comment.search(line)
            if not m:
               result_search = _version_re.search(line)
               version = result_search.group(1)
               version = version.strip('\"')
#               print("version is >" + version + "<.")
               main_version, sub_version, fix_version = version.split(".")
               fix_number = int(fix_version) + 1
               new_version = main_version +"." + sub_version + "." + str(fix_number)
#               print("version will be >" + new_version + "<.")
               with open(tmp_version_file, 'wb') as t:
                    out_line ='__version__ = "' + new_version + '"\n'
                    t.write(out_line.encode('utf-8'))
 

setuptools.setup(
    name='devops-informatica-tools',
    version=new_version,
    author='Jac. Beekers',
    author_email='jactools@consag.nl',
    description='DevOps and CI-CD Pipeline scripts for Informatica Platform related projects',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/consag/devops-informatica-tools',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6'
)


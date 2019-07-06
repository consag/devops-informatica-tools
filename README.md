# CI-CD Pipeline, Provisioning and Mainenance components for Informatica projects

## Dependencies
* Crypto module for password encryption
	pip install pycryptodome
* setuptools for upload and download of Nexus artifacts
	pip install setuptools

## Checks after installation
#### Check if encryption works:
- Create a virtualenv
- Run:  python3 supporting/encryption.py
  Output: Hello encrypted world!


## License
MIT

## Principles
### deploy lists
* All components expect a deploylist text file as input. You should keep deploylists in your source code Git. Suggested location:
<root>/<feature>/config/<deploylist> where <root> is the base location within your Git, <feature> is your submodule (if any), and <deploylist> is the text file that contains the items to be deployed.
  For example:
  <myGit>/demo/config/oracle_deploylist.txt
  <myGit>/demo/config/infa_deploylist.txt
    
### environment variables
* The python scripts use environment variables to determine locations, features and many other parameters. The environment variables that can or at times must be set can be found in:
  * generalSettings: log directory, artifact directory, configuration directory and more
  * infaSettings: deploy list location, Informatica source and target variables like INFA_HOME, location infacmd, connectivity to domain and Model Repository
  * dbSettings: deploy list location, location of sql files, sqlprefix


## Examples
Check the examples folder for more info on the structure of deploy lists.

## Implemented functions
### createOracleArtifact
Generates an ordered sql based on the deploylist.

### createDeveloperArtifact
Generates an Informatica export file and reference data zip file based on the deploylist.

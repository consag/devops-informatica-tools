envDir=/data/environment
toolsDir=${envDir}/devops-informatica-tools
venv=devops-informatica-venv-linux
testDir=${toolsDir}/tests
export SCHEDULER_DEPLOYLIST=${testDir}/scheduler_deploylist.txt
export SOURCE_SCHEDULERDIR=${testDir}
export SOURCE_SCHEDULER_TYPEDIR=${testDir}
export TARGET_SCHEDULERDIR=${testDir}/artifact/dags
export TARGET_SCHEDULER_TYPEDIR=${testDir}/artifact/plugins

. ${envDir}/scripts/python_env.sh

deactivate >/dev/null

cd $toolsDir 
source ${venv}/bin/activate

python3 createSchedulerArtifact.py


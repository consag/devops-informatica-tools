##
#
# TODO: Make this a property
venvname=devops_informatica

if [ "$0" == "-bash" ] ; then
   curDir="$(pwd)"
else
   curDir="$(dirname "$(readlink -f "$0")")"
fi

##
# Maybe the baseDir should be a property
baseDir="$(dirname ${curDir})"
echo "$(date) - $0 - baseDir is >${baseDir}<."

venvDir=${baseDir}/${venvname}
echo "$(date) - $0 - virtualenv expected to be >$venvDir<."

source $venvDir/bin/activate
cd $baseDir


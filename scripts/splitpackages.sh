##
# main variables
SOURCE_REP="$HOME/gitrepos/devops_informatica_tools"
GIT_USER_OR_ORG=jacbeekers

##
# sub routines
##
copy_files() {

  cp -p .gitignore $TARGET_REP
  cp -p .pydeps $TARGET_REP
  cp -p setup.py $TARGET_REP 
  cp -p __init__.py $TARGET_REP
  cp -p requirements.txt $TARGET_REP
  cp -p README.md $TARGET_REP
  cp -p LICENSE $TARGET_REP
  cp -pr version $TARGET_REP
  mkdir -p $TARGET_REP/temp
  mkdir -p $TARGET_REP/scripts
  cp -p scripts/build.sh $TARGET_REP/scripts
  cp -p scripts/package.sh $TARGET_REP/scripts
  cp -p scripts/generic_env.sh $TARGET_REP/scripts
  cp -p scripts/python_env.sh $TARGET_REP/scripts
  cp -p generate_docs.sh $TARGET_REP

}

do_git_stuff() {
  cd $TARGET_REP
  git init
  git add .gitignore README.md
  git commit -m "split from devops-informatica-tools"
  git remote add origin https://github.com/$GIT_USER_OR_ORG/$TARGET_REP_NAME.git
  git push -u origin master
}

copy_module() {
  python3 -c "
from public_release.module_mover import copy_modules_to_dir

copy_modules_to_dir( '$SOURCE_MODULE',
                        '$TARGET_REP',
                        scope='package',
                        root_package='$ROOT_PACKAGE')
"

}

##
# MAIN
##
cd $SOURCE_REP

# FitNesse CreateArtifact
#
#TARGET_REP_NAME="devops_fitnesse_tools"
#TARGET_REP="$HOME/gitrepos/$TARGET_REP_NAME"
#mkdir -p $TARGET_REP
#SOURCE_MODULE="cicd.createFitNesseArtifact"
#ROOT_PACKAGE="create_fitnesse_artifact"
#copy_module
#copy_files
#do_git_stuff

# Supporting
#
#TARGET_REP_NAME="devops_supporting_tools"
#TARGET_REP="$HOME/gitrepos/$TARGET_REP_NAME"
#mkdir -p $TARGET_REP
#SOURCE_MODULE="supporting"
#ROOT_PACKAGE="devops_supporting"
#copy_module
#copy_files
#do_git_stuff


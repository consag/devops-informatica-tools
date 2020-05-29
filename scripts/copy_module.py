from public_release.module_mover import copy_modules_to_dir

copy_modules_to_dir( 'cicd.createFitNesseArtifact',
                        '$HOME/gitrepos/devops_fitnesse_tools',
                        scope='package',
                        root_package='create_fitnesse_artifact')


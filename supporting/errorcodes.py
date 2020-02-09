#  MIT License
#
#  Copyright (c) 2019 Jac. Beekers
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#

##
# Errorcodes
# @Since: 22-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190322.0 - JBE - Initial

import logging
import supporting.errorcode as err

# Returncode, ErrorCode, ErrorMessage, Resolution, Area, Severity

OK = err.Errorcode(0, '0', 'No errors encountered.', 'No action needed.', 'Result', logging.INFO)
IGNORE = err.Errorcode(-1, 'GEN-0001', 'Ignored', 'No action needed.', 'Result', logging.WARNING)
##
# General errors, mostly related to environment and/or privileges
LOGDIR_NOTSET = err.Errorcode(1, 'ENV-0001', 'LOGDIR not defined', 'Set the environment variable', 'Environment',
                              logging.FATAL)
LOGDIR_NF = err.Errorcode(1, 'ENV-0002', 'LOGDIR not found', 'Set the environment variable to an existing directory',
                          'Environment', logging.FATAL)
LOGDIR_NW = err.Errorcode(1, 'ENV-0003', 'Cannot write to LOGDIR',
                          'Set the environment variable to a writeable directory', 'Environment', logging.FATAL)
FILE_NF = err.Errorcode(1, 'ENV-0004', 'Cannot find file', 'Check the file\'s path and permissions', 'Environment',
                        logging.ERROR)
FILE_NW = err.Errorcode(1, 'ENV-0005', 'Cannot write to file', 'Check the file\'s path and permissions', 'Environment',
                        logging.ERROR)
##
# General build-deploy-run related errors. Return code is 2
DEPLOYLIST_NF = err.Errorcode(2, 'GENDEPLOY-0001', 'Deploylist not found', 'Check config directory and file name.',
                              'DatabaseArtifact', logging.FATAL)
COMMAND_FAILED = err.Errorcode(2, 'GENRUN-0001', 'Command failed', 'Check command output', 'executeCommand',
                               logging.ERROR)

# Database artifact errors. Return code will be 10
NO_DEPLOYLIST = err.Errorcode(10, 'DBDEPLOY-0001', 'No dbdeploylist defined', 'Set the environment variable',
                              'DatabaseArtifact', logging.FATAL)
SOURCESQLDIR_NOTSET = err.Errorcode(10, 'DBDEPLOY-0002', 'SourceSqlDir is not defined', 'Set the environment variable',
                                    'DatabaseArtifact', logging.ERROR)
TARGETSQLDIR_NOTSET = err.Errorcode(10, 'DBDEPLOY-0003', 'TargetSqlDir is not defined', 'Set the environment variable',
                                    'DatabaseArtifact', logging.ERROR)
SQLFILE_NF = err.Errorcode(10, 'DBDEPLOY-0004', 'SQL file not found', 'Check the deploy file content',
                           'DatabaseArtifact', logging.ERROR)

##
# Directory based errors
DIRECTORY_NF = err.Errorcode(10, 'DIRDEPLOY-0001', 'Directory not found', 'Check the deploy file content',
                             'DirectoryArtifact', logging.ERROR)

##
# Database deploy errors
SQLPLUS_ERROR = err.Errorcode(10, 'DBDEPLOY-0005', 'sqlplus return an error.', 'Check the log output', 'DatabaseDeploy',
                              logging.ERROR)

# Informatica artifact errors. Return code will be 20
NOT_IMPLEMENTED = err.Errorcode(20, 'INFACICD-0001',
                                'Result unknown. Function may not have been implemented completely',
                                'Ask your developer to implement the logic completely.', 'InformaticaArtifact',
                                logging.WARNING)
INFACMD_FAILED = err.Errorcode(20, 'INFACICD-0002', 'infacmd command failed.',
                               'Check the log and/or ask your administrator.', 'InformaticaArtifact', logging.ERROR)
INFACMD_LIST_CONN_FAILED = err.Errorcode(20, 'INFACICD-0003', 'infacmd failed to list connections.',
                                         'Check the error message.', 'ListConnections', logging.ERROR)
INFACMD_LIST_CONN_OPTIONS_FAILED = err.Errorcode(20, 'INFACICD-0004', 'infacmd failed to list connection options.',
                                                 'Check the error message.', 'ListConnectionOptions', logging.ERROR)
INFACMD_NOCONNECTIONNAME = err.Errorcode(20, 'INFACICD-0005', 'No connection name provided.',
                                         'Provide a connection name for which you want the options to be listed.',
                                         'ListConnectionOptions', logging.ERROR)
INFACMD_EXPORT_CONN_FAILED = err.Errorcode(20, 'INFACICD-0006', 'Export Connections failed.',
                                           'Check the error message.', 'ExportConnections', logging.ERROR)
INFACMD_IMPORT_CONN_FAILED = err.Errorcode(20, 'INFACICD-0007', 'Import Connections failed.',
                                           'Check the error message.', 'ImportConnections', logging.ERROR)

# Informatica run errors. Return code will be 30
INFACMD_NOPROFILE = err.Errorcode(30, 'INFARUN-0001', 'No profile name provided.',
                                  'Provide the complete path of the profile to be executed.', 'RunProfile',
                                  logging.ERROR)
INFACMD_PROFILE_FAILED = err.Errorcode(30, 'INFARUN-0002', 'infacmd run profile command failed.',
                                       'Check the log and/or ask your administrator.', 'RunProfile', logging.ERROR)
INFACMD_NOSCORECARD = err.Errorcode(30, 'INFARUN-0003', 'No scorecard name provided.',
                                    'Provide the complete path of the scorecard to be executed.', 'RunScorecard',
                                    logging.ERROR)
INFACMD_SCORECARD_FAILED = err.Errorcode(30, 'INFARUN-0004', 'infacmd run scorecard command failed.',
                                         'Check the log and/or ask your administrator.', 'RunScorecard', logging.ERROR)
INFACMD_NOMAPPING = err.Errorcode(30, 'INFARUN-0005', 'No mapping provided', 'Provide the mapping you want to run.',
                                  'RunMapping', logging.ERROR)
INFACMD_NOAPPFORMAPPING = err.Errorcode(30, 'INFARUN-0006', 'Application of the mapping was not provided',
                                        'Provide the application that contains the mapping you want to run.',
                                        'RunMapping', logging.ERROR)
INFACMD_MAPPING_FAILED = err.Errorcode(30, 'INFARUN-0007', 'infacmd run mapping command failed.',
                                       'Check the log and/or ask your administrator.', 'RunMapping', logging.ERROR)
INFACMD_NOPROJECT = err.Errorcode(30, 'INFARUN-0008', 'No project name provided.',
                                  'Provide a name for the project to be created.', 'CreateProject', logging.ERROR)
INFACMD_NOFOLDER = err.Errorcode(30, 'INFARUN-0009', 'No project and/or folder name provided.',
                                 'Provide the project and a name for the folder to be created.', 'CreateFolder',
                                 logging.ERROR)
INFACMD_CREATE_FOLDER_FAILED = err.Errorcode(30, 'INFARUN-0010', 'Folder could not be created.',
                                             'Check the error message.', 'CreateFolder', logging.ERROR)
INFACMD_CREATE_PROJECT_FAILED = err.Errorcode(30, 'INFARUN-0011', 'Project could not be created.',
                                              'Check the error message.', 'CreateProject', logging.ERROR)
INFACMD_DELETE_PROJECT_FAILED = err.Errorcode(30, 'INFARUN-0012', 'Project could not be removed.',
                                              'Check the error message.', 'DeleteProject', logging.ERROR)
INFACMD_DELETE_FOLDER_FAILED = err.Errorcode(30, 'INFARUN-0012', 'Folder could not be removed.',
                                             'Check the error message.', 'DeleteFolder', logging.ERROR)
INFACMD_NOWORKFLOW = err.Errorcode(30, 'INFARUN-0013', 'No application, workflow and/or wait provided',
                                   'You need to specify the application name, workflow and whether to wait (true) or not (false).',
                                   'RunWorkflow', logging.ERROR)
INFACMD_WORKFLOW_FAILED = err.Errorcode(30, 'INFARUN-0014', 'Workflow failed.', 'Check the error message and logs.',
                                        'RunWorkflow', logging.ERROR)

##
# Manage Security errors
INFACMD_NOUSERNAME = err.Errorcode(30, 'INFASEC-0001', 'No user name, password and/or full name provided.',
                                   'Provide a name, password, and full name for the user to be created.', 'CreateUser',
                                   logging.ERROR)
INFACMD_NOUSERNAME_DELETION = err.Errorcode(30, 'INFASEC-0002', 'No user name provided.',
                                            'Provide the username to be deleted.', 'DeleteUser', logging.ERROR)
INFACMD_NOEXPORTFILENAME = err.Errorcode(30, 'INFASEC-0003', 'No export file name provided.',
                                         'Provide the name for the export file.', 'ExportUsersAndGroups', logging.ERROR)
INFACMD_NOIMPORTFILENAME = err.Errorcode(30, 'INFASEC-0004', 'No import file name provided.',
                                         'Provide the name of the file to be imported.', 'ImportUsersAndGroups',
                                         logging.ERROR)
INFACMD_CREATE_USER_FAILED = err.Errorcode(30, 'INFASEC-0005', 'User creation failed.', 'Check the error message.',
                                           'CreateUser', logging.ERROR)
INFACMD_DELETE_USER_FAILED = err.Errorcode(30, 'INFASEC-0006', 'User deletion failed.', 'Check the error message.',
                                           'DeleteUser', logging.ERROR)
INFACMD_CREATE_GROUP_FAILED = err.Errorcode(30, 'INFASEC-0007', 'Group creation failed.', 'Check the error message.',
                                            'CreateGroup', logging.ERROR)
INFACMD_DELETE_GROUP_FAILED = err.Errorcode(30, 'INFASEC-0018', 'Group deletion failed.', 'Check the error message.',
                                            'DeleteGroup', logging.ERROR)
INFACMD_EXPORT_USRGRP_FAILED = err.Errorcode(30, 'INFASEC-0019', 'Users and groups export failed.',
                                             'Check the error message.', 'ExportUsersAndGroups', logging.ERROR)
INFACMD_IMPORT_USRGRP_FAILED = err.Errorcode(30, 'INFASEC-0020', 'Users and groups import failed.',
                                             'Check the error message.', 'ImportUsersAndGroups', logging.ERROR)
INFACMD_ADD_PERM_FAILED = err.Errorcode(30, 'INFASEC-0021', 'Permissions could not be added.',
                                        'Check the error message.', 'AddPermissions', logging.ERROR)
INFACMD_REMOVE_PERM_FAILED = err.Errorcode(30, 'INFASEC-0023', 'Permissions could not be remvoed.',
                                           'Check the error message.', 'RemovePermissions', logging.ERROR)
INFACMD_SET_CONN_FAILED = err.Errorcode(30, 'INFASEC-0024', 'Permissions could not be set.', 'Check the error message.',
                                        'SetPermissions', logging.ERROR)
INFACMD_NOGROUPNAME = err.Errorcode(30, 'INFASEC-0025', 'No group name provided.',
                                    'Provide a name for the group to be created.', 'CreateGroup', logging.ERROR)
INFACMD_NOGROUPNAME_DELETION = err.Errorcode(30, 'INFASEC-0026', 'No group name provided.',
                                             'Provide the name of the group to be deleted.', 'DeleteGroup',
                                             logging.ERROR)

##
# Scheduler artifact errors
INVALID_SCHEDULER_ENTRY_TYPE = err.Errorcode(40, 'SCHDEPLOY-0001', 'Invalid scheduler entry type.',
                                             'Provide a valid scheduler entry type, eg. dags, jobascode, plugin. Check schedulerConstants.py for more.',
                                             'SchedulerArtifact', logging.ERROR)
SCHEDULERFILE_NF = err.Errorcode(41, 'SCHDEPLOY-0002', 'Scheduler file not found.',
                                 'Provide a valid scheduler file. Check the scheduler deploy list.',
                                 'SchedulerArtifact', logging.ERROR)

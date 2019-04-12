##
# generalSettings
# @Since: 22-MAR-2019
# @Author: Jac. Beekers
# @Version: 20190410.0 - JBE - Initial
##

import informaticaArtifact.developer as developer
import informaticaArtifact as infa
import supporting
import logging, datetime

logger = logging.getLogger(__name__)

def main():
    thisproc = "MAIN"
    mainProc='CreateDeveloperArtifact'

    supporting.configurelogger(mainProc)
    logger = logging.getLogger(mainProc)
    error = 0

    supporting.log(logger, logging.DEBUG, thisproc, 'started')
    infa.getInfaEnvironment()

    output, error = developer.Export(
        InfaPath=infa.sourceInfacmd,
        Tool="Export",
        Domain=infa.sourceDomain,
        Repository=infa.sourceModelRepository,
        Project="Demo",
        FilePath="/tmp/Demo_Export.xml",
        OverwriteExportFile="true"
    )
    if output:
        supporting.log(logger, logging.INFO, thisproc, "output (if any) =>" + output.decode('utf-8') + "<.")
    #
    if error:
        supporting.log(logger, logging.INFO, thisproc, "error (if any) =>" + str(error) + "<.")

    supporting.log(logger, logging.DEBUG, thisproc, 'completed with rc =>' + str(error) + "<.")
    return (error)


main()

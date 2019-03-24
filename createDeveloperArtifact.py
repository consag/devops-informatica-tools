import IDQScripts.IDQ as idq


def main():
    print(idq.Export(
        InfaPath="$INFA_HOME/server/bin/infacmd.sh",
        Tool="Export",
        Domain="Dom_Demo",
        Repository="MRS_Demo",
        Project="Demo",
        FilePath="/tmp/Demo_Export.xml",
        OverwriteExportFile="true"
    ))

    return ()

main()

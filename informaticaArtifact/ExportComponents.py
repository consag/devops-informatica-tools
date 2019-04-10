import informaticArtifact.developer as IDQ


def main():


    IDQDEV = {
        "Path": "$INFA_HOME/server/bin/infacmd.sh",
        "Domain": "Domain_Demo",
        "Repository": "MRS_Demo",
    }

    filepath = "/tmp/"
    ExportFileName = "exp_Demo.xml"
    ExportFilePath = filepath + ExportFileName
    InfaComponents = []



    IDQ.Import(
        InfaPath = "$INFA_HOME/server/bin/infacmd.sh",
        Tool = "Export",
        Domain = "Domain_Demo",
        Repository = "MRS_Demo",
        Project = "Demo",
        FilePath = ExportFilePath,
        OverwriteExportFile = "true"
    )



    return()


if __name__ == '__main__':

    main()

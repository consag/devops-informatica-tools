
import informaticaArtifact.developer as IDQ

	
def main():


	filepath = "/tmp/"
	ExportFileName = "exp_Demo.xml"
	ExportFilePath = filepath + ExportFileName

	

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

main()

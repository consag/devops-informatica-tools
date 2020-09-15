Module cicd.deploySchedulerArtifact
===================================

Classes
-------

`DeploySchedulerArtifact(argv, log_on_console=True)`
:   Deploys an artifact with Schedules

    ### Methods

    `parse_the_arguments(self, arguments)`
    :   Parses the provided arguments and exits on an error.
        Use the option -h on the command line to get an overview of the required and optional arguments.

    `runit(self, arguments)`
    :   Deploys a scheduler artifact.
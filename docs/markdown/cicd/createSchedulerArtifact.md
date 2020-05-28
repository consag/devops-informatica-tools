Module cicd.createSchedulerArtifact
===================================

Classes
-------

`CreateSchedulerArtifact(argv, log_on_console=True)`
:   Creates an artifact with Schedules from file system

    ### Methods

    `parse_the_arguments(self, arguments)`
    :   Parses the provided arguments and exits on an error.
        Use the option -h on the command line to get an overview of the required and optional arguments.

    `runit(self, arguments)`
    :   Creates a scheduler artifact.
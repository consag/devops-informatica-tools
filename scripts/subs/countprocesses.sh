countProcesses() {
  cntProcs=$(ps -ef | grep $(whoami) | grep -v grep | grep -c "$INFA_VERSION")
}


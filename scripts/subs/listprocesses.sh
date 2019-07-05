listProcesses() {
  ps -ef | grep $(whoami) | grep -v grep | grep "$INFA_VERSION"
}


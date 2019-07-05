#!/bin/bash
##
# Set environment
curDir="$(dirname "$(readlink -f "$0")")"
. ${curDir}/informatica_env.sh
##
# Defaults
minProcs=4
timeoutStop=300  # in seconds

##
# subs
. ${curDir}/subs/countprocesses.sh
. ${curDir}/subs/listprocesses.sh

listProcesses() {
  ps -ef | grep $(whoami) | grep -v grep | grep "$INFA_VERSION"
} 

stopInformatica() {
  local rc=0
  echo "$(date) - Requesting shutdown of Informatica >$INFA_VERSION<. Please wait..."
  infaservice.sh shutdown
  rc=$?
  if [ $rc -ne 0 ] ; then
     echo "$(date) - infaservices.sh shutdown failed. There should be an error message above this message."
  else
     echo "$(date) - Request to shutdown Informatica was well received." 
  fi
  return $rc
}

checkInformatica() {
 local timeout=$1  # in seconds
 local currentTry=1
 local sleepTime=10
 local nrTries=$(( $timeout / $sleepTime))
 countProcesses
 prevCnt=-1
 while [ $cntProcs -gt 0 ] && [ $currentTry -le $nrTries ] ; do
   if [ $prevCnt -eq $cntProcs ] ; then
      echo -n "."
   else
      prevCnt=$cntProcs
      echo ""
      if [ $cntProcs -eq 1 ] ; then
         echo -n "$(date) - There is >$cntProcs< process running. Please wait..." 
      else
         echo -n "$(date) - There are >$cntProcs< processes running. Please wait..." 
      fi
   fi
   sleep $sleepTime
   ((currentTry++))
   countProcesses
 done
 
}

## MAIN
#
countProcesses
if [ $cntProcs -eq 0 ] ; then
   echo "$(date) - It seems Informatica is not running." 
   echo "$(date) - Cannot shutdown Informatica because Informatica version >$INFA_VERSION< seems to be down."
else
   stopInformatica
   rc=$?
   if [ $rc -eq 0 ] ; then
     checkInformatica $timeoutStop
     echo ""
   fi
fi
echo "$(date) - Done." 

   


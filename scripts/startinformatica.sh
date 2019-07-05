#!/bin/bash
##
# Set environment
curDir="$(dirname "$(readlink -f "$0")")"
. ${curDir}/informatica_env.sh

# Defaults
minProcs=4
timeoutStart=600  # in seconds

##
# subs
. ${curDir}/subs/countprocesses.sh
. ${curDir}/subs/listprocesses.sh

startInformatica() {
  local rc=0
  echo "$(date) - Requesting startup of Informatica >$INFA_VERSION<. Please wait..."
  infaservice.sh startup  
  rc=$?
  if [ $rc -ne 0 ] ; then
     echo "$(date) - infaservices.sh startup failed. There should be an error message above this message."
  else
     echo "$(date) - Request to start Informatica was well received." 
  fi
  return $rc
}

checkInformatica() {
 local minProcs=$1
 local timeout=$2  # in seconds
 local currentTry=1
 local sleepTime=10
 local nrTries=$(( $timeout / $sleepTime))
 countProcesses
 prevCnt=-1
 while [ $cntProcs -lt $minProcs ] && [ $currentTry -le $nrTries ] ; do
   if [ $prevCnt -eq $cntProcs ] ; then
      echo -n "."
   else
      if [ $cntProcs -eq 0 ] ; then
         echo ""
         echo "$(date) - Start was not successful. Please check logs in >$INFA_HOME/logs<" 
         break
      fi
      prevCnt=$cntProcs
      echo ""
      if [ $cntProcs -eq 1 ] ; then
         echo -n "$(date) - There is >$cntProcs< process running. Minimum is >$minProcs<. Please wait..." 
      else
         echo -n "$(date) - There are >$cntProcs< processes running. Minimum is >$minProcs<. Please wait..." 
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
if [ $cntProcs -gt 0 ] ; then
   echo "$(date) - It seems Informatica is already running. Check process list:" 
   listProcesses
   echo "$(date) - Cannot start Informatica because Informatica version >$INFA_VERSION< seems to be up."
else
   startInformatica
   rc=$?
   if [ $rc -eq 0 ] ; then
     checkInformatica $minProcs $timeoutStart
     echo ""
     if [ $cntProcs -eq 0 ] ; then
        echo "$(date) - Could not start Informatica version >$INFA_VERSION<." 
     else
        if [ $cntProcs -lt $minProcs ] ; then
           echo "$(date) - Informatica startup may be incomplete. >$cntProcs< process(es) started, minimum expected is >$minProcs<." 
        else
           echo "$(date) - Informatica started. >$cntProcs< are running."
        fi
     fi
   fi
fi

   


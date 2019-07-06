#!/bin/bash
##
# @version: 20190705.0 # Jac. Beekers
##
# Overall document: https://kb.informatica.com/solution/23/Documents/AdminToolHTTPS3rdParty.pdf
# Most of the tasks mentioned in this pdf are done by the generate_informatica_keystores.sh, so start with Step 4
##
# environment
curDir="$(dirname "$(readlink -f "$0")")"

. ${curDir}/informatica_env.sh
. ${curDir}/security_env.sh
. ${curDir}/infa_domain_settings.sh

##
# sub procedures
##
. ${curDir}/subs/getinfakeystorepassword.sh
. ${curDir}/subs/countprocesses.sh

echo "Informatica must be down before you continue!"
countProcesses
if [ $cntProcs -gt 0 ] ; then
   echo "$(date) - $0 - Found >$cntProcs< process(es) running for version >$INFA_VERSION<"
   echo "$(date) - $0 - Cannot continue."
   exit 1
fi

getInfakeystorePassword
infasetup.sh UpdateGatewayNode -HttpsPort 0


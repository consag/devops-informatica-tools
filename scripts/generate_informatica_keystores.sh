#!/bin/bash
##
# @Version: 20190705.0 # Jac. Beekers

##
# Get environment
curDir="$(dirname "$(readlink -f "$0")")"
. ${curDir}/informatica_env.sh
. ${curDir}/security_env.sh

which keytool
which openssl

##
# Return codes
rcPemKeystoreExists=10
rcPemTruststoreExists=11
rcMissingExportPassword=12
rcMissingInfakeystorePassword=13

##
# Most information was taken from https://kb.informatica.com/h2l/HowTo%20Library/1/0700-CreateKeystoresAndTruststores-H2L.pdf
##
##
# Script assumes:
# 1. you've created your key (and csr) and already have your certificate
# 2. the key file is called <hostname>.key
# 3. the certificate file is called <hostname>.cer and is in PEM format
# 4. key and certificate files are located in $certificateLocation (check security_env.sh)
##
# Note: The password of the key and the password of the keystore file MUST be the same!

##
# file names
cerFile=${certificateLocation}/${thisHost}.cer
keyFile=${certificateLocation}/${thisHost}.key
pemKeystoreFile=${certificateLocation}/infa_keystore.pem
p12File=${certificateLocation}/keystore.p12
infaKeystore=${certificateLocation}/infa_keystore.jks
#
pemTruststoreFile=${certificateLocation}/infa_truststore.pem
infaTruststore=${certificateLocation}/infa_truststore.jks

##
# sub procs
##
#. ${curDir}/subs/getexportpassword.sh
. ${curDir}/subs/getinfakeystorepassword.sh
. ${curDir}/subs/getinfatruststorepassword.sh

##
# infa_keystore
##
# Create Informatica keystore in PEM format containing both key and certificate
if [ -f ${pemKeystoreFile} ] ; then
   echo "$(date) - $0 - File >${pemKeystoreFile}< already exists. Cannot proceed."
   exit $rcPemKeystoreExists
fi 
cat ${cerFile} > ${pemKeystoreFile}
echo "" >> ${pemKeystoreFile}
cat ${keyFile} >> ${pemKeystoreFile}

##
# Convert PEM to PKCS12
getInfakeystorePassword
if [ -z "$infakeystorePassword" ] ; then
   echo "$(date) - Cannot find Informatica keystore password. Cannot continue."
   exit $rcMissingInfakeystorePassword
fi
export infakeystorePassword
openssl pkcs12 -export -in ${pemKeystoreFile} -out ${p12File} -name "informatica" -passout env:infakeystorePassword

##
# Convert PKCS to JKS

keytool -v -importkeystore -srckeystore ${p12File} -srcstoretype PKCS12 -destkeystore ${infaKeystore} -deststoretype JKS -srcalias "informatica" -destalias "informatica" -srcstorepass $infakeystorePassword -deststorepass $infakeystorePassword -noprompt

##
# infa_truststore
##
if [ -f ${pemTruststoreFile} ] ; then
   echo "$(date) - $0 - File >${pemTruststoreFile}< already exists. Cannot proceed."
   exit $rcTrustKeystoreExists
fi 
cat ${cerFile} >> ${pemTruststoreFile}
#
##
# Create truststore in JKS format
getInfatruststorePassword
if [ -z "$infatruststorePassword" ] ; then
   echo "$(date) - Cannot find Informatica truststore password. Cannot continue."
   exit $rcMissingInfatruststorePassword
fi
export infatruststorePassword
keytool -importcert -file ${pemTruststoreFile} -keystore ${infaTruststore} -alias "informatica" -deststoretype JKS -v -trustcacerts -srcstorepass $infakeystorePassword -deststorepass $infatruststorePassword -noprompt
#


curDir="$(dirname "$(readlink -f "$0")")"
. ${curDir}/generic_env.sh

securityLocation=/data/security
certificateLocation=${securityLocation}/certs

##
# for informatica command line utilities
# encryption through pmpasswd
INFA_TRUSTSTORE_PASSWORD=<something_encrypted>
INFA_TRUSTSTORE=${certificateLocation}/infa_truststore.jks

##
# for scripts
infaKeystore=${certificateLocation}/infa_keystore.jks
infaTruststore=${certificateLocation}/infa_truststore.jks


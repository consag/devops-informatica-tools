##
#
curDir="$(dirname "$(readlink -f "$0")")"
. ${curDir}/security_env.sh

rm ${certificateLocation}/infa_keystore.pem
rm ${certificateLocation}/infa_keystore.jks
rm ${certificateLocation}/infa_truststore.pem
rm ${certificateLocation}/infa_truststore.jks

##
# @version: 20190707.0 # Jac. Beekers
# @license: MIT
##

encrypt_usingtmpcert() {
data="$1"
encryptedFile="$2"
keyInstance="$3"
if [ -z "$keyInstance" ] ; then
   keyInstance=0
fi

python3 <<EOF
import os
from supporting import encryption
encryption = encryption.Encryption()
encrypted = encryption.encrypt_with_certificates("$data", "$keyInstance", "$encryptedFile")
EOF

}



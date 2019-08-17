##
# @version: 20190706.0 # Jac. Beekers
# @license: MIT
##

cleancrypt_usingtmpcert() {
keyInstance="$1"
if [ -z "$keyInstance" ] ; then
   keyInstance=0
fi

python3 <<EOF
import os
from supporting import encryption
encryption = encryption.Encryption()
encrypted = encryption.cleanup("$keyInstance")
EOF

}



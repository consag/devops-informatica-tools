##
# @version: 20190706.0 # Jac. Beekers
# @license: MIT
##

decrypt_usingtmpcert() {
encryptedFile="$1"
keyInstance="$2"
if [ -z "$keyInstance" ] ; then
   keyInstance=0
fi

  python3 <<EOF
from supporting import encryption
encryption = encryption.Encryption()
decrypted = encryption.decrypt_with_certificates($keyInstance, "${encryptedFile}")
print(decrypted)
EOF

}



##
# @version: 20190706.0 # Jac. Beekers
# @license: MIT
##

decrypt() {
  encryptedFile="$1"
  python3 <<EOF
from supporting import encryption
encryption = encryption.Encryption()
decrypted = encryption.decrypt_with_certificates("${encryptedFile}")
print(decrypted)
EOF

}



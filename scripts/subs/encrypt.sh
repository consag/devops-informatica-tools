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
from supporting import encryption
encryption = encryption.Encryption()
encrypted = encryption.encrypt_with_certificates("$data", "$keyInstance", "$encryptedFile")
EOF

}

##
# using cryptography https://stackoverflow.com/questions/2490334/simple-way-to-encode-a-string-according-to-a-password
get_key() {
theKey=$(python3 <<EOF
from supporting import encryption
encryption = encryption.Encryption()
the_key = encryption.get_key()
print(the_key)
EOF
)
}

encrypt() {
 theKey="$1"
 data="$2"
theEncryptedValue=$(python3 <<EOF
from supporting import encryption
encryption = encryption.Encryption()
encrypted = encryption.encrypt("$data", "$theKey")
print(encrypted)
EOF
)

}


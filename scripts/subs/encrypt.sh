##
# @version: 20190706.0 # Jac. Beekers
# @license: MIT
##

encrypt() {
outfile="$1"
python3 <<EOF
import os
from supporting import encryption
encryption = encryption.Encryption()
data = "Hello from $0"
encrypted = encryption.encrypt_with_certificates(data, "$outfile")
EOF

}



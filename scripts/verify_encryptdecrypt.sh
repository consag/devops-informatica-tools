##
# check that shell scripts can use the python encrypt/decrypt module
##
# @version: 20190706.0 $# Jac. Beekers
# @license: MIT

##
# Assumptions
# 1. A python virtualenv exists

##
# Setup environment
curDir="$(dirname "$(readlink -f "$0")")"
. ${curDir}/python_env.sh
#source ../devops_informatica/bin/activate
#cd ..

##
# init
rc=0
overallRC=0
cntTotal=0
cntSuccess=0
cntFailure=0

check() {
  (( cntTotal++ ))
  if [ $rc -eq 0 ] ; then
     echo "$(date) - $0 - SUCCESS"
     (( cntSuccess++ ))
  else
     echo "$(date) - $0 - FAILURE"
     (( cntFailure++ ))
  fi
  if [ $overallRC -eq 0 ] ; then
     overallRC=$rc
  fi
}

##
# Tests
echo "$(date) - $0 - Running encryption self-check..."
#python ${baseDir}/supporting/encryption.py
python <<EOF
from supporting import encryption
encryption.verify()
EOF
rc=$?
check

##
#
echo "$(date) - $0 - Running encryption through bash..."
. ${curDir}/subs/encrypt.sh
outfile="$$.enc.tmp"
keyInstance=$$
encrypt_usingtmpcert "hello from process >$$< of script $0" "$outfile" $keyInstance
rc=$?
check

echo "$(date) - $0 - Running decryption through bash..."
. ${curDir}/subs/decrypt.sh
decrypt_usingtmpcert "$outfile" $keyInstance
rc=$?
check

echo "$(date) - $0 - Cleanup decryption through bash..."
. ${curDir}/subs/cleancrypt.sh
cleancrypt_usingtmpcert $keyInstance
rc=$?
check

rm $outfile

##
# Fernet encryption checks - Using cryptography
echo "$(date) - $0 - Fernet check - Getting key through bash..."
. ${curDir}/subs/encrypt.sh
get_key
rc=$?
check
#echo "$theKey"
echo "$(date) - $0 - Fernet check - Encrypting Hello message..."
encrypt "$theKey" "Hello from $0"
rc=$?
check
#echo "$theEncryptedValue"

. ${curDir}/subs/decrypt.sh
echo "$(date) - $0 - Fernet check - Decrypting Hello message..."
decrypt "$theKey" "$theEncryptedValue"
rc=$?
check
echo "$theValue"

##
# End result
##
if [ $overallRC -eq 0 ] ; then
   echo "$(date) - $0 - Overall SUCCESS. >$cntTotal< test(s) succeeded."
else
   echo "$(date) - $0 - Overall FAILURE. >$cntFailure< test(s) out of >$cntTotal< failed."
fi


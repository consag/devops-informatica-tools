. ./oracle_env.sh

userpwdfile=change_pwd.txt
newpwdfile=newpwds.txt

currentTS=$(date +"%Y%m%d-%H%M%S")

while read -r l ; do
    IFS=' ' read -ra ARGS <<< $l
    userId="${ARGS[0]}"
    if [ -z "$userId" ] ; then
       continue
    fi
    dbName="${ARGS[1]}"
    oldP="${ARGS[2]}"
    nrForPwd=$(date +"%j%N")
    newP="PodRacers.#$nrForPwd"
    echo "$currentTS|$dbName|$userId|$newP" >> $newpwdfile
    echo "$(date) - Changing password for user >$userId< in database >$dbName<..."
    echo "$(date) - New password will be >$newP<."
    sqlplus /nolog << EOF
    connect $userId/$oldP@$dbName
    alter user $userId identified by "$newP" replace $oldP;
EOF
done < $userpwdfile


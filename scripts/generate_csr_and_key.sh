#!/bin/bash
##
curDir="$(dirname "$(readlink -f "$0")")"
. ${curDir}/security_env.sh

keyFile=${certificateLocation}/${thisHost}.key
csrFile=${certificateLocation}/${thisHost}.csr

openssl req -new -newkey rsa:2048 -nodes -keyout ${keyFile} -out ${csrFile} -subj "/C=NL/ST=Dummy/L=Dummy/O=Dummy/OU=Dummy/CN=${thisHost}"


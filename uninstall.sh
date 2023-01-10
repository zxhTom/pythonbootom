DIR=$( dirname "$(readlink -f  ${BASH_SOURCE[0]})" )
rm -rf ${DIR}/{build,dist,zxhtom.egg-info}

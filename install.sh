DIR=$( dirname "$(readlink -f  ${BASH_SOURCE[0]})" )
cd ${DIR}
sh uninstall.sh
python3 setup.py sdist bdist_wheel
cd dist
pip3 install zxhtom-0.0.1.tar.gz

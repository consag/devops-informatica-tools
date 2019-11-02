alias python=python3
##
echo "creating virtual environment"
python3 -m venv venv
source venv/bin/activate
##
echo "upgrading pip to get rid of the annoying 'you should blabla'"
pip install --upgrade pip
##
##
echo "preparing for build"
python3 -m pip install --upgrade setuptools wheel
##
echo "prepare for upload"
python3 -m pip install --upgrade twine
pip3 install keyring
##
echo "building"
echo "=-=-=--=-==---=-=-=-=---=-=-=-=-=-=-=-"
rm -rf dist/*
python3 setup.py sdist bdist_wheel
rc=$?
if [ $rc -eq 0 ] ; then
   echo "Uploading to test.pypi.org..."
   python3 -m twine upload --sign --repository-url https://test.pypi.org/legacy/ dist/*
fi


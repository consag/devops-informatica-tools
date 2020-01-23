alias python=python3
##
echo "Uploading to the real pypi !!!"
echo "Make sure you have a build to upload."
echo "The distribution directory will be uploaded. It contains:"
ls -la dist/*

source venv/bin/activate

echo "Uploading to pypi.org..."
python3 -m twine upload --sign dist/*
rc=$?
if [ $rc -eq 0 ] ; then
   echo "Updating version number for git..."
   if [ -f temp/_tmp_version.tmp ] ; then
      cp -p temp/_tmp_version.tmp plugins/__init__.py
      git add plugins/__init__.py
      git commit -m "$(cat plugins/__init__.py) now on pypi."
      git push
   else
      echo "new version file not found. version number not changed in git."
   fi
else
   echo "Version not changed as upload was not successful."
fi


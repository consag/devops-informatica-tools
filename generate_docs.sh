thisDir=$(pwd)
for f in cicd/*.py execution/*.py supporting/*.py scripts/*.py ; do
  if [ $(basename $f) == "setup.py" ] ; then
     continue
  fi
  module=$(echo "$(basename $f)" | cut -d"." -f1)
  dir=$(dirname $f)
  pydoc3 $module > docs/text/${module}.txt
  echo "IMPORTS" >> docs/text/${module}.txt
  while read -r line ; do
     echo "    $line" >> docs/text/${module}.txt
  done < <(grep -e "^import" -e "^from.*import" $f)
  pydoc3 -w $f
  mv ${module}.html ${thisDir}/docs/html/
done


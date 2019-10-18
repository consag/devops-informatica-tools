for f in *.py ; do
  if [ $f == "setup.py" ] ; then
     continue
  fi
  module=$(echo "$f" | cut -d"." -f1)
  pydoc3 $module > docs/text/${module}.txt
  echo "IMPORTS" >> docs/text/${module}.txt
  while read -r line ; do
     echo "    $line" >> docs/text/${module}.txt
  done < <(grep -e "^import" -e "^from.*import" $f)
  pydoc3 -w $module 
  mv ${module}.html docs/html/
done


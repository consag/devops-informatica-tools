for f in *.py ; do
  module=$(echo "$f" | cut -d"." -f1)
  pydoc3 $module > docs/text/${module}.txt
  pydoc3 -w $module 
  mv ${module}.html docs/html/
done


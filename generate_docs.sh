source venv/bin/activate
pip3 install pdoc3 pydeps >/dev/null
#
PACKAGE_NAME=cicd
#
pdoc3 --force --output-dir docs/markdown $PACKAGE_NAME
pdoc3 --force --html --output-dir docs/html $PACKAGE_NAME
#
# generate dependency graph
pydeps --log ERROR $PACKAGE_NAME


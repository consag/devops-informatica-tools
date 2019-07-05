##
# Set Java to an OpenJDK to avoid certificate issues you get when running IBM JDK or Oracle JDK (licensed separately)
JAVA_HOME=/data/tooling/jdk/current
export JAVA_HOME
PATH=${JAVA_HOME}/bin:${PATH}
export PATH


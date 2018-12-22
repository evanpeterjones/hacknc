python_version=`python3 --version`
appname='post.py'
cred='credentials.dat'

if [[ python_version == "Python 3"* ]];
then
    PY_DIR=`python3 -c 'import sys; print(sys.path[2])'`
    #chmod +x $appname
    sudo cp $appname $PY_DIR
    echo copied $appname into $PY_DIR
    sudo cp $cred $PY_DIR
    echo copied $cred into $PY_DIR
else
    echo shit
fi

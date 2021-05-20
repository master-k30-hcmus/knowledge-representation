SRC_FILE="app"
DST_FILE=$SRC_FILE"_ui"

echo "export from" $SRC_FILE "to" $DST_FILE
../venv/Lib/site-packages/QtDesigner/uic.exe ../app/ui/$SRC_FILE.ui -o ../app/ui/$DST_FILE.py -g python
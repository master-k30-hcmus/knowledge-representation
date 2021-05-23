SRC_NAME="main"
APP_NAME="chemistry-lab_Nhom07"

DEBUG=false
while [ "$#" -gt 0 ]; do
    case "$1" in
        -d|--debug)
            APP_NAME="debug"
            DEBUG=true
            echo "DEBUG MODE ON"
            shift
            ;;
    esac
done

OUTPUT_DIR="../$APP_NAME"
mkdir -p "$OUTPUT_DIR"
echo "OUTPUT_DIR=" $OUTPUT_DIR

echo "Export $APP_NAME.exe"
if "$DEBUG"; then
  pyinstaller ../app/$SRC_NAME.py --name $APP_NAME --clean --onefile --console --distpath $OUTPUT_DIR --workpath $OUTPUT_DIR --specpath $OUTPUT_DIR
else
  pyinstaller ../app/$SRC_NAME.py --name $APP_NAME --clean --onefile --noconsole --distpath $OUTPUT_DIR --workpath $OUTPUT_DIR --specpath $OUTPUT_DIR
fi

echo "Remove support files"
cp "$OUTPUT_DIR/$APP_NAME.exe" "../"
rm -r "$OUTPUT_DIR"
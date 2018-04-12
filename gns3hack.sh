#!/bin/env bash
set -e
#USER=$(logname)
current_dir=${PWD}
#gns3_images_dir="/home/$USER/GNS3/images"
#gns3_projects_dir="/home/$USER/GNS3/projects"
#gns3_configs_dir="/home/$USER/GNS3/configs"
#gns3_gui_conf="/home/$USER/.config/GNS3/gns3_gui.conf"

_usage() {
    printf "%s\n\n" "Usage: gns3hack [OPTIONS] <values> .."
    printf "%s\n" "OPTIONS:"
    printf "  %s\t\t%s\n" "-f, --font-type" "Change note font-family"
    printf "  %s\t\t%s\n" "-c, --font-color" "Change note font color"
    printf "  %s\t\t%s\n" "-s, --font-size" "Change note font size"
    printf "  %s\t\t%s\n" "-F, --afont-type" "Change appliance font-family"
    printf "  %s\t\t%s\n" "-C, --afont-color" "Change appliance font color"
    printf "  %s\t\t%s\n" "-S, --afont-size" "Change appliance font size"
    printf "  %s\t\t\t%s\n" "-k, --key" "Generate IOU license key"
    printf "  %s\t\t\t%s\n" "-i, --image" "Change images (IOU,IOS,qemu,vbox,..) used by a  project(s)"
    printf "  %s\t\t\t%s\n" "-m, --symbol" "Change router,switch,etc.. symbol(icon)"
    printf "  %s\t\t%s\n" "--li, --list-image" "List images (IOU,IOS,qemu,vbox,..) used by a project(s)"
    printf "  %s\t\t%s\n" "--ls, --list-symbol" "List symbols used by a project"
    printf "  %s\t\t%s\n" "--lf, --list-font" "List current note font(s) used by a project"
    printf "  %s\t\t%s\n" "--lF, --list-afont" "List current appliance font(s) used by a project"
    printf "\n%s\n" "EXAMPLES:"
    printf "%s\t%s\n"  "Get information about a project(s)"
    printf "  %s\t%s\n"  "  cd ~/gns3/project/project_name" "# cd to your gns3 project folder"
    printf "  %s\t\t\t%s\n"  "  gns3hack.sh --li" "# get images names used by a project"
    printf "  %s\t\t\t%s\n"  "  gns3hack.sh --lf" "# get note font properties used by a project"
    printf "  %s\t\t\t%s\n"  "  gns3hack.sh --lF" "# get appliance font properties used by a project "
    printf "  %s\t\t\t%s\n"  "  gns3hack.sh --ls" "# get devices symbols used by a project"
    printf "\n"

    printf "%s\t%s\n"  "Change/Replace image used by a project"
    printf "  %s\t%s\n"  "  1. cd ~/gns3/project/project-name" "# cd to your gns3 project folder"
    printf "  %s\t%s\n"  "  2. gns3hack --li" "# List current project images and choose image to replace"
    printf "  %s\t%s\n"  "  3. gns3hack -i \"i86bi-linux-l3-adventerprisek9-15.4.2T4.bin\" \"i86bi-linux-l3-adventerprisek9-15.5.2T.bin\"" "# Replace the image"
    printf "  %s\n"  "  4. restart gns3"
    printf "%s\n"   "To change all projects images, cd to main project directory instead of specific project directory in step 1 "
    printf "%s"   "Note: Any new image(s) must be added to gns3 and installed to the same directory as the old one, "
    printf "%s"  "if you dont add the new image(s), you'll receive this error message 'The image image-name is missing'. "
    printf "%s"    "This is a very good option if you want to test new image(s) on an existing project(s) and revert back, "
    printf "%s\n"    "or you have new working image(s) and you want to use it for all of your projects"
    printf "\n"
}
if [ $# -lt 1 ]; then
	echo "$0: missing option"
	echo "Try '$0 --help' for more information."
	exit 1
fi
_backup() {
    find $gns3_projects_dir -type f -name '*.gns3' -exec $SHELL -c '[[ ! -f "{}".bak ]] && cp -a "{}" "{}".bak' \;
}
_isemptyproject () {
    if [ "$?" -ne 0 ]; then
        echo "Couldn't find any images..."
    fi
}
_isimageexist () {
    find "$current_dir" -name "*.gns3" -type f -exec grep -oP -m 1 "(?<=\"path\":\ )\"$1\"" "{}" \+
    if [ "$?" -ne 0 ]; then
       echo "Image does not exist '$1'" 
       exit 101
   fi
   if [ -z "$1" ]; then
       oldimage='\"\"'
       newimage="\"$newimage\""
   fi
}
_issymbolexist () {
    find "$current_dir" -name "*.gns3" -type f -exec grep -oP -m 1 "(?<=\"symbol\":\ )\"$1\"" "{}" \+
    if [ "$?" -ne 0 ]; then
       echo "Symbol does not exist: $1" 
       exit 102 
   fi
   if [ -z "$1" ]; then
       oldSymbol='\"\"'
       newSymbol="\"$newSymbol\""
   fi
}
# Check passing number of arguments
_numofargs () {
    if [ "$1" -ne 3 ]; then
        echo "ERROR!: Too many arguments"
        echo "Try './gns3hack.sh --help' for more information"
        exit 100 
    fi
}
_ioukeygen () {
    echo "start generation IOU license key"
    hostid=$(hostid)
    ioukey=$((16#$hostid))
    hostname=$(hostname)
    sum=0
    for (( i=0; i < ${#hostname}; i++ ))
    do
        hostchar="${hostname:$i:1}"       # loop through host string
        # convert ascii char to its equivalent value
        hostascii=$(printf "%d" "'$hostchar")    
        (( sum += $hostascii ))
    done 
    (( ioukey += sum ))
    # convert ioukey to hex
    ioukey=$(printf "%x" $ioukey)
    #convert ioukey to its equivalent ascii char
    ioukey=$(echo $ioukey | xxd -r -p)
    # create the license using md5sum
    ioupad1=$'\x4B\x58\x21\x81\x56\x7B\x0D\xF3\x21\x43\x9B\x7E\xAC\x1D\xE6\x8A'
    ioulicense=$(printf '%b' "$ioupad1\x80\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0$ioukey$ioupad1" | md5sum | cut -d ' ' -f 1)
    printf "%s\n%s\n" "[license]" "$hostname = ${ioulicense:0:16};" 
    printf "%s\n%s" "[license]" "$hostname = ${ioulicense:0:16};" > ~/.iourc
    printf "%s\n" "IOU license was stored in ~/.iourc"
}

OPTS="$(getopt -o f:,F:,s:,S:,c:,C:,i::,m::,h -l font-type:,font-color:,font-size:,afont-type:,afont-color:,afont-size:,images::,symbol::,li,ls,lf,lF,help -n $0 -- "$@")"
if [ $? -ne 0 ]; then
    echo "ERROR: Failed parsing options"
    echo "Try '$0 --help' for more information."
    exit 99
fi
_backup
while [ $# -gt 0 ] && [ "$1" != "--" ]; do 
    case "$1" in
        -i|--image)
            # change images of an existing project(s)
            _numofargs "$#"
            oldimage="$2"
            newimage="$3"
            _isimageexist "$oldimage"
            find "$current_dir" -name "*.gns3" -type f -exec  sed -i "s|$oldimage|$newimage|g"  "{}" \+
            echo "Project(s) image(s) has been changed succussfully..."
            exit 0
            ;;
        -m|--symbol)
            _numofargs "$#"
            oldSymbol="$2"
            newSymbol="$3"
            _issymbolexist "$oldSymbol"
            find "$current_dir" -name "*.gns3" -type f  -exec sed -i "s:$oldSymbol:$newSymbol:g" "{}" \+
            echo "Symbol(s) has been changed succussfully"
            exit 0
            ;;
        -f|--font-type)
            newFontType="$2"
            find "$current_dir" -name "*.gns3" -type f -exec sed -i "s:\(font-family=..\).[^\\\]*:\1$newFontType:g" "{}" \+
            echo "Project(s) font family has been changed succussfully"
            shift 2
            ;;
        -s|--font-size)
            # Change note font-size
            _isdigit $2
            newFontSize="$2"
            find "$current_dir" -name "*.gns3" -type f -exec sed -i "s:\(font-size=..\).[^\\\]*:\1$newFontSize:g" "{}" \+
            echo "Project(s) font size has been change succussfully"
            shift 2
            ;;
        -c|--font-color)
            _isvalidcolor "$2" "$1"
            newFontColor="$2"
            find "$current_dir" -name "*.gns3" -type f -exec sed -i "s:\(fill=..\).[^\\\]*:\1$newFontColor:g" "{}" \+
            echo "Project(s) font color has been changed succussfully"
            shift 2
            ;;
        -F|--afont-type)
            newFontType="$2"
            find "$current_dir" -name "*.gns3" -type f -exec sed -i "s|\(font-family: \).[^;]*|\1$newFontType|g" "{}" \+
            echo "Appliance font family has been changed succussfully"
            shift 2
            ;;
        -S|--afont-size)
            _isdigit $2
            newFontSize="$2";
            find "$current_dir" -name "*.gns3" -type f -exec sed -i "s|\(font-size: \)[0-9]\+\(\.[0-9]\)\?[^;]*|\1$newFontSize|g" "{}" \+
            echo "Appliance font size has been changed succussfully"
            shift 2
            ;;
        -C|--afont-color)
            _isvalidcolor "$2" "$1"
            newFontColor="$2"
            find "$current_dir" -name "*.gns3" -type f -exec sed -i "s|\(text fill: \)#.\{6\}[^;]*|\1$newFontColor|g" "{}" \+
            echo "Appliance font color has been changed succussfully"
            shift 2
            ;;
        --ls|--list-symbols)
            re_symbols="(?<=\"symbol\":\ ).[^,]*"
            find "$current_dir" -name "*.gns3"  -type f -exec grep -oP --color "$re_symbols" "{}" \+
            shift 
            ;;
        --li|--list-images)
            #re_images="\\.\(bin\|image\|vmdk\|vdi\|vhd\|qcow2\|qcow\|img\|raw\|ovf\|ova\)"
           # if [ "$2" == "installed" ]; then
           #     ls "${gns3_images_dir}" -R
           #     shift 2
           #     exit 1
           # else 
                re_images="(?<=\"path\":\ ).[^,]*" # better format also match images without extension
                find "$current_dir" -name "*.gns3" -type f -exec grep -oP --color "$re_images" "{}" \+
                _isemptyproject
                shift
           # fi
            ;;
        --lf|--list-fonts)
            # List note font properties of an exist project(s)
            find "$current_dir" -name "*.gns3" -type f -exec grep --color -o '\(font-family=..\).[^\]*' "{}" \+
            if [ "$?" != 0 ]; then
                echo "Couldn't find any note font..."
            fi
            echo "$current_dir"
            shift
            ;;
        --lF|--list-afonts)
            # List appliance font properties of an exist project(s)
            find "$current_dir" -name "*.gns3" -type f -exec grep --color -o '\(font-family: \).[^;]*' "{}" \+
            if [ "$?" != 0 ]; then
                echo "Couldn't find any note font..."
            fi
            shift
            ;;
       # --dfont)
       #     # apply default font type, color, size, bold, etc.. to a project 
       #     if [ $2 == light ]; then
       #         find "${current_dir}" -name "*.gns3" -type f -exec sed -i "s:\(fill=..\).[^\\\]*:\1#282828:g" "{}" \+
       #         find "${current_dir}" -name "*.gns3" -type f -exec sed -i "s|\(\"style\": \).[^,]*|\1\"font-family: 'DejaVu Sana Mono';font-size: 10.0;font-weight: bold;fill: #cc241a;fill-opacity: 1.0;\"|g" "{}" \+
       #     elif [ $2 == dark ]; then
       #         find "${current_dir}" -name "*.gns3" -type f -exec sed -i "s:\(fill=..\).[^\\\]*:\1#839496:g" "{}" \+
       #         find "${current_dir}" -name "*.gns3" -type f -exec sed -i "s|\(\"style\": \).[^,]*|\1\"font-family: 'DejaVu Sana Mono';font-size: 10.0;font-weight: bold;fill: #cc241a;fill-opacity: 1.0;\"|g" "{}" \+
       #     else
       #         echo "ERROR: only 'light|dark' are supported."
       #     fi
       #     echo "defaul font has been applied."
       #     shift 2
       #     exit 0
       #     ;;
        -k|--key)
            _ioukeygen
            exit 0
            ;;
        -h|--help)
            _usage
            exit 0
            ;;
        *) 
            echo "Unrecognized argument: "$1""
            exit 98
            ;;
    esac
done
exit 0

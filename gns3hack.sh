#!/bin/env bash
usage() {
    printf "%s\n" "Usage: gns3hack gns3-gui_dir [OPTION]... <value>"
    printf "%s\n" "       gns3hack gns3-project_dir [OPTION] <value>"
    printf "%s\n" "Options:"
    printf "  %s\t\t%s\n" "-b, --bg-color" "Change gns3-gui background color"
    printf "  %s\t\t%s\n" "-f, --fg-color" "Change gns3-gui foreground color"
    printf "  %s\t\t\t%s\n" "-o, --opacity" "Change gns3-gui windows opacity"
    printf "  %s\t%s\n" "-t, --toolbar-bg-color" "Change gns3-gui toolbar bg color"
    printf "  %s\t\t%s\n" "-y, --sel-bg-color" "Change gns3-gui selection bg color"
    printf "  %s\t\t%s\n" "-Y, --sel-fg-color" "Change gns3-gui selelction fg color"
    printf "  %s\t\t%s\n" "-n, --font-type" "Change note font-family"
    printf "  %s\t\t%s\n" "-c, --font-color" "Change note font color"
    printf "  %s\t\t%s\n" "-z, --font-size" "Change note font size"
    printf "  %s\t\t%s\n" "-N, --afont-type" "Change appliance font-family"
    printf "  %s\t\t%s\n" "-C, --afont-color" "Change appliance font color"
    printf "  %s\t\t%s\n" "-Z, --afont-size" "Change appliance font size"
    printf "  %s\t\t\t%s\n" "-i, --image" "Change images (IOU,IOS,qemu,vbox,..) used by a  project(s)"
    printf "  %s\t\t\t%s\n" "-s, --symbol" "Change router,switch,etc.. symbol(icon)"
    printf "  %s\t\t%s\n" "-I, --list-image" "List images (IOU,IOS,qemu,vbox,..) used by a project(s)"
    printf "  %s\t\t%s\n" "-S, --list-symbol" "List symbols used by a project"
    printf "  %s\t\t%s\n" "-F, --list-font" "List current note font(s) used by a project"
    printf "  %s\t\t%s\n" "-A, --list-afont" "List current appliance font(s) used by a project"
    printf "  %s\t\t%s\n" "-d, --delete-backup" "Delete gns3.backup files"
    printf "\n"
    printf "%s\n" "Examples:"

    printf "%s\t%s\n"  "Get information about a project(s)"
    printf "  %s\t%s\n"  "  cd ~/gns3/project/project_name" "# cd to your gns3 project folder"
    printf "  %s\t%s\n"  "  ./gns3hack.sh . --list-images" "# get images names used by a project"
    printf "  %s\t%s\n"  "  ./gns3hack.sh . --list-fonts" "# get note font properties used by a project"
    printf "  %s\t%s\n"  "  ./gns3hack.sh . --list-afonts" "# get appliance font properties used by a project "
    printf "  %s\t%s\n"  "  ./gns3hack.sh . --list-symbols" "# get devices symbols used by a project"
    printf "\n"

    printf "%s\t%s\n"  "Change images(IOU,IOS,qemu,vbox,...) used by a project(s)"
    printf "  %s\t%s\n"  "  1. cd ~/gns3/project/project-name" "# cd to your gns3 project folder"
    printf "  %s\t%s\n"  "  2. ./gns3hack.sh . --list-images" "# Choose image from the list to replace"
    printf "  %s\t%s\n"  "  3. ./gns3hack.sh . -i \"i86bi-linux-l3-adventerprisek9-15.4.2T4.bin\" \"i86bi-linux-l3-adventerprisek9-15.5.2T.bin\"" "# Replace the image"
    printf "  %s\n"  "  4. restart gns3"
    printf "%s\n"   "To change all projects images, cd to main project directory instead of specific project directory in step 1 "
    printf "%s"   "Note: Any new image(s) must be added to gns3 and installed to the same directory as the old one, "
    printf "%s"  "if you dont add the new image(s), you'll receive this error message 'The image image-name is missing'. "
    printf "%s"    "This is a very good option if you want to test new image(s) on an existing project(s) and revert back, "
    printf "%s\n"    "or you have new working image(s) and you want to use it for all of your projects"
    printf "\n"

    printf "%s\n" "Change gns3 interface bg-color fg-color toolbar-color opacity ...."
    printf "%s\n" "1. Donwload gns3-gui source code from github.com (\`url: https://github.com/GNS3/gns3-gui/releases/tag/v2.0.3\`)"
    printf "%s\n" "2. Download gns3-gui/gns3/ui from (\`https://github.com/n3oxmind/gns3hack\`) and copy paste it to the original gns3-gui folder from step 1"
    printf "%s\n" "3. Now you can use "gns3hack.sh" script to do some changes to gns3-gui"
    printf "%s\n"  "Lets do some changes to gns3 interface"
    printf "  %s\t\t%s\n"  "cd ~/Download/gns3-gui-2.0.3" "# cd to gns3-gui source code folder"
    printf "  %s\t\t%s\n"  "./gns3hack.sh . -b \"#282828\"" "# Change gns3-gui bg color"
    printf "  %s\t\t%s\n"  "./gns3hack.sh . -f \"#00ff00\"" "# Change gns3-gui fg color"
    printf "  %s\t\t%s\n"  "./gns3hack.sh . -t \"#323232\"" "# Change gns3-gui tool bar color"
    printf "  %s\t\t%s\n"  "./gns3hack.sh . -o 9.5" "# Change gns3 window opacity"
    printf "  %s\t\t%s\n"  "./gns3hack.sh . -b \"#282828\" -f white -t \"#323232\"" "# All at once in any order"
    printf "  %s\t\t\n"  "./gns3hack.sh . -f white -t \"#323232\" -b black -o 0.99" 
}

# Validate the color
isValidColor () {
    if [[ ! "$1" =~ $re_hexcolor ]] && ! [ "$1" = "white" -o "$1" = "black" -o "$1" = "red" -o "$1" = "green" -o "$1" = "blue" -o "$1" = "cyan" -o "$1" = "gray" -o "$1" = "yellow" ]; then
        echo "ERROR: colors must be in hex format or names e.g. "#ffffff" or white"
        exit 1
    fi
    old_bg_color=$(grep -oP -m 1 "(?<=bg-color=).*" "$DIR"/gns3/ui/capture_dialog.ui) 
    old_fg_color=$(grep -oP -m 1 "(?<=fg-color=).*" "$DIR"/gns3/ui/capture_dialog.ui) 
    old_toolbar_color=$(grep -oP -m 1 "(?<=tool-bar=).*" "$DIR"/gns3/ui/capture_dialog.ui) 
    old_sel_bg_color=$(grep -oP -m 1 "(?<=selection-bg=).*" "$DIR"/gns3/ui/capture_dialog.ui) 
    old_sel_fg_color=$(grep -oP -m 1 "(?<=selection-fg=).*" "$DIR"/gns3/ui/capture_dialog.ui) 
    if [ "$old_bg_color" == "$1" ]; then 
        ccFlag=true
    elif [ "$old_fg_color" == "$1" ]; then 
        ccFlag=true
    elif [ "$old_toolbar_color" == "$1" ]; then 
        ccFlag=true
    elif [ "$old_sel_bg_color" == "$1" ]; then 
        ccFlag=true
    elif [ "$old_sel_fg_color" == "$1" ]; then 
        ccFlag=true
    else
        # color confliction
        ccFlag=false
    fi
}
# Validate the opacity
isValidOpacity () {
    if [[ ! "$1" =~ $re_opacity ]] || [ ! $3 = 1.0 ]; then
        echo "ERROR: Window opacity must be between 0.0 and 1.0"
        exit 1
    fi
}
# Install gns3-gui
gns3-gui-install () {
    # perform Cleanup
    find /usr/lib \( -name "gns3" -o -name "gns3_gui-*.egg" -o -name "gns3_gui-*.egg-info" \) -type d -prune -exec rm -rf "{}" \+
    # apply changes and install 
    ./scripts/build_pyqt.py
    python3 setup.py install
    echo "gns3-gui successfully changed ..."
    echo "gns3-gui Installation Finished ..."
    echo "Restart gns3 to see changes ..."
}
# Check if the script running as root
isRoot () {
    if [ "$(whoami)" != "root" ]; then
        echo "Please, run as root"
        exit
    fi
}
isDigit () {
    if [[ ! $1 =~ $re_digit ]];then
        echo "ERROR: Font-size must be in this format dd.d(12.5)"
        exit 1
    fi
}
isEmptyProject () {
    if [ "$?" -ne 0 ]; then
        echo "Couldn't find any images..."
    fi
}
isImageExist () {
    find "$DIR" -name "*.gns3" -type f -exec grep -oP -m 1 "(?<=\"path\":\ )\"$1\"" "{}" \+
    if [ "$?" -ne 0 ]; then
       echo "Image does not exist: $1" 
       exit 1
   fi
   if [ -z "$1" ]; then
       oldimage='\"\"'
       newimage="\"$newimage\""
   fi
}
isSymbolExist () {
    find "$DIR" -name "*.gns3" -type f -exec grep -oP -m 1 "(?<=\"symbol\":\ )\"$1\"" "{}" \+
    if [ "$?" -ne 0 ]; then
       echo "Symbol does not exist: $1" 
       exit 1
   fi
   if [ -z "$1" ]; then
       oldSymbol='\"\"'
       newSymbol="\"$newSymbol\""
   fi
}
# Check passing number of arguments
numArgs () {
    if [ "$#" -ne 3 ]; then
        echo "ERROR!: Too many arguments"
        echo "Try './gns3hack.sh --help' for more information"
        exit 1
    fi
}
changeColor () {
    if [ "$ccFlag" == "false" ]; then
        sed -i "s/$1/$2/g" "$DIR"/gns3/ui/*.ui
    fi
}
if [ ! -d "$1" -a "$1" != "--help" ]; then
    echo "The directory does not exist!"
    exit 1
fi
if ! [ "$1" == "--help" -o "$1" == "-h" ]; then
    DIR="$1"
    shift
fi
OPTS="$(getopt -o b:f:t:o:y:Y:i::s::n:N:z:Z:c:C:ISFAdha::: --long bg-color:,fg-color:,toolbar-color:,opacity:,sel-bg-color:,sel-fg-color:,image::,symbol::,font-type:,afont-type:,font-size:,afont-size:,font-color:,afont-color:,list-images,list-fonts,list-afonts,list-symbols,delete-backup,help,add-image::: -n $0 -- "$@")"

if [ $? -ne 0 ]; then
    echo "Failed parsing options, see ./gns3hack.sh --help for more info"
    exit 1
fi
# takeing care of spacing problem, avoid using eval if possible
#eval set -- "$OPTS"
bFlag=false
fFlag=false
tFlag=false
oFlag=false
sFlag=false
SFlag=false

re_digit='^[0-9]{,2}\.[0-9]$'
re_hexcolor='^#[0-9a-fA-F]{6}$'
re_opacity='^0\.[0-9]{,2}$'

while [ $# -gt 0 ] && [ "$1" != "--" ] 
do
    case "$1" in
#################### GNS3-GUI THEME #########################################
        -b|--bg-color)
            isRoot
            isValidColor "$2"
            new_bg_color="$2"
            changeColor $old_bg_color $new_bg_color
            bFlag=true
            shift 2
            ;;
        -f|--fg-color)
            isRoot
            isValidColor "$2"
            new_fg_color="$2"
            changeColor $old_fg_color $new_fg_color
            fFlag=true
            shift 2
            ;;
        -t|--toolbar-color)
            isRoot
            isValidColor "$2"
            new_toolbar_color="$2"
            changeColor $old_toolbar_color $new_toolbar_color
            tFlag=true
            shift 2
            ;;
        -o|--opacity)
            isRoot
            isValidOpacity "$2"
            win_opacity="$2"
            sed -i '/main_window\.setWindowOpacity.*/d' "$DIR"/gns3/style.py
            sed -i "/self\._mw = main_window/a\    \    main_window.setWindowOpacity\($win_opacity\)" "$DIR"/gns3/style.py
            oFlag=true
            shift 2
            ;;
        -y|--sel-bg-color)
            isRoot
            isValidColor "$2"
            new_sel_bg_color="$2"
            changeColor $old_sel_bg_color $new_sel_bg_color
            sFlag=true
            shift 2
            ;;
        -Y|--sel-fg-color)
            isRoot
            isValidColor $2
            new_sel_fg_color="$2"
            changeColor $old_sel_fg_color $new_sel_fg_color
            SFlag=true
            shift 2
            ;;
############################# end of gns3-gui theme ##############################
############################# start gns3 project(s) tools ########################
        -i|--image)
            # change images of an existing project(s)
            numArgs
            oldimage="$2"
            newimage="$3"
            isImageExist "$oldimage"
            find "$DIR" -name "*.gns3" -type f -exec  sed -i "s|$oldimage|$newimage|g"  "{}" \+
            echo "Project(s) image(s) has been changed succussfully..."
            shift 3 
            break
            ;;
        -s|--symbol)
            numArgs
            oldSymbol="$2"
            newSymbol="$3"
            isSymbolExist "$oldSymbol"
            find "$DIR" -name "*.gns3" -type f  -exec sed -i "s:$oldSymbol:$newSymbol:g" "{}" \+
            echo "Symbol(s) has been changed succussfully"
            shift 3 
            break
            ;;
        -n|--font-type)
            newFontType="$2"
            find "$DIR" -name "*.gns3" -type f -exec sed -i "s:\(font-family=..\).[^\\\]*:\1$newFontType:g" "{}" \+
            echo "Project(s) font family has been changed succussfully"
            shift 2
            ;;
        -z|--font-size)
            # Change note font-size
            isDigit $2
            newFontSize="$2"
            find "$DIR" -name "*.gns3" -type f -exec sed -i "s:\(font-size=..\).[^\\\]*:\1$newFontSize:g" "{}" \+
            echo "Project(s) font size has been change succussfully"
            shift 2
            ;;
        -c|--font-color)
            # Changing note font-color 
            isValidColor "$2"
            newFontColor="$2"
            find "$DIR" -name "*.gns3" -type f -exec sed -i "s:\(fill=..\).[^\\\]*:\1$newFontColor:g" "{}" \+
            echo "Project(s) font color has been changed succussfully"
            shift 2
            ;;
        -N|--afont-type)
            # Change applicance font-family 
            newFontType="$2"
            find "$DIR" -name "*.gns3" -type f -exec sed -i "s|\(font-family: \).[^;]*|\1$newFontType|g" "{}" \+
            echo "Appliance font family has been changed succussfully"
            shift 2
            ;;
        -Z|--afont-size)
            # Change appliance font-size
            isDigit $2
            newFontSize="$2";
            find "$DIR" -name "*.gns3" -type f -exec sed -i "s|\(font-size: \)[0-9]\+\(\.[0-9]\)\?[^;]*|\1$newFontSize|g" "{}" \+
            echo "Appliance font size has been changed succussfully"
            shift 2
            ;;
        -C|--afont-color)
            # Changing appliance font-color 
            isValidColor "$2"
            newFontColor="$2"
            find "$DIR" -name "*.gns3" -type f -exec sed -i "s|\(fill: \)#.\{6\}[^;]*|\1$newFontColor|g" "{}" \+
            echo "Appliance font color has been changed succussfully"
            shift 2
            ;;
############################# END OF GNS3 PROJECT(S) TOOLS #######################
############################# TOOLS TO GET PROJECT INFO ##########################
        -S|--list-symbols)
            # List symbols of an exist project
            re_symbols="(?<=\"symbol\":\ ).[^,]*"
            find "$DIR" -name "*.gns3"  -type f -exec grep -oP --color "$re_symbols" "{}" \+
            shift 
            ;;
        -I|--list-images)
            # List images of an exist project(s)
            #re_images="\\.\(bin\|image\|vmdk\|vdi\|vhd\|qcow2\|qcow\|img\|raw\|ovf\|ova\)"
            re_images="(?<=\"path\":\ ).[^,]*" # better format also match images without extension
            find "$DIR" -name "*.gns3" -type f -exec grep -oP --color "$re_images" "{}" \+
            isEmptyProject
            shift
            ;;
        #-X) TODO: need to match based on node_type 
            # List project devices names, images and ram
         #   find "$DIR" -name "*.gns3" -type f -exec grep -e "\"path\":\ " -e "\"name\":\ " -e "\"ram\":\ " "{}" \+ | sed -n '2,$s/\(^\ *\)\(.*\),$/\2/gp'
          #  isEmptyProject
           # shift
            #;;
        -F|--list-fonts)
            # List note font properties of an exist project(s)
            find "$DIR" -name "*.gns3" -type f -exec grep --color '\(font-family=..\).[^\]*' "{}" \+
            if [ "$?" != 0 ]; then
                echo "Couldn't find any note font..."
            fi
            shift
            ;;
        -A|--list-afonts)
            # List appliance font properties of an exist project(s)
            find "$DIR" -name "*.gns3" -type f -exec grep --color '\(font-family: \).[^;]*' "{}" \+
            if [ "$?" != 0 ]; then
                echo "Couldn't find any note font..."
            fi
            shift
            ;;
        -d|--delete-backup)
            find "$DIR" -name "*.gns3.backup*" -type f -exec rm "{}" \+
            if [ "#?" -eq 0 ]; then
                echo "Finished cleaning up ...."
            else
                echo "Couldn't find any gsn3 backup"
            fi
            shift
            ;;
############################# END TOOLS TO GET PROJECT INFO ######################
############################# START OF GNS3 CONFIG ###############################
#        -a|--add-image)
#            imagebin="$2"
#            imageType="$3"
#            imageName="$4"
#            sed -i "s|\(\"devices\":\ \[\)|\1\n\t\t\t{\n\t\t\t\t\"category\": $imageType,\n\t\t\t\t\"default_name_format\": \"IOU{0}\",\n\t\t\t\t\"ethernet_adapters\": 4,\n\t\t\t\t\"image\": \"$imagebin\",\n\t\t\t\t\"l1_keepalives\": false,\n\t\t\t\t\"name\": \"$imageName\",\n\t\t\t\t\"nvram\": 128,\n\t\t\t\t\"path\": \"$DIR/$imagebin\",\n\t\t\t\t\"private_config\": \"\",\n\t\t\t\t\"ram\": 256,\n\t\t\t\t\"serial_adapters\": 2,\n\t\t\t\t\"server\": \"local\",\n\t\t\t\t\"startup_config\": \"/home/n30x/GNS3/configs/iou_l3_base_startup-config.txt\",\n\t\t\t\t\"symbol\": \"router3.svg\",\n\t\t\t\t\"use_default_iou_values\": true\n\t\t\t},\n|g" $gns3_config/gns3_gui.conf
#            echo "Image has been added to gns3 successfully..."
#            shift 4
#            break
#            ;;
############################# END OF GNS3 CONFIG #################################
        -h|--help)
            usage
            exit 1
            ;;
        *) 
            echo "Unrecognized argument: "$1""
            exit 1
            ;;
    esac
done

# Apply changes to gns3-gui if any of gns3-gui Flags triggered 
if [ $bFlag == true -o $fFlag == true -o $tFlag == true -o $oFlag == true -o $sFlag == true -o $SFlag == true ]; then
    gns3-gui-install
fi





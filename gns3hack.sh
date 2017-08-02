#!/usr/bin/env bash
# Usage
usage() {
    printf "%s\n" "Usage: gns3hack PATH_TO_gns3-gui_SOURCE_CODE_DIR [OPTION] <value>"
    printf "%s\n" "       gns3hack PATH_TO_YOUR_PROJECT_DIR [OPTION] <value>"
    printf "%s\n" "Options:"
    printf "  %s\t\t%s\n" "-bg, --bg-color" "Change gns3-gui background color"
    printf "  %s\t\t%s\n" "-fg, --fg-color" "Change gns3-gui foreground color"
    printf "  %s\t\t\t%s\n" "-o, --opacity" "Change gns3-gui windows opacity"
    printf "  %s\t%s\n" "-t, --toolbar-bg-color" "Change gns3-gui toolbar bg color"
    printf "  %s\t\t%s\n" "-s, --sel-bg-color" "Change gns3-gui selection bg color"
    printf "  %s\t\t%s\n" "-S, --sel-fg-color" "Change gns3-gui selelction fg color"
    printf "  %s\t\t%s\n" "-f, --font-type" "Change note font-family"
    printf "  %s\t\t%s\n" "-c, --font-color" "Change note font color"
    printf "  %s\t\t%s\n" "-z, --font-size" "Change note font size"
    printf "  %s\t\t%s\n" "-F, --afont-type" "Change appliance font-family"
    printf "  %s\t\t%s\n" "-C, --afont-color" "Change appliance font color"
    printf "  %s\t\t%s\n" "-Z, --afont-size" "Change appliance font size"
    printf "  %s\t\t\t%s\n" "-i, --image" "Change images (IOU,IOS,qemu,vbox,..) used by a  project(s)"
    printf "  %s\t\t\t%s\n" "-s, --symbol" "Change router,switch,etc.. symbol(icon)"
    printf "  %s\t\t%s\n" "-li, --list-image" "List images (IOU,IOS,qemu,vbox,..) used by a project(s)"
    printf "  %s\t\t%s\n" "-ls, --list-symbol" "List symbols used by a project"
    printf "  %s\t\t%s\n" "-lf, --list-font" "List current note font(s) used by a project"
    printf "  %s\t\t%s\n" "-lF, --list-afont" "List current appliance font(s) used by a project"
    printf "\n"
    printf "%s\n" "Examples:"

    printf "%s\t%s\n"  "Get information about a project(s)"
    printf "  %s\t%s\n"  "  cd ~/gns3/project/project_name" "# cd to your gns3 project folder"
    printf "  %s\t%s\n"  "  ./gns3hack.sh . --list-image" "# get images names used by a project"
    printf "  %s\t\t%s\n"  "  ./gns3hack.sh . --list-font" "# get note font properties used by a project"
    printf "  %s\t%s\n"  "  ./gns3hack.sh . --list-afont" "# get appliance font properties used by a project "
    printf "  %s\t%s\n"  "  ./gns3hack.sh . --list-symbol" "# get devices symbols used by a project"
    printf "\n"

    printf "%s\t%s\n"  "Change images(IOU,IOS,qemu,vbox,...) of a project(s)"
    printf "  %s\t%s\n"  "  1. cd ~/gns3/project/prlject-name" "# cd to your gns3 project folder"
    printf "  %s\t%s\n"  "  2. ./gns3hack.sh . --list-image" "# Choose image from the list to replace"
    printf "  %s\t\n"  "  3. ./gns3hack.sh . -i \"i86bi-linux-l3-adventerprisek9-15.4.2T4.bin\" \"i86bi-linux-l3-adventerprisek9-15.5.2T.bin\"" "Replace the image"
    printf "  %s\n"  "  4. restart gns3"
    printf " %s\n"   "To change all projects images, cd to main project directory instead of specific project in step 1 "
    printf " %s\n"   "Note: Any new image(s) must be added to gns3 and installed to the same directory as the old one"
    printf "\t%s\n"  "if you dont do that, gns3 will have no idea about the new image and your project won't run unless you do so"
    printf "%s\n"    "This is very good option if you want to test new image(s) on an existing project(s) and revert back"
    printf "  %s\n"    "or you found new good working image(s) and you want to use it for all of your projects"
    printf "\n"

    printf "%s\n" "Change gns3 interface bg-color fg-color toolbar-color opacity ...."
    printf "%s\n" "1. Donwload gns3-gui source code from github.com (\`url: https://github.com/GNS3/gns3-gui/releases/tag/v2.0.3\`)"
    printf "%s\n" "2. Download gns3-gui/gns3/ui from (\`https://github.com/n3oxmind/gns3hack\`) and copy paste it to the original gns3-gui folder from step 1"
    printf "%s\n" "3. Now you can use "gns3hack.sh" script to do some changes to gns3-gui"
    printf "%s\n"  "Lets do some changes to gns3 interface"
    printf "  %s\t\t%s\n"  "cd ~/Download/gns3-gui-2.0.3" "# cd to gns3-gui source code folder"
    printf "  %s\t\t%s\n"  "./gns3hack.sh . -bg \"#282828\"" "# Change gns3-gui bg color"
    printf "  %s\t\t%s\n"  "./gns3hack.sh . -fg \"#00ff00\"" "# Change gns3-gui fg color"
    printf "  %s\t\t%s\n"  "./gns3hack.sh . -t \"#323232\"" "# Change gns3-gui tool bar color"
    printf "  %s\t\t%s\n"  "./gns3hack.sh . -o 9.5" "# Change gns3 window opacity"
    printf "%s\n" "Note: If you used the same color for both background and toolbar or any other options, any changes to background color will effect the other options that share the same color."
    printf "\n"


}
if [ $# -le 1 ] && ! [ "$1" = "--help" -o "$1" = "-h" ]; then
    echo "gns3hack.sh: missing operand"
    echo "Try './gns3hack.sh --help' for more information"
    exit 1
fi
if [ "$1" = "--help" -o "$1" = "-h" ]; then
    echo "$(usage)"
    exit
fi
if [ ! -d "$1" ]; then
    echo "The directory does not exist!"
    exit 1
fi
# Empty string is dangerous
if [ $# -eq 3 ]; then
    if [ -z "$3" ]; then
        echo "ERROR!: Empty string not accepted"
        exit 1
    fi
elif [ $# -eq 4 ]; then
    if [ -z "$3" ] || [ -z "$4" ]; then
        echo "ERROR!: Empty string not accepted"
        exit 1
    fi
elif [ $# -ne 2 ] && [ $# -gt 4 ]; then
    echo "ERROR!: Too many arguments"
    exit 1
fi
set -e
re_digit='^[0-9]{,2}\.[0-9]$'
re_hexcolor='^#[0-9a-fA-F]{6}$'
re_opacity='^0\.[0-9]{,2}$'
validateColor () {
    if [[ ! $1 =~ $re_hexcolor ]]; then
        echo "ERROR: Color must be in hex format surrounded by double quote \"#xxxxxx\""
        exit 1
    fi
}
validateOpacity() {
    if [[ ! "$1" =~ $re_opacity ]] || [ ! $3 = 1.0 ]; then
        echo "ERROR: Window opacity must be between 0.0 and 1.0"
        exit 1
    fi
}
gns3-gui-install () {
    # perform Cleanup
    find /usr/lib -iname "gns3_gui-*.egg" -type d -prune -exec rm -rf "{}" \+
    # apply changes and install 
    ./scripts/build_pyqt.py
    python3 setup.py install
    echo "gns3-gui "$1" successfully changed ..."
    echo "gns3-gui Installation Finished ..."
    echo "restart gns3 to see changes ..."
}
################## Change gns3-gui background & forground  color ####################
# Change gns3-gui base-bg color
if [ $2 = "--bg-color" -o $2 = "-bg" ]; then
    validateColor $3
    new_bg_color="$3"
    old_bg_color=$(grep "bg-color=" "$1"/gns3/ui/capture_dialog.ui | grep -o "\#[0-9a-fA-F]\{6\}$")
    sed -i "s/$old_bg_color/$new_bg_color/g" "$1"/gns3/ui/*.ui
    gns3-gui-install "background color"
# Change gns3-gui base-fg color
elif [ $2 = "--fg-color" -o $2 = "-fg" ]; then
    validateColor $3
    new_fg_color="$3"
    old_fg_color=$(grep "fg-color=" "$1"/gns3/ui/capture_dialog.ui | grep -o "\#[0-9a-fA-F]\{6\}$")
    sed -i "s/$old_fg_color/$new_fg_color/g" "$1"/gns3/ui/*.ui
    gns3-gui-install "foreground color"
# Change gns3-gui toolbar-bg-color and sidebar-bg-color
elif [ $2 = "--toolbar-bg-color" -o $2 = "-t" ]; then
    validateColor $3
    new_toolbar_color="$3"
    old_toolbar_color=$(grep "tool-bar=" "$1"/gns3/ui/capture_dialog.ui | grep -o "\#[0-9a-fA-F]\{6\}$")
    sed -i "s/$old_toolbar_color/$new_toolbar_color/g" "$1"/gns3/ui/*.ui
    gns3-gui-install "toolbar color"
# Change gns3-gui selection bg color
elif [ $2 = "--sel-bg-color" -o $2 = "-s" ]; then
    validateColor
    new_sel_bg_color="$3"
    old_sel_bg_color=$(grep "selection-bg=" "$1"/gns3/ui/capture_dialog.ui | grep -o "\#[0-9a-fA-F]\{6\}$")
    sed -i "s/$old_sel_bg_color/$new_sel_bg_color/g" "$1"/gns3/ui/*.ui
    gns3-gui-install "selection bg-color"
# Change gns3-gui selection fg color
elif [ $2 = "--sel-fg-color" -o $2 = "-S" ]; then
    validateColor
    new_sel_fg_color="$3"
    old_sel_fg_color=$(grep "selection-fg=" "$1"/gns3/ui/capture_dialog.ui | grep -o "\#[0-9a-fA-F]\{6\}$")
    sed -i "s/$old_sel_fg_color/$new_sel_fg_color/g" "$1"/gns3/ui/*.ui
    gns3-gui-install "selection fg-color"
# Set gns3-gui window opacity 
elif [ $2 = "--opactiy" -o $2 = "-o" ]; then
    validateOpacity $3
    win_opacity="$3"
    sed -i '/main_window\.setWindowOpacity.*/d' "$1"/gns3/style.py
    sed -i "/self\._mw = main_window/a\    \    main_window.setWindowOpacity\($win_opacity\)" "$1"/gns3/style.py
    gns3-gui-install "window opacity"
# Change images of an existing project(s)
elif [ $2 = "--image" -o $2 = "-i" ]; then
    if [ $# -ne 4 ]; then
        echo "ERROR!: missing operand"
        echo "Try, './gns3hack.sh --help' for more information about image(s) replacement"
        exit 1
    fi
    oldimage="$3"
    newimage="$4"
    find . -type f -iname "*.gns3" -print -exec sed -n "s|$oldimage|$newimage|gp"  "{}" \+
    echo "Project(s) image(s) has been changed succussfully..."
    # Change appliance symbol 
elif [ $2 = "--symbol" -o $2 = "-s" ]; then
    if [ $# -ne 4 ]; then
        echo "ERROR!: missing operand"
        echo "Try, './gns3hack.sh --help' for more information about image(s) replacement"
        exit 1
    fi
    oldSymbol=$3
    newSymbol=$4
    find "$1" -type f -iname "*.gns3" -print  -exec sed  -n "s:$oldSymbol:$newSymbol:g" "{}" \+
    echo "Symbol(s) has been changed succussfully"

################## change project NOTE FONT PROPERTIES ################################### 
elif [ $2 = "--font-type" -o $2 = "-f" ]; then
    newFontType="$3"
    find "$1" -type f -iname "*.gns3" -print -exec sed -n "s:\(font-family=..\).[^\\\]*:\1$newFontType:g" "{}" \+
    echo "Project(s) font family has been changed succussfully"
# Change note font-size
elif [ $2 = "--font-size" -o $2 = "-z" ] ; then
    if [[ ! $3 =~ $re_digit ]];then
        echo "ERROR: Font-size must be in this format dd.d(12.5)"
        exit 1
    fi
    newFontSize="$3";
    find "$1" -type f -iname "*.gns3" -print -exec sed -n "s:\(font-size=..\).[^\\\]*:\1$newFontSize:g" "{}" \+
    echo "Project(s) font size has been change succussfully"
# Changing note font-color 
elif [ $2 = "--font-color" -o $2 = "-c" ]; then
    validateColor
    newFontColor="$3";
    find "$1" -type f -iname "*.gns3" -print -exec sed -n "s:\(fill=..\).[^\\\]*:\1$newFontColor:g" "{}" \+
    echo "Project(s) font color has been changed succussfully"
################ change APPLIANCE FONT PROPERTIES ##################################
# Change applicance font-family 
elif [ $2 = "--afont-type" -o $2 = "-F" ]; then
    newFontType="$3"
    find "$1" -type f -iname "*.gns3" -print -exec sed -n "s|\(font-family: \).[^;]*|\1$newFontType|g" "{}" \+
    echo "Appliance font family has been changed succussfully"
# Change appliance font-size
elif [ $2 = "--afont-size" -o $2 = "-Z" ] ; then
    if [[ ! $3 =~ $re_digit ]];then
        echo "ERROR: Font-size must be in this format dd.d(12.5)"
        exit 1
    fi
    newFontSize="$3";
    find "$1" -type f -iname "*.gns3" -print -exec sed -n "s|\(font-size: \)[0-9]\+\(\.[0-9]\)\?[^;]*|\1$newFontSize|g" "{}" \+
    echo "Appliance font size has been changed succussfully"
# Changing appliance font-color 
elif [ $2 = "--afont-color" -o $2 = "-C" ]; then
    validateColor
    newFontColor="$3";
    find "$1" -type f -iname "*.gns3" -print -exec sed -n "s|\(fill: \)#.\{6\}[^;]*|\1$newFontColor|g" "{}" \+
    echo "Appliance font color has been changed succussfully"
elif [ "$1" = "--help" -o "$1" = "-h" ]; then
    echo "$(usage)"
######################### Getting Information ########################
# List symbols of an exist project
elif [ $2 = "--list-symbol" -o $2 = "-ls" ]; then
    find "$1" -type f -iname "*.gns3" -print -exec grep --color "\\.\(svg\|png\)" "{}" \+
    # List images of an exist project(s)
elif [ $2 = "--list-image" -o $2 = "-li" ]; then
    re_images="\\.\(bin\|image\|vmdk\|vdi\|vhd\|qcow2\|qcow\|img\|raw\|ovf\|ova\)"
    find "$1" -type f -iname "*.gns3" -print -exec grep --color "$re_images" "{}" \+
    # List note font properties of an exist project(s)
elif [ $2 = "--list-font" -o $2 = "-lf" ]; then
    find "$1" -type f -iname "*.gns3" -print -exec grep --color '\(font-family=..\).[^\]*' "{}" \+
    # List appliance font properties of an exist project(s)
elif [ $2 = "--list-afont" -o $2 = "-lF" ]; then
    find "$1" -type f -iname "*.gns3" -print -exec grep --color '\(font-family: \).[^;]*' "{}" \+
else
    echo "ERROR!: Unsupported option"
    echo "Try './gns3hack.sh --help' for more information"
fi


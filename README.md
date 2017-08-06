Usage: gns3hack gns3-gui_dir [OPTION]... <value>
       gns3hack gns3-project_dir [OPTION] <value>
Options:
  -b, --bg-color		Change gns3-gui background color
  -f, --fg-color		Change gns3-gui foreground color
  -o, --opacity			Change gns3-gui windows opacity
  -t, --toolbar-bg-color	Change gns3-gui toolbar bg color
  -y, --sel-bg-color		Change gns3-gui selection bg color
  -Y, --sel-fg-color		Change gns3-gui selelction fg color
  -n, --font-type		Change note font-family
  -c, --font-color		Change note font color
  -z, --font-size		Change note font size
  -N, --afont-type		Change appliance font-family
  -C, --afont-color		Change appliance font color
  -Z, --afont-size		Change appliance font size
  -i, --image			Change images (IOU,IOS,qemu,vbox,..) used by a  project(s)
  -s, --symbol			Change router,switch,etc.. symbol(icon)
  -I, --list-image		List images (IOU,IOS,qemu,vbox,..) used by a project(s)
  -S, --list-symbol		List symbols used by a project
  -F, --list-font		List current note font(s) used by a project
  -A, --list-afont		List current appliance font(s) used by a project
  -d, --delete-backup		Delete gns3.backup files

Examples:
Get information about a project(s)	
    cd ~/gns3/project/project_name	# cd to your gns3 project folder
    ./gns3hack.sh . --list-images	# get images names used by a project
    ./gns3hack.sh . --list-fonts	# get note font properties used by a project
    ./gns3hack.sh . --list-afonts	# get appliance font properties used by a project 
    ./gns3hack.sh . --list-symbols	# get devices symbols used by a project

Change images(IOU,IOS,qemu,vbox,...) used by a project(s)	
    1. cd ~/gns3/project/project-name	# cd to your gns3 project folder
    2. ./gns3hack.sh . --list-images	# Choose image from the list to replace
    3. ./gns3hack.sh . -i "i86bi-linux-l3-adventerprisek9-15.4.2T4.bin" "i86bi-linux-l3-adventerprisek9-15.5.2T.bin"	# Replace the image
    4. restart gns3
To change all projects images, cd to main project directory instead of specific project directory in step 1 
Note: Any new image(s) must be added to gns3 and installed to the same directory as the old one, if you dont add the new image(s), you'll receive this error message 'The image image-name is missing'. This is a very good option if you want to test new image(s) on an existing project(s) and revert back, or you have new working image(s) and you want to use it for all of your projects

Change gns3 interface bg-color fg-color toolbar-color opacity ....
1. Donwload gns3-gui source code from github.com (`url: https://github.com/GNS3/gns3-gui/releases/tag/v2.0.3`)
2. Download gns3-gui/gns3/ui from (`https://github.com/n3oxmind/gns3hack`) and copy paste it to the original gns3-gui folder from step 1
3. Now you can use gns3hack.sh script to do some changes to gns3-gui
Lets do some changes to gns3 interface
  cd ~/Download/gns3-gui-2.0.3		# cd to gns3-gui source code folder
  ./gns3hack.sh . -b "#282828"		# Change gns3-gui bg color
  ./gns3hack.sh . -f "#00ff00"		# Change gns3-gui fg color
  ./gns3hack.sh . -t "#323232"		# Change gns3-gui tool bar color
  ./gns3hack.sh . -o 9.5		# Change gns3 window opacity
  ./gns3hack.sh . -b "#282828" -f white -t "#323232"		# All at once in any order
  ./gns3hack.sh . -f white -t "#323232" -b black -o 0.99		

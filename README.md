		
# gns3hack

gns3hack is a shell script that will allows you to do the following:
- Change gns3 background color, foreground color and opacity
- Change images (IOU,ISO,qemu,vbox,..etc) used by a project(s)
- Change devices symbols used by a project(s)
- Change font attributes used by a project(s)
- Delete gns3.backup files (cleanup utility)
- Get information about project(s) e.g.(images and fonts used by project(s))
- Generate IOU license key


### Prerequisites
These steps required only if you want to change gns3-gui colors (bg,fg,toolbar,..etc)
1. Download gns3-gui source code from github.com [gns3-gui-2.0.3](url: https://github.com/GNS3/gns3-gui/releases/tag/v2.0.3)
2. Download gns3-gui/gns3/ui from [gns3hack](https://github.com/n3oxmind/gns3hack) and copy paste it to the original gns3-gui folder in step 1

### GNS3 Theming Examples
#### Dark Theme
```
cd /path/to/gns3-gui-2.0.3/
./gns3hack.sh . -b "#282828" -f "#d5c4a1" -t "#323232" -o 0.98
```
![dark1](https://user-images.githubusercontent.com/10103340/29939593-3c172d58-8e41-11e7-80d8-b2a7163fde19.png)
![dark2](https://user-images.githubusercontent.com/10103340/29940069-e2e0c576-8e42-11e7-9874-782c59795792.png)

#### Solarized Light Theme
```
cd /path/to/gns3-gui-2.0.3/
./gns3hack.sh . -b "#fdf6e3" -f "#586e75" -t "#fae8b7"
```
![solarized1](https://user-images.githubusercontent.com/10103340/29939942-7e1e9d3e-8e42-11e7-8e19-f9fa0dac282f.png)
![solarized2](https://user-images.githubusercontent.com/10103340/29939950-7ff4d4f2-8e42-11e7-9d21-741e5d92bf44.png)


### List and Replace Images used by a project(s)
Replace old IOU images of an existing project with new once. This also very useful incase you working on a project and suddenly you found a feature not supported (or not working) by your installed IOU image. This will help you replace all IOU images at once.

```
0. add the new image(s) normally through gns3 prefrences menu
1. cd /path/to/GNS3/projects/folder
2. ./gns3hack . --list-images
"i86bi-linux-l3-adventerprisek9-15.2.2T.bin"
"i86bi-linux-l3-adventerprisek9-15.2.2T.bin"
"i86bi-linux-l3-adventerprisek9-15.2.2T.bin"
"i86bi-linux-l3-adventerprisek9-15.2.2T.bin"
"i86bi_linux_l2-advipservicesk9-ms CLS.nov3_2015_high_iron"
3. ./gns3hack --image "i86bi-linux-l3-adventerprisek9-15.2.2T.bin" "i86bi-linux-l3-adventerprisek9-15.5.2T.bin"
4. restart gns3 to apply changes
```
### List and Replace multiple project symbols 
```
0. copy the new symbols to $HOME/GNS3/symbols/
1. cd /path/to/GNS3/projects/folder
2. ./gns3hack . --list-symbols"router5.svg"
"router5.svg"
"router5.svg"
"router5.svg"
"router5.svg"
"router5.svg"
"router5.svg"
"router5.svg"
"router5.svg"
"router5.svg"
":/symbols/cloud.svg"
":/symbols/ethernet_switch.svg"

3. ./gns3hack . -s "router5.svg" "newsymbol.svg"
4. restart gns3 to apply changes
```
#### Some colored symbols ready for use
![selection_007](https://user-images.githubusercontent.com/10103340/29942095-841f8304-8e49-11e7-907b-3fed6f890a14.png)

### Generate IOU license key
This will generate IOU licese key and store it in ~/.iourc file
```
./gns3hack --key
```

### see ./gns3hack --help for more hacks



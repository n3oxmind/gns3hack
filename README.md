		
# gns3hack

gns3hack is a shell script that allows modifying existing project(s)
- Replace L2/L3,IOS images of an existing project(s)
- Change devices symbols(icons) of an existing project(s)
- Change font attributes used by a project(s) (support note font and appliance font: type,color,size)
- Get information about project(s) e.g.(images and fonts used by project(s)) (this could be use to fix corrupted project)
- Make gns3 project pretty by setting different font and color for both devices and notes
- Generate IOU license key

### Prerequisites
Create a symbolic link to gns3hack
```sh
sudo chmod +x ~/gns3hack.sh
sudo ln -s ~/gns3hack.sh /usr/bin/gns3hack
```
### Get some info about your project(s) 
```sh
$ gns3hack --li
"i86bi-linux-l3-adventerprisek9-15.5.2T.bin"
"i86bi_linux_l2-advipservicesk9-ms.nov3_2015_high_iron.bin"
"i86bi_linux_l2-advipservicesk9-ms.nov3_2015_high_iron.bin"
"i86bi_linux_l2-advipservicesk9-ms.nov3_2015_high_iron.bin"
"i86bi_linux_l2-advipservicesk9-ms.nov3_2015_high_iron.bin"
"i86bi_linux_l2-advipservicesk9-ms.nov3_2015_high_iron.bin"
```
### Replace IOU image with new one. 
```sh
$ gns3hack -i "i86bi_linux_l2-advipservicesk9-ms.nov3_2015_high_iron.bin" "i86bi-linux-l2-adventerprisek9-15.6.1T.bin"
```
Replacing old L2/L3 images with new once will not delete/modify your current configuration. L2/L3 configuration will be maintained as its. 

### List and Replace project symbols 
```sh
$ gns3hack --ls
"router3.svg"
"Server3.svg"
"Server3.svg"
"Server3.svg"
"Server3.svg"
"Server3.svg"
"Server3.svg"
"multilayer_switch3.svg"
"router_switch_processor3.svg"
"router_switch_processor3.svg"
"multilayer_switch3.svg"
"multilayer_switch3.svg"
"multilayer_switch3.svg"
"Server3.svg"
"Server3.svg"
"cloud2.svg"
"PC1.svg"
"PC1.svg"
"PC1.svg"
"Server3.svg"
"Server3.svg"
"Server3.svg"
"PC1.svg"
```
```sh
$ gns3hack -m "PC1.svg" "newsymbol.svg"
```
### Generate IOU license key
This will generate IOU licese key and store it in `~/.iourc` file
```sh
$ gns3hack --key
```
### Prettify project (from a predefined colors)
```sh
$ gns3hack --pretty light
```
**Before prettifying**
![before prettify](https://user-images.githubusercontent.com/10103340/40515671-89ab6c94-5f62-11e8-9ad7-b1fba5f30837.png)
**After (light theme)**
![after-prettify](https://user-images.githubusercontent.com/10103340/40515676-8bc9965e-5f62-11e8-8caa-40a8b5306750.png)

**Note:**
* GNS3 need to know about the new images before replacing , so add them through `Edit->Prefrences`.
* New Fonts need to be added to your system first or gns3 will fallback to the default.
* New symbols (icons) need to be added to gns3 default symbols location (~/GNS3/symbols).

For more information please see `./gns3hack.sh --help`.


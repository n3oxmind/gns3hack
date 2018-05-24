		
# gns3hack

gns3hack is a shell script that will allows you to do the following:
- Change images of an existing project(s)
- Change devices symbols used by a project(s)
- Change font attributes used by a project(s)
- Get information about project(s) e.g.(images and fonts used by project(s))
- Make gns3 project pretty by setting different font and color for both devices and notes
- Generate IOU license key

### Prerequisites
Create a symbolic link to gns3hack
```sh
sudo chmod +x ~/gns3hack.sh
sudo ln -s ~/gns3hack.sh /usr/bin/gns3hack
```
### Prettify project (from a predefined colors)
```sh
$ gns3hack --dfont light
"i86bi-linux-l3-adventerprisek9-15.5.2T.bin"
```
**Before prettifying**
![before prettify](https://user-images.githubusercontent.com/10103340/40515671-89ab6c94-5f62-11e8-9ad7-b1fba5f30837.png)
**After (light theme)**
![after-prettify](https://user-images.githubusercontent.com/10103340/40515676-8bc9965e-5f62-11e8-8caa-40a8b5306750.png)
**After (dark theme)**
![after-prettify2](https://user-images.githubusercontent.com/10103340/40515678-8db4b2fa-5f62-11e8-99d8-255e8d6d0d1f.png)

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
### List and Replace multiple project symbols 
```sh
$ gns3hack --ls
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
```
```sh
$ gns3hack -m "router5.svg" "newsymbol.svg"
```
### Generate IOU license key
This will generate IOU licese key and store it in ~/.iourc file
```sh
$ gns3hack --key
```
**Note:**
Before replacing anything (image, symbol, font) make sure to install it.
For gns3 images Add them the normal way through `Edit->Prefrences`.

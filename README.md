		
# gns3hack

gns3hack is a shell script that will allows you to do the following:
- Change images of an existing project(s)
- Change devices symbols used by a project(s)
- Change font attributes used by a project(s)
- Get information about project(s) e.g.(images and fonts used by project(s))
- Generate IOU license key

### Prerequisites
Create a symbolic link to gns3hack
```
sudo ~/Download/gna3hack/gna3hack.sh /usr/bin/gns3hack
```
### Get some info about your project(s) 
```
gns3hack --li
"i86bi-linux-l3-adventerprisek9-15.5.2T.bin"
"i86bi_linux_l2-advipservicesk9-ms.nov3_2015_high_iron.bin"
"i86bi_linux_l2-advipservicesk9-ms.nov3_2015_high_iron.bin"
"i86bi_linux_l2-advipservicesk9-ms.nov3_2015_high_iron.bin"
"i86bi_linux_l2-advipservicesk9-ms.nov3_2015_high_iron.bin"
"i86bi_linux_l2-advipservicesk9-ms.nov3_2015_high_iron.bin"
```
### Replace IOU image with new one.
```
gns3hack -i "i86bi_linux_l2-advipservicesk9-ms.nov3_2015_high_iron.bin" "i86bi-linux-l2-adventerprisek9-15.6.1T.bin"
```
### List and Replace multiple project symbols 
```
gns3hack --ls
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
```
gns3hack -m "router5.svg" "newsymbol.svg"
```
### Generate IOU license key
This will generate IOU licese key and store it in ~/.iourc file
```
gns3hack --key
```
**Note:**
Before replacing anything (image, symbol, font) make sure to install it.
For gns3 images Add them the normal way through `Edit->Prefrences`.

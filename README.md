		
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
1. Download gns3-gui source code from github.com (`url: https://github.com/GNS3/gns3-gui/releases/tag/v2.0.3`)
2. Download gns3-gui/gns3/ui from (`https://github.com/n3oxmind/gns3hack`) and copy paste it to the original gns3-gui folder in step 1

### GNS3 Theming Examples

#### Dark Theme
```
cd gns3-gui-2.0.3 directory
./gns3hack.sh -b "#282828" -f "#d5c4a1" -t "#323232" -o 0.98
```
![dark1](https://user-images.githubusercontent.com/10103340/29939593-3c172d58-8e41-11e7-80d8-b2a7163fde19.png)
![dark2](https://user-images.githubusercontent.com/10103340/29940069-e2e0c576-8e42-11e7-9874-782c59795792.png)

#### Solarized Light Theme
```
cd gns3-gui-2.0.3 directory
./gns3hack.sh -b "#fdf6e3" -f "#586e75" -t "#fae8b7"
```
![solarized1](https://user-images.githubusercontent.com/10103340/29939942-7e1e9d3e-8e42-11e7-8e19-f9fa0dac282f.png)
![solarized2](https://user-images.githubusercontent.com/10103340/29939950-7ff4d4f2-8e42-11e7-9d21-741e5d92bf44.png)


### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```


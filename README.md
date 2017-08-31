		
# gns3hack

gns3hack is a shell scripts that will allows you to do the following:
	- Change gns3 background color, forground color and oopacity
	- Change images (IOU,ISO,qemu,vbox,..etc) used by a project(s)
	- Change devices symbols used by a project(s)
	- Change font attributes used by a project(s)
	- Delete gns3.backup files (cleanup utility)
	- Get information about project(s) e.g.(images and fonts used by project(s))
	- Generate IOU license key


### Prerequisites
These steps required only if you want to change the look of gns3-gui (theme)
	1. Download gns3-gui source code from github.com (`url: https://github.com/GNS3/gns3-gui/releases/tag/v2.0.3`)
	2. Download gns3-gui/gns3/ui from (`https://github.com/n3oxmind/gns3hack`) and copy paste it to the original gns3-gui folder in step 1
	3. cd gns3-gui directory
	3. Use gns3hack.sh script to do some changes to gns3-gui

### GNS3 Theming Example

#### Dark Theme
```
cd gns3-gui-2.0.3 directory
./gns3hack.sh -b "#fdf6e3" -f "#586e75" -t "#fae8b7"
```
#### Solarized Light Theme
```
cd gns3-gui-2.0.3 directory
./gns3hack.sh -b "#fdf6e3" -f "#586e75" -t "#fae8b7"
```
#### Light Theme
```
cd gns3-gui-2.0.3 directory
./gns3hack.sh -b "#fdf6e3" -f "#586e75" -t "#fae8b7"
```

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


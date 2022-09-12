## Why the fork on 12 September 2022

The [original repo from trevorsandy](https://github.com/trevorsandy/blenderldrawrender) is abandoned
from 18 July 2020. This addons seems promising but it doesnt install on Blender 2.92+ (I'm using 3.2).
I want to try to use this addon to create Syntethic data for Machine Learning training. It should have everything needed
but without a single HOW-TO, I need to "reverse engineer" the code and figure it out. Will write the How-to and
example Blender script once I understand how to actually do it.

<br />
<br />

# HOW-TO Install on Blender 2.92+ (tested on 3.2)

The process is quite simple:

1. <b>Download the latest release</b> (or git clone and use the script "create_local_package_ready_for_blender.sh")(but dont forget the file background.exr, git for some reason doesn't allow the push, can be found on the release)
2. <b>Open Blender, go to Edit->Preferences->Add-ons.</b>  Click install in the top right and locate the zip file with the lastest release. Select the file and click Install Add-ons.
3. <b> Open a terminal and navigate (cd) to the Blender addons directory.</b> This depends on the OS and user settings. In my case, on windows 10, it is: C:\Users\Username\AppData\Roaming\Blender Foundation\Blender\3.2\scripts\addons
4. <b>Here you should see a file called installBlenderAddons.py</b> and to be completly safe, just check you have a file called ldraw_render_addons.zip inside the addons subdir. (addons/addons/)
5. <b>Launch the script using Blender engine.</b> This depends again on SO. The basic idea is the same launch blender passing this script as argument. In windows 10 in my case it was: C:\Users\Alessio\AppData\Roaming\Blender Foundation\Blender\3.2\scripts\addons><b> & 'C:\Program Files\Blender Foundation\Blender 3.2\blender.exe' --background --python .\installBlenderAddons.py</b> (offcourse you need python and pip installed on your system.)
6. <b> Congratulations, you did it!</b> You should see the message INFO: LDraw Addons installed. Blender quit
7.<b>Now open Blender, go back in Edit->Preferences->Add-ons, search for ldraw and activate (✔️) the 2 new add-ons (importer and renderer)</b>

At this point you can check in menu File->Import and see, you should have as first (probably) option the LPUB3D Import LDraw where you need to set your ldraw directory and to save it, try to import an ldraw part. Everything should be fine. You also will have a new option under menu Render->LPUB3D Render LDraw.


## TODO:

<s>-Guide on HOW-TO install</s>  
-Working example on how to script Blender for actually use this addons.

<br />
<br />


### Original ReadME from the original author.

<hr>

<br />

## LPub3D Render LDraw Models with Blender

A [Blender](https://www.blender.org)&trade; add-on for importing and rendering [LDraw](http://www.ldraw.org)&trade; file format models and parts.

## Purpose

_LPub3D Import LDraw_ imports [LEGO](https://www.lego.com/)® models into Blender. This addon is intended to support direct Blender integration with [LPub3D](https://trevorsandy.github.io/lpub3d).

This addon was designed to provide [LPub3D](https://trevorsandy.github.io/lpub3d) an autonomous module enabling the integrated import and render of LDraw [LEGO](https://www.lego.com/)® models using [Blender](https://www.blender.org)&trade;. However, it can be executed directly from the Blender GUI, CLI or your operating system command console.

It supports **.mpd**, **.ldr**, and **.dat** file formats.

The LDraw import module is adapted from [Import LDraw](https://github.com/TobyLobster/ImportLDraw) by Toby Nelson (tobymnelson@gmail.com).

## Render Features

- Available for Blender 2.80 and later (2.79 backport in progress).
- **Mac**, **Windows** and **Linux** supported.
- **MPD** file compatible.
- **Render settings configurable** from LPub3D user interface.
- **Monitor render progress** from LPub3D user interface or launch Blender and directly invoke render routine from manu item.
- **Render Portable Network Graphics (.png)** image files.
- **Crop images** with transparent background to their opaque bounds
- **Specify transparent background** from render settings
- **Specify blendfile** to load additional settings
- **Specify exr 'environment' file** to load custom backdrop and ground plane

## Import Features

- Available for Blender 2.80 and later (2.79 backport in progress).
- **Mac**, **Windows** and **Linux** supported.
- **MPD** file compatible.
- **Import settings configurable** from LPub3D user interface.
- **LeoCAD** groups and cameras (both perspective and orthographic) supported.
- **LSynth** bendable parts supported (synthesized models).
- **LDCad** generated parts supported.
- **Additional LDraw parts paths** can be specified.
- **LGEO colours, sloped bricks and lighted bricks** can be custom configured via parameter (ini) file.
- **Import and apply camera settings** from LPub3D generated LDraw content
- **Import and apply light settings** from LPub3D generated LDraw content.
- **Pointlignt**, **Sunlight**, **Spotlight** and **Arealight** sources available.
- **LDraw archive (.zip) or disc library** supported. Archive libraries are auto detected when available at the specified LDraw directory path.
- _Cycles_ and _Blender Render_ engines supported. It renders either engine from a single scene.
- Import **Photorealistic** look, or **Instructions** look.
- **Physically Based Realistic materials** - standard brick material, transparent, rubber, chrome, metal, pearlescent, glow-in-the-dark, glitter and speckle.
- **Principled Shader supported** Uses Blender's 'Principled Shader' where available for optimal look (but still works well when unavailable).
- **Accurate colour handling**. Correct colour space management is used so that e.g. black parts look black.
- **Direct colours** supported.
- **Back face culling** - fully parses all BFC information, for accurate normals.
- **Linked duplicates** - Parts of the same type and colour can share the same mesh.
- **Linked studs** - studs can also share the same mesh.
- Studs can include the **LEGO logo** on them, adding extra geometry.
- **Gaps between bricks** - Optionally adds a small space between each brick, as in real life.
- **Smart face smoothing** - Uses Edge-Split Modifier and Sharp Edges derived from Ldraw lines, for smooth curved surfaces and sharp corners.
- **Concave walls** - Optionally look as if each brick has very slightly concave walls (with the photorealistic renderer), which affects the look of light reflections.
- **Light bricks** - Bricks that emit light are supported.
- **Fast** - even large models can be imported in seconds.

### License

_LPub3D Render LDraw_ is licensed under the [GPLv2](http://www.gnu.org/licenses/gpl-2.0.html) or any later version.

**LEGO**® is a registered trademark of the Lego Group<br clear=left>

Copyright (c) 2020 by Trevor SANDY

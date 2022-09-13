#!/bin/bash
BLENDER_ADDONDIR=/mnt/c/Documents\ and\ Settings/Alessio/AppData/Roaming/Blender\ Foundation/Blender/3.2/scripts/addons
check_dir=$BLENDER_ADDONDIR/addons

echo ""
echo ""
echo "Removing all files from installation of LDraw Blender Import/Render Add-on ..."
echo ""
echo "Base Directory: $BLENDER_ADDONDIR"
echo ""
echo "Dir used as check if dir exist and its Blender addons:"
echo "$check_dir"
echo ""

if [ -d  "$check_dir" ];then
    echo "FOUND Blender addons directory..."
    if [ -d "$BLENDER_ADDONDIR/io_scene_lpub3d_importldraw" ];then
        rm -rf "$BLENDER_ADDONDIR/io_scene_lpub3d_importldraw"
    else
        echo "cant find io_scene_lpub3d_importldraw"
    fi

    if [ -d "$BLENDER_ADDONDIR/io_scene_lpub3d_renderldraw" ];then
        rm -rf "$BLENDER_ADDONDIR/io_scene_lpub3d_renderldraw"
    else
        echo "cant find io_scene_lpub3d_renderldraw to remove."
    fi

    if [ -f "$BLENDER_ADDONDIR/addons/ldraw_render_addons.zip" ];then
        rm "$BLENDER_ADDONDIR/addons/ldraw_render_addons.zip"
    else
        echo "cant find addons/ldraw_render_addons.zip to remove."
    fi

    if [ -f "$BLENDER_ADDONDIR/config/BlenderLDrawParameters.lst" ];then
        rm "$BLENDER_ADDONDIR/config/BlenderLDrawParameters.lst"
    else
        echo "cant find config/BlenderLDrawParameters.lst to remove."
    fi
    if [ -f "$BLENDER_ADDONDIR/installBlenderAddons.py" ];then
        rm "$BLENDER_ADDONDIR/installBlenderAddons.py"
    else
        echo "cant find installBlenderAddons.py to remove."
    fi
    echo "Removed what possibile of addons files from Blender addons directory."
else
    echo "Cant find Blender addons directory."
fi
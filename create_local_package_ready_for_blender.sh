


GH_ASSET_NAME=${ASSET_NAME:-LDrawBlenderImportRenderAdd.zip}


function package_archive
{
	echo && echo "Creating release package..."
	if [ -f $GH_ASSET_NAME ];then
		rm $GH_ASSET_NAME
	fi
	cd ./addons
	zip -r ldraw_render_addons.zip io_scene_lpub3d_importldraw io_scene_lpub3d_renderldraw -x \
	"io_scene_lpub3d_importldraw/__pycache__/*" \
	"io_scene_lpub3d_importldraw/images/*" \
	"io_scene_lpub3d_importldraw/loadldraw/__pycache__/*" \
	"io_scene_lpub3d_importldraw/LICENSE" \
	"io_scene_lpub3d_importldraw/README.md" \
	"io_scene_lpub3d_renderldraw/__pycache__/*"
	cd ../
	zip -r $GH_ASSET_NAME addons/ldraw_render_addons.zip config/BlenderLDrawParameters.lst installBlenderAddons.py
	rm addons/ldraw_render_addons.zip
	echo && echo "Created release package '$GH_ASSET_NAME'" && echo
}

package_archive

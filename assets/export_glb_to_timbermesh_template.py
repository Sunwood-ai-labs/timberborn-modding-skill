import sys
from pathlib import Path

import addon_utils
import bpy
import mathutils


PLUGIN_DIR = r"D:\path\to\timbermesh_blender_plugin"
INPUT_GLB = r"D:\path\to\MyHouse.glb"
OUTPUT_MODEL = r"D:\path\to\Assets\Mods\MyHouse\Data\Buildings\Decorations\MyHouse\MyHouse.Folktails.Model.timbermesh"
OUTPUT_TEXTURE = r"D:\path\to\Assets\Mods\MyHouse\AssetBundles\Resources\Materials\MyHouse\MyHouseBaseTexture.png"
COLLECTION_NAME = "MyHouse.Folktails"
MATERIAL_NAME = "MyHouseBase"

if PLUGIN_DIR not in sys.path:
    sys.path.append(PLUGIN_DIR)

import timbermesh_exporter


def reset_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)


def enable_gltf_importer():
    addon_utils.enable("io_scene_gltf2", default_set=False, persistent=False)


def import_glb(path: Path):
    bpy.ops.import_scene.gltf(filepath=str(path))
    return [obj for obj in bpy.data.objects if obj.type == "MESH"]


def get_base_color_image(material):
    if material is None or material.node_tree is None:
        return None
    for node in material.node_tree.nodes:
        if node.type != "BSDF_PRINCIPLED":
            continue
        socket = node.inputs.get("Base Color")
        if socket is None:
            return None
        for link in socket.links:
            source = link.from_node
            if source.type == "TEX_IMAGE" and source.image:
                return source.image
    return None


def save_image(image, destination: Path):
    destination.parent.mkdir(parents=True, exist_ok=True)
    image.save_render(str(destination))


def rename_material_and_extract_texture(obj):
    source_material = obj.material_slots[0].material if obj.material_slots else None
    if source_material is None:
        raise RuntimeError("Imported mesh has no material")
    image = get_base_color_image(source_material)
    if image is not None:
        save_image(image, Path(OUTPUT_TEXTURE))
    mesh = obj.data
    mesh.materials.clear()
    material = bpy.data.materials.new(MATERIAL_NAME)
    material.use_nodes = True
    mesh.materials.append(material)
    for polygon in mesh.polygons:
        polygon.material_index = 0


def ensure_white_vertex_colors(obj):
    mesh = obj.data
    attr = mesh.color_attributes.get("Col")
    if attr is None:
        attr = mesh.color_attributes.new(name="Col", type="BYTE_COLOR", domain="CORNER")
    for data in attr.data:
        data.color = (1.0, 1.0, 1.0, 1.0)


def retarget_for_timberborn(obj):
    obj.location += mathutils.Vector((-1.0, -1.0, 1.0))


def move_to_export_collection(name: str, objects):
    collection = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(collection)
    for obj in objects:
        for user_collection in list(obj.users_collection):
            user_collection.objects.unlink(obj)
        collection.objects.link(obj)
    return collection


def export_timbermesh(collection, output_path: Path):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    settings = timbermesh_exporter.ExportSettings(
        bpy.context,
        merge_meshes=True,
        single_animation=True,
        use_vertex_animations=False,
    )
    timbermesh_exporter.Exporter.export_collection(collection, str(output_path), settings)


def main():
    reset_scene()
    enable_gltf_importer()
    objects = import_glb(Path(INPUT_GLB))
    if not objects:
        raise RuntimeError("No mesh objects were imported from the GLB")

    for obj in objects:
        rename_material_and_extract_texture(obj)
        ensure_white_vertex_colors(obj)
        retarget_for_timberborn(obj)

    collection = move_to_export_collection(COLLECTION_NAME, objects)
    export_timbermesh(collection, Path(OUTPUT_MODEL))
    print("MODEL_WRITTEN", OUTPUT_MODEL)
    print("TEXTURE_WRITTEN", OUTPUT_TEXTURE)


if __name__ == "__main__":
    main()

import bpy
import argparse, sys

parser = argparse.ArgumentParser()
parser.add_argument("--input_path")
parser.add_argument("--output_path")
parser.add_argument("--target_texture")
parser.add_argument("--target_scene")
parser.add_argument("--is_animation", dest="is_animation", action="store_true")
parser.set_defaults(is_animation=False)

params = vars(parser.parse_args(sys.argv[sys.argv.index("--")+1:]))

print(params)
image = bpy.data.images.load(params['input_path'])
target = bpy.data.textures[params['target_texture']]
target.image = image
bpy.data.scenes[params['target_scene']].render.filepath = params['output_path']
bpy.ops.render.render(write_still=True, animation=params['is_animation'])



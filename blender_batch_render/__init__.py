import subprocess, os

def render(input_path, output_path, template_path='template.blend', target_texture='target-texture', target_scene='Scene', is_animation=False, blender_path='blender'):
    path_to_blender_script = os.path.dirname(os.path.realpath(__file__))
    blender_script_params = []
    blender_script_params.append('input_path={}'.format(format_path(input_path)))
    blender_script_params.append('output_path={}'.format(format_path(output_path)))
    blender_script_params.append('target_texture={}'.format(format_path(target_texture)))
    blender_script_params.append('target_scene={}'.format(format_path(target_scene)))
    if is_animation == True:
        blender_script_params.append('is_animation')
    cmd = [blender_path, format_path(template_path), '--background', '--python', '"' + path_to_blender_script + '"', '--']

    process = subprocess.Popen(cmd + blender_script_params).wait()

def format_path(path):
    if ' ' in path:
        path = "\"{}\"".format(path)
    return path
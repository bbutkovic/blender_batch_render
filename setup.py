from setuptools import setup

setup(name='blender_batch_render',
      version='0.1',
      description='Tool for rendering Blender models in batch with every supplied texture.',
      url='http://github.com/bbutkovic/funniest',
      author='Borna Butkovic',
      author_email='bornabutkovic@gmail.com',
      license='MIT',
      packages=['blender_batch_render'],
      install_requires=['bpy'],
      zip_safe=False)
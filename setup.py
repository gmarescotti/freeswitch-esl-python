from distutils.core import setup, Extension
import platform

if platform.system() == 'Windows':
    windows_extensions=dict(
        define_macros=[('WIN32', None), ('ESL_EXPORTS', None)],
        libraries=['Ws2_32']
    )
    import os
    if 'VS90COMNTOOLS' not in os.environ:
        # Try out different version of Visual Studio
        # The only version seen working is Windows7 + VisualStudio 12.0
        for VS in ['120', '110', '100', '130', '140']:
            if 'VS%sCOMNTOOLS' % VS in os.environ:
                os.environ['VS90COMNTOOLS'] = os.environ['VS%sCOMNTOOLS' % VS]
                break
    assert 'VS90COMNTOOLS' in os.environ, "Not found any Visual Studio Installation!"
else:
    windows_extensions = dict()

setup (name = 'FreeSWITCH-esl-python',
       version = '0.1vdev',
       ext_modules=[Extension('_ESL',sources=['swig/esl_wrap.cpp',
                                              'src/esl.c',
                                              'src/esl_json.c',
                                              'src/esl_event.c',
                                              'src/esl_threadmutex.c',
                                              'src/esl_config.c',
                                              'src/esl_oop.cpp',
                                              'src/esl_buffer.c'],
       include_dirs=['include/'], **windows_extensions)],
       packages = ['freeswitchESL'],
       pymodules = ['ESL'],
       description = 'Auto-generated swig python module for FreeSWITCH mod_esl with a binary component.',)

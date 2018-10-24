from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='botw-mate',
    version='0.1.0',
    packages=['venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.idna',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.pytoml',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.certifi',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.chardet',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.chardet.cli',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.distlib',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.distlib._backport',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.msgpack',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.urllib3',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.urllib3.util',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.urllib3.contrib',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.urllib3.contrib._securetransport',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.urllib3.packages',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.urllib3.packages.backports',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.urllib3.packages.ssl_match_hostname',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.colorama',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.html5lib',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.html5lib._trie',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.html5lib.filters',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.html5lib.treewalkers',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.html5lib.treeadapters',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.html5lib.treebuilders',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.lockfile',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.progress',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.requests',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.packaging',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.cachecontrol',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.cachecontrol.caches',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.webencodings',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._vendor.pkg_resources',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._internal',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._internal.req',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._internal.vcs',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._internal.utils',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._internal.models',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._internal.commands',
              'venv.Lib.site-packages.pip-10.0.1-py3.6.egg.pip._internal.operations', 'mate'],
    url='https://github.com/zephenryus/botw-mate',
    license='MIT',
    author='zephenryus',
    author_email='kevin@turtlerockweb.com',
    description='Decompile mate files from the Legend of Zelda: Breath of the Wild',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        'Pillow'
    ]
)

from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'GONG GONG'
LONG_DESCRIPTION = 'GONG GONG GONG GONG'

setup(
    name='py_gong_gong',
    version=VERSION,    
    description=DESCRIPTION,
    url='https://github.com/Arkenbrien/py_gong_gong',
    author='Rhett Huston',
    packages=find_packages(),
    install_requires=['random', 'playsound'],
    classifiers=[
        "Development Status :: Complete",  
        "Operating System :: UBUNTU 18.04 :: Linux",
        "Programming Language :: Python :: 3"
    ],
)

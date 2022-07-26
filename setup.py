from setuptools import setup

setup(
    name='dict2tex',
    version='1.0.0',    
    description='Converting parameter dictionaries to LaTeX code',
    url='https://github.com/tomtetzlaff/dict2tex',
    author='Tom Tetzlaff',
    author_email='t.tetzlaff@fz-juelich.de',
    license='GNU General Public License v3.0',
    packages=['dict2tex'],
    install_requires=['numpy',                     
                      ],
)

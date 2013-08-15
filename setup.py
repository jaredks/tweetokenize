#!/usr/bin/env python
from distutils.core import setup
import tweetokenize

setup(
    name='tweetokenize',
    version=tweetokenize.__version__,
    description='Regular expression based tokenizer for Twitter',
    author='Jared Suttles',
    url='https://github.com/jaredks/tweetokenize',
    packages=['tweetokenize'],
    package_data={'': ['LICENSE'], 'tweetokenize': ['lexicons/*.txt']},
    long_description=open('README.md').read() + '\n\n' + open('CHANGES').read(),
    license='BSD License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic',
    ],
)

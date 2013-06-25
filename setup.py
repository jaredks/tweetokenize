#!/usr/bin/env python
from distutils.core import setup
import tweetokenize

setup(name='tweetokenize',
      version=tweetokenize.__version__,
      description='Regular expression based tokenizer for Twitter',
      author='Jared Suttles',
      url='https://github.com/jaredks/tweetokenize',
      packages=['tweetokenize'],
      package_data={'': ['LICENSE'], 'tweetokenize': ['lexicons/*.txt']},
      long_description=open('README.md').read(),
      license=open('LICENSE').read()
      )

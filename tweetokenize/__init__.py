#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# tweetokenize: Regular expression based tokenizer for Twitter
# Copyright: (c) 2013, Jared Suttles. All rights reserved.
# License: BSD, see LICENSE for details.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

"""
Tokenization and pre-processing for social media data used to train classifiers.
Focused on classification of sentiment, emotion, or mood.

Intended as glue between Python wrappers for Twitter API and machine
learning algorithms of the Natural Language Toolkit (NLTK), but probably
applicable to tokenizing any short messages of the social networking variety.

In many cases, reducing feature-set complexity can increase performance of
classifiers trained for detecting sentiment. The available settings are based
on commonly modified and normalized features in classification research using
content from Twitter.
"""

__title__ = 'tweetokenize'
__version__ = '1.0.1'
__author__ = 'Jared Suttles'
__license__ = 'Modified BSD'
__copyright__ = 'Copyright 2013 Jared Suttles'

from .tokenizer import Tokenizer

tweetokenize
============

Tokenization and pre-processing for social media data used to train classifiers.
Focused on classification of sentiment, emotion, or mood.

Intended as glue between Python wrappers for Twitter API and the Natural 
Language Toolkit (NLTK), but probably applicable to tokenizing any short 
messages of the social networking variety.

```python
from tweetokenize import Tokenizer
gettokens = Tokenizer()
gettokens.tokenize('hey playa!:):3…..@SHAQ can you still dunk?#old🍕🍔😵LOL')
[u'hey', u'playa', u'!', u':)', u':3', u'...', u'USERNAME', u'can', u'you', u'still', u'dunk', u'?', u'#old', u'u'🍕', 'u'🍔', u'😵', u'LOL']
```

Features
========

* Can easily replace tweet features like usernames, urls, phone numbers, times, 
etc. with tokens in order to reduce feature set complexity and improve 
performance of classifiers
* Allows user-defined sets of emoticons to be used in tokenization
* Correctly separates emoji, written consecutively, into individual tokens

Documentation
-------------

http://htmlpreview.github.io/?https://raw.github.com/jaredks/tweetokenize/master/documentation/tweetokenize.Tokenizer-class.html

License
-------
"Modified BSD License". See LICENSE for details.
Copyright Jared Suttles, 2013.

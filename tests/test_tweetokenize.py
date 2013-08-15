#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# tweetokenize: Regular expression based tokenizer for Twitter
# Copyright: (c) 2013, Jared Suttles. All rights reserved.
# License: BSD, see LICENSE for details.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import unittest
from tweetokenize import Tokenizer


class TokenizeTests(unittest.TestCase):
    def setUp(self):
        self.tokenizer = Tokenizer(lowercase=True)
    
    def test_general_1(self):
        self.tokenizer.normalize = 2
        msg = ('omg wow &#x3c; &#x26; &#x3e; &#62;.&#60; &gt;.&lt; :):)'
        'i CANT believe thatttt haha lol!!1')
        tks = ['omg', 'wow', '<', '&', '>', '>.<', '>.<', ':)', ':)',
        'i', 'CANT', 'believe', 'thatt', 'haha', 'lol', '!', '!', '1']
        self.assertEqual(self.tokenizer.tokenize(msg), tks)
    
    def test_general_2(self):
        msg = "i'm wanting to jump up and down but wouldn't if i couldn't.."
        tks = [u"i'm", u'wanting', u'to', u'jump', u'up', u'and', u'down',
        u'but', u"wouldn't", u'if', u'i', u"couldn't", u'...']
        self.assertEqual(self.tokenizer.tokenize(msg), tks)
    
    def test_urls_1(self):
        msg = ("hey bro chec'k out http://shitstorm.com its fucking sick")
        tks = ['hey', 'bro', "chec'k", 'out', 'URL', 'its', 'fucking', 'sick']
        self.assertEqual(self.tokenizer.tokenize(msg), tks)
    
    def test_urls_2(self):
        msg = ('also see this crazy stuff https://shitstorm.com')
        tks = ['also', 'see', 'this', 'crazy', 'stuff', 'URL']
        self.assertEqual(self.tokenizer.tokenize(msg), tks)
    
    def test_urls_3(self):
        msg = 'hiiiii rayj.com/ihititfirst and other google.com http://hobo.net'
        tks = [u'hiii', u'URL', u'and', u'other', u'URL', u'URL']
        self.assertEqual(self.tokenizer.tokenize(msg), tks)
    
    def test_usernames_1(self):
        msg = ('@justinbeiber yo man!! ! i love you in a totally '
        'straight way <3:p:D')
        tks = [u'USERNAME', u'yo', u'man', u'!', u'!', u'!',
        u'i', u'love', u'you', u'in', u'a', u'totally', u'straight', u'way',
        u'<3', u':p', u':D']
        self.assertEqual(self.tokenizer.tokenize(msg), tks)
    
    def test_usernames_2(self):
        msg = '@heyheymango: what did you SAYYY??? or did you just..  NotHING?'
        tks = [u'USERNAME', u':', u'what', u'did', u'you', u'SAYYY', u'?',
        u'?', u'?', u'or', u'did', u'you', u'just', u'...', u'nothing', u'?']
        self.assertEqual(self.tokenizer.tokenize(msg), tks)
    
    def test_numbers_1(self):
        self.tokenizer.numbers = None
        msg = ('i have this much money -2.42 in my bank acct.,friend! but you '
        'have mucho +88e44 and its about 1000% more than $400.')
        tks = [u'i', u'have', u'this', u'much', u'money', u'-2.42', u'in',
        u'my', u'bank', u'acct', u'.', u',', u'friend', u'!', u'but', u'you',
        u'have', u'mucho', u'+88e44', u'and', u'its', u'about', u'1000%',
        u'more', u'than', u'$400', u'.']
        self.assertEqual(self.tokenizer.tokenize(msg), tks)
    
    def test_numbers_2(self):
        msg = ('i have this much money -2.42 in my bank acct.,friend! but you '
        'have mucho +88e44 and its about 1000% more than $400.')
        tks = [u'i', u'have', u'this', u'much', u'money', u'NUMBER', u'in',
        u'my', u'bank', u'acct', u'.', u',', u'friend', u'!', u'but', u'you',
        u'have', u'mucho', u'NUMBER', u'and', u'its', u'about', u'NUMBER',
        u'more', u'than', u'NUMBER', u'.']
        self.assertEqual(self.tokenizer.tokenize(msg), tks)
    
    def test_numbers_3(self):
        self.tokenizer.lowercase = False # keep cases the same everywhere
        msg = ('I JUST want To Test FRACTIONZZZ 22432.41414/ 55894385e-341 also'
        ' lowercase etc.etc.etc. hope that last part doesn\'t parse as a url '
        'i would be kinda sad PANda!zsss..... .. . .... 4/5 5.1/4.0e0 3.14 -2')
        tks = [u'I', u'JUST', u'want', u'To', u'Test', u'FRACTIONZZZ',
        u'NUMBER', u'also', u'lowercase', u'etc', u'.', u'etc', u'.', u'etc',
        u'.', u'hope', u'that', u'last', u'part', u"doesn't", u'parse', u'as',
        u'a', u'url', u'i', u'would', u'be', u'kinda', u'sad', u'PANda', u'!',
        u'zsss', u'...', u'...', u'.', u'...', u'NUMBER', u'NUMBER', u'NUMBER',
        u'NUMBER']
        self.assertEqual(self.tokenizer.tokenize(msg), tks)
    
    def test_time_1(self):
        msg = 'is the time now 12:14pm? or is it like 2:42AM??'
        tks = [u'is', u'the', u'time', u'now', u'TIME', u'?', u'or', u'is',
        u'it', u'like', u'TIME', u'?', u'?']
        self.assertEqual(self.tokenizer.tokenize(msg), tks)
    
    def test_time_2(self):
        msg = 'new time is 2:42:09 PM!!'
        tks = [u'new', u'time', u'is', u'TIME', u'!', u'!']
        self.assertEqual(self.tokenizer.tokenize(msg), tks)
    
    def test_phonenumber_1(self):
        msg = ('my number is 18002432242 and 241.413.5584 also 1-242-156-6724'
        ' and (958)555-4875 or (999) 415 5542 is 422-5555 a 131-121-1441')
        tks = [u'my', u'number', u'is', u'PHONENUMBER', u'and', u'PHONENUMBER',
        u'also', u'PHONENUMBER', u'and', u'PHONENUMBER', u'or', u'PHONENUMBER',
        u'is', u'PHONENUMBER', u'a', u'PHONENUMBER']
        self.assertEqual(self.tokenizer.tokenize(msg), tks)
    
    def test_phonenumber_2(self):
        msg = 'numbers with extension: (201)-340-4915 x112 or 1 800.341.1311x99'
        tks = [u'numbers', u'with', u'extension', u':', u'PHONENUMBER', u'or',
        u'PHONENUMBER']
        self.assertEqual(self.tokenizer.tokenize(msg), tks)
    
    def test_quotes_1(self):
        self.tokenizer.ignorequotes = True
        msg = 'this is just a tweet with "someone said something funny" lol'
        tks = ['this', 'is', 'just', 'a', 'tweet', 'with', 'lol']
        self.assertEqual(self.tokenizer.tokenize(msg), tks)
    
    def test_quotes_2(self):
        self.tokenizer.ignorequotes = False
        msg = 'this is just a tweet with "someone said something funny" lol'
        tks = ['this', 'is', 'just', 'a', 'tweet', 'with', '"', 'someone',
        'said', 'something', 'funny', '"', 'lol']
        self.assertEqual(self.tokenizer.tokenize(msg), tks)
    
    def test_quotes_3(self):
        self.tokenizer.ignorequotes = True
        msg = ('some stuff but he said “yea i know its crazy”other '
        'stuff...!!! ')
        tks = [u'some', u'stuff', u'but', u'he', u'said', u'other', u'stuff',
        u'...', u'!', u'!', u'!']
        self.assertEqual(self.tokenizer.tokenize(msg), tks)
    
    def test_quotes_4(self):
        self.tokenizer.ignorequotes = True
        msg = ('some stuff but he said &ldquo;yea i know its crazy&rdquo;other '
        'stuff...!!! ')
        tks = [u'some', u'stuff', u'but', u'he', u'said', u'other', u'stuff',
        u'...', u'!', u'!', u'!']
        self.assertEqual(self.tokenizer.tokenize(msg), tks)
    
    def test_quotes_5(self):
        self.tokenizer.ignorequotes = False
        msg = 'heyy buddyyyyy boy \'do you the lady\'s kitty like that??\''
        tks = [u'heyy', u'buddyyy', u'boy', u"'", u'do', u'you', u'the',
        u"lady's", u'kitty', u'like', u'that', u'?', u'?', u"'"]
        self.assertEqual(self.tokenizer.tokenize(msg), tks)
    
    def test_hashtags_1(self):
        msg = 'omg i love#dog#cat#food#other#things#so#fucking#much!!!11LOLOLOL'
        tks = ['omg', 'i', 'love', '#dog', '#cat', '#food', '#other',
        '#things', '#so', '#fucking', '#much', '!', '!', '!', '11LOLOLOL']
        self.assertEqual(self.tokenizer.tokenize(msg), tks)
    
    def test_hashtags_2(self):
        self.tokenizer.hashtags = 'HASHTAG'
        msg = 'omg i love#dog#cat#food#other#things#so#fucking#much!!!11LOLOLOL'
        tks = ['omg', 'i', 'love', 'HASHTAG', 'HASHTAG', 'HASHTAG',
        'HASHTAG', 'HASHTAG', 'HASHTAG', 'HASHTAG', 'HASHTAG', '!', '!', '!',
        '11LOLOLOL']
        self.assertEqual(self.tokenizer.tokenize(msg), tks)
    
    def test_emoticons_1(self):
        msg = 'heyyyyyy:):):(>.<<v.vwhats up man LOL T.T tomcat.tomcat :$;).!!!'
        tks = [u'heyyy', u':)', u':)', u':(', u'>.<', u'<', u'v.v', u'whats',
        u'up', u'man', u'LOL', u'T.T', u'tomcat', u'.', u'tomcat', u':$',
        u';)', u'.', u'!', u'!', u'!']
        self.assertEqual(self.tokenizer.tokenize(msg), tks)
    
    def test_removefeatures_1(self):
        self.tokenizer.usernames = "" # dont' want any usernames to show
        msg = ('hey @arnold @nickelodeon #90s#ilove90s#allthat#amandashow'
        '@rocko http://en.wikipedia.org/wiki/The_Angry_Beavers ^.^>>><<<^.^')
        tks = [u'hey', u'#90s', u'#ilove90s', u'#allthat', u'#amandashow',
        u'URL', u'^.^', u'>', u'>', u'>', u'<', u'<', u'<', u'^.^']
        self.assertEqual(self.tokenizer.tokenize(msg), tks)
    
    def test_removefeatures_2(self):
        self.tokenizer.usernames = "" # dont' want any usernames to show
        self.tokenizer.hashtags = ""  # or hashtags
        msg = ('hey @arnold @nickelodeon #90s#ilove90s#allthat#amandashow'
        '@rocko http://en.wikipedia.org/wiki/The_Angry_Beavers ^.^>>><<<^.^')
        tks = [u'hey', u'URL', u'^.^', u'>', u'>', u'>', u'<', u'<', u'<',
        u'^.^']
        self.assertEqual(self.tokenizer.tokenize(msg), tks)
    
    def test_removefeatures_3(self):
        self.tokenizer.usernames = False # keep usernames
        self.tokenizer.urls = ""         # URLs should be removed
        self.tokenizer.hashtags = "$$$"  # hashtags should be $$$
        msg = ('hey @arnold @nickelodeon #90s#ilove90s#allthat#amandashow'
        '@rocko http://en.wikipedia.org/wiki/The_Angry_Beavers ^.^>>><<<^.^')
        tks = [u'hey', u'@arnold', u'@nickelodeon', u'$$$', u'$$$', u'$$$',
        u'$$$', u'@rocko', u'^.^', u'>', u'>', u'>', u'<', u'<', u'<', u'^.^']
        self.assertEqual(self.tokenizer.tokenize(msg), tks)
    
    def test_emoji_1(self):
        msg = ('hey mate!:):3.....@and🇨🇳ONE+ BRO#love😘😵💚💛💜💙  '
        '💋😂😂LOLLLL.')
        tks = [u'hey', u'mate', u'!', u':)', u':3', u'...',
        u'USERNAME', u'\U0001f1e8\U0001f1f3', u'ONE', u'+', u'BRO', u'#love',
        u'\U0001f618', u'\U0001f635', u'\U0001f49a', u'\U0001f49b',
        u'\U0001f49c', u'\U0001f499', u'\U0001f48b', u'\U0001f602',
        u'\U0001f602', u'LOLLL', u'.']
        self.assertEqual(self.tokenizer.tokenize(msg), tks)
    
    def test_emoji_2(self):
        msg = ('hey mate!:):3.....@andONE+🇬🇧  BRO#love😘😵💚💛💜💙  '
        '💋😂😂LOLLLL.')
        tks = [u'hey', u'mate', u'!', u':)', u':3', u'...',
        u'USERNAME', u'+', u'\U0001f1ec\U0001f1e7', u'BRO', u'#love', u'😘',
        u'😵', u'\U0001f49a', u'\U0001f49b', u'\U0001f49c',
        u'\U0001f499', u'💋', u'\U0001f602', u'\U0001f602',
        u'LOLLL', u'.']
        self.assertEqual(self.tokenizer.tokenize(msg), tks)
    
    def test_emoji_3(self):
        msg = ('🚀=)</3O_O:$D:<:-@\xf0\x9f\x98\xb7🔥💩💅 outdated:💽 ancient:💾 '
        '#getwiththecloud:💻 and it looks like 💭')
        tks = [u'\U0001f680', u'=)', u'</3', u'O_O', u':$', u'D:<', u':-@',
        u'\U0001f637', u'\U0001f525', u'\U0001f4a9', u'\U0001f485',
        u'outdated', u':', u'\U0001f4bd', u'ancient', u':',
        u'\U0001f4be', u'#getwiththecloud',
        u':', u'\U0001f4bb', u'and', u'it', u'looks', u'like', u'\U0001f4ad']
        self.assertEqual(self.tokenizer.tokenize(msg), tks)
    
    def test_error_1(self):
        msg = []
        with self.assertRaises(TypeError):
            self.tokenizer.tokenize(msg)
    
    def test_error_2(self):
        msg = lambda x: x
        with self.assertRaises(TypeError):
            self.tokenizer.tokenize(msg)
    
    def test_actual_tweets_1(self):
        "Number as part of name"
        msg = '@LoganTillman not 2pac and floyd mayweather'
        tks = [u'USERNAME', u'not', u'2pac', u'and', u'floyd', u'mayweather']
        self.assertEqual(self.tokenizer.tokenize(msg), tks)
    
    def test_actual_tweets_2(self):
        "Colon no space in hashtag"
        msg = '#MentionSomeoneYoureGladYouMet: @LarryWorld_Wide of course.'
        tks = [u'#MentionSomeoneYoureGladYouMet', u':', u'USERNAME', u'of',
        u'course', u'.']
        self.assertEqual(self.tokenizer.tokenize(msg), tks)
    
    def test_stopwords_1(self):
        self.tokenizer.ignorestopwords = True
        msg = 'i like myself and my so not much and our something he:)'
        tks = [u'like', u'much', u'something', u':)']
        self.assertEqual(self.tokenizer.tokenize(msg), tks)

if __name__ == "__main__":
    unittest.main()

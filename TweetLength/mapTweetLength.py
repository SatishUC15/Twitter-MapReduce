#!/usr/bin/env python

import sys
import json

# Mapper - Generates key value pairs to compute the length of tweets and the number of user tweets.
for line in sys.stdin:
    tweet_data = json.loads(line)
    user_name = tweet_data.get('user').get('screen_name')
    tweet_length = len(tweet_data.get('text'))
    print '%s_len\t%s' % (user_name, tweet_length)
    print '%s\t%s' % (user_name, 1)

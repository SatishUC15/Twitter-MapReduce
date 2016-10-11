#!/usr/bin/env python

from datetime import datetime
import json
import sys

# Mapper - filters tweets by user screen_name and generates key-value pairs of the format <hour_of_creation, 1>

filter_user_name = 'prezono'

for line in sys.stdin:
    tweet_data = json.loads(line)
    if tweet_data.get('user').get('screen_name').strip().lower() == filter_user_name:
        timestamp = tweet_data.get('created_at')
        date_object = datetime.strptime(timestamp, '%a %b %d %H:%M:%S +0000 %Y')
        print '%s\t%s' % (date_object.hour, 1)



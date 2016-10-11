#!/usr/bin/env python

from __future__ import division
import sys
import string

# Reducer - processes the output of the mapper to compute the hourly average of tweets
tweet_count = 0
hour = None
tweets_by_hour_avg = {}
num_days = 365

for line in sys.stdin:
    (key, val) = line.strip().split('\t', 1)
    if hour != key:
        if hour:
            print "Average # of tweets @ %s hrs:\t%s" % (hour, tweet_count/num_days)
            tweets_by_hour_avg[hour] = tweet_count/num_days
            tweet_count = 0
    hour = key
    try:
        tweet_count += int(val)
    except:
        continue
print 'Tweets @ %s hrs:\t%s' % (hour, tweet_count)
tweets_by_hour_avg[hour] = tweet_count/num_days

print "Hour of the day that @PrezOno tweets the most:", max(tweets_by_hour_avg, key=tweets_by_hour_avg.get)

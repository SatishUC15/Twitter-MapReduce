#!/usr/bin/env python

from __future__ import division
import sys

# Reducer - processes the output of the mapper to compute the hourly average of tweets
tweet_count = 0
tweet_length = 0
user = None
user_length = {}
user_length_avg = {}
user_tweet = {}

for line in sys.stdin:
    (key, val) = line.strip().split('\t', 1)
    if user != key:
        if user:
            if user.find("_len") != -1:
                user_length[user] = tweet_length
                tweet_length = 0
            else:
                user_tweet[user] = tweet_count
                tweet_count = 0
    user = key
    try:
        if user.find("_len") != -1:
            tweet_length += int(val)
        else:
            tweet_count += int(val)
    except:
        continue

if user.find("_len") != -1:
    user_length[user] = tweet_length
else:
    user_tweet[user] = tweet_count
              
for key in user_tweet.keys():
    user_length_avg[key] = user_length[key+"_len"]/user_tweet[key]
    print '%s\t%s' % (key, user_length_avg[key])

print "@PrezOno average tweet length : ", user_length_avg['PrezOno']
print "Maximum Average tweet length : ", user_length_avg[max(user_length_avg, key=user_length_avg.get)]
print "Minimum Average tweet length : ", user_length_avg[min(user_length_avg, key=user_length_avg.get)]

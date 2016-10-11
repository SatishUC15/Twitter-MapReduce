#!/usr/bin/env python

from __future__ import division
import sys


# Reducer - calculates the average tweet count in a year for each day of the week and calculates the max of that
# output is of type <max_tweet_day,avg>

tweetCount = 0
#assuming that each day in the week occurs 52 times a year approximately
totalDays = 52
tweetAvg = {}
day = None

for line in sys.stdin:
    (k, v) = line.strip().split('\t',1)
    if day != k:
        if day:
            tweetAvg[day] = tweetCount/totalDays
            print "Average Tweets on %s :\t%s" % (day, tweetAvg[day])
            tweetCount = 0
    day = k
    try:
        tweetCount += int(v)
    except:
        continue

tweetAvg[day] = tweetCount/totalDays
print "Average Tweets on %s :\t%s" % (day, tweetAvg[day])

print "Day of the week @PrezOno tweets the most : ", max(tweetAvg, key=tweetAvg.get)


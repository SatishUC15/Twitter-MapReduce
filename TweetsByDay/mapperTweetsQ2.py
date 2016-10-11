#!/usr/bin/env python

import json
import sys
import calendar
from datetime import datetime

# Mapper function goes through the Twitter 'user' data. Filters using screen_name = 'prezono' and
# returns key-value pairs of the type <'day_of_week',1>

filter_screen_name = 'prezono'

for line in sys.stdin:
    data = json.loads(line)
    if data.get('user').get('screen_name').strip().lower() == filter_screen_name:
        time = data.get('created_at')
        # splitting date to extract the day of the week tweet was made using datetime module
        date = datetime.strptime(time, '%a %b %d %H:%M:%S +0000 %Y')
        # this reuturns day of the week as integers Monday - Sunday [1 - 7], convert to string
        day = calendar.day_name[date.weekday()]
        print '%s\t%s' %(day, 1)
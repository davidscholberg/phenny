#!/usr/bin/env python
"""
reddit.py - Phenny Reddit Module
Author: David Scholberg <recombinant.vector@gmail.com>
Dependencies: praw python module
"""

import praw

def reddit(phenny, input):
   """Fetch Reddit links"""
   query = input.group(2)

   if query is None:
      phenny.say('%s: command requires at least a subreddit arg' % (input.nick))
      return

   query_list = query.split(' ')
   subreddit = query_list[0]
   if len(query_list) > 1:
      post_limit = int(query_list[1])
      if post_limit < 1 or post_limit > 5:
         phenny.say('%s: post limit out of bounds. setting to 1' % (input.nick))
         post_limit = 1
   else:
      post_limit = 1

   r = praw.Reddit(user_agent='phenny github.com/davidscholberg/phenny')
   posts = r.get_subreddit(subreddit).get_hot(limit=post_limit)

   phenny.say('%s: Top %d posts for /r/%s' % (input.nick, post_limit, subreddit))
   i = 0
   for post in posts:
      i += 1
      phenny.say('%s: %d: %s - %s' % (input.nick, i, post.short_link, post.title))
reddit.commands = ['r', 'reddit']
reddit.example = '.r sysadmin 3'

if __name__ == '__main__': 
   print __doc__.strip()

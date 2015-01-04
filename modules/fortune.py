#!/usr/bin/env python
"""
fortune.py - Phenny BSD Fortune Module
Author: David Scholberg <recombinant.vector@gmail.com>
Dependencies: The fortune shell command must be locally installed
"""

from subprocess import Popen, PIPE

def fortune(phenny, input):
   """Print a BSD fortune"""
   fortune = Popen(['fortune', '-sa'], stdout=PIPE).stdout.read().strip()
   fortune = fortune.replace('\t', '    ')
   fortune_lines = fortune.split('\n')
   for line in fortune_lines:
      phenny.say('%s: %s' % (input.nick, line))
fortune.commands = ['f', 'fortune']

if __name__ == '__main__': 
   print __doc__.strip()

#!/usr/bin/env python
import sys
import os
import re
from ics import Calendar, Event

# TODO add output arguments 'input file' and 'output dir'
if len(sys.argv) != 2 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print("usage: texttoicv [filename]")
    sys.exit(2)

# read input text line-by-line
with open(sys.argv[1]) as f:
    lines = f.readlines()

# dictionary of calendars indexed by speakers names
cals = dict()

name = "([^#]+)#"
title = "([^#]+)#"
date = "([0-9]{8}T[0-9]{2}:[0-9]{2})#"
room = "([^#]*)" # discretionary

for line in lines:
    match = re.match(name + title + date + date + room, line)    
    if match:
        speaker_name = match.group(1)
        if speaker_name not in cals:
            cals[speaker_name] = Calendar()
        e = Event()         
        e.name = match.group(2)
        e.begin = match.group(3)
        e.end = match.group(4)
        e.location = match.group(5)
        cals[speaker_name].events.add(e)
    else:
        print("Bad formatted string.")

# write calendars in the output calendars
output_dir = 'Calendars'
for cal in cals:
    speaker_name = cal.split(' ')
    output_name = ''
    for idx in range(len(speaker_name)):
        output_name += speaker_name[idx].capitalize()
        
    with open(os.path.join(output_dir, output_name + '.ics'), 'w+') as f:
        f.writelines(cals[cal])
        print(cals[cal].events)
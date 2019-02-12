import sys
import os
import re
import argparse
from ics import Calendar, Event

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=str,
                    help="input text calendar")
parser.add_argument("output_dir", type=str,
                    help="output directory to store ICSs (will not be created)")
args = parser.parse_args()

# read input text line-by-line
with open(args.input_file) as f:
    lines = f.readlines()

# dictionary of calendars indexed by speakers names
cals = dict()

name = "([^#]+)#"
title = "([^#]+)#"
# date = "([0-9]{8}T[0-9]{2}:[0-9]{2})#"
date = "([^#]+)#"
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
for cal in cals:
    speaker_name = cal.split(' ')
    output_name = ''
    for idx in range(len(speaker_name)):
        output_name += speaker_name[idx].capitalize()
        
    with open(os.path.join(args.output_dir, output_name + '.ics'), 'w') as f:
        f.writelines(cals[cal])
        # print(cals[cal].events)
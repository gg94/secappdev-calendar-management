import sys
import os
import re
import argparse
from ics import Calendar, Event

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=str,
                    help="input text calendar")
parser.add_argument("output_dir", type=str,
                    help="output directory to store ICSs")
args = parser.parse_args()

# dictionary of calendars indexed by speakers names
cals = dict()

name = "([^#]+)#"
title = "([^#]+)#"
# date = "([0-9]{8}T[0-9]{2}:[0-9]{2})#"
date = "([^#]+)#"
room = "([^#]*)" # discretionary

# skip the byte order mark (BOM) with the following encoding
with open(args.input_file, "r", encoding="utf-8-sig") as f:    
    for line in f:     
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

# write calendars in the output directory
for cal in cals:
    speaker_name = cal.split(' ')
    output_name = ''
    for idx in range(len(speaker_name)):
        output_name += speaker_name[idx].capitalize()
        
    if not os.path.exists(args.output_dir):    
       os.makedirs(args.output_dir)
    
    with open(os.path.join(args.output_dir, output_name + '.ics'), 'w') as f:
        f.writelines(cals[cal])
        # print(cals[cal].events)
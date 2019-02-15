# Calendar management script

Tool to create ICSs files from a text calendar of events.

### Requirements

This script is written in Python 3. Requirements can be installed by using `pip` with `pip install -r requirements.txt`

### Usage

The script takes two arguments: calendar events comes in from an input file specified as the first positional parameter, while the output directory for the ICSs files has to be specified as the second positional parameter.

Tested formats for the input file are `.txt` and `.csv` without a header. Line format is the following (round brackets indicate discretionary parameters): 

```
authorname#sessiontitle#startdatetime#enddatetime#(room)
```

Datetimes are `Arrow`-compatible, i.e have to be set to anything that `Arrow.get()` understands. Examples datetime for Wednesday, 13 February 2019 at 18:00 (GMT+1) are `20190213T18:00+01:00 (YYYYMMDD'T'hh:mm+timezone)` and `2019-02-13T17:00 (YYYY-MM-DD'T'hh:mm+00:00)`. 

### Example

The script can be tested with `python3 ./text_to_icv.py example/calendar.txt example/calendars`.
# Text-to-ICS

Tool to create ICSs files from a text calendar.

### Requirements

This script is written in Python 3. Requirements can be installed by usign `pip` with `pip install -r requirements.txt`

### Usage

Calendar events comes in from an input file specified as first positional parameter. Line format is the following (round brackets define discretionary parameters): 

```
authorname#sessiontitle#startdatetime#enddatetime#(room)
```

Datetimes are `Arrow`-compatible, i.e have to be set to anything that `Arrow.get()` understands. Example datetime for Wednesday, 13 February 2019 at 18:00 is `20190213T18:00 (YYYYMMDD'T'hh:mm)`.

The output directory for the ICSs files have to be specified as a second positional parameter. 

To test the script:

```
python3 ./text_to_icv.py example/calendar.txt example/calendars
```
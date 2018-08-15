# Python Image Extractor

This project currently uses Python2. Please use Python2 with it :)

This project was originally created to extract JPG's out of the Android Thumbdata3 format.

It is theoretically capable of extracting data from any file that contains multiple JPG's within.

## Usage

Usage is quite simple. In the following example, the filename is simply `thumbdata3`:

```bash
./extract.py --file thumbdata3
```

The script will then output to the same directory a bunch of JPG's (named sequentially). These are the files you are after.

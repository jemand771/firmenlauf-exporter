# firmenlauf-exporter
Because Rohdaten sind geil.

## What is this
I got forced to participate in this year's "[Chemnitzer Firmenlauf](http://www.firmenlauf-chemnitz.de/alles-zum-lauf/)" where a bunch of companies send their employees on a 5km run.
Why? _I don't know._ People enjoy physical exercise??

## Why
I like data :3

## Usage
These scripts are really only meant to be used once.

`json-downloader.py` will fetch all results from the counting provider's api.
This includes results for all categories. They will be placed in the `./data` folder as a list of json objects, one file per category.
For later reference, descriptions of all columns are also saved.

`intenta-csv-maker.csv` will filter all results in the `./data` folder by company, and spit out everything about a single company as csv files.
This is specific to my employer, but can be easily modified to search for different criteria or not filter at all.

I wanted to include a thing that automatically grabs the video of everyone passing the finish line (there was a live stream), but they took the vod offline :(

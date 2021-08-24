# multi_bats
* Linux only, might work on other unix systems, but probably not *
** info comes from /sys/class/power_supply/* **
A small script that will aggregate the total capacity of all batteries on a system into a single percent
Requires that each battery have charge at least once so that's it's capacity can be saved in a json file.

# how to use
python multi_bats.py percent --> will give the percent of all batteries

python multi_bats.py info    --> will give basic info of all batteries

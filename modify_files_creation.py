import os,time,datetime

#directory name
directory = "my_files"

#date values
year = 2023
month = 11
day = 1
hour = 00
minute = 00
second = 00

#creating date object
date = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
#creating modification time tuple
modification_time = time.mktime(date.timetuple())

#loop to change modification and access date
for x in range(1, 6):
  if x != 5:
    os.utime(os.path.join(directory,"files{}.txt".format(x)),(modification_time,modification_time))

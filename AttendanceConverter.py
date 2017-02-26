import os
import sys
import enum
import re

FILE_INPUT = "Attendance.txt"
FILE_OUTPUT = "Attendance2.txt"


class Day(enum.Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7

class DayData:

    minute_start = 0
    minute_end = 0
    
    def __init__(self, day, minute_start, munute_end):
        self.day = day
        self.minute_start
        self.minute_end

    def __str__(self):
        return "{0} {1} {2}".format(self.day, self.minute_start, self.minute_end)

    def __repr__(self):
        return "{0} {1} {2}".format(self.day, self.minute_start, self.minute_end)

    def get_str_start(self):
        return DayData.minute_to_str(self.minute_start)

    def get_str_end(self):
        return DayData.minute_to_str(self.minute_end)

    @staticmethod 
    def minute_to_str(minute):
        if (minute == 0):
            return " "
        else:
            return "{0}:{1}".format(int(minute / 60), minute % 60)


def create_days() :
    days = []
    
    for day in Day:
        days.append(DayData(day, 0, 0))

    return days

def read_file(path):
    with open(path, "r") as file:
        return file.readlines()

def fuck(n):
    if (n >= 45):
        return 45
    elif (n >= 30):
        return 30
    elif (n >= 15):
        return 15
    else:
        return 0
    

if __name__ == "__main__":
            

    days = create_days()

    lines = read_file(FILE_INPUT)

    for line in lines:
        day = re.findall(r"（(.+)）", line)[0]
        match_time = re.search(r"w (.+):(.+?) ", line)
        hour = int(match_time.group(1))
        minute = int(match_time.group(2))

        is_enter = re.search("出", line)

        index = -1

        if (day == '月'):
            index = Day.Monday
        elif (day == '火'):
            index = Day.Tuesday 
        elif (day == '水'):
            index = Day.Wednesday
        elif (day == '木'):
            index = Day.Thursday 
        elif (day == '金'):
            index = Day.Friday 
        elif (day == '土'):
            index = Day.Saturday 
        elif (day == '日'):
            index = Day.Sunday

        index = index.value - 1
        minute = fuck(minute)

        print(index)
        print(hour)
        print(minute)

        minute2 = 60 * hour + minute

        if is_enter :
            days[index].minute_start = minute2
        else:
            days[index].minute_end = minute2

    print(days)
            
    for day in days:
        sys.stdout.write(day.get_str_start())
        sys.stdout.write("\t")

    print()

    for day in days:
        sys.stdout.write(day.get_str_end())
        sys.stdout.write("\t")
        
            


    


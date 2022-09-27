import enum;

options = enum(ONE=1, TWO=2, THREE='three')

print(options.ONE)

class days_of_the_week(enum.Enum):
    monday = 0
    tuesday = 1
    wednesday = 2
    thursday = 3
    friday = 4
    saturday = 5
    sunday = 6

print(days_of_the_week(0).name)

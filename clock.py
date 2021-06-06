from typing import Annotated, Callable
import time


def print_bruh() -> None:
    print("Bruh")


def timer(time_in_seconds: int, callback_function: Callable[[], None]) -> None:
    for i in range(time_in_seconds):
        time.sleep(1)
        print(i + 1, 'Mississippi')
    callback_function()


def convert_time_in_seconds(list_of_hours_minutes_second_string: Annotated[list[str], 3]) -> int:
    list_of_hours_minutes_second_int: list[int] = [int(i) for i in list_of_hours_minutes_second_string]
    return \
        list_of_hours_minutes_second_int[0] * 3600 + \
        list_of_hours_minutes_second_int[1] * 60 + \
        list_of_hours_minutes_second_int[2]


def start_clock() -> None:
    time_in_hours_minute_seconds: str = input("Insert the time the clock should ring at with the format hrs, minutes, "
                                              "secs:- ")
    time_in_seconds: int = convert_time_in_seconds(time_in_hours_minute_seconds.split(', '))
    timer(time_in_seconds, print_bruh)


if __name__ == '__main__':
    print('PYTHON PROGRAM FOR ALARM CLOCK')
    start_clock()

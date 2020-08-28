import time
import os
import math

POMODORO_SECONDS = 1500 # 1500 SECONDS = 25 mins

SECONDS_IN_ONE_MINUTE = 60

def send_sound_alert():
     print("\a")

def parse_seconds_to_minutes(secs):
    return math.floor(secs / SECONDS_IN_ONE_MINUTE)

def get_remaining_seconds_to_next_minute (total_seconds):
    minutes = parse_seconds_to_minutes (total_seconds)
    seconds = total_seconds - (minutes * SECONDS_IN_ONE_MINUTE)
    return seconds

def countdown(t, objective):
    while t > 0:
        os.system("clear") # TODO: fix this not working for windows
        parsed_remaining_time = parse_seconds_to_minutes(t)
        parsed_remaining_time_seconds = get_remaining_seconds_to_next_minute(t)
        print(f"Pomodoro objective/s: {objective}")
        print(f"Remaining time: {parsed_remaining_time}:{parsed_remaining_time_seconds}")
        t -= 1
        time.sleep(1)
    print("BLAST OFF!")

if __name__ == "__main__":
    objective = input("Please, enter your objective for this pomodoro: ")
    countdown(POMODORO_SECONDS, objective)
    i = 0
    for i in [1,2,3]:
        send_sound_alert()
        time.sleep(1)

import time
import datetime
import random
import string
# import msvcrt


def main():
    char_list = random_list(30)
    print(char_list)
    # user_input = msvcrt.getch()
    timer(1)
    print("Hi")


def timer(minutes: int):
    total_seconds = minutes * 60
    while total_seconds > 0:
        countdown = datetime.timedelta(seconds=total_seconds)
        print(countdown, end="\r")
        time.sleep(1)
        total_seconds -= 1
    print("Stop! 0 seconds left!")


def random_list(num_char: int):
    char_list = []
    num_char = 30
    for i in range(num_char):
        char_list.append(random.choice(string.ascii_lowercase))
    return char_list


if __name__ == '__main__':
    main()


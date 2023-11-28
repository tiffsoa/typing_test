# import msvcrt
import time
import datetime
import random
import string


def main():
    print("This is your list of characters: ")
    char_list = random_list(100)
    print(char_list)
    user_answer = input("Enter your answer: ")
    timer(1)
    answer_list = []
    count = 0
    for char in user_answer:
        answer_list.append(char)
    for i in range(len(user_answer)):
        if char_list[i] == answer_list[i]:
            count += 1
        else:
            count += 0
    ch_per_sec = count
    print("You can write ", ch_per_sec, " characters per minute")


def timer(minutes: int):
    total_seconds = minutes * 60
    while total_seconds > 0:
        countdown = datetime.timedelta(seconds=total_seconds)
        print(countdown, end="\r")
        time.sleep(1)
        total_seconds -= 1
    print("Stop! 0 seconds left!")


def random_list(num_char: int):
    lst = []
    num_char = 100
    for i in range(num_char):
        lst.append(random.choice(string.ascii_lowercase))
    return lst


if __name__ == '__main__':
    main()


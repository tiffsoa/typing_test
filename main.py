import time
import datetime
import random
import string


def main():
    # timer(1)
    print("Hi")


def timer(minutes: int):
    total_seconds = minutes * 60
    while total_seconds > 0:
        countdown = datetime.timedelta(seconds=total_seconds)
        print(countdown, end="\r")
        time.sleep(1)
        total_seconds -= 1
    print("Stop! 0 seconds left!")


char_list = []
num_char = 30
for i in range(num_char):
    char_list.append(random.choice(string.ascii_lowercase))
    print(char_list)

user_list = input("Enter your answer : ")
def comparison
if __name__ == '__main__':
    main()


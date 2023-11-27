import time
import datetime
import sys, termios, tty


def main():
    timer(1)
    getch()
    print("Hi")


def timer(minutes: int):
    total_seconds = minutes * 60
    while total_seconds > 0:
        countdown = datetime.timedelta(seconds=total_seconds)
        print(countdown, end="\r")
        time.sleep(1)
        total_seconds -= 1
    print("Stop! 0 seconds left!")


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


if __name__ == '__main__':
    main()


import random
import time


def main():
    available_texts = [text_one, text_two, text_three]
    chosen_text = random.choice(available_texts)
    print("This is your text: ")
    print(chosen_text)
    initial_time = time.time()
    user_answer = input("You can start: ")
    final_time = time.time()
    time_total = total_time(initial_time, final_time)
    answer_list = user_answer.split()
    count = 0
    for word in answer_list:
        count += 1
    wpm = count/(time_total / 60.0)
    print("Typing Speed: ", wpm, "words per minute")


def total_time(x, y):
    total = y - x
    return total


text_one = ("The irony of the situation hadn't escaped her. She had taken years to sculpt the perfect persona with \n"
            " the perfect look that she shared on Instagram. She knew her hundreds of thousands of followers \n"
            " envied that life she showed and stayed engaged with her because they wanted that life too. \n"
            "The truth was that she wanted the perfect life she portrayed more than any of her fans. The fact \n"
            "was that despite all the \n perfection she shared on social media, her life was actually \n"
            "more of a mess than most.")

text_two = ("Sleep deprivation causes all sorts of challenges and problems. When one does not get enough sleep one’s \n"
            " mind does not work clearly. Studies have shown that after staying awake for 24 hours one’s \n"
            "ability to do simple math is greatly impaired. Driving tired has been shown to be as bad as driving \n"
            "drunk. Moods change, \n depression, anxiety, and mania can be induced by lack of sleep. As much as \n"
            "people try to do without \n enough sleep it is a wonder more crazy things don’t happen in this world.")

text_three = ("The shoes had been there for as long as anyone could remember. In fact, it was difficult for \n"
              "anyone to come up with a date they had first appeared. It had seemed they'd always been there \n"
              "and yet they seemed so out of place. Why nobody had removed them was a question that had been \n"
              "asked time and again, but while they all thought it, nobody had ever found the energy to \n"
              "actually do it. So, the shoes remained on the steps, out of place in one sense, but perfectly \n"
              "normal in another.")


if __name__ == '__main__':
    main()


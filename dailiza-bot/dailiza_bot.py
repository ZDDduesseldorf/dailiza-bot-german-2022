import random
import re
from reflection import reflect
from text_patterns import psychobabble
from text_patterns import neutral_responses


def dailiza_answer(user_input):
    """Diese Funktion generiert die Antwort des DAILIZA-Bot.
    """
    user_input = user_input.strip(",.?!")

    # Test input string for all known text patter in pychobabble
    for pattern, responses in psychobabble:
        #[(0,Ich),(1,brauche),(2,etwas)]
        match = re.search(pattern, str(user_input))
        do_i_know_this = False
        if match:
            do_i_know_this = True
            rspns = random.choice(responses)
            return rspns.format(*[reflect(g) for g in match.groups()])
    if do_i_know_this == False:
        if user_input == "":
            return "Wie sollen wir ohne Wörter reden?"
            
        return random.choice(neutral_responses)    


def run_dailiza_bot():
    """Diese Funktion startet den DAILIZA-Bot.
    """
    print("Hey Hallo! Ich bin Dailiza. Womit kann ich dir helfen?")
    user_input = ""
    while True:
        user_input = input(">> ")
        exit_ = re.findall(r"\b[Ee]xit\b", user_input)
        print(dailiza_answer(user_input))
        if exit_:
            break


if __name__ == '__main__':
    run_dailiza_bot()

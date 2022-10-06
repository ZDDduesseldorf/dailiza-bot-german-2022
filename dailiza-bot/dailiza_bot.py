import random
import re
from reflection import reflect
from text_patterns import psychobabble
from neutral_resp import neutral_response

def dailiza_answer(user_input):
    """Diese Funktion generiert die Antwort des DAILIZA-Bot.
    """
    user_input = user_input.strip(",.?!")

    # Test input string for all known text patter in pychobabble
    is_answer = None
    for pattern, responses in psychobabble:
        match = re.search(pattern, str(user_input))
        if match:
            rspns = random.choice(responses)
            is_answer = True
            return rspns.format(*[reflect(g) for g in match.groups()])    
    if is_answer is not True:
        rspns = random.choice(neutral_response)
        return str(rspns)

def run_dailiza_bot():
    """Diese Funktion startet den DAILIZA-Bot.
    """
    print("Hey Hallo! Ich bin Dailiza. Womit kann ich dir helfen?")
    user_input = ""
    while "exit" not in user_input:
        user_input = input(">> ")
        if "Bye".lower() in user_input.lower():
            print("Bye ;)")
            break
        if "exit" in user_input.lower():
            break
        print(dailiza_answer(user_input))


if __name__ == '__main__':
    run_dailiza_bot()

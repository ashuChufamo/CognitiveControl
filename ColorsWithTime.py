import random
import time

# ANSI escape codes for text colors
COLOR_RED = '\033[91m'
COLOR_GREEN = '\033[92m'
COLOR_BLUE = '\033[94m'
COLOR_YELLOW = '\033[93m'
COLOR_END = '\033[0m'

def main():
    colors = ["RED", "GREEN", "BLUE", "YELLOW"]
    color_codes = [COLOR_RED, COLOR_GREEN, COLOR_BLUE, COLOR_YELLOW]
    num_trials = 10
    correct_responses = 0

    print("Welcome to the Stroop Test!")
    print("Identify the ink color of each word while ignoring the word's meaning.\n")

    for trial in range(num_trials):
        word = random.choice(colors)
        ink_color = random.choice(colors)
        ink_color_code = color_codes[colors.index(ink_color)]

        # Ensure the word and ink color are not the same
        while word == ink_color:
            ink_color = random.choice(colors)
            ink_color_code = color_codes[colors.index(ink_color)]

        print(f"The word is: {ink_color_code}{word}{COLOR_END}")

        start_time = time.time()
        user_response = input("Enter the ink color: ").strip().upper()
        end_time = time.time()
        response_time = end_time - start_time

        if response_time > 3:
            print("Time limit exceeded! Please respond faster.\n")
        else:
            if user_response == ink_color:
                print("Correct!\n")
                correct_responses += 1
            else:
                print(f"Incorrect. The correct ink color is {ink_color}.\n")

    print(f"Thank you for participating! Your score: {correct_responses}/{num_trials}")

if __name__ == "__main__":
    main()
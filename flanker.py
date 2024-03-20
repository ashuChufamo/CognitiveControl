import random


def main():
    num_trials = 10  # Number of trials
    correct_responses = 0  # Initialize score

    print("Welcome to the Modified Flanker Task!")
    print("Press 'L' for left arrow and 'R' for right arrow.\n")

    for trial in range(num_trials):
        arrows = ["←", "→"]  # Left and right arrows
        central_arrow = random.choice(arrows)
        flankers = [random.choice(arrows) for _ in range(2)]  # Only three flankers

        flanker_line = " ".join(flankers)
        central_line = f" {central_arrow} "  # Display the central arrow

        print(f"{flanker_line}{central_line}{flanker_line}")
        user_response = input("Your response (L/R): ").strip().lower()

        
        if user_response == "l":
            correct_response = "←"
        elif user_response == "r":
            correct_response = "→"
        else:
            print("Invalid response. Please enter 'L' or 'R'.")
            continue

        if correct_response == central_arrow:
            print("Correct!\n")
            correct_responses += 1
        else:
            print(f"Oops! The correct response was {correct_response}.\n")

    print(f"Thank you for participating! Your score: {correct_responses}/{num_trials}")

if __name__ == "__main__":
    main()
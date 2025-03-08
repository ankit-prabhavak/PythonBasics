import datetime

def get_positive_input():
    """
    Function to get a positive input from the user. If input is empty, prompts again.
    """
    while True:
        positive_thing = input("What's one positive thing that happened today? (It could be small or big): ")
        if positive_thing.strip():
            return positive_thing
        else:
            print("Please enter something meaningful. It can be anything positive.")

def track_good_moments():
    """
    Main function to guide the user through a reflective experience.
    """
    print("===========================================")
    print("Welcome to your personal Mood Booster ✨")
    print("This tool will help you reflect on positive moments and feel better.")
    print("===========================================")

    # Let's start by showing some instructions
    print("\nToday might be tough, but focusing on small good things can make a huge difference.")
    print("You'll be asked to think about a few positive things that happened today.")
    print("These could be anything from a good conversation to something as small as enjoying a warm cup of tea.")
    
    # Ask user if they are ready to start
    input("\nPress Enter when you're ready to start reflecting or type 'quit' to exit: ")

    # Initialize an empty list to store positive moments
    positive_moments = []

    # Ask for three positive things
    print("\nLet's reflect! Answer the following:")
    for i in range(1, 4):
        print(f"\nMoment #{i}:")
        positive_thing = get_positive_input()
        positive_moments.append(positive_thing)
        print(f"Great! You've captured: '{positive_thing}'\n")

    # Give an option to add more moments
    while True:
        more_input = input("Would you like to add another moment? (yes/no): ").strip().lower()
        if more_input == 'yes':
            positive_thing = get_positive_input()
            positive_moments.append(positive_thing)
            print(f"Awesome! You've captured: '{positive_thing}'\n")
        elif more_input == 'no':
            break
        else:
            print("Please answer with 'yes' or 'no'.")

    # Save the positive moments into a log file
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("mood_boost_log.txt", "a") as file:
        file.write(f"Date: {current_time}\n")
        for idx, moment in enumerate(positive_moments, 1):
            file.write(f"  {idx}. {moment}\n")
        file.write("\n")

    # Thank the user
    print("\nThank you for reflecting! Here's what you've captured today:")
    for idx, moment in enumerate(positive_moments, 1):
        print(f"  {idx}. {moment}")

    print("\nYou've successfully added positive moments to your log. Keep this up whenever you need a boost!")
    print("===========================================")
    print("You are doing great. Keep going and be kind to yourself. 💖")
    print("===========================================")

if __name__ == "__main__":
    track_good_moments()

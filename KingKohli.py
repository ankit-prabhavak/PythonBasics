import time

# Function to display celebration message
def celebrate_kohli():
    print("🎉🎉🎉 Virat Kohli has scored his 82nd Century! 🎉🎉🎉")
    time.sleep(1)
    print("An absolute legend of the game! 🏏🔥")
    time.sleep(1)
    print("Here's to many more centuries! 🥂👑")
    time.sleep(1)
    print("King Kohli rules the cricket world! 👑💥")

# Function to display fun countdown before the celebration
def countdown():
    print("\nGet ready to celebrate...\n")
    for i in range(5, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    celebrate_kohli()

# Run the program
if __name__ == "__main__":
    countdown()

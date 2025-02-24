import datetime

def wish_ronaldo():
    # Get today's date
    current_date = datetime.datetime.now()
    
    # Ronaldo's birthday is February 5th
    if current_date.month == 2 and current_date.day == 5:
        message = """
        🏆⚽️ **HAPPY BIRTHDAY, CR7!** ⚽️🏆
        
        🎉 To the legend who has inspired millions and shown the world the power of hard work and dedication. 🎉
        
        On your special day, we wish you nothing but pure joy, endless victories, and more goals than ever before! 🥳
        
        Here's to more hat-tricks, more titles, and more iconic moments on and off the field! 🔥💪
        
        May your year ahead be as epic as your career! 🙌
        
        #HappyBirthdayCR7 #Legend #GOAT #CR7
        """
    else:
        message = f"Today may not be Ronaldo's birthday, but we still gotta appreciate the legend! ⚽️💥"

    print(message)

# Call the function
wish_ronaldo()

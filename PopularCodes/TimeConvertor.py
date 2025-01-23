def convert_time(time):
    if time[-2:] == "AM" and time[:-2] != "12:00:00":
        return "00"+time[2:-2]
    elif time[-2:] == "PM" and time[:-2] == "12:00:00":
        return time[:-2]
    
    elif time[-2:] == "PM":
        return str(int(time[:2]) + 12) + time[2:8]
    else:
        return time[:-2]
    
# Input time from the user
time = input("Enter a time in 12-hour format (HH:MM:SS AM/PM): ")
changed_time = convert_time(time)
print(changed_time)
# Output: 12:00:00
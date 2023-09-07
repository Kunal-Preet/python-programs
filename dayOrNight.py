import time

def is_dark_outside():
    current_time = time.localtime()
    hour = current_time.tm_hour
    
    # Define the start and end hours for daytime (adjust as needed)
    start_daytime = 6
    end_daytime = 18
    
    # Check if the current hour is within the daytime range
    if start_daytime <= hour < end_daytime:
        return False  # It's daytime, so not dark
    else:
        return True   # It's not daytime, so it's dark

# Get the result of whether it's dark outside or not
dark = is_dark_outside()

# Display the result
if dark:
    print("It is dark outside.")
else:
    print("It is not dark outside.")

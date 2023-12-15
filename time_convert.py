# This function converts a given time in 12-hour format to 24-hour format.

def convert_time(hour, minutes, period):
    # Check if the period is 'am' and the hour is '12'.
    if period == "am" and hour == 12:
        # If so, set the hour to '00' for 24-hour format.
        time = '00'
    # Check if the period is 'am'.
    elif period == 'am':
        # If the hour is greater than 10, keep it as is; otherwise, add a leading '0'.
        time = f'{hour}' if hour > 10 else f'0{hour}'
    # Check if the period is 'pm'.
    elif period == "pm":
        # If the hour is '12', keep it as is; otherwise, add 12 to the hour.
        time = '12' if hour == 12 else f'{hour + 12}'
    
    # Add the minutes to the time, adding a leading '0' if the minutes are less than 10.
     time = f'{time}{minutes}' if minutes > 10 else f'{time}0{minutes}'
    
    # Return the converted time in 24-hour format.
    return 

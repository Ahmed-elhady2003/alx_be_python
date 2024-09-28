def display_current_datetime():
    from datetime import datetime
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: ", formatted_time)

def calculate_future_date():
    from datetime import datetime, timedelta
    current_date = datetime.now()
    num = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=num)
    new_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {new_date}")




display_current_datetime()  
calculate_future_date()
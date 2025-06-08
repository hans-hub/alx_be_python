from datetime import datetime,date,timedelta


""""
current_date = datetime.now()
print(current_date)

specific_date = date(2025,10,12)
print(specific_date)

#format date
formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
print(f"{formatted_date}")

#future date

future_date = current_date + timedelta(days=7)
print(future_date)

"""""

#function to display current date and time

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(formatted_date)
display_current_datetime()


#futuredate function 

def calculate_future_date():
    current_date = datetime.now()
    number_of_days = int(input("Enter the number of days to add to the current date: ").strip())
    future_date = current_date + timedelta(days=number_of_days)
    formatted_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Future date: {formatted_date}")
    
calculate_future_date()
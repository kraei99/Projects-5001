'''
    CS5001
    2023 Fall
    Kayser Raei
    Homework 6 - Hyperspace BnB
'''

# load travelers from the 'travelers.txt' file into a dictionary
def load_travelers(travelers_file_name: str):
    try:
        with open(travelers_file_name, 'r') as file:
            travelers_data = {}
            for line in file:
                name, user_id, credits = line.strip().split('@')
                travelers_data[user_id] = {'name': name, 'credits': int(credits)}
            return travelers_data
    # if the file doesn't exist, return an empty dictionary
    except Exception as e:
        print(f"An error occurred while loading travelers: {e}")
        return {}

# process the requests from the 'requests.txt' file and update the 'bookings.txt' file
def process_requests(travelers_data, request_file_name: str):
    try:
        # load the requests from the 'requests.txt' file
        with open(request_file_name, 'r') as file:
            requests = file.readlines()
        
        # sort the requests by week
        requests.sort(key=lambda x: int(x.split()[1]))

        # set stores the weeks that are already booked
        booked_weeks = set()

        # list stores the bookings into bookings.txt
        successful_bookings = []

        for request in requests:
            parts = request.strip().split()
            user_id, week = parts[0], int(parts[1])
            # Check if the week is already booked and if the user has enough credits to book the week
            if week not in booked_weeks and user_id in travelers_data and travelers_data[user_id]['credits'] >= 500:
                # Deduct 500 credits from the user's account
                travelers_data[user_id]['credits'] -= 500
                booked_weeks.add(week)
                successful_bookings.append(f"{week} - {user_id} - {travelers_data[user_id]['name']}\n")

        # Update the travelers.txt file with the new credits
        with open('bookings.txt', 'w') as file:
            file.writelines(successful_bookings)

        print("Finished processing reservations. Beam us up Scottie!")
    except Exception as e:
        print(f"An error occurred while processing requests: {e}")

# load the travelers from the 'travelers.txt' file
travelers_data = load_travelers('travelers.txt')
process_requests(travelers_data, 'requests.txt')
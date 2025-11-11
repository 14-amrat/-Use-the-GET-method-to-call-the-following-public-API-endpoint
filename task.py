import requests

def fetch_users():
    # API endpoint for user data
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        # Send a GET request to the API
        response = requests.get(url)
        response.raise_for_status()  # check if the request was successful

        # Convert the response data to JSON
        users = response.json()

        # If no users found, show message
        if not users:
            print("No users found from the API.")
            return

        print("Users whose city starts with 'S':\n")

        count = 0
        # Go through each user one by one
        for i, user in enumerate(users, start=1):
            name = user.get("name")
            username = user.get("username")
            email = user.get("email")
            city = user.get("address", {}).get("city")

            # Print only if city name starts with 'S' (bonus part)
            if city and city.lower().startswith('s'):
                count += 1
                print(f"User {count}:")
                print(f"  Name: {name}")
                print(f"  Username: {username}")
                print(f"  Email: {email}")
                print(f"  City: {city}")
                print("-" * 25)

        if count == 0:
            print("No users found with city name starting with 'S'.")

    except requests.exceptions.RequestException as e:
        # This will run if there’s an error in the API call
        print("Error while fetching data:", e)


# Run the function
if __name__ == "__main__":
    fetch_users()


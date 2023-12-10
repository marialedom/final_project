import requests
from requests.auth import HTTPBasicAuth

def get_canvas_access_token(client_id, client_secret, username, password):
    canvas_url = "https://babson.instructure.com"  # Replace with your Canvas instance URL

    auth = HTTPBasicAuth(client_id, client_secret)
    data = {
        'grant_type': 'password',
        'username': username,
        'password': password,
    }

    response = requests.post(f"{canvas_url}/login/oauth2/token", auth=auth, data=data)

    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        print(f"Error: Unable to retrieve access token. Status code: {response.status_code}")
        return None

def get_canvas_courses(api_url, access_token):
    # Construct the API endpoint for retrieving course information
    courses_endpoint = f"{api_url.rstrip('/')}/api/v1/courses"

    # Set up headers with access token
    headers = {"Authorization": f"Bearer {access_token}"}

    # Make a request to the API endpoint
    response = requests.get(courses_endpoint, headers=headers)

    try:
        # Check if the request was successful (status code 200)
        response.raise_for_status()

        # Attempt to parse the JSON response
        courses = response.json()

        # Print course information
        for course in courses:
            print(f"Course ID: {course.get('id', 'N/A')}, Name: {course.get('name', 'N/A')}, Code: {course.get('course_code', 'N/A')}")
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")

if __name__ == "__main__":
    client_id = input("Enter your Canvas client ID: ")
    client_secret = input("Enter your Canvas client secret: ")
    username = input("Enter your Canvas username: ")
    password = input("Enter your Canvas password: ")

    access_token = get_canvas_access_token(client_id, client_secret, username, password)

    if access_token:
        babson_url = input("Enter your Babson Instructure website URL: ")
        get_canvas_courses(babson_url, access_token)


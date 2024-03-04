import requests

API_key = '8dfe086d738c02b628c9dc28c2944a1d'


def get_data(place, days=None, option=None):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}'
    response = requests.get(url)
    data = response.json()

    # Print the entire data dictionary for debugging
    print("API Response:", data)

    # Check if the key 'list' exists in the data dictionary
    if 'list' not in data:
        raise KeyError("Key 'list' not found in API response.")

    filtered_data = data["list"]
    nrdata = days * 8
    filtered_data = filtered_data[:nrdata]

    if option == 'temperature':
        filtered_data = [dict['main']['temp'] for dict in filtered_data]
    elif option == 'sky':
        filtered_data = [dict['weather'][0]['main'] for dict in filtered_data]

    return filtered_data


if __name__ == '__main__':
    print(get_data(place='tokyo', days=5, option='sky'))

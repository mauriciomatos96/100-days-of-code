import requests
from pprint import pprint

SHEETY_ENDPOINT = "https://api.sheety.co/50be8a6d6d45fb4f33d46550838a7ddf/flightDeals/prices"


class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(SHEETY_ENDPOINT)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
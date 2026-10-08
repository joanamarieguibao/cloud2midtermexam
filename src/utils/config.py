import json


class Config:

    def __init__(self, filename="config/config.json"):
        self.filename = filename
        self.settings = self.load()

    def load(self):

        try:
            with open(self.filename, "r") as file:
                return json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def get(self, key, default=None):
        return self.settings.get(key, default)
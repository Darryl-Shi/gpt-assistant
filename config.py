import json

class Config:
    def __init__(self, config_file="config.json"):
        with open(config_file) as f:
            self.data = json.load(f)

    def get_openai_base_url(self):
        return self.data["openai_base_url"]

    def get_openai_api_key(self):
        return self.data["openai_api_key"]

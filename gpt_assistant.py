import openai

class GPTAssistant:
    def __init__(self, config):
        self.config = config
        openai.api_key = self.config.get_openai_api_key()

    def generate_reply(self, prompt):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()

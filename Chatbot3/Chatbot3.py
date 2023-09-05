from nemoguardrails.rails import LLMRails, RailsConfig
import openai
import os
openai.api_key = ('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')
os.environ['OPENAI_API_KEY'] = ('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')
config = RailsConfig.from_path("Chatbot3.yaml")
app = LLMRails(config, verbose=False)
history = [{"role": "user", "content": "When did Neil Armstrong walk on the moon with Jyothika?"}]
bot_message = await app.generate_async(messages=history)
print(bot_message['content'])

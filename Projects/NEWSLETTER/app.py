
import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model = 'Claude-3-5-sonnet-20240620',
    max_tokens = 1000,
    messages = [
        {
            "role": 'user',
            "content":[
                {
                    "type":"text",
                    "text": "Hi"
                }
            ]
        }
    ]
)

print(message.content)
import os
import openai

# Set your OpenAI API key here
openai.api_key = "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"


# Rest of your code
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "Write an email to my boss for resignation\n"
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response)

"""
{
  "id": "chatcmpl-7hgEckrn46Bmklqh1Eby57gDVmSYm",
  "object": "chat.completion",
  "created": 1690644810,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Dear [Boss's Name],\n\nI hope this email finds you well. I am writing to formally resign from my position at [Company Name], effective [last working day], as I have accepted another opportunity that aligns more closely with my career goals and personal aspirations.\n\nI want to express my gratitude for the opportunities and valuable experiences I have had during my time at [Company Name]. It has been an incredible journey working alongside such talented individuals, and I am incredibly grateful for the support and guidance you have provided me throughout my tenure.\n\nDuring my time here, I have gained valuable skills and knowledge that will undoubtedly contribute to my future career growth. I am proud of the achievements I have made and the contributions I have been able to make to the success of the team and the organization as a whole.\n\nI will do everything I can to ensure a seamless transition of my responsibilities and will be available to assist in any way possible during my notice period. I am committed to ensuring that all ongoing projects are completed and that there is no disruption in the workflow.\n\nI would like to take this opportunity to express my appreciation for your leadership and for being an exceptional boss. Your guidance, trust, and support have been instrumental in my professional development, and I am truly grateful for the opportunities you have given"
      },
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 16,
    "completion_tokens": 256,
    "total_tokens": 272
  }
}

"""


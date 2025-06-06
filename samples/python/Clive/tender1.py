import os
from openai import OpenAI

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model_name = "openai/gpt-4o"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

'''
Contract Reference Number	PH/2025/458
https://www.stoke.gov.uk/homepage/75/tender_and_quotation_opportunities_-_detail/?ID=339
'''

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "I would like to respond to the tender question in between <>. The award criteria is Price and Quality Mix(MEAT). What is the optimal answer to ensure I make a profit and win the tender? <The service is for provision of a Smoking Cessation Service for individuals aged 12 and over who live, work, attend education settings, or are registered with a GP within the Stoke-on-Trent geographical area. Stop Smoking Service providing specialist support to high risk groups and digital support and signposting to national resources for other groups. Vulnerable people including pregnant women and their unborn children / families, and people with mental health problems will have access to specialist support to help them stop smoking. This will improve health and wellbeing, and lower the risk of smoking related ill health and premature mortality. This procurement follows Provider Selection Regime.>",
        }
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(response.choices[0].message.content)
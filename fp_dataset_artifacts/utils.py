import os
import openai

from dotenv import load_dotenv


def init_openai():
    load_dotenv()  # take environment variables from .env.
    openai.api_key = os.getenv('OPENAI_API_KEY')


def get_qa_response(prompt, engine='curie'):
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=['\n'],
    )
    return response


def get_clf_response(prompt, engine='curie'):
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=0.3,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=['###'],
    )
    return response


def get_finetune_response(prompt, model):
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=0.3,
        max_tokens=10,
        stop=['\n'],
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0,
    )
    return response


def upload(dataset, filename, purpose='fine-tune'):
    dataset.to_json(filename)
    response = openai.File.create(
        file=open(filename), purpose=purpose
    )
    file_id = response['id']
    return file_id
    

def save_results(file_id, filename):
    with open(f'../results/{filename}', 'wb') as f:
        f.write(openai.File.download(file_id))

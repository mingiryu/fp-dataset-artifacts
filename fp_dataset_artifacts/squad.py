INTRO = (
    'I am a highly intelligent question answering bot. '
    + 'If you ask me a question that is rooted in truth, '
    + 'I will give you the answer.'
)

INTRO_2 = (
    INTRO
    + ' If you ask me a question that is nonsense, '
    + 'trickery, or has no clear answer, I will respond with "Unknown".'
)


def map_example(x):
    question = x['question']
    answer = x['answers']['text'][0]
    context = x['context']
    return {'example': f'{context}\nQ: {question}\nA: {answer}'}


def map_query(x):
    question = x['question']
    context = x['context']
    return {'query': f'{context}\nQ: {question}\nA: '}

INTRO = (
    'I am a highly intelligent question answering bot. '
    + 'If you ask me a question that is rooted in truth, '
    + 'I will answer in either "Yes" or "No".'
)

LONG_INTRO = (
    'I am a highly intelligent question answering bot. '
    + 'If you ask me a question that is rooted in truth, '
    + 'I will read the given passage thoroughly and '
    + 'answer in either "Yes" or "No".'
)


def format_question(q):
    return q.capitalize() + '?'


def format_answer(a):
    return 'Yes' if a else 'No'


def get_zeroshot_prompt(x, intro=INTRO, passage=True):
    question = format_question(x['question'])

    if passage:
        passage = x['passage']
        return f"{intro}\n\n{passage}\n\nQ: {question}\n\nA: "
    else:
        return f"{intro}\n\nQ: {question}\n\nA: "


def get_fewshot_prompt(x, exs, intro=LONG_INTRO, passage=True, sep='###'):
    examples = [
        get_zeroshot_prompt(ex, intro=sep, passage=passage)
        + format_answer(ex['answer'])
        for ex in exs
    ]
    target = get_zeroshot_prompt(x, intro=sep, passage=passage)
    return '\n\n'.join([intro, *examples, target])


def map_finetune_train(x):
    question = format_question(x['question'])
    passage = x['passage']
    answer = format_answer(x['answer'])

    return {
        'prompt': f"{passage}\n\nQ: {question}\n\nA: ",
        'completion': answer,
    }


def get_finetune_prompt(x):
    question = format_question(x['question'])
    passage = x['passage']

    return f"{passage}\n\nQ: {question}\n\nA: "

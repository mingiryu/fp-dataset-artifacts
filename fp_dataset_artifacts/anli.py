import openai


INTRO = (
    'I am a highly intelligent natural language inference bot. '
    + 'If you give me a pair of premise and hypothesis, '
    + 'I will tell you whether the hypothesis is entailment, neutral, or contradiction.'
)


def int2label(i):
    return ['Entailment', 'Neutral', 'Contradiction'][i]


def label2int(x):
    return {
        'Entailment': 0,
        'Neutral': 1,
        'Contradiction': 2
    }[x]


def map_finetune(x):
    premise = x['premise']
    hypothesis = x['hypothesis']
    label = int2label(x['label'])

    return {
        'prompt': f"Premise: {premise}\n\nHypothesis: {hypothesis}\n\nLabel: ",
        'completion': label
        + '\n',  # '\n' added to prevent further text generation.
    }


def get_examples(exs):
    prompts = exs['prompt']
    completions = exs['completion']
    examples = [p + c for p, c in zip(prompts, completions)]
    return '\n\n'.join(examples)


def get_prompt(x, exs, intro=INTRO):
    examples = get_examples(exs)
    query = x['prompt']
    prompt = f'{intro}\n\n{examples}\n\n{query}'
    return prompt


def get_response(prompt, model):
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

INTRO = (
    'I am a highly intelligent natural language inference bot. '
    + 'If you give me a pair of premise and hypothesis, '
    + 'I will tell you whether the hypothesis is entailment, neutral, or contradiction.'
)


def int2label(i):
    return ['Entailment', 'Neutral', 'Contradiction'][i]


def map_finetune_train(x):
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

INTRO = 'This is a natural language inference (NLI) classifier'


def int2label(i):
    return ['Entailment', 'Neutral', 'Contradiction'][i]


def map_example(x):
    premise = x['premise']
    hypothesis = x['hypothesis']
    label = int2label(x['label'])

    return {
        'example': f"Premise: {premise}\nHypothesis: {hypothesis}\nLabel: {label}",
    }


def get_examples(exs):
    return '\n###\n'.join(exs['example'])


def get_premises(exs):
    return '\n'.join(f'{i+1}. "{x}"' for i, x in enumerate(exs['premise']))


def get_hypotheses(exs):
    return '\n'.join(f'{i+1}. "{x}"' for i, x in enumerate(exs['hypothesis']))


def get_labels(exs):
    return '\n'.join(
        f'{i+1}: {int2label(x)}' for i, x in enumerate(exs['label'])
    )

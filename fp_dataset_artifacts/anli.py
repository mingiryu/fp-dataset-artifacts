def int2label(i):
    return ['Entailment', 'Neutral', 'Contradiction'][i]


def map_finetune_train(x):
    premise = x['premise']
    hypothesis = x['hypothesis']
    label = int2label(x['label'])

    return {
        'prompt': f"Premise: {premise}\n\nHypothesis: {hypothesis}\n\nLabel: ",
        'completion': label + '\n', # '\n' added to prevent further text generation.
    }

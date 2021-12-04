# Evaluating the Robustness and Fairness of Commercially Available GPT-3 Models

## Abstract

OpenAI released the GPT-3 API to the public after long period of closed beta. From Codex to recruitment, there are many applications of NLP models that are sensitive to personal information, institutional bias, and a certain degree of reliability. We investigate the robustness and fairness of GPT-3 models in both few-shot learning and fine-tuned models to evaluate whether GPT-3 models are good enough to be used in commercial applications.

## Introduction

## Few-shot Learning

GPT-3 is well known for zero/one/few-shot learning. It can learn on the stop from none to few examples and perform surprisingly well. However, it can always behave quite unpredictably at times due to the natural of text generation. For instance, it can _hallucinate_ some information it learned during pre-training, which makes it difficult to trust whether the model is actually performing the task without bias. Also, it can sometimes decide not to follow the example at all and go on its merry way of composing examples without labels (which is what we want).

### Question and Answering

In this section, we consider one of the most well regarded NLP tasks, the question and answering.

We evaluate on the following datasets:

-   SQuAD 1.1
-   SQuAD 2.0
-   HotpotQA
-   BoolQ

These datasets are chosen for their popularity and the subtle differences (SQuAD 2.0 includes questions that cannot be answered) that might bring insight to the strengths and weakness of the model.

### State of the Art and Baseline Performance

Here we show the available benchmarks for each datasets from PaperWithCode.com

| Model                  | SQuAD 1.1 dev (EM F1) | SQuAD 2.0 (EM F1) | HotpotQA | BoolQ |
| ---------------------- | --------------------- | ----------------- | -------- | ----- |
| T5-11B                 | 90.06 95.64           |                   |          | 91.2  |
| LUKE                   | 89.8 95               | 87.429 90.163     |          |       |
| XLNet (single model)   | 89.7 95.1             |                   |          |       |
| BERT large             | 84.1 90.9             |                   |          |       |
| BERT base (single)     | 80.8 88.5             |                   |          |       |
| BERT (single model)    |                       | 80.005 83.061     |          |       |
| ALBERT (Single model)  |                       | 88.107 90.902     |          |       |
| XLNet (single model)   |                       | 87.926 90.689     |          |       |
| RoBERTa (single model) |                       | 86.820 89.795     |          |       |
| DeBERTalarge           |                       | 88.0 90.7         |          |       |
| DeBerta-1.5B           |                       |                   |          | 90.4  |
| FLAN 137B zero-shot    |                       |                   |          | 82.9  |
| GPT-3 175B (Few-Shot)  |                       |                   |          | 76.4  |

The obvious issue here is that there aren't any available benchmarks for GPT-3 that can be reliably compared with other transformer models.

As a result, we need to come up with out own baseline.

### Datasets

All datasets are sourced via HuggingFace Datasets library.

### Implementation

At the time of this writing, OpenAI offers 4 different tier of models (or Engines) that differs in cost and performance (speed and accuracy). More details about the model can be found in [Engines - OpenAI API](https://beta.openai.com/docs/engines). Based on our prior exploration, _Ada_ model is too weak for question and answering and _Davinci_ model is simply too expensive. We'll use the _Curie_ model to evaluate the general performance of OpenAI's GPT-3 offerings.

### Results

#### Zero-shot Learning

GPT-3 delivers practically no results on zero-shot learning.

For a perfectly valid prompt such as the following, the model fails or refuses to generate a valid text.

**SQuAD Examples**

Hyperparameters:

```
  engine='curie',
  prompt=prompt,
  temperature=0,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\n"]
```

Prompt 1:

```
I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer.

Context: Architecturally, the school has a Catholic character. Atop the Main Building's gold dome is a golden statue of the Virgin Mary. Immediately in front of the Main Building and facing it, is a copper statue of Christ with arms upraised with the legend "Venite Ad Me Omnes". Next to the Main Building is the Basilica of the Sacred Heart. Immediately behind the basilica is the Grotto, a Marian place of prayer and reflection. It is a replica of the grotto at Lourdes, France where the Virgin Mary reputedly appeared to Saint Bernadette Soubirous in 1858. At the end of the main drive (and in a direct line that connects through 3 statues and the Gold Dome), is a simple, modern stone statue of Mary.

Question: To whom did the Virgin Mary allegedly appear in 1858 in Lourdes France?

Answer:
```

Generated text:

```
_________
```

Prompt 2 (w/o context):

```
I am a highly intelligent question answering bot.

Q: What countries are recognized as Nuclear Weapons States?

A:
```

Generated text:

```

```

Prompt 3 (w/o context):

```
I am a highly intelligent question answering bot.

Q: On what part of the island is Fort Oscar located on the far side of?

A:
```

Generated text:

```
????
```

Prompt 4 (w/o context using `Davinci`):

```
I am a highly intelligent question answering bot.

Q: On what part of the island is Fort Oscar located on the far side of?

A:
```

Generated text:

```
\u0caa\u0ccd\u0cb0\u0cbf\u0caf\u0cae\u0ccd\u0cae\u0ca8\u0ccd \u0cae\u0ca8\u0cc6\u0caf\u0cbf\u0c82\u0ca6 \u0cae\u0cc1\u0c82\u0ca6\u0cc1\u0cb5\u0cb0\u0cc6\u0caf\u0cb2\u0ccd\u0cb2\u0cbf \u0c85\u0cb5
```

Prompt 5 (w context using `Davinci`):

```
I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer.

Among the notable structures in the town are the three forts built by the Swedes for defense purposes. One of these forts, known as Fort Oscar (formerly Gustav Adolph), which overlooks the sea is located on the far side of La Pointe. However, the ruins have been replaced by a modern military building which now houses the local gendarmerie. The other fort known as Fort Karl now presents a very few ruins. The third fort built by the Swedes is the Fort Gustav, which is also seen in ruins strewn around the weather station and the Light House. The fort built in 1787 over a hill slope has ruins of ramparts, guardhouse, munitions depot, wood-burning oven and so forth.

Q: On what part of the island is Fort Oscar located on the far side of?

A:
```

Generated text:

```

```

These examples demonstrate that GPT-3 models cannot perform zero-shot learning on SQuAD dataset. Same is true for other datasets such as _BoolQ_ dataset.

**BoolQ Examples**

Hyperparameters: Same as _SQuAD_ examples.

Prompt 1:

```
I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will answer in either "Yes" or "No".

Q: Do iran and afghanistan speak the same language?

A:
```

Generated text:

```
????
```

Prompt 2 (with passage):

```
I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will answer in either "Yes" or "No".

Persian (/ˈpɜːrʒən, -ʃən/), also known by its endonym Farsi (فارسی fārsi (fɒːɾˈsiː) ( listen)), is one of the Western Iranian languages within the Indo-Iranian branch of the Indo-European language family. It is primarily spoken in Iran, Afghanistan (officially known as Dari since 1958), and Tajikistan (officially known as Tajiki since the Soviet era), and some other regions which historically were Persianate societies and considered part of Greater Iran. It is written in the Persian alphabet, a modified variant of the Arabic script, which itself evolved from the Aramaic alphabet.

Q: Do iran and afghanistan speak the same language?

A:
```

Generated text:

```
\u06cc\u06a9\u06cc \u0627\u0632 \u062f\u06cc\u06af\u0631 \u062f\u0648\u0644\u062a \u0647\u0627\u06cc \u062c\u0647\u0627\u0646 \u0628\u0647 \u0639\u0646\u0648\u0627\u0646 \u06cc\u06a9 \u062f\u0648\u0644\u062a \u062f\u0631 \u062c\u0647\u0627\u0646 \u0628\u0647 \u0639\u0646\u0648\u0627\u0646 \u06cc\u06a9 \u062f\u0648\u0644\u062a \u062f\u0631 \u062c\u0647\u0627\u0646 \u0628\u0647 \u0639\u0646\u0648\u0627\u0646 \u06cc\u06a9
```

Prompt 3 (with passage):

```
I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will answer in either "Yes" or "No".

Harry Potter and the Forbidden Journey uses KUKA robocoaster technology, which allows the seats to pivot while being held above the track by a robotic arm. However, the ride is not a roller coaster but a scenic dark ride. The experience includes a flight around Hogwarts castle, an encounter with the Whomping Willow and a horde of Dementors, and a Quidditch match. The ride drops, spins around, twists and turns, but does not turn upside down, though passengers sometimes lie flat on their backs. Over-the-shoulder bars are used to secure guests in their seats, and a single parabolic metal bar is used as a hand grip. At the conclusion of the ride, guests exit into Filch's Emporium of Confiscated Goods gift shop.

Q: Is the harry potter and the forbidden journey ride a roller coaster?

A:
```

Generated text:

```
ive been on it and it isnt a roller coaster.
```

Prompt 4 (with passage):

```
I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will answer in either "Yes" or "No".

Goalkeepers are normally allowed to handle the ball within their own penalty area, and once they have control of the ball in their hands opposition players may not challenge them for it. However the back-pass rule prohibits goalkeepers from handling the ball after it has been deliberately kicked to them by a team-mate, or after receiving it directly from a throw-in taken by a team-mate. Back-passes with parts of the body other than the foot, such as headers, are not prohibited. Despite the popular name ``back-pass rule'', there is no requirement in the laws that the kick or throw-in must be backwards; handling by the goalkeeper is forbidden regardless of the direction the ball travels.

Q: Can you pass to the goalie in soccer?

A:
```

Generated text:

```

```
While these are only a handful of examples, but it demonstrate one of the most notable weaknesses of GPT-3 zero-shot learning: failing to generate text. This is quite ironic since GPT-3 is a celebrated as generative model, but it cannot produce a valid text even without the `stop='\n'` parameter.


### Natural Language Inference

### State of the Art and Baseline Performance

## Fine-tuning

### Question and Answering

### Natural Language Inference

## Prompt Engineering

## Adversarial Attacks and Challenges Datasets

### CheckList

### Contrastive and Counterfactuals

## Language Modeling

### Masked Language Modeling

### Next Token Language Modeling

## Societal Implications

### Misinformation

### Unemployment

### Surveillance Capitalism

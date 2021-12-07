# Analyzing and Mitigating Dataset Artifacts in OpenAI's Commercially Available GPT-3 Models

## Abstract

We investigated few-shot and fine-tuned GPT-3 models using OpenAI's GPT-3 API. We experimented with question answering and natural language inference tasks and their respective datasets to figure out which dataset would be the most suitable to use for analyzing dataset artifacts in OpenAI GPT-3. Due to some mysterious challenges with few-shot learning and the black box nature of the model, we settled with NLI task. To establish a baseline, we fine-tuned the model with _SNLI_ and compared the performance in _SNLI_ and _ANLI_ test sets. 

## Introduction

OpenAI released the GPT-3 API to the public after long period of closed beta. From Codex to recruitment, there are many applications of NLP models that are sensitive to personal information, institutional bias, and a certain degree of reliability. We investigate the robustness of GPT-3 models in both few-shot learning and fine-tuned models to evaluate whether GPT-3 models are good enough to be used in commercial applications.

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

The obvious issue here is that there aren't any available benchmarks for GPT-3 that can be reliably compared with other transformer models. As a result, we need to come up with our own baseline in order to evaluate how dataset artifacts affect GPT-3.

> Note: Since _HotpotQA_ doesn't have any benchmark results for any of those models, we won't be considering it going forward. However, preliminary work demonstrates GPT-3 potential in multi-hop question answering.

### Datasets

All datasets are sourced via HuggingFace Datasets library.

### Implementation

At the time of this writing, OpenAI offers 4 different tier of models (or Engines) that differs in cost and performance (speed and accuracy). More details about the model can be found in [Engines - OpenAI API](https://beta.openai.com/docs/engines). Based on our prior exploration, _Ada_ model is too weak for question and answering and _Davinci_ model is simply too expensive. We'll use the _Curie_ model to evaluate the general performance of OpenAI's GPT-3 offerings.

### Results

#### Zero-shot Learning

GPT-3 delivers practically no results on zero-shot learning.

For a perfectly valid prompt such as the following, the model fails (or refuses) to generate a valid text.

**SQuAD Samples**

Hyperparameters:

```py
engine='curie',
prompt=prompt,
temperature=0,
max_tokens=100,
top_p=1,
frequency_penalty=0.0,
presence_penalty=0.0,
stop=['\n']
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

These samples demonstrate that GPT-3 models cannot perform zero-shot learning on SQuAD dataset. Same is true for other datasets such as _BoolQ_ dataset.

**BoolQ Samples**

Hyperparameters: Same as _SQuAD_ samples.

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

Since zero-shot GPT-3 is non-functional, we can assume that the performance is near zero.

#### Few-shot Learning

On the other hand, GPT-3 can be quite good at few-shot learning and can perform well even without the context. However, due to the nature of text generation, exact match (EM) performance is quite bad and it makes it challenging to evaluate the performance accurately.

**SQuAD 2.0 Samples**

Hyperparameters:

```py
engine='ada',
prompt=prompt,
temperature=0,
max_tokens=100,
top_p=1,
frequency_penalty=0.0,
presence_penalty=0.0,
stop=['\n']
```

We use _Ada_ model here because we found that this model was good enough for few-shot learning.

Prompt 1 w/ a single example:

```
I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with "Unknown".

Q: What areas did Beyonce compete in when she was growing up?
A: singing and dancing

Q: In which decade did Beyonce become famous?
A:
```

Generated text:

```
1980s
```

Expected text:

```
late 1990s
```

Prompt 2 w/ a few examples:

```
I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with "Unknown".

Q: What areas did Beyonce compete in when she was growing up?
A: singing and dancing

Q: In what city and state did Beyonce  grow up?
A: Houston, Texas

Q: In which decade did Beyonce become famous?
A:
```

Generated text:

```
1980s
```

Expected text:

```
late 1990s
```

Prompt 3 w/ a very similar question as an example:

```
I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with "Unknown".

Q: When did Beyonce start becoming popular?
A: in the late 1990s

Q: What areas did Beyonce compete in when she was growing up?
A: singing and dancing

Q: When did Beyonce leave Destiny's Child and become a solo singer?
A: 2003

Q: In what city and state did Beyonce  grow up?
A: Houston, Texas

Q: In which decade did Beyonce become famous?
A:
```

Generated text:

```
the late 1990s
```

Expected text:

```
late 1990s
```

Prompt 4 w/o the problematic question:

```
I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with "Unknown".

Q: What areas did Beyonce compete in when she was growing up?
A: singing and dancing

Q: When did Beyonce leave Destiny's Child and become a solo singer?
A: 2003

Q: In what city and state did Beyonce  grow up?
A: Houston, Texas

Q: In which decade did Beyonce become famous?
A:
```

Generated text:

```
1980s
```

Expected text:

```
late 1990s
```

Prompt 5 w/ context & w/o the problematic question:

```
I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with "Unknown".

Context: Beyoncé Giselle Knowles-Carter (/biːˈjɒnseɪ/ bee-YON-say) (born September 4, 1981) is an American singer, songwriter, record producer and actress. Born and raised in Houston, Texas, she performed in various singing and dancing competitions as a child, and rose to fame in the late 1990s as lead singer of R&B girl-group Destiny's Child. Managed by her father, Mathew Knowles, the group became one of the world's best-selling girl groups of all time. Their hiatus saw the release of Beyoncé's debut album, Dangerously in Love (2003), which established her as a solo artist worldwide, earned five Grammy Awards and featured the Billboard Hot 100 number-one singles "Crazy in Love" and "Baby Boy".

Q: What areas did Beyonce compete in when she was growing up?
A: singing and dancing

Q: When did Beyonce leave Destiny's Child and become a solo singer?
A: 2003

Q: In what city and state did Beyonce  grow up?
A: Houston, Texas

Q: In which decade did Beyonce become famous?
A:
```

Generated text:

```
1990s
```

Expected text:

```
late 1990s
```

Prompt 5 w/ context, w/ a single example, and w/o the problematic question:

```
I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with "Unknown".

Beyoncé Giselle Knowles-Carter (/biːˈjɒnseɪ/ bee-YON-say) (born September 4, 1981) is an American singer, songwriter, record producer and actress. Born and raised in Houston, Texas, she performed in various singing and dancing competitions as a child, and rose to fame in the late 1990s as lead singer of R&B girl-group Destiny's Child. Managed by her father, Mathew Knowles, the group became one of the world's best-selling girl groups of all time. Their hiatus saw the release of Beyoncé's debut album, Dangerously in Love (2003), which established her as a solo artist worldwide, earned five Grammy Awards and featured the Billboard Hot 100 number-one singles "Crazy in Love" and "Baby Boy".

Q: What areas did Beyonce compete in when she was growing up?
A: singing and dancing

Q: In which decade did Beyonce become famous?
A:
```

Generated text:

```
1990s
```

Expected text:

```
late 1990s
```

These samples illustrate a few characteristics of GPT-3.

-   Context does matter, but the model can make a decent guess without it.
-   The model will _cheat_ from the examples if it can.
-   Not all structure is useful. Adding or removing `Context:` doesn't seem to affect the result.
-   Getting the model to generate an exact match text seems tricky.

**BoolQ**

On the other hand, few-shot GPT-3 fails to generate any text on _BoolQ_ dataset even with as many example as 5 and with the complete passages.

Similar to zero-shot SQuAD, GPT-3 generates empty strings even for fairly sophisticated prompts. However, removing the `stop=['\n']` hyperparameter constraint does alleviate the empty string issue, but the generated text is a continuation of the examples with _hallucinated_ passage and question about the previous question and answer.

In essence, GPT-3 fails to generate a simple text "Yes" or "No" even with the provided examples to learn from on the spot.

> Note: The _BoolQ_ samples aren't included in this section for the sake of brevity.

### Natural Language Inference

In this section, we investigate another well known NLP task - _Natural Language Inference_. We are curious why the GPT-3 wasn't able to perform few-shot learning on the _BoolQ_ dataset even though it only had a two possible text to generate. Furthermore, it seems quite challenging to evaluate the exact match score for SQuAD dataset by hand. We think that these classification tasks are first step in the establishing a baseline performance for GPT-3.

For NLI, we'll only consider the _SNLI_, _ANLI_, and _CommitmentBank_ datasets.

For the sake of brevity, we won't be doing complete evaluations on all three datasets. We may come back to this task with more experiments if we find any issues with this particular task.

### State of the Art and Baseline Performance

Here we show the available benchmarks for each datasets from PaperWithCode.com

| Model                 | SNLI | CommitmentBank (F1 Accuracy) | ANLI test (A1 A2 A3) |
| --------------------- | ---- | ---------------------------- | -------------------- |
| T5-11B                |      | 93.9 96.8                    |                      |
| DeBerta-1.5B          |      | 94.9 97.2                    |                      |
| RoBERTa (Large)       |      |                              | 72.4 49.8 44.4       |
| XLNet (Large)         |      |                              | 70.3 50.9 49.4       |
| GPT-3 175B (Few-Shot) |      | 52 75.6                      |                      |
| GPT-3                 |      |                              | 36.8 34 40.2         |

Same as the Question and Answering task, there isn't a straight-forward way of estimating relative performance of GPT-3 compared to other models. In this case, _SNLI_ dataset doesn't even have any metrics available for the models that can be measured against GPT-3 in another dataset.

Regardless, we are still interested in GPT-3 performance on _SNLI_ and the other aforementioned datasets. We'll try to see if we can build a reasonable baseline for the use in dataset artifacts analysis.

> Note: _CommitmentBank_ dataset is not available via Huggingface's Datasets.

### Datasets

Same as Q&A section. All datasets are sourced via HuggingFace Datasets library.

### Implementation

Same as Q&A section. We'll use the _Curie_ model to evaluate the general performance of OpenAI's GPT-3 offerings.

### Results

In both _SNLI_ and _ANLI_, we were not able to make the model to generate a valid text ("Entailment", "Neutral", "Contradiction") regardless of how many examples we threw at it. Similar to _BoolQ_ dataset, we suspect that GPT-3 is not well suited for a complex classification tasks such as NLI.

Despite it's oddly redundant prompt and engineered structure, the [tweet sentiment classifier example](https://beta.openai.com/examples/default-adv-tweet-classifier) from OpenAI demonstrates GPT-3 ability to perform few-shot learning on sentiment classification. However, adapting this style of prompt did not allow the GPT-3 to perform the NLI task.

> Note: We won't be sharing the examples here for the sake of brevity.

## Fine-tuning

On the other hand, fine-tuning GPT-3 using [OpenAI's Fine-tunes](https://beta.openai.com/docs/guides/fine-tuning) allowed the fine-tuned models to perform the tasks where the few-shot learning had failed to generate a valid text.

With fine-tuning, we were able to verify the feasibility of using GPT-3 on _SNLI_, _ANLI_, and _BoolQ_ datasets. This meant that we can establish a baseline performance for each datasets.

At the time of this writing, fine-tuning on OpenAI's GPT-3 models are restricted to 2.5M tokens for the training and validation datasets. As a result, we weren't able to fine-tune with the entire datasets for most of the datasets.

### Implementation

All fine-tuning were done with the default hyperparameters (`n_epochs=4`) and appropriate classification metrics configuration. We found that four epochs was more than enough to reach the training token accuracy of `1.0`. However, some degree of prompt engineering was required to reliably get high score on training sequence accuracy.

### Question and Answering

With _BoolQ_, we fine-tuned on the entire training dataset and the reported validation accuracy was `85.7798`. Given that the published few-shot performance of GPT-3 is `76.4`, `85.7798` is a a reasonable starting point.

### Natural Language Inference

With _SNLI_, we fine-tuned on 10% of the training dataset due to the token limit imposed by OpenAI. The reported validation F1 score was `88.974`. The F1 and accuracy for test set was `91.33` and `91.3` respectively.

With _ANLI_, we fine-tuned only on the round 1 dataset due to the token limit. The reported validation F1 score was `55.0766` and test test F1 score was `56.398`, which is considerably higher than published GPT-3 (few-shot) round 1 F1 score of `36.8`.

## Adversarial Attack and Datasets

### Adversarial Datasets

In order to evaluate whether the adversarial dataset (_ANLI_) improved the performance of fine-tuned GPT-3 model, we fine-tuned two separate models on _SNLI_ and _ANLI_.

For _test_ model, we fine-tuned GPT-3 on both _SNLI_ and _ANLI_ (round 1). We used the entire _ANLI_ (round 1) training and a small portion (25,000) of _SNLI_ training set due to the token limit.

For _control_ model, we fine-tuned GPT-3 on only the _SNLI_ but with a larger training set to get the same training set size (41,946).

In both model, the training data for the _SNLI_ portion were identical and were shuffled beforehand. Same hyperparameters were used and same prompt structure were used to isolate any possible external variables.

**F1 score on SNLI or ANLI test set**

|                       | SNLI test | ANLI test |
| --------------------- | --------- | --------- |
| _test_ (SNLI & ANLI)  | 88.93     | 58.65     |
| _control_ (SNLI only) | 89.35     | 33.50     |

We found that augmenting the adversarial datasets did improve the test score on the adversarial set, but did not improve the test score on the original set. However, the test score on original set only dropped by `0.42` whereas the test score on the adversarial set increased by `25.15`. This is a much better trade off considering that the _control_ model is not doing much better than the `1/3` random guesses.

### CheckList and TextAttack

Due to the natural of OpenAI GPT-3 being a black box, we won't able to use adversarial attack tools such as _CheckList_ and _TextAttack_.

## Prompt Engineering

### Few-shot Learning

For Q&A, the prompt engineering had a notable impact on the text generation results. We found that more examples doesn't necessity help and it introduces the possibility of the model cheating based on the examples.

While introductions and the prompt structure do help, but it's not obvious why certain things help and not the others. While having "Q:" and "A:" was crucial in making the model work, having "Context:" did not make any notable difference in the result.

For NLI, any degree of prompt engineering didn't seem to help the model to make the correct text generation. We first thought that the label text we were asking the model was not "natural" enough, so we tried changing the examples to have complete sentences. Then, we tried rephrasing the task as Q&A since that prompt was working properly. Without much luck, that approach was also unsuccessful. We also adapted OpenAI's tweet sentiment classifier example to NLI to see if it was a problem of some obscure structure. However, that didn't work as well.

Some could argue that NLI task is simply too difficult for the model to learn on the spot, but it seems quite problematic that the model _cannot_ any relevant text regardless of the correctness.

However, a further ablation study of Q&A suggests that difficulty of the task is not the issue. If the prompt includes examples that are unrelated, then the model will fail to generate a valid text as well.

In conclusion, GPT-3 seems unable to learn to generate a valid label when there's too much and too broad of information in the prompt. It seems to end up focusing on the example generation rather label generation.

### Fine-tuning

In fine tuning, certain prompt aspects such as introduction and examples aren't necessary. However, basic prompt structure remain crucial in making the model perform.

Furthermore, adding in an end token such as a newline ("\n") or triple hashtags ("###") is necessary for the text generation to stop after the label is generated.

## Future Works

**Fine-tune on the entire SNLI training dataset**

-   Due to the token limitation, we were only able to train on roughly 10% of the training dataset for SNLI. Even with the restriction removed, it will cost significant amount of time and money to fine-tune the model. So, it needs to be carried out with a direct support from OpenAI.

**Investigate the issue in few-shot learning**

-   It's quite mysterious as to why GPT-3 fails to generate valid text in certain instances. This requires us evaluating GPT-3 model against larger selection of tasks to identify the characteristics of the dataset and task that makes it challenging for the model.

**Data Augmentation for Adversarial Attack**

-   Despite the black box limitation, we can explore data augmentation approach with either _CheckList_ or _TextAttack_. This would allow us to test the robustness of the model without needing to have access to the model weights and gradients. Since this consist of a lot of trial & error and brute-force methods, it will require expensive amounts of usage credits.

## Conclusion


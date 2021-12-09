## Abstract

Here we show that scaling up language models greatly improves task-agnostic,
few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art fine-
tuning approaches. 

Specifically, we train GPT-3, an autoregressive language model with 175 billion
parameters, 10x more than any previous non-sparse language model, and test its performance in
the few-shot setting.

For all tasks, GPT-3 is applied without any gradient updates or fine-tuning,
with tasks and few-shot demonstrations specified purely via text interaction with the model

## Introduction

Second, the potential to exploit spurious correlations in training data fundamentally grows with the expressiveness
of the model and the narrowness of the training distribution. This can create problems for the pre-training plus
fine-tuning paradigm, where models are designed to be large to absorb information during pre-training, but are then
fine-tuned on very narrow task distributions.

While it has shown some initial promise, this approach still achieves results far inferior to fine-tuning

Meta-learning clearly requires substantial improvement in order to be viable as a practical method of
solving language tasks.

Each increase has brought improvements in text synthesis and/or downstream
NLP tasks, and there is evidence suggesting that log loss, which correlates well with many downstream tasks, follows a
smooth trend of improvement with scale [KMH+20]. 

Since in-context learning involves absorbing many skills and
tasks within the parameters of the model, it is plausible that in-context learning abilities might show similarly strong
gains with scale.

In the context of language models this has sometimes been called “zero-shot transfer”, but this term is potentially ambiguous:
the method is “zero-shot” in the sense that no gradient updates are performed, but it often involves providing inference-time
demonstrations to the model, so is not truly learning from zero examples. 

We further specialize the description to “zero-shot”, “one-shot”, or “few-shot” depending on how many
demonstrations are provided at inference time. 

(a) “few-shot learning”, or in-context learning where we
allow as many demonstrations as will fit into the model’s context window (typically 10 to 100), (b) “one-shot learning”,
where we allow only one demonstration, and (c) “zero-shot” learning, where no demonstrations are allowed and only
an instruction in natural language is given to the model. GPT-3 could also in principle be evaluated in the traditional
fine-tuning setting, but we leave this to future work.

Broadly, on NLP tasks GPT-3 achieves promising results in the zero-shot and one-shot settings, and in the the few-shot
setting is sometimes competitive with or even occasionally surpasses state-of-the-art

GPT-3 also displays one-shot and few-shot proficiency at tasks designed to test rapid adaption or on-the-fly reasoning,
which include unscrambling words, performing arithmetic, and using novel words in a sentence after seeing them
defined only once.

At the same time, we also find some tasks on which few-shot performance struggles, even at the scale of GPT-3. This
includes natural language inference tasks like the ANLI dataset, and some reading comprehension datasets like RACE
or QuAC.

## Approach

Zero-Shot (0S) is the same as one-shot except that no demonstrations are allowed, and the model is only given
a natural language instruction describing the task. This method provides maximum convenience, potential for
robustness, and avoidance of spurious correlations (unless they occur very broadly across the large corpus of
pre-training data), but is also the most challenging setting.

Model Name nparams nlayers dmodel nheads dhead Batch Size Learning Rate
GPT-3 175B or “GPT-3” 175.0B 96 12288 96 128 3.2M 0.6 ×10−4

We use the same model and architecture as GPT-2 [RWC+19], including the modified initialization, pre-normalization,
and reversible tokenization described therein, with the exception that we use alternating dense and locally banded sparse
attention patterns in the layers of the transformer, similar to the Sparse Transformer.

A major methodological concern with language models pretrained on a broad swath of internet data, particularly large
models with the capacity to memorize vast amounts of content, is potential contamination of downstream tasks by
having their test or development sets inadvertently seen during pre-training. To reduce such contamination, we searched
for and attempted to remove any overlaps with the development and test sets of all benchmarks studied in this paper.
Unfortunately, a bug in the filtering caused us to ignore some overlaps, and due to the cost of training it was not feasible
to retrain the model.

### Training Dataset

However, we have found that unfiltered or lightly filtered versions of Common Crawl tend to have
lower quality than more curated datasets. Therefore, we took 3 steps to improve the average quality of our datasets:
(1) we downloaded and filtered a version of CommonCrawl based on similarity to a range of high-quality reference
corpora, (2) we performed fuzzy deduplication at the document level, within and across datasets, to prevent redundancy
and preserve the integrity of our held-out validation set as an accurate measure of overfitting, and (3) we also added
known high-quality reference corpora to the training mix to augment CommonCrawl and increase its diversity.

## Evaluation

For few-shot learning, we evaluate each example in the evaluation set by randomly drawing K examples from that
task’s training set as conditioning, delimited by 1 or 2 newlines depending on the task.

On tasks that involve binary classification, we give the options more semantically meaningful names (e.g. “True” or
“False” rather than 0 or 1) 

## Results

### Closed Book Question Answering

Since this setting allows a system to search for and condition on text which potentially contains the answer it
is denoted “open-book”. [RRS20] recently demonstrated that a large language model can perform surprisingly well
directly answering the questions without conditioning on auxilliary information. 

The results for GPT-3 are shown in Table 3.3. On TriviaQA, we achieve 64.3% in the zero-shot setting, 68.0% in the
one-shot setting, and 71.2% in the few-shot setting. The zero-shot result already outperforms the fine-tuned T5-11B by
14.2%, and also outperforms a version with Q&A tailored span prediction during pre-training by 3.8%. The one-shot
result improves by 3.7% and matches the SOTA for an open-domain QA system which not only fine-tunes but also
makes use of a learned retrieval mechanism over a 15.3B parameter dense vector index of 21M documents [LPP+20].
GPT-3’s few-shot result further improves performance another 3.2% beyond this.

### NLI

SuperGLUE includes an NLI dataset, RTE, which evaluates the binary version of the task. On RTE, only the largest
version of GPT-3 performs convincingly better than random (56%) in any evaluation setting, but in a few-shot setting
GPT-3 performs similarly to a single-task fine-tuned BERT Large. 

These results on both RTE and ANLI suggest that NLI is still a very difficult
task for language models and they are only just beginning to show signs of progress.

## Measuring and Preventing Memorization Of Benchmarks

although models did perform moderately better on data that overlapped between training and testing, this did not
significantly impact reported results due to the small fraction of data which was contaminated (often only a few percent).

due to the large amount of data, even GPT-3 175B
does not overfit its training set by a significant amount

We initially tried to address the issue of contamination by proactively searching for and attempting to remove any overlap
between our training data and the development and test sets of all benchmarks studied in this paper. Unfortunately, a
bug resulted in only partial removal of all detected overlaps from the training data. Due to the cost of training, it wasn’t
feasible to retrain the model.

meaning the model gains only
background information and cannot memorize the answer to a specific question.

We found the 4 Wikipedia language modeling benchmarks measured in GPT-2, plus the
Children’s Book Test dataset, to be almost entirely contained in our training data.

## Limitations

Thus our design decision comes at the cost of potentially worse performance on tasks
which empirically benefit from bidirectionality. This may include fill-in-the-blank tasks, tasks that involve looking back
and comparing two pieces of content, or tasks that require re-reading or carefully considering a long passage and then
generating a very short answer

ANLI (which involves
comparing two sentences to see if one implies the other)

A limitation, or at least uncertainty, associated with few-shot learning in GPT-3 is ambiguity about whether few-shot
learning actually learns new tasks “from scratch” at inference time, or if it simply recognizes and identifies tasks that it
has learned during training.

A limitation associated with models at the scale of GPT-3, regardless of objective function or algorithm, is that they are
both expensive and inconvenient to perform inference on, which may present a challenge for practical applicability of
models of this scale in their current form.

## Broader Impacts

### Fairness, Bias, and Representation

Broadly, our analysis indicates that internet-trained models have internet-scale biases; models tend to reflect stereotypes
present in their training data.

We found
that occupations in general have a higher probability of being followed by a male gender identifier than a female one

We found that, when prompted with "The competent
{occupation} was a," the majority of occupations had an even higher probability of being followed by a
male identifier than a female one than was the case with our original neutral prompt,

‘Asian’ had a consistently high sentiment - it ranked 1st in 3 out of 7 models. On the
other hand, ’Black’ had a consistently low sentiment - it ranked the lowest in 5 out of 7 models. These differences
narrowed marginally on the larger model sizes. 

with the religion Islam, we found that words such
as ramadan, prophet and mosque co-occurred at a higher rate than for other religions. We also found that words such
as violent, terrorism and terrorist co-occurred at a greater rate with Islam than with other religions 

## Results on All Tasks for All Model Sizes

Name Metric Split SOTA K Small Med Large XL 2.7B 6.7B 13B 175B Small Med Large XL 2.7B 6.7B 13B 175B Small Med Large XL 2.7B 6.7B 13B 175B

SQuADv2 em dev 90.7 16 22.6 32.8 33.9 43.1 43.6 45.4 49.0 52.6 25.1 37.5 37.9 47.9 47.9 51.1 56.0 60.1 27.5 40.5 39.2 53.5 50.0 56.6 62.6 64.9
SQuADv2 f1 dev 93.0 16 28.3 40.2 41.4 50.3 51.0 52.7 56.3 59.5 30.1 43.6 44.1 54.0 54.1 57.1 61.8 65.4 32.1 45.5 44.9 58.7 55.9 62.1 67.7 69.8
BoolQ acc dev 91.0 32 49.7 60.3 58.9 62.4 67.1 65.4 66.2 60.5 52.6 61.7 60.4 63.7 68.4 68.7 69.0 76.7 43.1 60.6 62.0 64.1 70.3 70.0 70.2 77.5 
ANLI R1 acc test 73.8 50 33.4 34.2 33.4 33.4 34.2 32.3 33.2 34.6 32.1 31.6 31.9 34.6 30.6 31.6 32.7 32.0 32.1 32.5 30.9 32.5 33.5 33.1 33.3 36.8
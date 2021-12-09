## Abstract

ANLI is a new large-scale NLI benchmark dataset, collected via an iterative, adversarial human-and-model-in-the-loop procedure. 

## Introduction

The speed with which benchmarks become ob-
solete raises another important question: are cur-
rent NLU models genuinely as good as their high
performance on benchmarks suggests? A grow-
ing body of evidence shows that state-of-the-art
models learn to exploit spurious statistical patterns
in datasets (Gururangan et al., 2018; Poliak et al.,
2018; Tsuchiya, 2018; Glockner et al., 2018; Geva
et al., 2019; McCoy et al., 2019), instead of learn-
ing meaning in the flexible and generalizable way
that humans do

Adversarial NLI data collection via human-and-model-in-the-loop enabled training (HAMLET). 

Here, we focus on natural language inference
(NLI), arguably the most canonical task in NLU.

## Dataset Collection

### HAMLET

Rather than employing auto-
mated adversarial methods, here the model’s “ad-
versary” is a human annotator.

Given a context
(also often called a “premise” in NLI), and a desired
target label, we ask the human writer to provide a
hypothesis that fools the model into misclassifying
the label.

We employed Mechanical Turk workers with quali-
fications and collected hypotheses via the ParlAI1
framework.

### Comparing with other datasets

First,
and most obviously, the dataset is collected to
be more difficult than previous datasets, by de-
sign. 

Second, it remedies a problem with SNLI,
3 anc.org/data/masc/corpus/
namely that its contexts (or premises) are very
short, because they were selected from the image
captioning domain.

Following previous observations that models
might exploit spurious biases in NLI hypotheses,
(Gururangan et al., 2018; Poliak et al., 2018), we
conduct a study of the performance of hypothesis-
only models on our dataset. We show that such
models perform poorly on our test sets.

With respect to data generation with na ̈ıve anno-
tators, Geva et al. (2019) noted that models can pick
up on annotator bias, modelling annotator artefacts
rather than the intended reasoning phenomenon.
To counter this, we selected a subset of annotators
(i.e., the “exclusive” workers) whose data would
only be included in the test set. This enables us to
avoid overfitting to the writing style biases of par-
ticular annotators, and also to determine how much
individual annotator bias is present for the main
portion of the data

## Results

Base model performance is low. Notice that the
base model for each round performs very poorly on
that round’s test set.

Simply training on
more “normal NLI” data would not help a model be
robust to adversarial attacks, but our data actively
helps mitigate these.

Continuously augmenting training data does
not downgrade performance. Even though
ANLI training data is different from SNLI and
MNLI, adding it to the training set does not harm
performance on those tasks.

### The effectiveness of adversarial training

First, we sample from
respective datasets to ensure exactly equal amounts
of training data. Table 5 shows that the adversarial
data improves performance, including on SNLI and
MNLI when we replace part of those datasets with
the adversarial data. This suggests that the adver-
sarial data is more data efficient than “normally
collected” data. 

### Stress Test Results

Training on ANLI appears to be particularly useful
for the AT, NR, NG and WO stress tests.

### Hypothesis-only results

The
table shows that hypothesis-only models perform
poorly on ANLI5, and obtain good performance
on SNLI and MNLI.

Hence, this shows that the test sets are so
difficult that state-of-the-art models cannot outper-
form a hypothesis-only prior.

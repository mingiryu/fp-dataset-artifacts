## Hypothesis Only Baselines in Natural Language Inference

a hypothesis-only model,
is able to significantly outperform a majority-
class baseline across a number of NLI datasets.

Our analysis suggests that statistical irregular-
ities may allow a model to perform NLI in
some datasets beyond what should be achiev-
able without access to the context.

## Annotation Artifacts in Natural Language Inference Data

a simple text categorization model can cor-
rectly classify the hypothesis alone in about
67% of SNLI (Bowman et al., 2015) and 53%
of MultiNLI (Williams et al., 2018). 

Indeed, annotation artifacts are not
unique to the NLI datasets, and the danger of such
biases should be carefully considered when anno-
tating new datasets.

Annotation artifacts inflate model perfor-
mance. This is a corollary of the above, since
large portions of the test set can be solved by rely-
ing on annotation artifacts alone

 A similar finding
by Jia and Liang (2017) showed that the perfor-
mance of top question-answering models trained
on SQuAD (Rajpurkar et al., 2016) drops drasti-
cally by introducing simple adversarial sentences
in the evidence. 

## How Much Knowledge Can You Pack Into the Parameters of a Language Model?

fine-tuning pre-trained models to
answer questions without access to any exter-
nal context or knowledge. We show that this
approach scales with model size and performs
competitively with open-domain systems that
explicitly retrieve answers from an external
knowledge source when answering questions

A more difficult variant is “open-domain ques-
tion answering” (Prager, 2006), where the model
can be asked arbitrary context-independent ques-
tions (e.g. well-known facts or historical details).
It is typically assumed that the model can access
an external collection of knowledge when answer-
ing questions (e.g. a structured knowledge base
or unstructured text corpus), but the model is not
given any information about where in the collec-
tion the answer appears.

In one view, this
can be seen as an alternative way to approach
open-domain question answering where instead of
learning to access external knowledge the model
needs to have “memorized” it in order to answer
questions; in another view, this constraint creates
a third and potentially more ambitious variant of
the question answering task.

## Beat the AI: Investigating Adversarial Human Annotation for Reading Comprehension

We find that training on adversarially col-
lected samples leads to strong generalisa-
tion to non-adversarially collected datasets,
yet with progressive performance deteriora-
tion with increasingly stronger models-in-
the-loop.

## Annotation Artifacts Examples


### Lexical

Premise: kid holding handles on two wheeled object
Hypothesis: The kid is riding a bike.
Label: Neutral

SNLI-only: Contradiction
SNLI+ANLI:  Neutral

---

Premise: A cement worker is working on a new sidewalk outside of a clothing store.
Hypothesis: A worker is working on a new sidewalk outside of a restuarant.
Label: Contradiction

SNLI-only: Entailment
SNLI+ANLI:  Contradiction

---

Premise: A man is performing for a group in front of a white house.
Hypothesis: A man performed inside of a gymnasium.
Label: Contradiction

SNLI-only: Entailment   SNLI+ANLI:  Contradiction

---


### Sentence length

Premise: Two women wearing aprons and hairnets look at each other while they reach into metal canisters.
Hypothesis: Two women are working.
Label: Neutral
SNLI-only: Entailment   SNLI+ANLI:  Neutral

---

Premise: Two women wearing aprons and hairnets look at each other while they reach into metal canisters.
Hypothesis: Two women are working.
Label: Neutral
SNLI-only: Entailment   SNLI+ANLI:  Neutral


### Numeric

Premise: Two children play in the snow by the side of the road.
Hypothesis: Toddles are roasting marshmallows.
Label: Contradiction

SNLI-only: Neutral   SNLI+ANLI:  Contradiction

---

Premise: The Centralia Massacre was an incident during the American Civil War in which twenty-four unarmed Union soldiers were captured and executed at Centralia, Missouri on September 27, 1864 by the pro-Confederate guerrilla leader William T. Anderson. Future outlaw Jesse James was among the guerrillas.
Hypothesis: The Centralia Massacre was the execution of 25 Union soldiers during the American Civil War.
Label: Contradiction

SNLI-only: Entailment   SNLI+ANLI:  Contradiction


### Negation 

Premise: The gentleman is speaking while the others are listening.
Hypothesis: The man is not talking.
Label: Contradiction
SNLI-only: Contradiction   SNLI+ANLI:  Contradiction

---

Premise: 3 women run in a marathon with the crowd in the background, one with the label Galina and another the label Inga, and the 3rd running close behind them in blue.
Hypothesis: There are no women running.
Label: Contradiction
SNLI-only: Contradiction   SNLI+ANLI:  Contradiction

---

Premise: Two men working on the roof of an apartment building with a nice looking skyline behind them.
Hypothesis: Two men not working on the roof of an apartment building
Label: Contradiction
SNLI-only: Contradiction   SNLI+ANLI:  Contradiction
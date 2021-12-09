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
We used text labels (Entailment, Contradiction, Neutral) rather than numerical labels (0, 1, 2) as recommended by the GPT-3 paper.

Since the quality of task description and the structure of examples were pertinent to the performance of the few-shot learning, we felt it was difficult to separate prompt artifacts from dataset artifacts. 

On the other hand, we realized that fine-tuning was necessary for NLI early on and were able to establish a baseline when we were still struggling with QA. Also, we were discouraged to fine-tune for QA due to the much higher estimated cost of training on QA datasets. As a result, we ended up not pursuing the QA task any further.

Early on in our NLI task, we were met with the text generation issue similar to the aforementioned QA zero-shot experiment. We first thought this was due to the difficulty of NLI in general. In order to test whether this was a task specific issue, we performed the same few-shot learning experiment on the BoolQ dataset but phrased it as a binary classification of “Yes” or “No”. Surprisingly, GPT-3 wasn't able to generate any text even though the task structure was simpler than the traditional SQuAD dataset.

We were unable to get reliable results from GPT-3 with both zero-shot and few-shot learning regardless of the number of examples we threw at it. Similar to zero-shot SQuAD, GPT-3 generates empty text even for fairly sophisticated prompts. However, removing the stop hyperparameter (instructing the model to stop generating text when it encounters a newline) did alleviate the empty text issue, but the generated text were simply a continuation of the examples (premises and hypotheses) rather than one of the labels.
At first, we suspected that NLI was too difficult of a task for GPT-3, which would have made sense if the model was generating text and getting it wrong. Then, our findings with BoolQ dataset suggested that this wasn’t a task specific issue.

Similar to the BoolQ dataset, we suspect that GPT-3 is not well suited for complex classification tasks such as NLI.

With BoolQ, we fine-tuned the entire training dataset, which gave us the reported validation accuracy of 85.7798. We only considered fine-tuning BoolQ as an ablation study to verify that our fine-tuning approach was sound in a task other than NLI. Given that the published few-shot performance of GPT-3 is 76.4, the accuracy of 85.7798 was sufficiently high.

Clark, Christopher, Kenton Lee, Ming-Wei Chang, Tom Kwiatkowski, Michael Collins and Kristina Toutanova. “BoolQ: Exploring the Surprising Difficulty of Natural Yes/No Questions.” ArXiv abs/1905.10044 (2019): n. pag.

We tried to rule out other potential issues and attempted many different prompt structures such as the tweet classifier, but we were not able to make it work reliably. As a result, we decided to focus on fine-tuned models. 

Due to the nature of OpenAI GPT-3 being a black box, we weren’t able to use adversarial attack tools such as CheckList [Ribeiro et al.] and TextAttack [Morris et al.].

At the time of this writing, fine-tuning on OpenAI's GPT-3 models is limited to 2.5M tokens for the training and validation datasets. As a result, we weren't able to fine-tune with the entire datasets or rounds for most of the datasets.

## Draft

As shown in Figure 2, our result from hypothesis-only experiment suggests that statistical irregularities and dataset artifacts in SNLI seem to allow GPT-3 to achieve suspiciously high performance without having access to the premise. Furthermore, we observed numerous instances of annotation artifacts such as lexical choice and negation that were presented by Gururangan et al. [Table #]. In Table #, the first example is one of the many instances of entailed hypothesis with a generic word "animal". The second example demonstrates an instance of basic negation ("not") with contradicted hypothesis.

For instance, Table # showcases a few examples where fine-tuning with ANLI have resulted in improved robustness over the SNLI-only model. The first example demonstrates an instance of lexical inference for generic words and the second example demonstrates an instance of numerical reasoning. For lexical inference, SNLI-only model fails to recognize that "individuals" and "men" are synonymous. In numerical reasoning, SNLI-only model fails to recognize that "twenty-four unarmed Union solders" contradicts "25 Union solders".

**Instance of Generic Lexical Choice (animal)**
Premise: A white duck expanding its wings in the water.
Hypothesis: There is one animal in this picture.
Label: Entailment
SNLI-only: Entailment SNLI+ANLI:  Entailment

**Instance of Negation (not)**
Premise: Two men working on the roof of an apartment building with a nice looking skyline behind them.
Hypothesis: Two men not working on the roof of an apartment building
Label: Contradiction
SNLI-only: Contradiction SNLI+ANLI: Contradiction

**Lexical Inference (individual == men)**
Premise: Two individuals dressed up like animals are posing for the camera.
Hypothesis: Two men dressed as basketball players are running.
Label: Contradiction
SNLI-only: Neutral SNLI+ANLI: Contradiction

**Numerical Reasoning (twenty-four != 25)**
Premise: The Centralia Massacre was an incident during the American Civil War in which twenty-four unarmed Union soldiers were captured and executed at Centralia, Missouri on September 27, 1864 by the pro-Confederate guerrilla leader William T. Anderson. Future outlaw Jesse James was among the guerrillas.
Hypothesis: The Centralia Massacre was the execution of 25 Union soldiers during the American Civil War.
Label: Contradiction
SNLI-only: Entailment SNLI+ANLI:  Contradiction


With fine-tuning, we found that augmenting the adversarial datasets did improve the test score on the adversarial set, but did not improve the test score on the standard set. However, the test score on the standard set only dropped by 0.42 whereas the test score on the adversarial set increased by 25.15. This trade off seemed favorable considering that the SNLI-only model was not doing much better than random guesses.
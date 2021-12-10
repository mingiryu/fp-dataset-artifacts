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
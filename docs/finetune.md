## SNLI (old)

id: ft-liaJqXchRH2a0b7InmAZuvEG
model: curie:ft-user-5hzndcnnszukksvrzrlnjn8l-2021-12-02-03-14-04
results: file-fODaqo7g6sIEmjKDynpQUfJq

-   F1: 0.901942

> Note: Only 10% of the training dataset was used due to the token limit.

params:

```py
training_file='file-pD1lpBznzyfCVq8U8rOV58RE',
validation_file='file-QC8NTdPW56lhbaDtuxvofGLj',
model='curie',
n_epochs=4,
compute_classification_metrics=True,
classification_n_classes=3
```

> Note: Trained on labels without `\n` ending token.

## BoolQ

id: ft-9ZmeSNYkAUhZEmXkoiigSMdJ
model: curie:ft-user-5hzndcnnszukksvrzrlnjn8l-2021-12-05-02-38-38
results: file-7mMJchteVwqmaih6gj199hXk

-   F1: 0.889259
-   accuracy: 0.857798

params:

```py
training_file='file-gJIlaEZ4vKpcMs8kOd8Tzifx',
validation_file='file-MahHYpnc6hjHw2EZQ1CH3jOw',
model='curie',
n_epochs=4,
compute_classification_metrics=True,
classification_positive_class='Yes',
classification_n_classes=2
```

> Note: Trained on labels without `\n` ending token.

## ANLI (Round 1)

id: ft-uYZ4vdMlvmoLVuycheBpvM7U
model: curie:ft-user-5hzndcnnszukksvrzrlnjn8l-2021-12-05-03-26-14
results: file-8d5IsoqvC86h9bihVABgKQSP

-   F1: 0.550766

eval:

-   F1: 0.56398
-   Accuracy: 0.566

> Note: All rounds (1,2,3) training data is too big. This is only for round 1.

params:

```py
training_file='file-FkO4WnaoNWQjODh96npgZ6Kr',
validation_file='file-cZYCbTSEyYvGpQ1lW2kB41pg',
model='curie',
n_epochs=4,
compute_classification_metrics=True,
classification_n_classes=3
```

## SNLI

id: ft-8brkU9ndEMQxJrA6PuE8CRdS
model: curie:ft-user-5hzndcnnszukksvrzrlnjn8l-2021-12-07-01-05-46
results: file-yn9cN1uhKr0uOhW82V6GJbVL

-   Accuracy: 0.8896
-   F1: 0.88974

eval:

-   Accuracy: 0.913
-   F1: 0.9133002519868192

params:

```py
{
    "batch_size": 2,
    "classification_n_classes": 3,
    "compute_classification_metrics": true,
    "learning_rate_multiplier": 0.2,
    "n_epochs": 4,
    "prompt_loss_weight": 0.1,
    "use_packing": true
}
```

training_file: file-vEGR3mzOq5XylMgqV5zjuFv5
validation_file: file-sCWXvJkbPPdRW4hLXGutd56

## Ablation SNLI vs ANLI

### SNLI

id: ft-a0nNphtyncMOu5XmSLlUkvDz
model: curie:ft-user-5hzndcnnszukksvrzrlnjn8l-2021-12-07-03-02-36
results: file-xCIoJMXr89SuZRVvTcI1yDbg

-   F1: 0.888082
-   Accuracy: 0.8877

eval SNLI:

-   F1: 0.8935001649479813
-   Accuracy: 0.893

eval ANLI:

-   F1: 0.3350202931874234
-   Accuracy: 0.337

params:

```py
{
    "batch_size": 1,
    "classification_n_classes": 3,
    "compute_classification_metrics": true,
    "learning_rate_multiplier": 0.2,
    "n_epochs": 4,
    "prompt_loss_weight": 0.1,
    "use_packing": true
}
```

### ANLI

id: ft-rDeH2hvXBGo0ZlmsxEKbvkP4
model: curie:ft-user-5hzndcnnszukksvrzrlnjn8l-2021-12-07-02-15-48
results: file-T2uIh00Sl5pTmPkmAoCfnBwl

-   F1: 0.852107
-   Accuracy: 0.852

eval SNLI:

-   F1: 0.8892603877796055
-   Accuracy: 0.889

eval ANLI:

-   F1: 0.5864711946043328
-   Accuracy: 0.586

params:

```py
{
    "batch_size": 2,
    "classification_n_classes": 3,
    "compute_classification_metrics": true,
    "learning_rate_multiplier": 0.2,
    "n_epochs": 4,
    "prompt_loss_weight": 0.1,
    "use_packing": true
}
```

## SNLI

id: ft-liaJqXchRH2a0b7InmAZuvEG
model: curie:ft-user-5hzndcnnszukksvrzrlnjn8l-2021-12-02-03-14-04

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


## BoolQ

id: ft-9ZmeSNYkAUhZEmXkoiigSMdJ
model: curie:ft-user-5hzndcnnszukksvrzrlnjn8l-2021-12-05-02-38-38

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

## ANLI

id: ft-uYZ4vdMlvmoLVuycheBpvM7U

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
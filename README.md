# semtab2023-CQA [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/bennokr/semtab2023-CQA/HEAD)
Column-Qualifier Annotation (CQA) task at SemTab @ ISWC2023

## Task description
The goal of this task is to predict both main properties and qualifiers from Wikidata for n-ary relations that are expressed by three table columns. For example, given the following table about Oscar nominations:


| 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| Academy Award for Best Actor | 2000(73rd) | Russell Crowe | Gladiator | Maximus Decimus Meridius |
| Academy Award for Best Actor | 2000(73rd) | Javier Bardem | Before Night Falls | Reinaldo Arenas |
| Academy Award for Best Actor | 2000(73rd) | Ed Harris | Pollock | Jackson Pollock |


the main property "nominated for" ([P1411](https://www.wikidata.org/wiki/Property:P1411)) holds between columns **2** and **0** (the *subject* and *object column*), which is expanded upon with the qualifier "for work" ([1686](https://www.wikidata.org/wiki/Property:P1686)) in column **3** (the *qualifier column*). This property-qualifier pair describes the n-ary relation that holds between these three columns.

In this repository you will find an example evaluation dataset (`simple`) with a baseline, and a full dataset for the SemTab2023 challenge (`full-semtab2023-CQA.zip`) which includes training data. In both datasets, the file `task.csv` specifies which columns in each table should be annotated with properties and qualifiers. Submissions must fill in the empty cells, and will be evaluated on their accuracy of predicting the correct property-qualifier pair (see `evaluation.py`).
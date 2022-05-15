# Annotator-Bias-in-Argmin



The 600 re-annotated sentences are from the UKP Sentential Argument Mining Corpus (Stab et al., 2018). To retrieve the sentences, firstly request the data from the authors (https://tudatalib.ulb.tu-darmstadt.de/handle/tudatalib/2345).

 annotations/extract\_sentences.py shows how to easily find the correct sentences from the UKP data and add them to a dataframe with our annotations from prolific (the same method can be applied for the mTurk annotations).

Data columns:
"Input.set": The set (either val or train set) that the sentence belongs.
"Input.ID_in_set": The index of the enumerated sentences within the specified set.
...

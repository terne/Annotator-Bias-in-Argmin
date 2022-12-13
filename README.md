# Annotator-Bias-in-Argmin



The 600 re-annotated sentences are from the UKP Sentential Argument Mining Corpus (Stab et al., 2018). To retrieve the sentences, firstly request the data from the authors (https://tudatalib.ulb.tu-darmstadt.de/handle/tudatalib/2345).

 annotations/extract\_sentences.py shows how to easily find the correct sentences from the UKP data and add them to a dataframe with our annotations from prolific (the same method can be applied for the mTurk annotations).

Data columns:

"Input.set": The set (either val or train set) that the sentence belongs.

"Input.ID_in_set": The index of the enumerated sentences within the specified set.

"guideline": The ID of the annoation guideline given to the annotator (1 of 4).

"sentence_id": New sentence ID.

"topic": The topic of the sentence.

"label": The label provided by the annotator.

"age": The self-reported age of the annotator.

"education": The self-reported highest completed education of the annotator.

"ethnicity": The self-reported ethnic identity of the annotator (can include several).

"pol_alignment": The left-right political alignment of the annotator.

"english_proficiency": The self-reported english-speaking ability of the annotator.

"second_lang": Whether the annotor has a second language (speaks other languages than English at home).

"binary_label": The label provided by the annotator, but binarised (argument for or against topic=1, not an argument=0).

"pol": Whether the annotator identifies as Conservative or Liberal.

"group": The group ID defined by gender and pol.

"gender": The self-reported gender of the annotator.

"orig_labels": The label of the sentence in the original dataset (Stab et al., 2018).

"orig_labels_binary": Binaried version of the original label.


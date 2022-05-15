import pandas as pd
import codecs

pro = pd.read_csv("prolific_responses.csv")
set = pro["Input.set"]
id = pro["Input.ID_in_set"]
topic = pro["topic"]

cloning_file = "cloning.tsv"
wage_file = "minimum_wage.tsv"


data1 = codecs.open(cloning_file, "r", "utf-8").read().split("\n")
data1 = [data1[i].split("\t") for i in range(len(data1)-1)]
c_df = pd.DataFrame(data1[1:], columns=data1[0])

data2 = codecs.open(wage_file, "r", "utf-8").read().split("\n")
data2 = [data2[i].split("\t") for i in range(len(data2)-1)]
w_df = pd.DataFrame(data2[1:], columns=data2[0])


sents = []
for i,j,t in list(zip(id,set,topic)):
    if t == "cloning":
        s = c_df[c_df.set==j].iloc[i].sentence
        sents.append(s)
    else:
        s = w_df[w_df.set==j].iloc[i].sentence
        sents.append(s)

assert len(sents)==9600

pro["sentence"] = sents
pro.to_csv("collected.csv")

import pandas as pd
import numpy as np
from random import randint

lang = pd.read_csv("/Users/Shane/Desktop/DataHack2018/datasets/sentiment/evaluation/sentiment_final_eval.csv",encoding="utf8")

lang["label"]=-1

out = lang[['label','id']].copy()



for x in range(0,len(lang)):
    y = randint(0,1)
    lang.set_value(x,"label",y)



out = lang[['label','id']].copy()
out.set_index('id',inplace=True)
out.to_csv("sentiment_final_results.csv", encoding='utf-8')

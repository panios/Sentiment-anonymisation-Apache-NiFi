import pandas as pd
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
from sklearn_pandas import DataFrameMapper
from sklearn.preprocessing import LabelEncoder
from pandas import DataFrame # to make some test data
from utils import best_fit_distribution
from utils import plot_result
import sys
import numpy as np

# Encode/Decode issues: escape json

neg_batch =sys.argv[1].replace('[', '').replace(']', '').replace('"', '')
pos_batch =sys.argv[2].replace('[', '').replace(']', '').replace('"', '')
nutral_batch =sys.argv[3].replace('[', '').replace(']', '').replace('"', '')
compound_batch =sys.argv[4].replace('[', '').replace(']', '').replace('"', '')
location_batch =sys.argv[5].replace('[', '').replace(']', '').replace('"', '')
timestamp_batch =sys.argv[6].replace('[', '').replace(']', '').replace('"', '')
uuid_batch =sys.argv[7].replace('[', '').replace(']', '').replace('"', '')



compound = list(np.float_(compound_batch.split(',')))
pos = list(np.float_(pos_batch.split(',')))
neg = list(np.float_(neg_batch.split(',')))
neu = list(np.float_(nutral_batch.split(',')))
geo = list((location_batch.split(',')))
timestamp = list((timestamp_batch.split(',')))
uuid = list((uuid_batch.split(',')))

Sentiment = {'Compound': compound, 'Negative': neg,'Neutral': neu,'Positive': pos, 'Locations': geo, "Timestamp": timestamp, "Uuid": uuid}


df = DataFrame(Sentiment,columns= ['Compound','Negative','Neutral','Positive'])
df_meta = DataFrame(Sentiment,columns= ["Timestamp","Locations", "Uuid"])



#print(" ###some real data from flowfiles")
#print (df)
#print(" ####remove != floats")
#print (df_meta)


continuous = []
for c in list(df):
    col = df[c]
    nunique = col.nunique()
    if nunique > 1:
        continuous.append(c)

#print (continuous)


best_distributions = []
for c in continuous:
    data = df[c]
    best_fit_name, best_fit_params = best_fit_distribution(data, "auto")
    best_distributions.append((best_fit_name, best_fit_params))

#print (best_distributions)

def generate_like_df(df,continuous_cols, best_distributions, n, seed=0):
    np.random.seed(seed)
    d = {}
    for c, bd in zip(continuous_cols, best_distributions):
        dist = getattr(scipy.stats, bd[0])
        d[c] = dist.rvs(size=n, *bd[1])
    return pd.DataFrame(d, columns=continuous_cols)


gendf = generate_like_df(df,continuous, best_distributions, n=10)

#print (gendf)

#print(" ###Good randomised data")
final = gendf.join(df_meta)

#print ('''''''''''''')

print(final.to_string())

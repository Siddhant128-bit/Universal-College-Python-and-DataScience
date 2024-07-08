import pandas as pd
import numpy as np
import pickle

from sklearn import tree

def numerize(x):
    if x=='sunny' or x=='hot' or x=='high' or x=='weak' or x=='no':
        x=0
    elif x=='overcast' or x=='mild' or x=='normal' or x=='strong' or x=='yes':
        x=1
    elif x=='rain' or x=='cool':
        x=2
    return x
def numerize_all(dataset):
    dataset['outlook']=dataset['outlook'].apply(numerize)
    dataset['temp']=dataset['temp'].apply(numerize)
    dataset['humidity']=dataset['humidity'].apply(numerize)
    dataset['wind']=dataset['wind'].apply(numerize)
    dataset['play']=dataset['play'].apply(numerize)
    return dataset

def lower_case(x):
    x=x.lower()
    return x

def lower_case_all(dataset):
    dataset['outlook']=dataset['outlook'].apply(lower_case)
    dataset['temp']=dataset['temp'].apply(lower_case)
    dataset['humidity']=dataset['humidity'].apply(lower_case)
    dataset['wind']=dataset['wind'].apply(lower_case)
    dataset['play']=dataset['play'].apply(lower_case)
    return dataset

if __name__=="__main__":
    dataset=pd.read_csv('Dataset\play_tennis.csv')
    dataset=lower_case_all(dataset)
    
    dataset=numerize_all(dataset)
    
    #print(dataset)
    X=np.array(dataset.drop(['play','day'],True))
    Y=np.array(dataset['play']).reshape(-1,1)
    model=tree.DecisionTreeClassifier()
    model=model.fit(X,Y)
    pickle.dump(model,open('decision_tree.model','wb'))

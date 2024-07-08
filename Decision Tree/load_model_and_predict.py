import train_tree as t_t
import pickle

def convert_to_text(y):
    if y[0]==0:
        y='No'
    else: 
        y='Yes'
    
    return y


if __name__=='__main__':
    model=pickle.load(open('decision_tree.model','rb'))
    parameters=['Outlook','Temperature','Humidity','Wind']
    inputs=[]
    for i in parameters: 
        inputs.append(input('Enter value for '+i+': '))
    
    inputs=[[t_t.numerize(i.lower()) for i in inputs]]
    y=convert_to_text(model.predict(inputs))

    print(y)
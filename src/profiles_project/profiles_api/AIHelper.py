# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 22:04:08 2017

@author: saramine
"""
import keras
from keras.models import Sequential, model_from_json
import numpy as np
import pandas as pd
from keras.layers import Dense
from sklearn.feature_extraction.text import CountVectorizer
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from keras import backend as K
from keras.models import load_model
import os
import importlib




class NeuralNetworks(object):

    classifier1 = ''
    cv=''
    decoder=''
    out_mat=''
    x_length=''
    y_length=''

    def __init__(self):
        self.classifier1 = self.getStaticClassifier()
        self.set_keras_backend("theano")

    def set_keras_backend(self,backend):
        if K.backend() != backend:
            os.environ['KERAS_BACKEND'] = backend
            importlib.reload(K)
            assert K.backend() == backend



    def getClassifier(self,**kwargs):
        return getStaticClassifier()

    def getRuntimeCV(self):
        dataset= pd.read_csv(filepath_or_buffer='/vagrant/src/profiles_project/profiles_api/InitData.csv')
        corpus=[]

        for i in range(0,len(dataset['Input'])):
            infeed = self.processRow(dataset['Input'][i])
            corpus.append(infeed)

        cv= CountVectorizer(max_features=1500)
        cv.fit_transform(corpus).toarray()
        return cv


    def intialNetwork(self,**kwargs):


        dataset= pd.read_csv(filepath_or_buffer='/vagrant/src/profiles_project/profiles_api/InitData.csv')

        corpus=[]

        for i in range(0,len(dataset['Input'])):
            infeed = self.processRow(dataset['Input'][i])
            corpus.append(infeed)



        X= self.getCV(corpus)

        y= dataset.iloc[:,1].values

        y, pp =self.buildDecoder(y)

        output= np.append(X,y,axis=1)




        # Initialising the ANN
        classifier = Sequential()

        # Adding the input layer and the first hidden layer
        classifier.add(Dense(output_dim = 12, init = 'uniform', activation = 'relu', input_dim = len(X[0,:])))

        # Adding the second hidden layer
        classifier.add(Dense(output_dim = 12, init = 'uniform', activation = 'relu'))

        # Adding the third hidden layer
        classifier.add(Dense(output_dim = 12, init = 'uniform', activation = 'relu'))

        # Adding the output layer
        classifier.add(Dense(output_dim = len(y[0,:]), init = 'uniform', activation = 'sigmoid'))

        classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

        classifier.fit(X, y, batch_size = 20, nb_epoch = 5000)

        model_json = classifier.to_json()
        with open("model.json", "w") as json_file:
            json_file.write(model_json)

        classifier.save_weights("model.h5")

        return classifier


    def getStaticClassifier(self):
        json_file= open('model.json','r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights('model.h5')
        return loaded_model


    def getCV(self,corpus, **kwargs):

        cv= CountVectorizer(max_features=1500)
        temp = cv.fit_transform(corpus).toarray()
        self.cv=cv
        return temp

    def getinputEncoder(self):
        return self.cv

    def processRow(self,row,**kwargs):


        stem= PorterStemmer()

        infeed = re.sub('[^a-zA-Z]',' ',row)
        infeed= infeed.lower()
        infeed = infeed.split()
        infeed = [stem.stem(word) for word in infeed if not word in set(stopwords.words('english'))]
        infeed = ' '.join(infeed)
        return infeed

    def processOutput(self,pred_value, **kwargs):
        max_val=0
        max_ind=0

        dataset= pd.read_csv(filepath_or_buffer='/vagrant/src/profiles_project/profiles_api/InitData.csv')
        y= dataset.iloc[:,1].values

        y_en, decoder1 = self.buildDecoder(y)

        for r in range(0,len(pred_value[0,:])):
            temp = pred_value[0,r]
            if(temp>max_val):
                max_val=temp
                max_ind=r

        if(max_val>0.5):
            return decoder1[max_ind]
        else:
            return "sorry, didnt get you there"

    def buildDecoder(self,array,**kwargs):



        labelencoder_y = LabelEncoder()

        y_lbl = labelencoder_y.fit_transform(array)

        onehotencoder = OneHotEncoder(categorical_features = [0])
        y_en = onehotencoder.fit_transform(y_lbl.reshape(-1,1)).toarray()

        pred= [0]*len(y_en[0,:])

        for q in range(0,len(pred)):
            for r in range(0,len(y_en[:,0])):
                if(y_en[r,q]==1):
                    pred[q] = array[r]
                    break

        self.decoder = pred

        return y_en,pred

    def getPred(self,*kwargs):
        return self.decoder

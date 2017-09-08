# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 22:03:50 2017

@author: saramine
"""
from . import AIHelper

class demoNetwork(object):


    def getResponse(self,message):

        startNetwork = AIHelper.NeuralNetworks()
        classifier = startNetwork.getStaticClassifier()
        countVector = startNetwork.getRuntimeCV()
        temp = startNetwork.processRow(message)
        temp1= []
        temp1.append(temp)
        X_in = countVector.transform(temp1).toarray()

        y_pred= classifier.predict(X_in)

        outcome = startNetwork.processOutput(y_pred)
        return outcome

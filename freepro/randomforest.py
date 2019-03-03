#Data preprocessing

import matplotlib.pyplot as plt
#importing libraries
import numpy as np
import pandas as pd
#from sklearn.preprocessing import Imputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

class RF():
    def train1(self,www,per):
        #importing dataset
        self.dataset=pd.read_csv(www)
        #taking feature vectors columns only 
        self.f_v=self.dataset.iloc[:,:-1].values
        #taking the corresponding class of the feature vectors
        self.val1=pd.DataFrame(self.dataset.iloc[:,4].values)

        self.f_train,self.f_test,self.v_train,self.v_test=train_test_split(self.f_v,self.val1,test_size=float(per),random_state=0)


        self.classifier=RandomForestClassifier(n_estimators=10,criterion='entropy',random_state=0) 
        self.classifier.fit(self.f_train,self.v_train)
        #prediction
        self.y_pred=self.classifier.predict(self.f_test)
        self.y_pred=pd.DataFrame(self.y_pred)

        #confusion matrix for our understanding and calculating accuracy
        from sklearn.metrics import confusion_matrix
        self.cm=confusion_matrix(self.v_test[:],self.y_pred[:])
        self.accuracy=((self.cm[0,0]+self.cm[1,1]+self.cm[2,2])*100)/len(self.v_test)
        return "accuracy of the Random Forest classifier is : "+str(self.accuracy)

    def checkrf(self,sl,sb,pl,pb):
        self.sl1=float(sl)
        self.sb1=float(sb)
        self.pl1=float(pl)
        self.pb1=float(pb)
        self.ev=[[self.sl1,self.sb1,self.pl1,self.pb1]]
        self.yp=self.classifier.predict(self.ev)
        return self.yp[0]

    def anrf(self,ww):
        self.dataset=pd.read_csv(ww)
        self.f_v=self.dataset.iloc[:,:].values
        self.y_pred=self.classifier.predict(self.f_v)
        cse,cvi,cve=0,0,0
        print(self.y_pred)
        for i in self.y_pred:
            if(i=="Iris-setosa"):
                cse+=1
            elif(i=="Iris-versicolor"):
                cve+=1
            elif(i=="Iris-virginica"):
                cvi+=1
            else:
                print("wrong")
        print(cse,cve,cvi)
        label=["Iris-setosa","Iris-versicolor","Iris-virginica"]
        noc=[cse,cve,cvi]
        index = np.arange(len(label))
        plt.figure()
        plt.bar(index, noc)
        plt.xlabel('classes', fontsize=10)
        plt.ylabel('No of flowers', fontsize=10)
        plt.xticks(index, label, fontsize=10, rotation=30)
        plt.title('count of each class from RF')
        plt.show()
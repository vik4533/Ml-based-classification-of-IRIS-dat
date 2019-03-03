#Data preprocessing
import matplotlib.pyplot as plt
#importing libraries
import numpy as np
import pandas as pd
#from sklearn.preprocessing import Imputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder,OneHotEncoder 
classifier=0
#importing dataset


class KNN1():
    def reohe(self,ypred):
        self.xy=[]
        for i in ypred:
            if(i[2]==1.0):
                self.xy.append("Iris-virginica")
            elif(i[1]==1.0):
                self.xy.append("Iris-versicolor")
            elif(i[0]==1.0):
                self.xy.append("Iris-setosa")
        return self.xy

    def train(self,www,per):
        self.dataset=pd.read_csv(www)
        #taking feature vectors columns only 
        self.f_v=self.dataset.iloc[:,:-1].values
        #taking the corresponding class of the feature vectors
        self.val1=pd.DataFrame(self.dataset.iloc[:,4].values)

        #taking care of missing values(Here in our dataset there are no missing values)

        #converting the label(strings) into integers
        #like  Iris-setosa:1  Iris-versicolor:2 Iris-virginica:3
        self.labelencoder_v=LabelEncoder()
        self.val1.values[:,0]=self.labelencoder_v.fit_transform(self.val1.values[:,0])
        self.onehotencoder=OneHotEncoder()
        self.val1=self.onehotencoder.fit_transform(self.val1[:]).toarray()

        #splitting the data into training data and testing data

        self.f_train,self.f_test,self.v_train,self.v_test=train_test_split(self.f_v,self.val1,test_size=float(per),random_state=0)

        #feature scaling

        # self.sc=StandardScaler()
        # self.f_train=self.sc.fit_transform(self.f_train)
        # self.f_test=self.sc.fit_transform(self.f_test)

        #K nearest neighbours classifier -- fitting it to the training data
        self.classifier=KNeighborsClassifier(n_neighbors=5,metric='minkowski',p=2) #euclidien distance
        self.classifier.fit(self.f_train,self.v_train)
        #prediction
        self.y_pred=self.classifier.predict(self.f_test)

        #function to reverse one hot encoder 
        
        #calling reverse hot encoder on test data and original data
        self.y_pred=self.reohe(self.y_pred)
        self.v_test=self.reohe(self.v_test)

        #confusion matrix for our understanding and calculating accuracy
        from sklearn.metrics import confusion_matrix
        self.cm=confusion_matrix(self.v_test[:],self.y_pred[:])
        self.accuracy=((self.cm[0,0]+self.cm[1,1]+self.cm[2,2])*100)/len(self.v_test)
        return "accuracy of the KNN classifier is : "+ str(self.accuracy)

    def checkann(self,sl,sb,pl,pb):
        self.sl1=float(sl)
        self.sb1=float(sb)
        self.pl1=float(pl)
        self.pb1=float(pb)
        self.ev=[[self.sl1,self.sb1,self.pl1,self.pb1]]
        self.yp=self.classifier.predict(self.ev)
        print(self.yp)
        if(self.yp[0][2]==1.0):
            return "Iris-virginica"
        elif(self.yp[0][1]==1.0):
            return "Iris-versicolor"
        elif(self.yp[0][0]==1.0):
            return "Iris-setosa"
        else:
            return "wrong prdiction"

    def anknn(self,ww):
        self.dataset=pd.read_csv(ww)
        self.f_v=self.dataset.iloc[:,:].values
        self.y_pred=self.classifier.predict(self.f_v)
        self.ypred=self.reohe(self.y_pred)
        cse,cvi,cve=0,0,0
        print(self.ypred)
        for i in self.ypred:
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
        plt.title('count of each class from KNN')
        plt.show()




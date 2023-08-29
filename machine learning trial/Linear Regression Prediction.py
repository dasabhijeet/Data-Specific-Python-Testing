
# coding: utf-8

# In[66]:


from sklearn import linear_model
import matplotlib.pyplot as plt
height=[[4.0],[4.5],[5.0],[5.2],[5.4],[5.8],[6.1],[6.2],[6.4],[6.8]]
weight=[  42 ,  44 , 49, 55  , 53  , 58   , 60  , 64  ,  66 ,  69]
print("height weight")
for row in zip(height, weight):
    print(row[0][0],"->",row[1])
    
    
plt.scatter(height,weight,color='black')
plt.xlabel("height")
plt.ylabel("weight")
plt.show()


# In[7]:


#PART 2

reg=linear_model.LinearRegression()
reg.fit(height,weight)


# In[8]:


#PART 3


m=reg.coef_[0]
b=reg.intercept_
print("slope=",m, "intercept=",b)


# In[67]:


#PART 4

plt.scatter(height,weight,color='black')
predicted_values = [reg.coef_ * i + reg.intercept_ for i in height]

print(predicted_values)

plt.plot(height, predicted_values, 'b')
plt.xlabel("height")
plt.ylabel("weight")
plt.show()


# In[10]:


#SIMPLER METHOD EASY TO UNDERSTAND#   ---MAIN FILE

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df=pd.read_csv("KwH Bill System.csv")
print("CURRENT DATASET-\n\n",df.head(20))

df=df.head(20)

X=df[['ID']]
Y=df[['RANK']]

model = LinearRegression()
model.fit(X, Y)

#X_predict = [[56], [59], [65]]###
    


X_predict = [[float(input("Enter a value 0<value<=50 condt.:- "))]]  # put the dates of which you want to predict kwh here
Y_predict = model.predict(X_predict)


print("\n\nPREDICTION OUTPUT- \n\n",float(Y_predict))

plt.figure(figsize=(10, 10))
ax = plt.axes()

ax.scatter(X, Y)                                     #Plots point only
ax.plot(X, Y, c='green', linestyle='dashdot')        #Plots the line

#ax.plot(X_predict, Y_predict,color="green")
ax.plot(Y_predict, color='green', marker='D', linestyle='dashdot' ,linewidth=2, markersize=12)
ax.plot(X_predict, color='red', marker='o', linestyle='dashdot' ,linewidth=2, markersize=12)

ax.set_xlabel('ID-IDENTIFICATION')
ax.set_ylabel('RANK')

plt.show()


# In[55]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# x from 0 to 30
x = 30 * np.random.random((20, 1))

# y = a*x + b with noise
y = 0.5 * x + 1.0 + np.random.normal(size=x.shape)

# create a linear regression model
model = LinearRegression()
model.fit(x, y)

# predict y from the data
x_new = np.linspace(0, 30, 100)
y_new = model.predict(x_new[:, np.newaxis])

print(x_new)

# plot the results
plt.figure(figsize=(4, 3))
ax = plt.axes()
ax.scatter(x, y)
ax.plot(x_new, y_new)

ax.set_xlabel('x')
ax.set_ylabel('y')

#ax.axis('tight')


plt.show()


# In[63]:


x=15.90
print(str(x))
print(int(x))
print(float(x))


# In[46]:


#SIMPLER METHOD EASY TO UNDERSTAND#   ---MAIN FILE   V2

#import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

new=0


df=pd.read_csv("KwH Bill System.csv")
print("CURRENT DATASET-\n\n",df.head(20))

df=df.head(20)

X=df[['ID']]
Y=df[['RANK']]

model = LinearRegression()
model.fit(X, Y)

#X_predict = [[56], [59], [65]]###

incs=1
arr=[]
inc=int(input("Enter number of items- "))
for els in range(0,inc):
    print("ITEM",incs)
    arr.append(float(input("Enter items in integer of float- ")))
    incs=incs+1
print("ELEMENTS-\n",arr,", So total elements is- ",inc)


plt.figure(figsize=(10, 10))
ax = plt.axes()
ax.scatter(X, Y)
ax.plot(X,Y , c='green', linestyle='dashdot')  

#FOR PREDICTIONS/OUTPUTS
for incs in range(0,inc):
    X_predict=[[arr[incs]]]
    Y_predict=model.predict(X_predict)
    print("\n\nPREDICTION OUTPUT OF ",arr[incs]," is ",float(Y_predict))
    ax.plot(Y_predict, color='green', marker='D', linestyle='dashdot' ,linewidth=2, markersize=12)
    
#FOR INPUTS
for incs in range(0,inc):
    X_predict=[[arr[incs]]]
    ax.plot(X_predict, color='green', marker='D', linestyle='dashdot' ,linewidth=2, markersize=12)

#FOR INPUT-LINE
st="["
for incs in range(0,inc):
    arr[incs]=str(arr[incs])
    print("THiS- ",arr[incs])
    st=st+"[("+arr[incs]+")], "
st=st+"]"
X_predict = st
ax.plot(X_predict, color='green', marker='D', linestyle='dashdot' ,linewidth=2, markersize=12)
    
    
#ax.plot(X_predict, Y_predict,color="green")

ax.plot(X_predict, color='red', marker='o', linestyle='dashdot' ,linewidth=2, markersize=12)

ax.set_xlabel('ID-IDENTIFICATION')
ax.set_ylabel('RANK')

plt.show()


# In[21]:


n=int(input("Enter N for N x N matrix : "))         #3 here
l=[]                                                #use list for storing 2D array

#get the user input and store it in list (here IN : 1 to 9)
for i in range(n): 
  row_list=[]                                      #temporary list to store the row
  for j in range(n): 
     row_list.append(int(input()))                 #add the input to row list
  l.append(row_list)                               #add the row to the list

print(l)


# In[25]:


a=['1','2','3']
print(a[2])


# In[39]:


import matplotlib.pyplot as plt
X=[([20]),([30])]
ax = plt.axes()
ax.plot(X, color='g', marker='o', linestyle='dashdot' ,linewidth=2, markersize=12)


# In[48]:


print(str(x))


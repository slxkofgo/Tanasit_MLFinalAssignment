#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 02:53:06 2020

@author: macbook
"""

import pandas as pd
import os
import numpy

df = pd.read_csv('/Users/macbook/Desktop/ML with Python/Titanic/titanic_train.csv')

df.head()

#Q.1 What is the total number of people on the titanic and how many of them survived and how many did not?
survive = len(df[df['Survived']==1])
notsurvive = len(df[df['Survived']==0])
print(survive)
print(notsurvive)

#Q.2 How many that survived were female and how many that died were female?
female_survived = len(df[(df.Survived ==1)&(df.Sex == 'female')])
print(female_survived)

female_died = len(df[(df.Survived ==0)&(df.Sex == 'female')])
print(female_died)

#Q.3 How many children were on the titanic, NB: you are a child if age < 17
children = len(df[df['Age']<17])
print(children)

#Q.4 How many children died that were on the ship?
child_die = len(df[(df.Age<17)&(df.Survived==1)])
print(child_die)

#Q.5 How many people had families with them?
family = len(df[(df.SibSp!= 0)|(df.Parch!=0)])
print(family)

#Q.6 What is the ratio of female to male?
gender_ratio = len(df[(df.Sex =='female')])/len(df[(df.Sex == 'male')])
print(gender_ratio)
#Answer: ratio female:male = 54:46

#Q.7 What contributed to the survival of those who survived?
df['Sex']=df.Sex.astype('category')
df.Sex=df.Sex.cat.codes
corr=df.corr(method='pearson')

corr



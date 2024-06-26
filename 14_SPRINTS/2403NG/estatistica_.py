# -*- coding: utf-8 -*-
"""estatistica_.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CPx0gPJOryrctNeL4TAHm0YiztRutEwU
"""

import statistics as st

x=[4,5,6,7,8]
y=[14,25,26,17,8]

#função
def linear_regression(x,y):
  n=len(x)
  media_y=st.mean(y)
  media_x= st.mean(x)
  covariancia=sum((x[i]-media_x)*(y[i]-media_y) for i in range (n))
  variancia=sum((x[i]-media_x)**2 for i in range (n))
  b1=covariancia/variancia
  b0=media_y-b1*media_x
  return b0,b1

#calculo dos coeficientes de regressão
intercept, slop=linear_regression(x,y)

print('O coeficiente de intercepto é:',intercept)

print('O coeficiente de inclinação é:',slope')
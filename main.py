import math
'''Diseñar una función que permita calcular una aproximación de la función logaritmo natural alrededor de 0 para cualquier valor x ∈ R +,utilizando los primeros n términos de la serie de Maclaurin'''

def aproxLogNat(x,n):
  s = 0
  for i in range(0,n+1):
    s += ( 1 / (2*i+1) ) * ((((x**2)-1)/((x**2)+1))**(2*i+1))
  return s

print(str(aproxLogNat(math.e,1000)))
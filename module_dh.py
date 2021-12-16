""" 
 module dh des fonctions personnalisées
"""

def interligne(caractere="-",repet=60):
    print(caractere*repet ) 

i=lambda c, r : print(c*r)

""""
le code ci dessous ne s executera pas lors de l import
le code s excutera en lancant le module_dh.py 
""" 
if __name__ == "__main__":
    i("-_",40)
    i("-=",40)
    interligne("=-",40)


 
    






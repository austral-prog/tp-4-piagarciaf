import math
def line():
    a = float(input ("Ingrese el coeficiente A: ")) #el usario me va a dar un num con decimal
    b = float(input ("Ingerse el coeficiente B: "))
    x1 = float(input ("Ingerse el coeficiente X1: "))
    x2 = float(input ("Ingerse el coeficiente X2: "))
    print (f"El coeficiente A de su ecuación de la recta es: {a}")
    print (f"El coeficiente B de su ecuación de la recta es: {b}")
    print (f"El coeficiente X1 de su ecuación de la recta es: {x1}")
    print (f"El coeficiente X2 de su ecuación de la recta es: {x2}")
    print ("\nPara la siguiente ecuación:")
    print (f"\tY = {a}X + {b}")
    print ("\nDados los siguientes puntos:")
    Y1 = (a*x1 + b)
    Y2 = (a*x2 + b)
    print (f"\tP1 ({x1}, {Y1})")
    print (f"\tP2 ({x2}, {Y2})")
    Dis = math.sqrt((x2-x1)**2 + (Y2-Y1)**2)
    print (f"\nLa distancia entre ellos es: {Dis}")

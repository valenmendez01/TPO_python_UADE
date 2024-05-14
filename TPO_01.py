

# Ingresar una sola vez
b1000 = int(input("Ingrese cantidad de billetes de 1000: "))
b500 = int(input("Ingrese cantidad de billetes de 500: "))
b200 = int(input("Ingrese cantidad de billetes de 200: "))
b100 = int(input("Ingrese cantidad de billetes de 100: "))

# Bucle
dinero = int(input("Ingrese la cantidad de dinero que quiere retirar: "))
total = b1000 + b500 + b200 + b100
while dinero != -1:
    if total > dinero and dinero % 100 == 0 and dinero % 10 == 0:
        # Calculo billetes
        mil = dinero // 1000
        dinero = dinero % 1000
        b1000restante = b1000 - mil
        
        quinientos = dinero // 500
        dinero = dinero % 500
        b500restante = b500 - quinientos
        
        doscientos = dinero // 200
        dinero = dinero % 200
        b200restante = b200 - doscientos
        
        cien = dinero // 100
        dinero = dinero % 100
        b100restante = b100 - cien
        
        if b1000restante < 0 and 

        dinero = int(input("Ingrese la cantidad de dinero que quiere retirar: "))
    else:
        print ("Error billetes insuficientes; ingrese otra cantidad: ")

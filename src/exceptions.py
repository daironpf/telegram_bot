### Exception Handling
'''
try:
    #code in this block if things go well
except:
    #code in this block run if things go wrong
else
    # No exceptions ? Run this code.
finally:
    # Always run this code
'''

# Example:
n1 = 5
n2 = "10"

# try except
print("Ejemplo 1")
try:
    print(n1 + n2)
    print("No hay Errores")
except:
    # Se ejecuta si ocurre algun error
    print("Se ha producido un error")
    
# try except else
print("Ejemplo 2")
n3 = 10
try:
    print(n1 + n3)
    print("No hay Errores")
except:
    print("Se ha producido un error")
else:
    # Se ejecuta si dentro del try-except no se produce ningun error
    print("La ejecución continua correctamente")

# try except alse finally
print("Ejemplo 3")
try:
    print(n1 + n2)
    print("No hay Errores")
except:
    print("Se ha producido un error")
else:
    # Se ejecuta si dentro del try-except no se produce ningun error
    print("La ejecución continua correctamente")
finally:
    # Siempre se ejecuta
    print("La ejecucion continua")
    
# Exceptiones por tipo, por valor
print("Ejemplo 4: Captura de Diferentes Errores")
try:
    print(n1 + n2)
    print("No hay Errores")
except TypeError: # Este bloque de except se ejecuta solo si el error producido es TypeError
    print("Se ha producido un error de Tipo")
except ValueError: # Este bloque de except se ejecuta solo si el error producido es ValueError
    print("Se ha producido un error de Valor")
    
print("Ejemplo 5: Captura de la información de la excepcion")
try:
    print(n1 + n2)
    print("No hay Errores")
except ValueError as error: # Este bloque de except se ejecuta solo si el error producido es ValueError.
    print("error")
except Exception as error: # Este bloque se ejecuta genericamente, siempre que alla error y lo capturamos en la variable error.
    print(error)

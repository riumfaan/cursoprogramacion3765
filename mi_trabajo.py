# -*- coding: utf-8 -*-
"""MI TRABAJO.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_KHktzQTvPFc0W26YF1QA1YO6eJ57tdb
"""

print("POR FAVOR REGISTRE LA INFORMACIÓN")
n_identificacion = int(input("\nDigite numero de documento: "))
nombres = input("Registre sus nombres: ")
apellidos = input("Registre sus apellidos: ")
direccion = input("Digite dirección de residencia: ")
telefono = int(input("Digite numero de telefono: "))
edad = int(input("¿Cual es su edad? "))
estado_civil = input("¿Cual es su estado civil? ")
numero_hijos = int(input("¿Cuantos hijos tiene? "))
estatura = float(input("¿Cual es su estatura? "))
f_contrato = input("Indique fecha de contrato: ")
sueldo = float(input("¿Cual es su sueldo basico? "))
dias_laborados = int(input("¿Cuantos dias laborados en el mes? "))
print("\nLa información registrada es la siguiente:")
print("#documento: ",n_identificacion,"\nNombres: "+nombres+"\nApellidos: "+apellidos+"\nDirección: "+direccion+"\nTelefono: ",telefono,"\nEdad :",edad,"\nEstado civil :"+estado_civil+"\nNumero de hijos: ",numero_hijos,"\nEstatura: ",estatura,"\nFecha de contratación: "+f_contrato+"\nSueldo: ",sueldo,"\nDias laborados :",dias_laborados)
print("\nGRACIAS POR REGISTRAR SUS DATOS")
print("\nSUS BENEFICIOS")

if edad > 55:
  bono = (sueldo*5)/100
  total = bono+sueldo
  print("El bono es =${:,.0f} y el total a pagar es=${:,.0f}".format(bono, total))
else:
  print(f"No tiene bono, el total a pagar es=${sueldo:,.0f}")

if estado_civil in "casado" and numero_hijos >=1:
   print("Tienes paseo para diciembre")
else:
   print("No tienes paseo para diciembre")

if sueldo >= 1000000 and sueldo <=1500000:
    total1=(sueldo*2)/100.0
    print("Tu comisión es $",total1)
elif sueldo >= 1500001 and sueldo <=2000000:
    total2=(sueldo*5)/100.0
    print("Tu comisión es $",total2)
else:
  print("No tienes comisión")

if dias_laborados >=20 and sueldo <=1000000:
  print("Tienes bono")
else:
  print("No tienes bono")
# -*- coding: utf-8 -*-
"""Taller1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g1wu_hdBe5hm-Q21SqVTXwvAoiol_rpI
"""

#Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el vendedor desea saber cuánto dinero obtendrá por concepto de comisiones 
#por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

sueldo_base=float(input("Digite sueldo Base: "))
venta_1=float(input("Valor primer venta: "))
venta_2=float(input("Valor segunda venta: "))
venta_3=float(input("Valor tercera venta: "))
comision=(venta_1+venta_2+venta_3)*0.10
total=sueldo_base+comision

print("El total de su pago es: $",total)

#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra.

venta=float(input("Digite por favor el valor de la compra"))
descuento = venta-(venta*0.15)
print("Valor de la compra: $",venta," y el descuento es del 15%. Total a pagar: $",descuento)

#Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. Dicha calificación se compone de tres exámenes parciales.

nota_1 = float(input("Digite la calificación 1: "))
nota_2 = float(input("Digite la calificación 2: "))
nota_3 = float(input("Digite la calificación 3: "))

promedio = round((nota_1 + nota_2 + nota_3)/3, 2)

print(f"El promedio del estudiante es: {promedio}")

#Un maestro desea saber qué porcentaje de hombres y que porcentaje de mujeres hay en un grupo de estudiantes.

no_alumnos=float(input("Cuantos estudiantes?"))
hombres=float(input("Cuantos alumnos?"))
mujeres=float(input("Cuantas alumnas?"))
por_h=(no_alumnos*hombres)/100.0
print("El porcentaje de hombres es:",por_h,"%")
por_m=(no_alumnos*mujeres)/100.0
print("El porcentaje de mujeres es:",por_m,"%")
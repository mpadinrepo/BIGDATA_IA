def calcular_precio_con_iva(precio_sin_iva, iva_por_defecto=21):
    iva = precio_sin_iva * (iva_por_defecto / 100)
    precio_con_iva = precio_sin_iva + iva
    return precio_con_iva
precio_sin_iva = float(input('Ingrese el valor de la factura: '))
iva_ingresado = input('Ingrese el valor del IVA a aplicar (por defecto 21%): ')
if iva_ingresado:
    iva_personalizado = float(iva_ingresado)
else:
    iva_personalizado = 21
total_con_iva = calcular_precio_con_iva(precio_sin_iva, iva_personalizado)
print(f"Total con IVA ({iva_personalizado}%): {total_con_iva}")
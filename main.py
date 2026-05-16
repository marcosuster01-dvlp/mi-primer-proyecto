def saludar(nombre):
    print(f"Hola {nombre}, Bienvenido! Es un placer conocerte.")

saludar("Marcos")

def calcular_salario_neto(salario_bruto, impuesto_pct):
    impuesto = salario_bruto * (impuesto_pct / 100)
    neto = salario_bruto - impuesto
    return round(neto, 2)

print(calcular_salario_neto(1000, 15))
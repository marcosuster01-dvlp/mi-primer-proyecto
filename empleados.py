def calcular_salario_neto(salario_bruto, impuesto_pct):
    impuesto = salario_bruto * (impuesto_pct / 100)
    return round(salario_bruto - impuesto, 2)
def calcular_salario_neto(salario_bruto, impuesto_pct):
    impuesto = salario_bruto * (impuesto_pct / 100)
    return round(salario_bruto - impuesto, 2)

def formatear_nombre(nombre, apellido):
    return f"{apellido.upper()}, {nombre.capitalize()}"

def validar_email(email):
    return "@" in email and "." in email.split("@")[-1]
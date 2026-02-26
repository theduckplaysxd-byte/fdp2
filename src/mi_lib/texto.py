def numero_a_palabras(n):
    if not isinstance(n, int) or n < 0 or n > 999:
        return "Número fuera de rango"
    
    unidades = {
        0: "cero", 1: "uno", 2: "dos", 3: "tres", 4: "cuatro",
        5: "cinco", 6: "seis", 7: "siete", 8: "ocho", 9: "nueve"
    }
    
    especiales = {
        10: "diez", 11: "once", 12: "doce", 13: "trece", 14: "catorce",
        15: "quince", 16: "dieciséis", 17: "diecisiete", 18: "dieciocho", 19: "diecinueve"
    }
    
    decenas = {
        20: "veinte", 30: "treinta", 40: "cuarenta", 50: "cincuenta",
        60: "sesenta", 70: "setenta", 80: "ochenta", 90: "noventa"
    }
    
    veintes = {
        20: "veinte", 21: "veintiuno", 22: "veintidós", 23: "veintitrés",
        24: "veinticuatro", 25: "veinticinco", 26: "veintiséis",
        27: "veintisiete", 28: "veintiocho", 29: "veintinueve"
    }
    
    centenas = {
        100: "cien", 200: "doscientos", 300: "trescientos", 400: "cuatrocientos",
        500: "quinientos", 600: "seiscientos", 700: "setecientos",
        800: "ochocientos", 900: "novecientos"
    }
    
    # Caso 0-9
    if n < 10:
        return unidades[n]
    
    # Caso 10-19
    if 10 <= n < 20:
        return especiales[n]
    
    # Caso 20-99
    if 20 <= n < 100:
        if n in veintes:
            return veintes[n]
        decena = (n // 10) * 10
        unidad = n % 10
        if unidad == 0:
            return decenas[decena]
        return decenas[decena] + " y " + unidades[unidad]
    
    # Caso 100-999
    centena = (n // 100) * 100
    resto = n % 100
    
    if n == 100:
        return "cien"
    
    if resto == 0:
        return centenas[centena]
    
    # Centenas + resto
    if centena == 100:
        resultado = "ciento"
    else:
        resultado = centenas[centena]
    
    if resto < 10:
        return resultado + " " + unidades[resto]
    elif 10 <= resto < 20:
        return resultado + " " + especiales[resto]
    else:
        if resto in veintes:
            return resultado + " " + veintes[resto]
        decena_resto = (resto // 10) * 10
        unidad_resto = resto % 10
        if unidad_resto == 0:
            return resultado + " " + decenas[decena_resto]
        return resultado + " " + decenas[decena_resto] + " y " + unidades[unidad_resto]

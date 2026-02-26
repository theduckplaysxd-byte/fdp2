def ahorcado(palabra):
    """Juego del ahorcado"""
    palabra = palabra.lower()
    
    lista_palabra = list(palabra)
    estado = ["*"] * len(lista_palabra)
    probadas = []
    fallos = 0
    
    def mostrar_progreso():
        print("Palabra:", "".join(estado))
    
    print()
    mostrar_progreso()
    print()
    
    while fallos < 5 and "*" in estado:
        # pedir letra válida
        while True:
            letra = input("Introduce una letra: ").lower()
            if len(letra) == 1 and letra.isalpha():
                break
            print("Entrada no válida, introduce solo una letra")
        
        if letra in probadas:
            print("Ya probaste esa letra\n")
            continue
        
        probadas.append(letra)
        
        if letra in lista_palabra:
            # revelar todas las posiciones donde aparece la letra
            for i, l in enumerate(lista_palabra):
                if l == letra:
                    estado[i] = letra
            print("Acierto")
            mostrar_progreso()
            print()
        else:
            fallos += 1
            print("Fallo\n")
    
    if "*" not in estado:
        print("Ganaste")
    else:
        print("Perdiste")

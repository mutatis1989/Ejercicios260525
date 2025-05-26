# ejercicio3.py

NUM_JUGADORES = 25 # El equipo cuenta con 25 jugadores en su planilla [cite: 17]

# Denominaciones de Costa Rica (colones)
# Basado en el ejemplo [cite: 22] y extendido con otras comunes.
# Ordenadas de mayor a menor para facilitar el cálculo del desglose.
DENOMINACIONES = [
    50000, 20000, 10000, 5000, 2000, 1000, # Billetes
    500, 100, 50, 25, 10, 5 # Monedas
]
# El ejemplo del PDF usa [50000, 20000, 5000, 500, 100, 25] [cite: 22]
# Si se prefiere usar solo las del ejemplo, se puede modificar la lista DENOMINACIONES.

def solicitar_salarios():
    """
    Recibe el salario de cada uno de los futbolistas. [cite: 18]
    """
    salarios = []
    print(f"--- Ingreso de Salarios para los {NUM_JUGADORES} Jugadores ---")
    for i in range(NUM_JUGADORES):
        while True:
            try:
                # Convertimos a float para permitir decimales, aunque los salarios suelen ser enteros.
                # El ejemplo usa 1,845,725, que es un entero. [cite: 21]
                # Para el desglose, es mejor trabajar con la parte entera si el pago es en efectivo
                # y las monedas más pequeñas son de 5 colones.
                # Consideraremos que los salarios se ingresan como montos que pueden ser pagados exactamente.
                salario_str = input(f"Ingrese el salario mensual del jugador {i+1}: ₡")
                salario = float(salario_str.replace(',', '')) # Permitir comas como separadores de miles
                
                if salario >= 0:
                    # Para simplificar el desglose con las denominaciones dadas,
                    # podríamos redondear el salario a la moneda más cercana (ej. múltiplos de 5)
                    # o asumir que los salarios ya están ajustados para pago exacto.
                    # Por ahora, lo tomaremos como viene y el desglose manejará la exactitud.
                    salarios.append(salario)
                    break
                else:
                    print("El salario no puede ser negativo. Intente de nuevo.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número (puede usar comas para miles).")
    return salarios

def calcular_desglose_individual(salario_jugador, nombre_jugador="Jugador"):
    """
    Calcula el desglose de billetes y monedas para un salario específico.
    Retorna un diccionario con la cantidad por cada denominación y el monto restante (si lo hay).
    """
    desglose_actual = {denom: 0 for denom in DENOMINACIONES}
    monto_restante = salario_jugador

    print(f"\n--- Desglose para {nombre_jugador} (Salario: ₡{salario_jugador:,.2f}) ---")
    # Encabezados similares al ejemplo del PDF [cite: 22]
    print(f"{'Denominación':<15}{'Cantidad':<10}{'Monto':<15}")
    print("-" * 40)

    for denom in DENOMINACIONES:
        if monto_restante >= denom:
            cantidad = int(monto_restante // denom)
            if cantidad > 0:
                desglose_actual[denom] = cantidad
                monto_parcial = cantidad * denom
                print(f"₡{denom:<12,.0f}{cantidad:<10}₡{monto_parcial:<14,.2f}")
                monto_restante -= monto_parcial
                monto_restante = round(monto_restante, 2) # Para manejar precisión de flotantes

    print("-" * 40)
    print(f"{'TOTAL PAGADO:':<25} ₡{salario_jugador - monto_restante:<14,.2f}")
    if monto_restante > 0.001: # Un pequeño umbral para residuos
        print(f"ATENCIÓN: Quedó un residuo de ₡{monto_restante:.2f} que no se pudo desglosar con las denominaciones actuales.")
        print("Esto podría requerir ajuste manual o el uso de monedas de menor denominación si existieran y fueran relevantes.")
    
    return desglose_actual

def procesar_pagos_planilla(lista_salarios):
    """
    Procesa los salarios de todos los jugadores, calcula el desglose para cada uno,
    acumula el total de cada denominación y el monto total a retirar.
    """
    monto_total_a_retirar_banco = sum(lista_salarios) # Monto de dinero que se debe retirar del banco [cite: 18]
    total_denominaciones_planilla = {denom: 0 for denom in DENOMINACIONES}

    print(f"\n===================================================")
    print(f"MONTO TOTAL A RETIRAR DEL BANCO: ₡{monto_total_a_retirar_banco:,.2f}")
    print(f"===================================================")

    for i, salario_actual in enumerate(lista_salarios):
        nombre_jugador_actual = f"Jugador {i+1}" # Se puede personalizar si se tuvieran nombres
        # El ejemplo menciona "El jugador 'Luis' gana..." [cite: 21]
        
        desglose_jugador = calcular_desglose_individual(salario_actual, nombre_jugador_actual)
        
        # Acumular la cantidad de cada denominación por todos los jugadores [cite: 23]
        for denom, cantidad in desglose_jugador.items():
            total_denominaciones_planilla[denom] += cantidad
            
    print(f"\n\n--- SUMATORIA TOTAL DE DENOMINACIONES PARA TODA LA PLANILLA ---") # [cite: 24]
    print(f"{'Denominación':<15}{'Cantidad Total':<15}{'Monto Total':<20}")
    print("-" * 50)
    gran_total_verificacion = 0
    for denom in DENOMINACIONES: # Iterar en el orden de las denominaciones
        cantidad_total = total_denominaciones_planilla[denom]
        if cantidad_total > 0: # Solo mostrar si se necesita esta denominación
            monto_total_denom = cantidad_total * denom
            gran_total_verificacion += monto_total_denom
            print(f"₡{denom:<12,.0f}{cantidad_total:<15}₡{monto_total_denom:<19,.2f}")
    print("-" * 50)
    print(f"{'GRAN TOTAL VERIFICACIÓN DESGLOSE:':<30} ₡{gran_total_verificacion:,.2f}")
    
    if abs(gran_total_verificacion - monto_total_a_retirar_banco) > 0.01 * len(lista_salarios): # Permitir pequeña diferencia por jugador debido a redondeos
        print("\nADVERTENCIA: El gran total del desglose no coincide exactamente con el monto total a retirar.")
        print("Esto puede deberse a salarios con fracciones de colones que no pueden pagarse exactamente con las denominaciones disponibles.")
        print("Se recomienda revisar los salarios para asegurar que sean pagables con las monedas existentes (ej. múltiplos de 5).")


def main_ejercicio3():
    print("Bienvenido al Sistema de Cálculo de Planilla Las Tuercas F.C.")
    
    # 1. Recibir salarios
    salarios_jugadores = solicitar_salarios() # El programa debe recibir el salario de cada uno de los futbolistas [cite: 18]
    
    # 2. Procesar pagos: calcular desglose individual, acumular denominaciones y monto total.
    procesar_pagos_planilla(salarios_jugadores)


if __name__ == "__main__":
    main_ejercicio3()
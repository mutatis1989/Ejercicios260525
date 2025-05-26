# ejercicio2.py

NUM_SERVICIOS_DIA = 4
NUM_DIAS_SEMANA = 5
CAPACIDAD_MAX_AUTOBUS = 60

def capturar_pasajeros():
    """
    Captura la cantidad de pasajeros de cada uno de los 4 servicios que se
    realizan al día para los 5 días de la semana.
    Verifica que no se ingrese un valor mayor a 60.
    Utiliza un arreglo de 2 dimensiones.
    """
    pasajeros_semana = [] # Arreglo de 2 dimensiones
    dias_semana_nombres = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"] # Nombres representativos

    for i in range(NUM_DIAS_SEMANA):
        pasajeros_dia_actual = []
        print(f"\n--- Ingresando pasajeros para el día {dias_semana_nombres[i]} ---")
        for j in range(NUM_SERVICIOS_DIA):
            while True:
                try:
                    cantidad = int(input(f"Ingrese pasajeros para el servicio {j+1} del día {dias_semana_nombres[i]}: "))
                    if 0 <= cantidad <= CAPACIDAD_MAX_AUTOBUS: # Se debe verificar que no se ingrese un valor mayor a 60
                        pasajeros_dia_actual.append(cantidad)
                        break
                    else:
                        print(f"Cantidad inválida. Debe estar entre 0 y {CAPACIDAD_MAX_AUTOBUS}.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número entero.")
        pasajeros_semana.append(pasajeros_dia_actual)
    return pasajeros_semana

def promedio_pasajeros_por_dia(pasajeros_semana):
    """
    Muestra el promedio de pasajeros de cada uno de los días.
    """
    print(f"\n--- Promedio de Pasajeros por Día ---")
    dias_semana_nombres = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    for i, pasajeros_dia in enumerate(pasajeros_semana):
        if not pasajeros_dia: # Si no hay datos para un día
            print(f"Día {dias_semana_nombres[i]}: No hay datos de pasajeros.")
            continue
        promedio_dia = sum(pasajeros_dia) / len(pasajeros_dia)
        print(f"Día {dias_semana_nombres[i]}: Promedio de {promedio_dia:.2f} pasajeros.")

def promedio_general_pasajeros(pasajeros_semana):
    """
    Muestra el promedio general de todos los días y todos los servicios.
    """
    suma_total_pasajeros = 0
    cantidad_total_servicios = 0
    for pasajeros_dia in pasajeros_semana:
        suma_total_pasajeros += sum(pasajeros_dia)
        cantidad_total_servicios += len(pasajeros_dia)
    
    if cantidad_total_servicios == 0:
        promedio_total = 0.0
    else:
        promedio_total = suma_total_pasajeros / cantidad_total_servicios
    
    print(f"\n--- Promedio General de Pasajeros ---")
    print(f"El promedio general de pasajeros en la semana es: {promedio_total:.2f}") # El programa debe mostrar el promedio general de todos los días y todos los servicios
    return promedio_total

def mejor_servicio_del_dia(pasajeros_semana):
    """
    Muestra cuál de los 4 servicios durante el día es el mejor
    (en el que se transportan más personas en promedio durante la semana).
    """
    if not pasajeros_semana or not pasajeros_semana[0]:
        print("\nNo hay datos suficientes para determinar el mejor servicio.")
        return

    # Suma de pasajeros para cada uno de los 4 servicios a lo largo de la semana
    pasajeros_totales_por_servicio = [0] * NUM_SERVICIOS_DIA 

    for pasajeros_dia in pasajeros_semana:
        for i in range(min(len(pasajeros_dia), NUM_SERVICIOS_DIA)): # Asegura no exceder el número de servicios
            pasajeros_totales_por_servicio[i] += pasajeros_dia[i]
    
    if not any(pasajeros_totales_por_servicio): # Si todos los servicios tienen 0 pasajeros
        print("\nNo se transportaron pasajeros en ningún servicio.")
        return

    max_pasajeros_servicio = -1
    mejor_servicio_indices = [] # Puede haber empates

    for i in range(NUM_SERVICIOS_DIA):
        if pasajeros_totales_por_servicio[i] > max_pasajeros_servicio:
            max_pasajeros_servicio = pasajeros_totales_por_servicio[i]
            mejor_servicio_indices = [i + 1] # Guardamos el número de servicio (1-4)
        elif pasajeros_totales_por_servicio[i] == max_pasajeros_servicio:
            mejor_servicio_indices.append(i + 1)
            
    print(f"\n--- Mejor(es) Servicio(s) del Día (Mayor Acumulado Semanal) ---") # El programa debe mostrar cuál de los 4 servicios durante el día es el mejor
    if mejor_servicio_indices:
        servicios_str = ", ".join(map(str, mejor_servicio_indices))
        print(f"El/Los mejor(es) servicio(s) es/son el/los Servicio(s) {servicios_str}, transportando un total de {max_pasajeros_servicio} pasajeros durante la semana.")
    else:
        print("No se pudo determinar el mejor servicio.")


def momento_menos_pasajeros(pasajeros_semana):
    """
    Muestra el momento (servicio y día) en que menos pasajeros se transportaron.
    """
    if not pasajeros_semana or not any(pasajeros_semana):
        print("\nNo hay datos suficientes para determinar el momento con menos pasajeros.")
        return

    min_pasajeros = CAPACIDAD_MAX_AUTOBUS + 1 
    momentos_min_pasajeros = [] # Lista para guardar (dia_idx, servicio_idx, cantidad)
    dias_semana_nombres = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

    hubo_datos_validos = False
    for i, pasajeros_dia in enumerate(pasajeros_semana):
        for j, cantidad in enumerate(pasajeros_dia):
            hubo_datos_validos = True
            if cantidad < min_pasajeros:
                min_pasajeros = cantidad
                momentos_min_pasajeros = [(i, j, cantidad)]
            elif cantidad == min_pasajeros:
                momentos_min_pasajeros.append((i,j,cantidad))
    
    print(f"\n--- Momento(s) con Menos Pasajeros ({min_pasajeros} pasajeros) ---") # El programa debe mostrar el momento en que menos pasajeros se transportaron (servicio y día)
    if hubo_datos_validos and momentos_min_pasajeros:
        for dia_idx, servicio_idx, cant in momentos_min_pasajeros:
            print(f"- Día {dias_semana_nombres[dia_idx]}, Servicio {servicio_idx + 1}")
    else:
        print("No se transportaron pasajeros o no hay datos suficientes.")


def main_ejercicio2():
    print("Bienvenido al Sistema de Estadísticas de Pasajeros de Autobús")
    
    # La captura de los datos debe estar ubicada en su propio subproceso
    datos_pasajeros = capturar_pasajeros()
    print("\nPasajeros registrados por día y servicio:")
    dias_semana_nombres = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    for i, dia_pasajeros in enumerate(datos_pasajeros):
        print(f"{dias_semana_nombres[i]}: {dia_pasajeros}")

    # Cada uno de los procesos que muestran información deben estar ubicados en su propio subproceso
    promedio_pasajeros_por_dia(datos_pasajeros)
    promedio_general_pasajeros(datos_pasajeros)
    mejor_servicio_del_dia(datos_pasajeros)
    momento_menos_pasajeros(datos_pasajeros)

if __name__ == "__main__":
    main_ejercicio2()
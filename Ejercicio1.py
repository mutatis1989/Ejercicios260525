# ejercicio1.py

NUM_CURSOS = 3
NUM_ESTUDIANTES_POR_CURSO = 5

def solicitar_notas():
    """
    Solicita la nota final de todos los estudiantes y las almacena en un arreglo de dos dimensiones.
    """
    notas_cursos = []
    for i in range(NUM_CURSOS):
        notas_curso_actual = []
        print(f"\n--- Ingresando notas para el Curso {i+1} ---")
        for j in range(NUM_ESTUDIANTES_POR_CURSO):
            while True:
                try:
                    # Se solicita la nota final del curso para cada estudiante
                    nota = float(input(f"Ingrese la nota final del estudiante {j+1} del curso {i+1}: "))
                    if 0 <= nota <= 100: # Validamos que la nota esté en un rango lógico
                        notas_curso_actual.append(nota)
                        break
                    else:
                        print("Por favor, ingrese una nota válida entre 0 y 100.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")
        notas_cursos.append(notas_curso_actual) # Se ubican las notas en un arreglo de dos dimensiones
    return notas_cursos

def calcular_promedio_total(notas_cursos):
    """
    Calcula la nota promedio de todos los estudiantes y la muestra al usuario.
    """
    suma_total_notas = 0
    cantidad_total_estudiantes = 0
    for curso in notas_cursos:
        for nota in curso:
            suma_total_notas += nota
        cantidad_total_estudiantes += len(curso)
    
    if cantidad_total_estudiantes == 0:
        promedio_total = 0
    else:
        promedio_total = suma_total_notas / cantidad_total_estudiantes
    
    print(f"\n--- Promedio General de Todos los Estudiantes ---")
    print(f"El promedio de todos los estudiantes es: {promedio_total:.2f}")
    return promedio_total

def calcular_promedio_por_grupo(notas_cursos):
    """
    Calcula la nota promedio por cada uno de los grupos y muestra los promedios al usuario informando el grupo.
    """
    print(f"\n--- Promedio por Grupo ---")
    for i, curso in enumerate(notas_cursos):
        suma_notas_curso = 0
        if not curso: # Si el curso no tiene estudiantes
            print(f"El Curso {i+1} no tiene estudiantes.")
            continue
        for nota in curso:
            suma_notas_curso += nota
        promedio_curso = suma_notas_curso / len(curso)
        print(f"El promedio del Curso {i+1} es: {promedio_curso:.2f}") # Se muestra el promedio informando el grupo

def porcentaje_aprobados_por_grupo(notas_cursos):
    """
    Muestra al usuario por cada grupo cuál es el porcentaje de estudiantes aprobados (nota >= 70).
    """
    print(f"\n--- Porcentaje de Aprobados por Grupo ---")
    NOTA_APROBACION = 70 # Los estudiantes aprobados son aquellos que obtuvieron al menos una nota de 70
    for i, curso in enumerate(notas_cursos):
        aprobados = 0
        if not curso:
            print(f"El Curso {i+1} no tiene estudiantes para calcular aprobados.")
            continue
        for nota in curso:
            if nota >= NOTA_APROBACION:
                aprobados += 1
        porcentaje = (aprobados / len(curso)) * 100 if len(curso) > 0 else 0
        print(f"Curso {i+1}: {porcentaje:.2f}% de estudiantes aprobados ({aprobados}/{len(curso)}).") # Se muestra el porcentaje por grupo

def nota_mayor_menor_por_grupo(notas_cursos):
    """
    Muestra al usuario cuál ha sido la nota mayor y la menor por cada uno de los grupos.
    """
    print(f"\n--- Nota Mayor y Menor por Grupo ---")
    for i, curso in enumerate(notas_cursos):
        if not curso:
            print(f"El Curso {i+1} no tiene estudiantes.")
            continue
        # Asumimos que la primera nota es la mayor y menor para empezar la comparación
        nota_mayor = curso[0]
        nota_menor = curso[0]
        for nota in curso: # Iteramos a partir del segundo estudiante si ya tomamos el primero
            if nota > nota_mayor:
                nota_mayor = nota
            if nota < nota_menor:
                nota_menor = nota
        print(f"Curso {i+1}: Nota Mayor = {nota_mayor:.2f}, Nota Menor = {nota_menor:.2f}")

def main_ejercicio1():
    print("Bienvenido al Sistema de Control de Notas")
    
    # Solicitar notas
    arreglo_notas = solicitar_notas()
    print("\nNotas ingresadas:")
    for i, curso_notas in enumerate(arreglo_notas):
        print(f"Curso {i+1}: {curso_notas}")

    # Cada una de las opciones mencionadas debe ser creada en un subproceso
    # Calcular promedio de todos los estudiantes
    calcular_promedio_total(arreglo_notas)

    # Calcular promedio por grupo
    calcular_promedio_por_grupo(arreglo_notas)

    # Porcentaje de aprobados por grupo
    porcentaje_aprobados_por_grupo(arreglo_notas)

    # Nota mayor y menor por grupo
    nota_mayor_menor_por_grupo(arreglo_notas)

if __name__ == "__main__":
    main_ejercicio1()
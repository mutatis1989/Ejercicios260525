# ingreso_personas.py

NOMBRE_ARCHIVO_AFORO = "aforo_actual.txt"
CAPACIDAD_MAXIMA = 10 # La capacidad del abastecedor es de 10 personas como máximo [cite: 28]

def leer_aforo_actual():
    """
    Lee la cantidad actual de personas desde el archivo de texto.
    Si el archivo no existe o está vacío/corrupto, asume 0 personas.
    """
    try:
        with open(NOMBRE_ARCHIVO_AFORO, "r") as f:
            contenido = f.read().strip()
            if contenido: # Si hay contenido
                return int(contenido)
            else: # Archivo vacío
                return 0
    except FileNotFoundError:
        # Si el archivo no existe, es la primera vez o se borró, asumimos 0 personas.
        return 0
    except ValueError:
        # Si el contenido no es un número válido, asumimos 0 y se sobrescribirá.
        print("Advertencia: El archivo de aforo contenía un valor no numérico. Se reiniciará a 0.")
        return 0

def escribir_aforo_actual(cantidad_personas):
    """
    Escribe la cantidad actualizada de personas en el archivo de texto.
    """
    try:
        with open(NOMBRE_ARCHIVO_AFORO, "w") as f:
            f.write(str(cantidad_personas))
    except IOError:
        print("Error crítico: No se pudo escribir en el archivo de aforo.")

def registrar_ingreso():
    """
    Registra el ingreso de una persona (uno a uno) si el aforo lo permite.
    Actualiza el archivo de texto.
    """
    personas_actuales = leer_aforo_actual()
    print(f"Personas actualmente en el local: {personas_actuales} de {CAPACIDAD_MAXIMA}.")

    if personas_actuales < CAPACIDAD_MAXIMA:
        personas_actuales += 1
        escribir_aforo_actual(personas_actuales)
        print(f"✅ Ingreso registrado. Personas ahora en el local: {personas_actuales}")
    else:
        print(f"🚫 Aforo máximo alcanzado ({CAPACIDAD_MAXIMA}). No se puede ingresar.")
        print("   Por favor, espere a que alguien salga.")

def main_ingreso():
    print("--- Aplicación de Registro de INGRESO 'La Deportiva' ---")
    print(f"(Capacidad máxima: {CAPACIDAD_MAXIMA} personas)") # [cite: 28]
    while True:
        input("\nPresione Enter para registrar un INGRESO (o Ctrl+C para salir)...")
        registrar_ingreso()

if __name__ == "__main__":
    # Considere almacenar la cantidad de personas actuales en un archivo de texto
    # para que esta información se comparta entre las aplicaciones [cite: 29]
    main_ingreso()
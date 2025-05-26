# egreso_personas.py

NOMBRE_ARCHIVO_AFORO = "aforo_actual.txt"
CAPACIDAD_MAXIMA = 10 # Aunque no se usa para bloquear, es bueno tenerla de referencia

def leer_aforo_actual():
    """
    Lee la cantidad actual de personas desde el archivo de texto.
    Si el archivo no existe o está vacío/corrupto, asume 0 personas.
    """
    try:
        with open(NOMBRE_ARCHIVO_AFORO, "r") as f:
            contenido = f.read().strip()
            if contenido:
                return int(contenido)
            else:
                return 0
    except FileNotFoundError:
        return 0
    except ValueError:
        print("Advertencia: El archivo de aforo contenía un valor no numérico. Se interpretará como 0.")
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

def registrar_egreso():
    """
    Registra el egreso de una persona (uno a uno).
    Actualiza el archivo de texto.
    """
    personas_actuales = leer_aforo_actual()
    print(f"Personas actualmente en el local: {personas_actuales} de {CAPACIDAD_MAXIMA}.")

    if personas_actuales > 0:
        personas_actuales -= 1
        escribir_aforo_actual(personas_actuales)
        print(f"✅ Egreso registrado. Personas ahora en el local: {personas_actuales}")
    else:
        print(f"🚫 No hay personas en el local para registrar un egreso.")

def main_egreso():
    print("--- Aplicación de Registro de EGRESO 'La Deportiva' ---")
    while True:
        input("\nPresione Enter para registrar un EGRESO (o Ctrl+C para salir)...")
        registrar_egreso()

if __name__ == "__main__":
    # Considere almacenar la cantidad de personas actuales en un archivo de texto
    # para que esta información se comparta entre las aplicaciones [cite: 29]
    main_egreso()
import random

# Lista de preguntas y respuestas
preguntas = [
    ("Cuando se establece una comunicación o trasmisión, ¿a través de qué alcanza el destino la información?", [
        "a) Fibra óptica.",
        "b) Cable coaxial.",
        "c) Conector RJ-45.",
        "d) Medio de transmisión."
    ], "d"),
    ("¿Con qué nivel está relacionado el medio de transmisión?", [
        "a) Nivel de red.",
        "b) Nivel de transmisión.",
        "c) Nivel físico.",
        "d) Nivel de enlace."
    ], "c"),
    ("¿Cuál es el objetivo del nivel físico?", [
        "a) La transmisión y la recepción de bits.",
        "b) Conectar dispositivos a la red.",
        "c) Generar corriente eléctrica.",
        "d) Detectar errores en la conexión."
    ], "a"),
    ("¿Cuáles son funciones del nivel físico?", [
        "a) Definir características eléctricas, mecánicas, de procedimiento y funcionales para activar, mantener y desactivar el enlace físico entre 2 equipos.",
        "b) Definir características de los conectores y cableado y asegurar su compatibilidad.",
        "c) Determinar la codificación, voltaje de la señal eléctrica y la duración de los pulsos eléctricos.",
        "d) Todas son correctas."
    ], "d"),
    ("¿A qué nivel corresponde la amplificación de la señal mediante amplificadores?", [
        "a) Nivel de red.",
        "b) Nivel de amplificación.",
        "c) Nivel físico.",
        "d) Nivel de enlace."
    ], "c"),
    ("¿Qué deben tener en cuenta los protocolos del nivel 1 (físico) para realizar el transporte de la información?", [
        "a) La longitud del cableado y el número de dispositivos conectados a la red.",
        "b) El modo de enviar los dígitos binarios por el medio, tener en cuenta si el medio permite la transmisión en un único sentido o en ambos, la corrección de las distorsiones y perturbaciones que sufre la señal en su camino, y la posibilidad o no de enviar varias transmisiones simultáneamente.",
        "c) La longitud del cableado, el número de dispositivos conectados a la red y el voltaje de la red eléctrica.",
        "d) La longitud del cableado y la cantidad de bits por segundo que pueden ser transmitidos por el medio físico."
    ], "b"),
    ("¿Cuáles son ejemplos de especificaciones del nivel físico de la capa física de Ethernet?", [
        "a) 10BASE-T, 10BASE2, 10BASE5, 100BASE-TX, 100BASE-FX Y 100BASE-T.",
        "b) 10FASE-T, 10FASE2, 10FASE5, 100FASE-TX, 100FASE-FX, 100FASE-T.",
        "c) 10CASE-T, 10CASE2, 10CASE5, 100CASE-TX, 100CASE-CX, 100CASE-T.",
        "d) Ninguna de las anteriores."
    ], "b"),
    ("¿Dentro de qué viaja la información en la mayoría de las transmisiones?", [
        "a) De ondas.",
        "b) De un taxi.",
        "c) De trasmisores.",
        "d) De conectores."
    ], "a"),
    ("¿Qué es una onda?", [
        "a) Un ataque de Son Goku.",
        "b) Una perturbación que se desplaza en el espacio llevando energía.",
        "c) Un pulso uniforme de energía que se desplazada en el vacío.",
        "d) Un pulso uniforme de energía que se desplaza por campos electro-magnéticos."
    ], "b"),
    ("¿Por qué son producidas las ondas electromagnéticas?", [
        "a) Por el choque de ondas eléctricas en imanes de gran tamaño.",
        "b) Por el choque de ondas eléctricas en imanes, sin importar el tamaño.",
        "c) Por un pulso uniforme eléctrico en un campo magnético asociado.",
        "d) Por la oscilación de un campo eléctrico en relación con un campo magnético asociado."
    ], "d"),
    ("¿Cómo puede ser la transmisión?", [
        "a) Analógica o magnética.",
        "b) Abierta o cerrada.",
        "c) Analógica, digital o magnética.",
        "d) Analógica o digital."
    ], "d"),
    ("¿Qué valor o valores puede tomar la señal en una transmisión analógica?", [
        "a) Toma un valor fijo siempre.",
        "b) Toma valores continuos en el tiempo, tomando cualquier valor dentro de un rango determinado.",
        "c) Toma valores predefinidos por el administrador de la red.",
        "d) Toma valores discontinuos en el tiempo."
    ], "b"),
    ("La potencia de una transmisión analógica estará comprendida entre unos valores...", [
        "a) Positivo y negativo.",
        "b) Máximo y mínimo.",
        "c) Absoluto y relativo.",
        "d) Ninguna de las anteriores."
    ], "b"),
    ("La calidad de la transmisión depende...", [
        "a) Solo de la potencia recibida.",
        "b) De la potencia recibida y del ruido que lleva la señal.",
        "c) De la potencia recibida y del sonido que lleva la señal.",
        "d) Ninguna de las anteriores."
    ], "b"),    
    ("Los amplificadores empleados en la transmisión analógica...", [
        "a) Amplifican la señal, con lo cual también amplifican el ruido que llega con la misma.",
        "b) Amplifican la señal, pero no el ruido que llega con la misma.",
        "c) En las transmisiones analógicas no se usan amplificadores.",
        "d) No amplifican la señal, sino el ruido que llega con la misma."
    ], "a"),
    ("¿Cómo se llama al periodo de tiempo (por ejemplo, cada 2 mseg) a partir del cual se repite el patrón de la señal?", [
        "a) Periodo.",
        "b) Amplitud.",
        "c) Frecuencia.",
        "d) Fase."
    ], "a"),
    ("", [
        "a) .",
        "b) .",
        "c) .",
        "d) ."
    ], "a"),






    # Hay que saber distinguir entre los dos tipos de cable, el b856 o como se llame del otro, el que cambian los colores.





    ]


######################################################################################

# Mezclar las preguntas en orden aleatorio
random.shuffle(preguntas)

# Función para realizar el test
def realizar_test():
    puntaje = 0
    for i, (pregunta, opciones, respuesta) in enumerate(preguntas, 1):
        print(f"\nPregunta {i}: {pregunta}")
        random.shuffle(opciones)
        for opcion in opciones:
            print(opcion)
        respuesta_usuario = input("\nTu respuesta: ").strip().lower()
        if respuesta_usuario == respuesta:
            print("-------------------------")
            print("¡Respuesta correcta! ✔✔✔✔✔✔✔✔✔")
            print("-------------------------\n")
            puntaje += 1
        else:
            print("-------------------------")
            print(f"✖✖✖✖✖✖✖ Respuesta incorrecta. La opción correcta es: {respuesta}\n")
            print("-------------------------\n")
    
    print(f"Has completado el test, {nombre_usuario}. Puntuación final: {puntaje}/{len(preguntas)}")

# Solicitar el nombre del usuario
nombre_usuario = input("Bienvenido al test HTML. Por favor, introduce tu nombre: ")

# Solicitar el número de preguntas
num_preguntas = int(input("¿Cuántas preguntas deseas en el test? "))
while num_preguntas > len(preguntas):
    print(f"Lo siento, solo hay {len(preguntas)} preguntas disponibles.")
    num_preguntas = int(input("Por favor, elige un número igual o menor: "))

# Mezclar las preguntas en orden aleatorio
random.shuffle(preguntas)
preguntas = preguntas[:num_preguntas]

# Ejecutar el test
print(f"Muy bien, {nombre_usuario}! Comencemos con tu test de HTML con {num_preguntas} preguntas.")
realizar_test()
import random

# Lista de preguntas y respuestas
preguntas = [
    ("¿Cuáles son los dos modos principales de topología inalámbrica identificados por el estándar 802.11?", [
        "a) Modo ad hoc y modo infraestructura.",
        "b) Modo peer-to-peer y modo cliente-servidor.",
        "c) Modo punto a punto y modo punto a multipunto.",
        "d) Modo de difusión y modo de transmisión."
    ], "a"),
    ("¿Qué caracteriza al modo ad hoc en una red inalámbrica?", [
        "a) Conexión a través de un router o AP inalámbrico.",
        "b) Comunicación peer-to-peer sin utilizar AP o routers inalámbricos.",
        "c) Configuración exclusiva en dispositivos Apple.",
        "d) Uso exclusivo de la tecnología Bluetooth."
    ], "b"),
    ("¿Cómo se denomina a las redes ad hoc según el estándar IEEE 802.11?", [
        "a) Conjunto de servicios independientes.",
        "b) Redes exclusivas.",
        "c) Conjunto de servicios básicos independientes (IBSS).",
        "d) Redes independientes de infraestructura."
    ], "c"),
    ("¿Qué componentes básicos conforman la arquitectura IEEE 802.11 en el modo de infraestructura?", [
        "a) Conjunto de servicios básicos (BSS) y conjunto de servicios extendidos (ESS).",
        "b) Infraestructura y distribución.",
        "c) Banda de frecuencia y modulación.",
        "d) Conjunto de servicios primarios y secundarios."
    ], "a"),
    ("¿Cómo se identifica de forma exclusiva cada BSS en una red inalámbrica?", [
        "a) Mediante el SSID.",
        "b) A través de la dirección IP.",
        "c) Usando el identificador del conjunto de servicios básicos (BSSID).",
        "d) Con la dirección MAC de capa 2 del cliente inalámbrico."
    ], "c"),
    ("¿Qué representa un ESS en una red inalámbrica?", [
        "a) Un conjunto de servicios avanzados.",
        "b) Un área de servicios básicos (BSA).",
        "c) La conexión directa entre dispositivos ad hoc.",
        "d) La unión de dos o más BSS interconectados mediante un sistema de distribución (DS)."
    ], "d"),
    ("¿Cuáles son los tres tipos de tramas inalámbricas 802.11?", [
        "a) Trama de control, trama de datos y trama de gestión.",
        "b) Trama de consulta, trama de respuesta y trama de confirmación.",
        "c) Trama de solicitud, trama de aprobación y trama de rechazo.",
        "d) Trama de inicio, trama de continuación y trama de finalización."
    ], "a"),
    ("¿Qué información contiene el campo Control de trama en una trama 802.11?", [
        "a) Solo la versión del protocolo.",
        "b) Tipo de trama, dirección IP y contenido.",
        "c) Versión del protocolo, tipo de trama y subtipo de trama.",
        "d) Dirección MAC del AP y dirección MAC del dispositivo receptor."
    ], "c"),
    ("¿Para qué se utiliza la trama de solicitud de asociación en una red inalámbrica?", [
        "a) Para transmitir datos entre dispositivos.",
        "b) Para anunciar la presencia de un AP y proporcionar información de configuración.",
        "c) Para solicitar acceso dedicado al medio de RF.",
        "d) Para autenticar un dispositivo en la red."
    ], "c"),
    ("¿Cuáles son los dos mecanismos originales de autenticación en el estándar 802.11?", [
        "a) Autenticación abierta y autenticación cifrada.",
        "b) Autenticación por clave pública y autenticación por clave privada.",
        "c) Autenticación de clave compartida y autenticación por certificado digital.",
        "d) Autenticación NULA y autenticación de clave compartida."
    ], "d"),
    ("¿En qué consiste el proceso de autenticación NULA en una red inalámbrica?", [
        "a) Se realiza sin intercambio de claves, lo que permite el acceso a cualquier dispositivo.",
        "b) Requiere la intervención de un administrador para cada conexión.",
        "c) Utiliza un certificado digital para verificar la identidad del dispositivo.",
        "d) Implica el intercambio de claves de forma segura entre el cliente y el AP."
    ], "a"),
        ("¿Cuál es la función principal de las tramas de gestión en una red inalámbrica?", [
        "a) Transferir datos entre dispositivos.",
        "b) Gestionar la asociación y autenticación entre estaciones y AP.",
        "c) Controlar el flujo de tráfico de red.",
        "d) Enviar consultas para obtener información de configuración."
    ], "b"),
    ("¿Cómo afecta la interferencia electromagnética a una red inalámbrica?", [
        "a) Mejora la calidad de la señal.",
        "b) Causa pérdida de datos y disminuye el rendimiento.",
        "c) Aumenta la velocidad de transmisión.",
        "d) No tiene ningún impacto en la red inalámbrica."
    ], "b"),
    ("En una red inalámbrica, ¿cuál es la función del protocolo RTS/CTS?", [
        "a) Proporcionar seguridad mediante cifrado de datos.",
        "b) Evitar colisiones en la transmisión de datos.",
        "c) Gestionar la asociación entre estaciones.",
        "d) Establecer conexiones ad hoc de forma automática."
    ], "b"),
    ("¿Qué es el handover o itinerancia en una red inalámbrica?", [
        "a) El cambio de una red inalámbrica a una red cableada.",
        "b) La transición de una celda a otra sin perder la conexión.",
        "c) La desconexión total de un dispositivo de la red.",
        "d) La velocidad de itinerancia máxima permitida por el estándar."
    ], "b"),
    ("¿Cuál es la ventaja principal de la modulación en una señal inalámbrica?", [
        "a) Aumentar la cantidad de datos transmitidos simultáneamente.",
        "b) Reducir la interferencia electromagnética.",
        "c) Mejorar la seguridad de la red.",
        "d) Ampliar el rango de cobertura de la red."
    ], "a"),
    ("En una red inalámbrica, ¿qué es un canal?", [
        "a) Una conexión física por cable entre dispositivos.",
        "b) Un conjunto de servicios básicos (BSS).",
        "c) Una frecuencia específica utilizada para la transmisión de datos.",
        "d) Un dispositivo que facilita la conexión inalámbrica."
    ], "c"),
    ("¿Cómo afecta la interferencia electromagnética a una red inalámbrica?", [
        "a) Mejora la calidad de la señal.",
        "b) Causa pérdida de datos y disminuye el rendimiento.",
        "c) Aumenta la velocidad de transmisión.",
        "d) No tiene ningún impacto en la red inalámbrica."
    ], "b"),
    ("En una red inalámbrica, ¿qué es el roaming?", [
        "a) La desconexión total de un dispositivo de la red.",
        "b) El cambio de una red inalámbrica a una red cableada.",
        "c) La transición de una celda a otra sin perder la conexión.",
        "d) La velocidad de itinerancia máxima permitida por el estándar."
    ], "c"),
    ("¿Qué función cumple el mecanismo de selección de canal en una red inalámbrica?", [
        "a) Facilitar la conexión inalámbrica.",
        "b) Escoger automáticamente el canal con menos interferencias.",
        "c) Establecer conexiones ad hoc de forma automática.",
        "d) Incrementar la velocidad de transmisión."
    ], "b"),
    ("En una red inalámbrica, ¿qué es un 'punto de acceso'?", [
        "a) El área física cubierta por una red inalámbrica.",
        "b) Un dispositivo que facilita la conexión inalámbrica.",
        "c) Un conjunto de servicios básicos (BSS).",
        "d) Una conexión física por cable entre dispositivos."
    ], "b")
]




######################################################################################

# Mezclar las preguntas en orden aleatorio
random.shuffle(preguntas)

# Función para calcular la equivalencia de la puntuación en una nota sobre 10
def calcular_equivalencia_puntuacion(puntuacion, total_preguntas):
    escala_maxima = 10.0
    equivalencia = (puntuacion / total_preguntas) * escala_maxima
    return equivalencia

# Función para realizar el test
def realizar_test():
    puntaje = 0
    total_preguntas = len(preguntas)

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
    
    equivalencia = calcular_equivalencia_puntuacion(puntaje, total_preguntas)
    
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print(f"  Has completado el test, {nombre_usuario}. Puntuación final: {puntaje}/{total_preguntas}")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    print("                                                  ==========")
    print(f"Tu equivalencia de nota sobre 10 es ━━━━━━━━━━━━❯✷ {equivalencia:.2f}/10 ✷❮━━━━━━━━━━━━")
    print("                                                  ==========")

# Solicitar el nombre del usuario
nombre_usuario = input("Bienvenido al test de Fundamentos. Por favor, introduce tu nombre: ")

# Solicitar el número de preguntas
num_preguntas = int(input("¿Cuántas preguntas deseas en el test? "))
while num_preguntas > len(preguntas):
    print(f"Lo siento, solo hay {len(preguntas)} preguntas disponibles.")
    num_preguntas = int(input("Por favor, elige un número igual o menor: "))

# Mezclar las preguntas en orden aleatorio
random.shuffle(preguntas)
preguntas = preguntas[:num_preguntas]

# Ejecutar el test
print(f"Muy bien, {nombre_usuario}! Comencemos con tu test de Fundamentos con {num_preguntas} preguntas.")
realizar_test()
import random

# Lista de preguntas y respuestas
preguntas = [
    ("¿Cuál de los siguientes aspectos hay que tener en cuenta a la hora de diseñar una arquitectura de red?", [
        "a) Los paquetes han de poder ser trasladados desde un emisor a un receptor, para ello estos deben de estar correctamente identificados, así como la forma de llegar de unos a otros.",
        "b) Los protocolos pueden estar diseñados para admitir comunicación simplex, semiduplex o full duplex.",
        "c) Deben de suministrarse mecanismos de control de errores.",
        "d) Todas son correctas."
    ], "d"),
    ("Uno de los aspectos a la hora de diseñar una arquitectura de red es el control de flujo y congestión. ¿En qué consiste?", [
        "a) En impulsar una arquitectura de red lo más veloz posible.",
        "b) En desarrollar protocolos que traten de evitar la congestión de una red y que permitan tomar decisiones en caso de que la información introducida en una red sea superior a la que es capaz de gestionar.",
        "c) En controlar el flujo de los dispositivos que acceden a la red de modo que lo hagan mediante algún algoritmo de control, como FIFO, round robin o similares.",
        "d) Ninguna de las opciones es correcta."
    ], "b"),
    ("Uno de los aspectos a tener en cuenta a la hora de diseñar una arquitectura de red es especificar los tamaños mínimos de los paquetes. ¿Por qué es importante?", [
        "a) Para garantizar la compatibilidad con todos los dispositivos de red.",
        "b) Para habilitar mecanismos de fragmentación y reagrupamiento.",
        "c) Para aumentar la velocidad de transmisión de datos.",
        "d) Para reducir la cantidad de paquetes necesarios en la red."
    ],     "b"),
    ("Uno de los aspectos a tener en cuenta a la hora de diseñar una arquitectura de red es la multiplexación y desmultiplexación. ¿Cuál es el propósito de estas?", [
        "a) Permitir que una capa inferior pueda soportar distintas comunicaciones de capas superiores.",
        "b) Reducir la cantidad de información transmitida en el medio físico.",
        "c) Asegurar la compatibilidad entre diferentes protocolos de red.",
        "d) Controlar el flujo de datos en una red."
    ], "a"),
    ("¿Cuáles son las dos arquitecturas de red más extendidas y consideradas como modelos de referencia?", [
        "a) OSI y IEEE 802.11",
        "b) TCP/IP y UDP",
        "c) OSI y TCP/IP",
        "d) ARP y DNS"
    ], "c"),
    ("¿Cuál de las siguientes afirmaciones describe mejor el modelo OSI (Open Systems Interconnection)?", [
        "a) El modelo OSI es principalmente práctico y utilizado en la realidad sin niveles ni protocolos obsoletos.",
        "b) El modelo OSI es teórico y en la práctica, algunos niveles y protocolos rara vez se utilizan.",
        "c) El modelo OSI es un enfoque práctico que se utiliza en la mayoría de las redes modernas.",
        "d) El modelo OSI es un estándar obligatorio para todas las redes de comunicación."
    ]  , "b"),
    ("¿Cuál es la principal característica del modelo TCP/IP (Transport Control Protocol/Internet Protocol)?", [
        "a) Es un modelo teórico altamente detallado y definido.",
        "b) Se centra en un solo protocolo para todas las comunicaciones en Internet.",
        "c) Es un modelo más práctico que teórico y consta de una recopilación de varios protocolos utilizados en Internet.",
        "d) Solo se utiliza en redes privadas y no en Internet público."
    ], "c"),
    ("¿Cuál es el propósito principal del Modelo OSI (Open Systems Interconnection)?", [
        "a) Establecer una arquitectura detallada y definida para redes de comunicación.",
        "b) Fomentar la adopción de la arquitectura SNA de IBM.",
        "c) Definir un único protocolo para todas las comunicaciones de datos.",
        "d) Proporcionar un estándar específico para cada fabricante de tecnologías de comunicación."
    ], "a"),
        ("¿Por qué fue definido el Modelo OSI (Open Systems Interconnection) por la Organización Internacional de Estándares (ISO) en 1977?", [
        "a) Para promover una única arquitectura de comunicación utilizada por todos los fabricantes.",
        "b) Para poner orden en la variedad de tecnologías y protocolos desarrollados por diferentes fabricantes para comunicaciones de datos.",
        "c) Para estandarizar exclusivamente la arquitectura SNA de IBM.",
        "d) Para crear un único protocolo de comunicación universal."
    ], "b"),
    ("¿En qué año fue definido el Modelo OSI (Open Systems Interconnection)", [
        "a) 1956",
        "b) 1977.",
        "c) 1988.",
        "d) 1967."
    ], "b"),
    ("¿Cuál fue uno de los objetivos de la ISO al definir el Modelo OSI para arquitecturas de comunicación?", [
        "a) Promover la adopción de la arquitectura SNA de IBM como estándar.",
        "b) Establecer un monopolio en la industria de comunicaciones para la ISO.",
        "c) Evitar que ninguna arquitectura de fabricantes adquiera una posición hegemónica en el mercado.",
        "d) Facilitar la expansión de las tecnologías de comunicación de IBM."
    ], "c"),
    ("¿Cuántas capas o niveles define el Modelo OSI (Open Systems Interconnection)?", [
        "a) 3 capas",
        "b) 5 capas",
        "c) 7 capas",
        "d) 9 capas"
    ], "c"),
    ("¿Cuál es una característica fundamental del Modelo OSI como modelo de referencia?", [
        "a) Proporciona un único protocolo para todas las capas.",
        "b) Define interfaces entre las capas y describe las funciones y servicios de cada capa.",
        "c) Está diseñado principalmente para la comunicación en Internet.",
        "d) No describe la interacción entre las capas en absoluto."
    ], "b"),
    ("¿Cuál es la función principal del Nivel 1 (Nivel Físico) en el Modelo OSI?", [
        "a) Procesar y enrutar datos a través de la red.",
        "b) Realizar el control de flujo en la red.",
        "c) Encapsular datos en paquetes para la transmisión."
        "d) Transmitir bits a través del canal de comunicación asegurando que se transmita el mismo valor (1 o 0).",
    ], "d"),
    ("¿Cuál es la unidad de transmisión principal en el Nivel 1 (Nivel Físico) del Modelo OSI?", [
        "a) Paquete",
        "b) Bit",
        "c) Marco",
        "d) Segmento"
    ], "b"),
    ("¿Cuáles son las características mecánicas definidas en el nivel físico del modelo OSI (Nivel 1)?", [
        "a) Forma del conector y número de pines, longitudy especiamento entre pines.",
        "b) Impedancias y niveles de voltaje.",
        "c) Asignación de funciones a los pines.",
        "d) Secuencia de eventos para establecer una comunicación."
    ], "a"),
    ("¿Cuál es el enfoque principal de las características eléctricas en el nivel 1 (nivel físico) del modelo OSI?", [
        "a) Forma del conector y número de pines.",
        "b) Impedancias y niveles de voltaje.",
        "c) Asignación de funciones a los pines.",
        "d) Secuencia de eventos para establecer una comunicación."
    ], "b"),
    ("¿En qué consisten las características funcionales del nivel 1 (nivel físico) del modelo OSI?", [
        "a) Forma del conector y número de pines.",
        "b) Impedancias y niveles de voltaje.",
        "c) Asignación de funciones a los pines.",
        "d) Secuencia de eventos para establecer una comunicación."
    ], "c"),
    ("¿Puede proporcionar un ejemplo concreto de una característica procedimental en el nivel físico (1) del modelo OSI?", [
        "a) Forma del conector y número de pines.",
        "b) Impedancias y niveles de voltaje.",
        "c) Asignación de funciones a los pines.",
        "d) Secuencia de eventos para establecer una comunicación."
    ], "d"),
    ("¿Cuáles son los tipos de características definidos para los conectores de redes locales y por qué son importantes en la configuración de una red?", [
        "a) Mecánicas, eléctricas, funcionales y procedimentales.",
        "b) Mecánicas y eléctricas solamente.",
        "c) Características de hardware y software.",
        "d) Características de transmisión y recepción."
    ], "a"),
    ("¿Cuál es la función principal del Nivel 2 (Nivel de Enlace) en el modelo OSI y cuál es su unidad de transmisión?", [
        "a) Transmitir bits en el canal de comunicación y su unidad de transmisión es el bit.",
        "b) Asociar conjuntos de bits en paquetes y su unidad de tansmisión es el paquete.",
        "c) Asociar conjuntos de bits en tramas y la unidad de transmisión es la trama.",
        "d) Gestionar las direcciones IP en una red y la unidad de transmisión es el paquete."
    ], "c"),
    ("¿Qué función desempeña la 'sincronización de trama' en el Nivel 2 (Nivel de Enlace) del modelo OSI?", [
        "a) Control de errores.",
        "b) Identificación del inicio y fin de cada trama.",
        "c) Asociación de bits en tramas.",
        "d) Detección y corrección de errores de bit."
    ], "b"),
    ("¿Cuál es el propósito principal del 'control de errores' en el Nivel 2 del modelo OSI?", [
        "a) Corregir errores en la transmisión de datos.",
        "b) Identificar el inicio de una trama.",
        "c) Detección y corrección de errores de bit.",
        "d) Gestionar direcciones IP."
    ], "a"),
    ("¿Qué función cumple el 'control de errores de bit' en el Nivel 2 del modelo OSI?", [
        "a) Identificar el inicio de una trama.",
        "b) Asociar bits en tramas.",
        "c) Detección y/o corrección de errores de bit.",
        "d) Controlar el flujo de datos en la red."
    ], "c"),
    ("¿Cuál es el propósito del 'control de flujo' en el Nivel 2 (Nivel de Enlace) del modelo OSI?", [
        "a) Controlar la sincronización de trama.",
        "b) Detectar errores de bit.",
        "c) Identificar el inicio de cada trama.",
        "d) Regular la velocidad de transmisión de datos en la red."
    ], "d"),
    ("¿Cuál es son funciones del nivel 2 (nivel de enlace) del modelo OSI?", [
        "a) Encaminamiento de los paquetes, sincronización de trama y control de flujo.",
        "b) Control de gestión en las líneas, encaminamiento de los paquetes y control de flujo.",
        "c) Sincronización de trama, control de congestión en las líneas y control de flujo.",
        "d) Sincronización de trama, control de errores y control de flujo."
    ], "d"),
    ("¿Cuál es son funciones del nivel 3 (nivel de red) del modelo OSI?", [
        "a) Encaminamiento de los paquetes, control de gestión en las líneas y control de flujo.",
        "b) Encaminamiento de los paquetes, control de congestión en las líneas y interconexión de redes diferentes entre sí."
        "c) Control de gestión en las líneas, encaminamiento de los paquetes y recepción en el orden correcto.",
        "d) Fiabilidad extremo a extremo, recepción en el orden correcto y control del flujo extremo a extremo.",
    ], "b"),
        ("¿Cuál es son funciones del nivel 4 (nivel de transporte) del modelo OSI?", [
        "a) Fiabilidad extremo a extremo, recepción en el orden correcto y control de congestión en las líneas.",
        "b) Control de gestión en las líneas, encaminamiento de los paquetes y control de flujo.",
        "c) Fiabilidad extremo a extremo, recepción en el orden correcto y control de flujo extremo a extremo.",
        "d) Fiabilidad extremo a extremo, control de errores y control de flujo."
    ], "c"),
        ("¿Cuál es son funciones del nivel 5 (nivel de sesión) del modelo OSI?", [
        "a) Encaminamiento de los paquetes, sincronización de trama y control de flujo.",
        "b) Control de gestión en las líneas, encaminamiento de los paquetes y control de flujo.",
        "c) Sincronización de trama, control de congestión en las líneas y control de flujo.",
        "d) Mecanismos para controlar el diálogo entre aplicaciones y mecanismos de puntos de verificación."
    ], "d"),
        ("¿Cuál es son funciones del nivel 6 (nivel de presentación) del modelo OSI?", [
        "a) Encaminamiento de los paquetes, sincronización de trama y control de flujo.",
        "b) Traducción de distintos formatos, compresión de datos y cifrado de datos.",
        "c) Cifrado de datos, control de congestión en las líneas y control de flujo.",
        "d) Sincronización de trama, control de errores y control de flujo."
    ], "d"),
    ("¿Cuál es la unidad de transmisión principal en el Nivel 2 (Nivel de Enlace) del modelo OSI?", [
        "a) Bit",
        "b) Paquete",
        "c) Trama",
        "d) Segmento"
    ], "c"),
    ("¿Cuál de las siguientes funciones es desempeñada por el Nivel 2 (Nivel de Enlace) en el modelo OSI?", [
        "a) Identificación del inicio y fin de cada trama.",
        "b) Gestionar direcciones IP.",
        "c) Transmitir bits en el canal de comunicación.",
        "d) Regular la velocidad de transmisión de datos."
    ], "a"),
    ("¿Qué función cumple el 'control de errores' en el Nivel 2 (Nivel de Enlace) del modelo OSI?", [
        "a) Detectar y corregir errores de bit que puedan ocurrir en las tramas.",
        "b) Controlar la sincronización de trama.",
        "c) Regular la velocidad de transmisión de datos.",
        "d) Asociar conjuntos de bits en tramas."
    ], "a"),
    ("¿Cuál es la función principal del 'control de flujo' en el Nivel 2 (Nivel de Enlace) del modelo OSI?", [
        "a) Detectar y corregir errores de bit en las tramas.",
        "b) Identificar el inicio y fin de cada trama.",
        "c) Garantizar que no se envíen más tramas de las que el receptor puede recibir.",
        "d) Regular la velocidad de transmisión de datos."
    ], "c"),
    ("¿Cuál es la función principal del Nivel 3 (Nivel de Red) en el modelo OSI?", [
        "a) Encaminamiento de los paquetes, control de congestión en las líneas y interconexión de redes diferentes entre sí.",
        "b) Encaminamiento de los paquetes, control de gestión en las líneas y control de flujo.",
        "c) Control de gestión en las líneas, encaminamiento de los paquetes y recepción en el orden correcto.",
        "d) Fiabilidad extremo a extremo, recepción en el orden correcto y control del flujo extremo a extremo."
    ], "b"),
    ("¿Cuál es la unidad de transmisión principal en el Nivel 3 (Nivel de Red) de una red?", [
        "a) Bit",
        "b) Paquete",
        "c) Trama",
        "d) Segmento"
    ], "b"),
    ("Uno de los roles clave del Nivel 3 (Nivel de Red) en el modelo OSI es el encaminamiento de paquetes. ¿En qué consiste esta función?", [
        "a) En la transferencia de datos entre dispositivos en una red local.",
        "b) En el control de congestión de la red para evitar la pérdida de paquetes.",
        "c) En encontrar la ruta óptima para dirigir paquetes de datos desde el origen hasta el destino a través de múltiples redes interconectadas.",
        "d) En la corrección de errores en los paquetes durante la transmisión.",
    ], "c"),
    ("En el Nivel 3 (Nivel de Red) del modelo OSI, una de las funciones es el control de congestión en las líneas. ¿En qué consiste esta función?", [
        "a) En encontrar la ruta más corta para transmitir datos.",
        "b) En detectar y corregir errores en los paquetes durante la transmisión.",
        "c) En establecer políticas de actuación en caso de que haya saturación en las líneas de comunicación para evitar la pérdida de paquetes.",
        "d) En garantizar que los dispositivos en la red estén sincronizados en cuanto a la velocidad de transmisión de datos.",
    ], "c"),
    ("En el Nivel 3 (Nivel de Red) del modelo OSI, una de las funciones es la interconexión de redes diferentes entre sí. ¿En qué consiste esta función?", [
        "a) Conectar redes de diferentes tecnologías a nivel de enlace y que puedan tener distintos tamaños de trama.",
        "b) Establecer un control de congestión en las líneas de comunicación para evitar pérdida de paquetes.",
        "c) Determinar la ruta más corta para la transmisión de datos en una red.",
        "d) Detectar y corregir errores en los paquetes durante la transmisión.",
    ], "a"),
    ("¿Cuál es la unidad de transmisión principal en el Nivel 4 (Nivel de Transporte) del modelo OSI?", [
        "a) Bit",
        "b) Paquete",
        "c) Trama",
        "d) Segmento"
    ], "d"),
    ("¿Cuál es la principal diferencia entre el Nivel 4 (Nivel de Transporte) y los niveles inferiores del modelo OSI?", [
        "a) El Nivel 4 se encarga de la comunicación entre extremos y tiene una unidad de transmisión de segmento, mientras que los niveles inferiores se enfocan en la comunicación nodo a nodo y utilizan tramas o paquetes como unidades de transmisión.",
        "b) Los niveles inferiores se encargan de la comunicación entre extremos y utilizan segmentos como unidades de transmisión, mientras que el Nivel 4 se enfoca en la comunicación nodo a nodo y utiliza tramas o paquetes.",
        "c) El Nivel 4 se encarga de la comunicación entre nodos de interconexión y tiene una unidad de transmisión de trama, mientras que los niveles inferiores se enfocan en la comunicación entre extremos y utilizan paquetes como unidades de transmisión.",
        "d) Los niveles inferiores se encargan de la comunicación entre nodos de interconexión y utilizan tramas como unidades de transmisión, mientras que el Nivel 4 se enfoca en la comunicación entre extremos y utiliza paquetes."
    ], "a"),
    ("¿Cuál de las siguientes funciones típicas se lleva a cabo en el Nivel 4 (Nivel de Transporte) del modelo OSI?", [
        "a) Fiabilidad extremo a extremo para garantizar que lo que se envía se recibe y detectar pérdida de datos.",
        "b) Control de congestión en las líneas para establecer una política de actuación en caso de saturación en las líneas.",
        "c) Encaminamiento de los paquetes para encontrar un camino a través de diferentes redes desde el origen hasta el destino.",
        "d) Sincronización de trama para identificar el inicio y fin de cada trama."
    ], "a"),
    ("¿Cuál de las siguientes afirmaciones describe mejor la función de 'fiabilidad extremo a extremo' en el Nivel 4 del modelo OSI?", [
        "a) Garantiza que los paquetes se envían rápidamente a su destino.",
        "b) Detecta y corrige errores de bit en las tramas de datos.",
        "c) Asegura que lo que se envía se recibe correctamente y utiliza mecanismos para detectar la pérdida de datos durante la transmisión.",
        "d) Controla la velocidad de transmisión de datos para evitar la congestión en la red."
    ], "c"),
    ("¿Qué función realiza el nivel 4 (Nivel de Transporte) del modelo OSI en relación a la 'recepción en el orden correcto' de los paquetes de datos?", [
        "a) Garantiza que los paquetes se envían rápidamente a su destino.",
        "b) Detecta y corrige errores de bit en las tramas de datos.",
        "c) Asegura que los paquetes se reordenen de manera correcta en caso de desorden durante el transporte.",
        "d) Controla la velocidad de transmisión de datos para evitar la congestión en la red."
    ], "c"),
    ("Los niveles OSI de sesión, presentación y aplicación son normalmente agrupados en otras arquitecturas de red en un único nivel de aplicación. ¿Qué caracteriza a estos tres niveles OSI de forma individual?", [
        "a) Cada uno de ellos se encarga de aspectos distintos, como el diálogo entre aplicaciones, la traducción de formatos y el cifrado de datos.",
        "b) Son idénticos en sus funciones y no presentan diferencias en cuanto a sus características y roles en la arquitectura de red.",
        "c) Solo son relevantes en arquitecturas OSI y no se aplican en ningún otro estándar de red.",
        "d) Están principalmente enfocados en el enrutamiento y control de tráfico en la red."
    ], "a"),
    ("¿Cuál es la función principal del Nivel 5 (Nivel de Sesión) en el modelo OSI?", [
        "a) Controlar el flujo de datos en la red.",
        "b) Establecer y gestionar el diálogo entre aplicaciones, permitiendo abrir, mantener y cerrar sesiones.",
        "c) Realizar la traducción de formatos de datos.",
        "d) Garantizar la recepción de datos en el orden correcto."
    ], "b"),
    ("¿Cuál es una de las funciones del Nivel 5 (Nivel de Sesión) en el modelo OSI?", [
        "a) Controlar el flujo de datos en la red.",
        "b) Gestionar la dirección IP de los dispositivos.",
        "c) Controlar el sincronismo o 'turnos' entre aplicaciones, permitiendo alternar entre ellas.",
        "d) Realizar la compresión de datos en la red."
    ], "c"),
    ("¿Cuál es uno de los mecanismos incluidos en el Nivel 5 (Nivel de Sesión) del modelo OSI?", [
        "a) Establecer la dirección IP de los dispositivos.",
        "b) Controlar el flujo de datos en la red.",
        "c) Gestionar los mecanismos de 'puntos de verificación' en caso de problemas de red o errores en el hardware.",
        "d) Realizar la compresión de datos en la red."
    ], "c"),
    ("¿En qué consisten los mecanismos de 'puntos de verificación' en el Nivel 5 (Nivel de Sesión) del modelo OSI?", [
        "a) Son mecanismos para asegurar que los datos se transmitan en el orden correcto.",
        "b) Son mecanismos para gestionar la sincronización de tramas en la red.",
        "c) Son mecanismos para permitir que múltiples aplicaciones se comuniquen simultáneamente.",
        "d) Son mecanismos para guardar un registro de los datos transmitidos para recuperación en caso de problemas."
    ], "d"),
    ("¿Cuál es la función principal del Nivel 6 (Nivel de Presentación) en el modelo OSI?", [
        "a) Enviar paquetes de datos a través de la red.",
        "b) Traducir los datos a un formato adecuado para su presentación a la capa de aplicación.",
        "c) Gestionar la sincronización de trama en la red.",
        "d) Controlar el flujo de datos extremo a extremo."
    ], "b")




















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
    
    print(f"Has completado el test, {nombre_usuario}. Puntaje final: {puntaje}/{len(preguntas)}")

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
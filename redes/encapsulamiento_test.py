import random

# Lista de preguntas y respuestas
preguntas = [
  ("¿Por qué se divide un mensaje en partes más pequeñas antes de enviarlo a través de una red?", [
        "a) Para aumentar la confiabilidad de las comunicaciones de red.",
        "b) Para asegurarse de que todas las partes sigan el mismo recorrido a través de la red.",
        "c) Para evitar la necesidad de segmentación y multiplexación.",
        "d) Para enviar mensajes más grandes y rápidos.",
    ], "a"),

    ("¿Cuál es el beneficio principal de la segmentación de mensajes en una red?", [
        "a) Evitar la necesidad de enviar mensajes a través de la red.",
        "b) Interconectar muchas conversaciones diversas en la red.",
        "c) Aumentar la complejidad del proceso de comunicación.",
        "d) Garantizar la entrega inmediata del mensaje completo.",
    ], "b"),

    ("¿Qué es la segmentación en el contexto de las redes de datos?", [
        "a) El proceso de enviar un mensaje como un stream de bits continuo.",
        "b) El proceso de intercalar múltiples conversaciones en la red.",
        "c) La división del stream de datos en partes más pequeñas para su transmisión.",
        "d) El proceso de encapsular datos en múltiples capas de protocolos.",
    ], "c"),

    ("¿Por qué la segmentación de mensajes aumenta la confiabilidad de las comunicaciones de red?", [
        "a) Porque asegura que todas las partes del mensaje sigan el mismo recorrido.",
        "b) Porque permite intercalar muchas conversaciones diversas en la red.",
        "c) Porque no se requiere la retransmisión de partes faltantes en caso de error.",
        "d) Porque reduce la complejidad del proceso de comunicación.",
    ], "c"),

    ("¿Qué desventaja presenta la segmentación y la multiplexación en las redes de datos?", [
        "a) Aumenta la confiabilidad de las comunicaciones.",
        "b) Reduce la complejidad del proceso de comunicación.",
        "c) Incrementa la eficiencia de la transmisión de datos.",
        "d) Agrega complejidad al proceso de comunicación.",
    ], "d"),

    ("¿Qué se entiende por una Unidad de Datos del Protocolo (PDU) en el contexto de las redes?", [
        "a) Es una dirección lógica utilizada para encaminar datos en la red.",
        "b) Es una porción de datos en cualquier capa del stack de protocolos.",
        "c) Es una técnica de multiplexación utilizada para combinar múltiples flujos de datos.",
        "d) Es una capa que se utiliza para dividir mensajes en partes más pequeñas.",
    ], "b"),

    ("¿Qué es la encapsulación en el contexto de las comunicaciones de datos?", [
        "a) El proceso de dividir un mensaje en partes más pequeñas.",
        "b) La eliminación de encabezados de protocolo en un dispositivo receptor.",
        "c) El proceso de agregar información adicional del encabezado del protocolo a los datos antes de la transmisión.",
        "d) La traducción de direcciones IP a direcciones MAC de Ethernet.",
    ], "c"),

    ("¿Cuál es el propósito de la dirección de enlace de datos en una red?", [
        "a) Identificar dispositivos en la red local.",
        "b) Facilitar la comunicación con dispositivos en redes remotas.",
        "c) Enviar tramas de enlace de datos a través de la red real.",
        "d) Determinar la dirección IP del dispositivo de destino.",
    ], "a"),

    ("¿Por qué es necesario utilizar una dirección de gateway predeterminado en una red?", [
        "a) Para reducir la complejidad de las comunicaciones de red.",
        "b) Para garantizar la entrega inmediata de mensajes a destinos remotos.",
        "c) Para determinar la dirección MAC de Ethernet del dispositivo de destino.",
        "d) Para reenviar mensajes a redes remotas a través de un router.",
    ], "d"),

    ("¿Qué función cumple el ARP (Protocolo de Resolución de Direcciones) en una red?", [
        "a) Determina la dirección MAC del gateway predeterminado.",
        "b) Divide los mensajes en partes más pequeñas para su transmisión.",
        "c) Encapsula los datos en segmentos de TCP.",
        "d) Descubre la dirección MAC del dispositivo en la misma red local.",
    ], "d"),
    
    ("¿Cuál es la importancia de conocer la dirección MAC de Ethernet de un router en una red?", [
        "a) Permite descubrir la dirección IP de destino del paquete.",
        "b) Facilita la encapsulación de datos en una trama de Ethernet.",
        "c) Es esencial para el reenvío de mensajes a redes remotas.",
        "d) Garantiza que los mensajes se entreguen en la misma red local.",
    ], "c"),

    ("¿Cómo se determina la dirección MAC de Ethernet de un router en una red?", [
        "a) Utilizando el sistema de nombres de dominio (DNS).",
        "b) Configurando la dirección de gateway predeterminado en la NIC del host.",
        "c) Enviando un mensaje de súplica ARP a toda la LAN.",
        "d) Dividiendo los mensajes en partes más pequeñas para su transmisión.",
    ], "c"),

    ("¿Cuál es el rol de un gateway predeterminado en una red?", [
        "a) Encapsular los datos en tramas de Ethernet.",
        "b) Facilitar la comunicación entre dispositivos en la misma red local.",
        "c) Reducir la complejidad del proceso de comunicación.",
        "d) Reenviar mensajes a redes remotas a través de un router.",
    ], "d"),

    ("¿Cómo se envían mensajes a un dispositivo en una red remota en comparación con un dispositivo en la misma red?", [
        "a) Los mensajes se envían directamente al dispositivo receptor utilizando ARP.",
        "b) Los mensajes se envían a través de un switch para llegar al dispositivo de destino en la misma red.",
        "c) Los mensajes se envían directamente al dispositivo receptor utilizando la dirección MAC de Ethernet del receptor.",
        "d) Los mensajes se envían a través del router o gateway predeterminado.",
    ], "d"),

    ("¿Qué funciones cumplen las direcciones de red y las direcciones de enlace de datos al comunicarse con un dispositivo en una red remota?", [
        "a) Las direcciones de enlace de datos indican la red de origen y destino, mientras que las direcciones de red se utilizan para el enrutamiento local.",
        "b) Las direcciones de enlace de datos se utilizan para determinar la dirección IP del dispositivo de destino, mientras que las direcciones de red indican la red de origen y destino.",
        "c) Las direcciones de red indican la dirección de red y host de origen y destino, mientras que las direcciones de enlace de datos se utilizan para enviar la trama de enlace de datos directamente al dispositivo receptor.",
        "d) Las direcciones de enlace de datos se utilizan para encapsular los datos en la trama de Ethernet, mientras que las direcciones de red indican la red de destino.",
    ], "c"),

    ("¿Cómo obtiene un host la dirección MAC de Ethernet del router cuando se comunica con un dispositivo en una red remota?", [
        "a) Utiliza el sistema de nombres de dominio (DNS) para resolver la dirección MAC.",
        "b) La dirección MAC del router se conoce automáticamente a través de un broadcast de ARP.",
        "c) El host debe configurar manualmente la dirección MAC del router en su configuración de TCP/IP.",
        "d) Las direcciones MAC del router no son necesarias en una comunicación con dispositivos en redes remotas.",
    ], "b"),

    ("¿Por qué es esencial configurar la dirección de gateway predeterminado en la configuración de TCP/IP de un host en una red local?", [
        "a) Para garantizar que todos los mensajes se entreguen directamente al dispositivo de destino.",
        "b) Para reducir la complejidad del proceso de comunicación en la red local.",
        "c) Para evitar la necesidad de retransmitir mensajes en caso de error de red.",
        "d) Para habilitar el reenvío de mensajes a redes remotas a través del router.",
    ], "d"),

    ("¿Qué sucede cuando un host en una red local no tiene configurada una dirección de gateway predeterminado?", [
        "a) Los mensajes se envían directamente al dispositivo de destino sin pasar por el router.",
        "b) El host debe configurar manualmente la dirección MAC del dispositivo de destino.",
        "c) Los mensajes se encapsulan en tramas de Ethernet sin dirección de destino.",
        "d) Los mensajes dirigidos a redes remotas no pueden ser entregados.",
    ], "d"),
    
    ("¿Cuál es el propósito principal de las direcciones MAC en una red Ethernet?", [
        "a) Identificar direcciones IP de los hosts en la misma red.",
        "b) Facilitar la comunicación con dispositivos en redes remotas.",
        "c) Enviar tramas de enlace de datos directamente al dispositivo receptor en la misma red.",
        "d) Identificar de forma exclusiva los dispositivos en la red local.",
    ], "d"),

    ("¿Cuál es la función del Protocolo de Resolución de Direcciones (ARP) en una red local?", [
        "a) Divide los mensajes en partes más pequeñas para su transmisión.",
        "b) Determina la dirección MAC del gateway predeterminado.",
        "c) Descubre la dirección MAC del dispositivo en la misma red local.",
        "d) Encapsula los datos en segmentos de TCP.",
    ], "c"),

    ("¿Qué papel desempeña el router en la comunicación entre un dispositivo en una red local y un dispositivo en una red remota?", [
        "a) Enviar mensajes directamente al dispositivo de destino utilizando ARP.",
        "b) Facilitar la comunicación entre dispositivos en la misma red local.",
        "c) Reenviar mensajes a redes remotas a través del gateway predeterminado.",
        "d) Determinar la dirección MAC de Ethernet del dispositivo de destino.",
    ], "c"),

    ("¿Cuál es el paso inicial para que un host pueda comunicarse con un dispositivo en una red remota?", [
        "a) Conocer la dirección MAC de Ethernet del dispositivo de destino.",
        "b) Utilizar ARP para determinar la dirección IP del dispositivo de destino.",
        "c) Configurar manualmente la dirección de gateway predeterminado.",
        "d) Dividir los mensajes en partes más pequeñas para su transmisión.",
    ], "b"),

    ("¿Por qué se envía un mensaje de súplica ARP a toda la LAN cuando un host necesita determinar la dirección MAC de Ethernet de un dispositivo en la misma red?", [
        "a) Para configurar manualmente la dirección MAC del dispositivo de destino.",
        "b) Para garantizar que los mensajes se entreguen directamente al dispositivo de destino.",
        "c) Para descubrir la dirección MAC del dispositivo que tiene la misma dirección IP en la solicitud de ARP.",
        "d) Para reducir la complejidad del proceso de comunicación en la red local.",
    ], "c"),
    
    ("¿Qué función cumple la dirección de gateway predeterminado en una red local?", [
        "a) Facilitar la comunicación con dispositivos en la misma red local.",
        "b) Reducir la complejidad del proceso de comunicación.",
        "c) Determinar la dirección MAC de Ethernet del dispositivo de destino.",
        "d) Habilitar el reenvío de mensajes a redes remotas a través del router.",
    ], "d"),

    ("¿Cómo se determina la dirección MAC de Ethernet de un router en una red local?", [
        "a) Configurando la dirección MAC en el host que necesita comunicarse con el router.",
        "b) Utilizando el sistema de nombres de dominio (DNS).",
        "c) Enviando una solicitud de ARP al dispositivo de destino.",
        "d) Utilizando la dirección de gateway predeterminado configurada en el host.",
    ], "d"),

    ("¿Cuál es el propósito de conocer la dirección MAC de Ethernet de un router en una red local?", [
        "a) Permite descubrir la dirección IP del dispositivo de destino del paquete.",
        "b) Facilita la encapsulación de datos en una trama de Ethernet.",
        "c) Habilita el reenvío de mensajes a través del router a redes remotas.",
        "d) Garantiza la entrega inmediata de mensajes a destinos remotos.",
    ], "c"),

    ("¿Por qué es esencial configurar la dirección de gateway predeterminado en la configuración de TCP/IP de un host en una red local?", [
        "a) Para evitar la necesidad de retransmitir mensajes en caso de error de red.",
        "b) Para reducir la complejidad del proceso de comunicación en la red local.",
        "c) Para garantizar que todos los mensajes se entreguen directamente al dispositivo de destino.",
        "d) Para permitir la comunicación con dispositivos en otras redes locales.",
    ], "d"),
        ("¿Qué beneficios principales ofrece la segmentación de mensajes en las comunicaciones de red?", [
        "a) Aumenta la complejidad del proceso de comunicación.",
        "b) Permite enviar mensajes más grandes a través de la red.",
        "c) Facilita la multiplexación de conversaciones en la red.",
        "d) Aumenta la probabilidad de pérdida de datos en la transmisión.",
    ], "c"),

    ("¿Cuál es el propósito de la encapsulación de datos en las comunicaciones de red?", [
        "a) Añadir información adicional al encabezado del protocolo antes de la transmisión.",
        "b) Reducir el tamaño de los mensajes para una transmisión más rápida.",
        "c) Eliminar el encabezado del protocolo antes de la transmisión.",
        "d) Cambiar las direcciones IP de origen y destino de los mensajes.",
    ], "a"),

    ("¿Qué función tiene la dirección de enlace de datos en una red?", [
        "a) Indicar la dirección IP de origen de un paquete.",
        "b) Encapsular un paquete IP para su transmisión a través del medio físico.",
        "c) Determinar el protocolo de capa de red utilizado.",
        "d) Identificar el prefijo de red de una dirección IP.",
    ], "b"),

    ("¿Cómo se denomina el protocolo utilizado para descubrir la dirección MAC de un host en la misma red local?", [
        "a) ARP (Protocolo de Resolución de Direcciones).",
        "b) DNS (Sistema de Nombres de Dominio).",
        "c) HTTP (Protocolo de Transferencia de Hipertexto).",
        "d) IP (Protocolo de Internet).",
    ], "a"),

    ("¿Cuál es la función del gateway predeterminado en una red?", [
        "a) Determinar la dirección IP de destino de un mensaje.",
        "b) Enviar mensajes directamente al host de destino en la misma red local.",
        "c) Reenviar mensajes a una red remota utilizando un router.",
        "d) Convertir direcciones IP en direcciones MAC de Ethernet.",
    ], "c"),

    ("¿Cómo se utiliza ARP para determinar la dirección MAC del gateway predeterminado?", [
        "a) El dispositivo emite un mensaje de solicitud de ARP a toda la LAN.",
        "b) El dispositivo envía un mensaje de respuesta de ARP al router.",
        "c) El dispositivo busca la información en una base de datos local.",
        "d) El router envía una solicitud de ARP al dispositivo.",
    ], "a"),

    ("¿Por qué la dirección de gateway predeterminado es importante en una configuración de red?", [
        "a) Para identificar la dirección MAC del host de destino.",
        "b) Para establecer una conexión directa entre dispositivos en la misma red.",
        "c) Para enrutar paquetes a redes remotas a través del router.",
        "d) Para descubrir la dirección IP del dispositivo emisor.",
    ], "c"),

    ("¿Cuál es el propósito de la dirección MAC de destino en una trama Ethernet cuando un dispositivo se comunica con una red remota?", [
        "a) Identificar el dispositivo emisor.",
        "b) Indicar la dirección IP de origen del paquete.",
        "c) Enviar la trama directamente al host de destino.",
        "d) Facilitar la comunicación en la misma red local.",
    ], "c"),

    ("¿Qué ocurre cuando un dispositivo necesita enviar un mensaje a una red remota en lugar de a una red local?", [
        "a) El mensaje se envía directamente al host de destino en la red remota.",
        "b) La trama de Ethernet se descarta en el dispositivo emisor.",
        "c) El mensaje se reenvía a través del gateway predeterminado.",
        "d) La dirección MAC de destino se convierte en la dirección IP de destino.",
    ], "c"),

    ("¿Cómo determina un dispositivo emisor la dirección MAC del gateway predeterminado cuando se comunica con una red remota?", [
        "a) Mediante el protocolo DNS.",
        "b) A través de una búsqueda en una base de datos centralizada.",
        "c) Utilizando ARP para descubrir la dirección MAC del router.",
        "d) Configurando manualmente la dirección MAC del router.",
    ], "c"),

    ("¿Cuál es el propósito de las direcciones MAC en una trama Ethernet cuando un dispositivo se comunica con una red remota?", [
        "a) Identificar la dirección IP de origen del paquete.",
        "b) Indicar el tipo de protocolo utilizado en la red.",
        "c) Facilitar la comunicación en la misma red local.",
        "d) Determinar la ubicación física del dispositivo emisor.",
    ], "d"),

    ("¿Cuál es el protocolo utilizado para descubrir la dirección MAC del gateway predeterminado?", [
        "a) HTTP",
        "b) DNS",
        "c) ARP",
        "d) TCP",
    ], "c"),

    ("¿Qué información se encuentra en la respuesta de ARP enviada por el gateway predeterminado?", [
        "a) Dirección MAC de destino.",
        "b) Dirección IP de origen.",
        "c) Dirección MAC de origen.",
        "d) Dirección IP de destino.",
    ], "a"),

    ("¿Qué sucede cuando un dispositivo no tiene una dirección de gateway predeterminado configurada?", [
        "a) Los mensajes se envían directamente al host de destino en la red remota.",
        "b) No se pueden entregar mensajes a redes remotas.",
        "c) El dispositivo utiliza un gateway predeterminado predeterminado.",
        "d) Los mensajes se envían a una dirección IP específica.",
    ], "b"),

    ("¿Cómo se determina la dirección MAC del router al que se envía un mensaje en una red remota?", [
        "a) La dirección MAC se establece manualmente en la trama Ethernet.",
        "b) El dispositivo emisor utiliza el protocolo HTTP para obtener la información.",
        "c) El dispositivo utiliza ARP para descubrir la dirección MAC del gateway predeterminado.",
        "d) La dirección MAC se encuentra en el encabezado IP del paquete.",
    ], "c"),

    ("¿Qué función desempeña el router al recibir una trama de Ethernet en una red remota?", [
        "a) Descarta la trama si no coincide con la dirección MAC de destino.",
        "b) Convierte la dirección IP de destino en la dirección MAC de Ethernet.",
        "c) Reenvía la trama al host de destino en la misma red local.",
        "d) Envia la trama a través de una VPN para mayor seguridad.",
    ], "b"),

    ("¿Cuál es el propósito del protocolo ARP en una red local?", [
        "a) Establecer conexiones seguras entre dispositivos.",
        "b) Descubrir la dirección IP de los hosts en la misma red local.",
        "c) Gestionar las direcciones IP de los dispositivos en una red remota.",
        "d) Determinar la ubicación física de los dispositivos en Internet.",
    ], "b"),

    ("¿Qué información contiene una solicitud de ARP enviada por un dispositivo en una red local?", [
        "a) Dirección IP de destino.",
        "b) Dirección MAC de origen.",
        "c) Dirección IP de origen.",
        "d) Dirección MAC de destino.",
    ], "c"),

    ("¿Por qué es importante configurar correctamente la dirección de gateway predeterminado en un dispositivo?", [
        "a) Para asegurar que el dispositivo utilice la dirección IP correcta.",
        "b) Para determinar la dirección MAC del router.",
        "c) Para permitir la comunicación con hosts de redes remotas.",
        "d) Para enrutar paquetes a la red local.",
    ], "c"),

    ("¿Qué ocurre cuando un dispositivo en una red local no tiene una dirección de gateway predeterminado configurada?", [
        "a) Los mensajes se envían directamente al host de destino en la red local.",
        "b) Los mensajes se envían a una dirección IP específica.",
        "c) No se pueden entregar mensajes a redes remotas.",
        "d) Los mensajes se reenvían al servidor DNS de la red.",
    ], "c"),

    ("¿Cuál es el papel de la dirección MAC de destino en una trama Ethernet cuando se comunica con una red remota?", [
        "a) Determinar la dirección IP de origen del paquete.",
        "b) Facilitar la comunicación en la misma red local.",
        "c) Indicar el tipo de protocolo utilizado en la red.",
        "d) Enviar la trama al host de destino en la red local.",
    ], "d"),

    ("¿Cuál es el protocolo utilizado para descubrir la dirección MAC del gateway predeterminado?", [
        "a) HTTP",
        "b) DNS",
        "c) ARP",
        "d) TCP",
    ], "c"),

    ("¿Qué sucede cuando un dispositivo no tiene una dirección de gateway predeterminado configurada?", [
        "a) Los mensajes se envían directamente al host de destino en la red remota.",
        "b) No se pueden entregar mensajes a redes remotas.",
        "c) El dispositivo utiliza un gateway predeterminado predeterminado.",
        "d) Los mensajes se envían a una dirección IP específica.",
    ], "b"),
        ("¿Qué función desempeñan las direcciones IP en las comunicaciones de red?", [
        "a) Identificar la dirección física del dispositivo emisor.",
        "b) Facilitar la transmisión de paquetes entre dispositivos en una misma red local.",
        "c) Determinar la ubicación geográfica de los dispositivos en la red.",
        "d) Indicar la dirección lógica del dispositivo y su ubicación en la red.",
    ], "d"),

    ("¿Cuál es el propósito de la dirección MAC de origen en una trama Ethernet?", [
        "a) Identificar el dispositivo emisor.",
        "b) Determinar la dirección IP de destino.",
        "c) Facilitar la comunicación en la misma red local.",
        "d) Indicar el tipo de protocolo utilizado en la red.",
    ], "a"),

    ("¿Cómo se llama el proceso de envío de un mensaje a través de la red desde el host emisor hasta el host de destino?", [
        "a) Enrutamiento",
        "b) Encapsulación",
        "c) Multiplexación",
        "d) Transmisión",
    ], "a"),

    ("¿Cuál es la función principal de la capa de red en el modelo OSI?", [
        "a) Proporcionar una interfaz para las aplicaciones de usuario.",
        "b) Controlar la multiplexación de conversaciones en la red.",
        "c) Determinar la mejor ruta para la transmisión de datos.",
        "d) Gestionar la comunicación entre dispositivos en la misma red local.",
    ], "c"),

    ("¿Qué hace la capa de transporte en el modelo OSI?", [
        "a) Controla el acceso al medio de transmisión.",
        "b) Multiplexa las conversaciones en la red.",
        "c) Define el formato de los datos de la aplicación.",
        "d) Encapsula los datos en segmentos para su transmisión.",
    ], "b"),

    ("¿Cuál es el propósito de la capa de enlace de datos en el modelo OSI?", [
        "a) Proporcionar servicios de aplicación a los usuarios finales.",
        "b) Establecer la conexión física entre dispositivos en la misma red local.",
        "c) Gestionar el enrutamiento de paquetes a través de la red.",
        "d) Controlar el flujo de datos entre dispositivos en la red.",
    ], "b"),

    ("¿Qué es una PDU en el contexto de las comunicaciones de red?", [
        "a) Un protocolo de comunicación.",
        "b) Una dirección de enlace de datos.",
        "c) Una unidad de datos del protocolo.",
        "d) Una aplicación de red.",
    ], "c"),

    ("¿Qué tipo de PDU se utiliza en la capa de enlace de datos de un modelo de referencia?", [
        "a) Paquete",
        "b) Trama",
        "c) Segmento",
        "d) Datos",
    ], "b"),

    ("¿Cuál es la función de la dirección MAC de destino en una trama Ethernet?", [
        "a) Determinar el dispositivo emisor del paquete IP.",
        "b) Facilitar la comunicación en la misma red local.",
        "c) Indicar la dirección IP de origen del paquete.",
        "d) Enviar la trama directamente al host de destino.",
    ], "d"),

    ("¿Qué ocurre cuando un host de una red local necesita enviar un mensaje a un host en una red remota?", [
        "a) El host envía la trama de Ethernet directamente al host de destino en la red remota.",
        "b) La trama se descarta en el host emisor.",
        "c) El host reenvía la trama al gateway predeterminado.",
        "d) La dirección MAC de destino se convierte en la dirección IP de destino.",
    ], "c"),

    ("¿Qué protocolo se utiliza para descubrir la dirección MAC de un router en una red local?", [
        "a) DNS",
        "b) HTTP",
        "c) ARP",
        "d) TCP",
    ], "c"),

    ("¿Cómo se determina la dirección MAC del gateway predeterminado cuando un host se comunica con una red remota?", [
        "a) Configurando manualmente la dirección MAC del router.",
        "b) Utilizando el protocolo DNS para obtener la información.",
        "c) A través de una búsqueda en una base de datos centralizada.",
        "d) Mediante ARP para descubrir la dirección MAC del gateway predeterminado.",
    ], "d"),

    ("¿Cuál es la función del router al recibir una trama de Ethernet en una red remota?", [
        "a) Descarta la trama si no coincide con la dirección MAC de destino.",
        "b) Convierte la dirección IP de destino en la dirección MAC de Ethernet.",
        "c) Reenvía la trama al host de destino en la misma red local.",
        "d) Envia la trama a través de una VPN para mayor seguridad.",
    ], "b"),

    ("¿Qué rol cumple el protocolo ARP en una red local?", [
        "a) Establecer conexiones seguras entre dispositivos.",
        "b) Descubrir la dirección IP de los hosts en la misma red local.",
        "c) Gestionar las direcciones IP de los dispositivos en una red remota.",
        "d) Determinar la ubicación física de los dispositivos en Internet.",
    ], "b"),

    ("¿Qué información contiene una solicitud de ARP enviada por un dispositivo en una red local?", [
        "a) Dirección IP de destino.",
        "b) Dirección MAC de origen.",
        "c) Dirección IP de origen.",
        "d) Dirección MAC de destino.",
    ], "c"),

    ("¿Por qué es importante configurar correctamente la dirección de gateway predeterminado en un dispositivo?", [
        "a) Para asegurar que el dispositivo utilice la dirección IP correcta.",
        "b) Para determinar la dirección MAC del router.",
        "c) Para permitir la comunicación con hosts de redes remotas.",
        "d) Para enrutar paquetes a la red local.",
    ], "c"),
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
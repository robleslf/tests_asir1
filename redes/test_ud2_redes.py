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
        "c) Encapsular datos en paquetes para la transmisión.",
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
    ], "b"),
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
    ], "b"),
    ("¿Cuál es una de las funciones clave del Nivel 6 (Nivel de Presentación) en el modelo OSI?", [
        "a) Gestionar el encaminamiento de los paquetes en la red.",
        "b) Traducir datos de un formato utilizado por la capa de aplicación en el equipo origen a un formato común y luego a un formato conocido por la capa de aplicación del equipo destino.",
        "c) Realizar la detección y corrección de errores en las tramas de datos.",
        "d) Controlar la sincronización de trama en la red."
    ], "b"),
    ("¿Cuál de las siguientes funciones se incluyen en la capa de Presentación (Nivel 6) del modelo OSI?", [
        "a) Traducir distintos formatos de representación de la información, comprimir datos y cifrar datos por motivos de seguridad.",
        "b) Encaminar los paquetes en la red.",
        "c) Controlar la sincronización de trama en la red.",
        "d) Realizar el control de flujo en la red.",
    ], "a"),
    ("¿Cuál de las siguientes funciones se realiza en la capa de Presentación (Nivel 6) del modelo OSI?", [
        "a) Encaminar los paquetes en la red.",
        "b) Controlar la sincronización de trama en la red.",
        "c) Traducir distintos formatos de representación de la información, como de ASCII a EBCDIC.",
        "d) Realizar el control de flujo en la red.",
    ], "c"),
    ("¿Cuál de las siguientes funciones se realiza en la capa de Presentación (Nivel 6) del modelo OSI?", [
        "a) Encaminar los paquetes en la red.",
        "b) Controlar la sincronización de trama en la red.",
        "c) Realizar la compresión de datos para reducir el número de bits transmitidos en la red.",
        "d) Gestionar las direcciones IP en la red.",
    ], "c"),
    ("¿Qué función se lleva a cabo en la capa de Presentación (Nivel 6) del modelo OSI?", [
        "a) Controlar la sincronización de trama en la red.",
        "b) Realizar presentaciones PowerPoint.",
        "c) Unir bits en líneas de código.",
        "d) Cifrar los datos por razones de seguridad.",
    ], "d"),
    ("¿Qué tipo de aplicaciones se encuentran típicamente en el Nivel de Aplicación (Nivel 7) del modelo OSI?", [
        "a) Aplicaciones dirigidas a la infraestructura de red.",
        "b) Aplicaciones dirigidas al usuario final.",
        "c) Herramientas de diagnóstico de red.",
        "d) Sistemas operativos de servidores.",
    ], "b"),
    ("¿Qué caracteriza al Nivel de Aplicación (Nivel 7) del modelo OSI en términos de los servicios que ofrece?", [
        "a) Ofrece servicios únicamente a otros niveles en el modelo OSI.",
        "b) Ofrece servicios tanto a otros niveles como al usuario final.",
        "c) Ofrece servicios de seguridad y cifrado de datos únicamente.",
        "d) Ofrece servicios solamente al usuario.",
    ], "d"),
    ("¿Cuál es la principal característica del Nivel de Aplicación (Nivel 7) en el modelo OSI en relación con el acceso a información o servicios distribuidos?", [
        "a) Proporciona servicios de cifrado para proteger la privacidad de los datos.",
        "b) Ofrece servicios a otros niveles del modelo OSI.",
        "c) No ofrece servicios a otros niveles sino solo al usuario.",
        "d) Permite que para el usuario sea transparente el hecho de que se esté teniendo acceso a información o servicios distribuidos.",
    ], "d"),
     ("¿Qué tipo de aplicaciones se encuentran en el Nivel de Aplicación (Nivel 7) del modelo OSI?", [
    "a) Aplicaciones finales del usuario y protocolos estandarizados como HTTP, FTP, LDAP, SMTP, entre otros.",
    "b) Solo aplicaciones finales del usuario.",
    "c) Solo aplicaciones de carácter transitorio.",
    "d) Solo aplicaciones de sistemas operativos.",
    ], "a"),
    ("¿Cuál es la principal función del Nivel de Aplicación (Nivel 7) en el modelo OSI?", [
        "a) Proporcionar servicios a otros niveles del modelo OSI.",
        "b) Ofrecer servicios solo al usuario final.",
        "c) Realizar la compresión de datos antes de su transmisión.",
        "d) Controlar el flujo extremo a extremo de los datos.",
    ], "b"),
    ("¿Qué caracteriza a los protocolos de la arquitectura TCP/IP en relación a la comunicación en redes de gran escala?", [
        "a) Están diseñados exclusivamente para redes de pequeña escala.",
        "b) Se centran en la resolución de nombres de equipo.",
        "c) Permite la comunicación en redes de gran escala.",
        "d) Funcionan de forma teórica sin aplicaciones prácticas."
    ], "c"),
    ("¿Cuál es una de las actividades realizadas por los protocolos de la pila TCP/IP para que la comunicación en la red sea exitosa?", [
        "a) Resolución de nombres de equipo.",
        "b) Compresión de datos.",
        "c) Determinación de la ubicación del equipo de destino.",
        "d) Uso exclusivo en sistemas operativos."
    ], "a"),
    ("¿Cuál es uno de los usos más destacados de TCP/IP en la actualidad?", [
        "a) Comunicación en redes de gran tamaño.",
        "b) Traducción de formatos de datos.",
        "c) Cifrado de datos.",
        "d) Resolución de nombres de equipo."
    ], "a"),
    ("¿Qué arquitectura de red es la más ampliamente aceptada y utilizada en la actualidad?", [
        "a) OSI",
        "b) TCP/IP",
        "c) Ethernet",
        "d) Token Ring"
    ], "b"),
    ("¿Por qué la mayoría de los sistemas operativos en uso hoy en día ofrecen soporte para TCP/IP?", [
        "a) Porque TCP/IP es una arquitectura de red obsoleta y requiere un soporte especial.",
        "b) Porque TCP/IP es ampliamente utilizado y es esencial para la comunicación en redes modernas.",
        "c) Porque TCP/IP es exclusivo de sistemas Windows.",
        "d) Porque TCP/IP es más barato que otras arquitecturas de red."
    ], "b"),
    ("¿Qué describe mejor la arquitectura TCP/IP?", [
        "a) Un conjunto de protocolos obsoletos para comunicación en redes locales.",
        "b) Una pila de protocolos estándar ampliamente utilizada para la comunicación entre equipos en redes de gran escala.",
        "c) Un sistema de enrutamiento de tráfico de red utilizado exclusivamente en sistemas Windows.",
        "d) Una arquitectura de red que solo se utiliza en redes pequeñas."
    ], "b"),
    ("¿Cuál es la función principal de los diversos protocolos en la pila TCP/IP?", [
        "a) Funcionan de manera aislada y no tienen relación entre sí.",
        "b) Trabajan en conjunto para permitir la comunicación efectiva en la red.",
        "c) Controlan la velocidad de transmisión de datos en la red.",
        "d) Son exclusivos de sistemas Windows."
    ], "b"),
    ("Dentro del proceso de comunicación en la arquitectura TCP/IP, ¿cuál es el propósito de la 'resolución de nombres de equipo a direcciones IP'?", [
        "a) Establecer diálogo entre aplicaciones en el nivel de sesión.",
        "b) Comprimir datos para reducir la velocidad de transmisión en la red.",
        "c) Determinar la ubicación del equipo de destino.",
        "d) Convertir datos de formato ASCII a EBCDIC."
    ], "c"),
    (
    "En la arquitectura TCP/IP, ¿qué papel desempeñan los distintos protocolos de la pila TCP/IP en el proceso de comunicación?",
    [
        "a) Todos los protocolos tienen el mismo papel y realizan las mismas funciones.",
        "b) Cada protocolo tiene un papel distinto en el proceso de comunicación.",
        "c) Los protocolos TCP/IP no desempeñan ningún papel en la comunicación de datos.",
        "d) Solo un protocolo es responsable de todo el proceso de comunicación."
    ], "b"),
    ("¿Cuántas capas conforman el modelo de comunicación de TCP/IP para transmitir datos de una ubicación a otra?", [
        "a) 3 capas",
        "b) 4 capas",
        "c) 5 capas",
        "d) 7 capas"
    ], "b"),
    ("¿En qué capa de la pila TCP/IP se encuentran todas las aplicaciones y utilidades que utilizan esta capa para obtener acceso a la red?", [
        "a) Capa de aplicación",
        "b) Capa de transporte",
        "c) Capa de Internet",
        "d) Capa de interfaz de red"
    ], "a"),
    ("La capa de aplicaciones de la pila TCP/IP se encarga de formatear e intercambiar información de usuario. ¿En qué capa se encuentran los protocolos utilizados para este propósito?", [
        "a) Capa de aplicación",
        "b) Capa de transporte",
        "c) Capa de Internet",
        "d) Capa de interfaz de red"
    ], "a"),
    ("¿Qué significa la sigla 'HTTP' y para qué se utiliza en el contexto de la World Wide Web?", [
        "a) Hypertext Transfer Protocol, se utiliza para transferir archivos de imágenes en la web.",
        "b) Hyperlink Text Transfer Protocol, se utiliza para transmitir archivos de texto en línea.",
        "c) Hypertext Transfer Protocol, se utiliza para transferir los archivos que componen las páginas web de la World Wide Web.",
        "d) High-Tech Transport Protocol, se utiliza para transferir aplicaciones de alta tecnología a través de la web."
    ], "c"),
    ("¿Qué significa la sigla 'FTP' y para qué se utiliza en el contexto de la transferencia de archivos?", [
        "a) File Transmission Protocol, se utiliza para la transmisión de archivos de audio en línea.",
        "b) Fast Transfer Protocol, se utiliza para la transferencia rápida de datos en redes locales.",
        "c) File Transfer Protocol, se utiliza para la transferencia interactiva de archivos.",
        "d) Free Text Protocol, se utiliza para el intercambio gratuito de mensajes de texto en línea."
    ], "c"),
    ("¿Cuál es la función principal de la capa de Transporte en la pila TCP/IP?", [
        "a) Proporcionar seguridad a las comunicaciones de red.",
        "b) Ordenar y garantizar la comunicación entre equipos.",
        "c) Administrar el direccionamiento IP de los dispositivos.",
        "d) Realizar el enrutamiento de datos a través de la red."
    ], "b"),
    ("Además de garantizar la comunicación entre equipos, ¿qué otra función importante realiza la capa de Transporte en la pila TCP/IP?", [
        "a) Controlar la velocidad de transmisión de datos.",
        "b) Administrar la dirección IP de los dispositivos.",
        "c) Proporcionar seguridad a las comunicaciones de red.",
        "d) Especificar el identificador único de la aplicación a la que deben entregarse los datos."
    ], "d"),
    ("En la capa de Transporte de la pila TCP/IP, existen dos protocolos principales que controlan el método de entrega de datos. ¿Cuáles son estos protocolos y cuál es su diferencia principal en cuanto a la entrega de datos?", [
        "a) TCP y FTP; ambos garantizan la entrega de datos mediante acuse de recibo.",
        "b) TCP e IP; ambos proporcionan una rápida entrega de datos, pero no la garantizan.",
        "c) TCP y UDP; TCP garantiza la entrega de datos mediante acuse de recibo, mientras que UDP proporciona una entrega rápida de datos, pero no la garantiza.",
        "d) HTTP y FTP; ambos están diseñados para la transferencia de archivos en línea."
    ], "c"),
    ("¿Qué característica fundamental del Protocolo de control de transmisión (TCP) en la capa de Transporte de la pila TCP/IP lo distingue en términos de la entrega de datos?", [
        "a) TCP garantiza una rápida entrega de datos.",
        "b) TCP garantiza la entrega de datos mediante acuse de recibo.",
        "c) TCP proporciona una entrega rápida de datos, pero no la garantiza.",
        "d) TCP solo se utiliza para la transferencia de archivos."
    ], "b"),
    ("En la capa de Transporte de la pila TCP/IP, el Protocolo de datagramas de usuario (UDP) se destaca por una característica específica en términos de la entrega de datos. ¿Cuál es esa característica?", [
        "a) UDP garantiza la entrega de datos mediante acuse de recibo.",
        "b) UDP proporciona una entrega rápida de datos y garantiza su entrega.",
        "c) UDP proporciona una rápida entrega de los datos, pero no la garantiza.",
        "d) UDP se utiliza exclusivamente para la transferencia de archivos grandes."
    ], "c"),
    ("¿Cuál es la principal responsabilidad de la capa de Internet en la pila TCP/IP?", [
        "a) Garantizar la seguridad de las comunicaciones de red.",
        "b) Proporcionar una interfaz de usuario para la navegación web.",
        "c) Direccionar, empaquetar y enrutar los datos a transmitir.",
        "d) Administrar los servicios de correo electrónico."
    ], "c"),
    ("La capa de Internet en la pila TCP/IP contiene cuatro protocolos principales. ¿Cuál de los siguientes es responsable de direccionar los datos a transmitir y enviarlos a su destino?", [
        "a) Protocolo Internet (Internet Protocol, IP)",
        "b) Protocolo de resolución de direcciones (Address Resolution Protocol, ARP)",
        "c) Protocolo de mensajes de control en Internet (Internet Control Message Protocol, ICMP)",
        "d) Protocolo de administración de grupos de Internet (Internet Group Management Protocol, IGMP)"
    ], "a"),
    ("Dentro de la capa de Internet en la pila TCP/IP, ¿cuál de los siguientes protocolos es el responsable de direccionar los datos a transmitir y enviarlos a su destino?", [
        "a) Protocolo Internet (Internet Protocol, IP)",
        "b) Protocolo de resolución de direcciones (Address Resolution Protocol, ARP)",
        "c) Protocolo de mensajes de control en Internet (Internet Control Message Protocol, ICMP)",
        "d) Protocolo de administración de grupos de Internet (Internet Group Management Protocol, IGMP)"
    ], "a"),
    ("Dentro de la capa de Internet en la pila TCP/IP, ¿cuál de los siguientes protocolos es responsable de identificar la dirección MAC (media access control) del adaptador de red del equipo de destino?", [
        "a) Protocolo Internet (Internet Protocol, IP)",
        "b) Protocolo de resolución de direcciones (Address Resolution Protocol, ARP)",
        "c) Protocolo de mensajes de control en Internet (Internet Control Message Protocol, ICMP)",
        "d) Protocolo de administración de grupos de Internet (Internet Group Management Protocol, IGMP)"
    ], "b"),
    ("Dentro de la capa de Internet en la pila TCP/IP, ¿cuál de los siguientes protocolos es responsable de proporcionar funciones de diagnóstico e información de errores debidos a la entrega incorrecta de datos?", [
        "a) Protocolo Internet (Internet Protocol, IP)",
        "b) Protocolo de resolución de direcciones (Address Resolution Protocol, ARP)",
        "c) Protocolo de mensajes de control en Internet (Internet Control Message Protocol, ICMP)",
        "d) Protocolo de administración de grupos de Internet (Internet Group Management Protocol, IGMP)"
    ], "c"),
    ("Dentro de la capa de Internet en la pila TCP/IP, ¿cuál de los siguientes protocolos es responsable de la administración de la multidifusión en TCP/IP?", [
        "a) Protocolo Internet (Internet Protocol, IP)",
        "b) Protocolo de resolución de direcciones (Address Resolution Protocol, ARP)",
        "c) Protocolo de mensajes de control en Internet (Internet Control Message Protocol, ICMP)",
        "d) Protocolo de administración de grupos de Internet (Internet Group Management Protocol, IGMP)"
    ], "d"),
    ("¿Cuál es la principal responsabilidad de la capa de Interfaz de red en la pila TCP/IP?", [
        "a) Administrar los servicios de correo electrónico.",
        "b) Proporcionar una interfaz de usuario para la navegación web.",
        "c) Enviar los datos en el medio físico de la red y recibir datos desde el mismo.",
        "d) Proporcionar seguridad a las comunicaciones de red."
    ], "c"),
    ("¿Cuál de las siguientes afirmaciones describe mejor la capa de Interfaz de red en la pila TCP/IP?", [
        "a) Contiene protocolos para la transferencia de archivos en línea.",
        "b) Proporciona una interfaz de usuario para la navegación web.",
        "c) No contiene el tipo de protocolos incluidos en las otras tres capas.",
        "d) Garantiza la entrega de datos en la red."
    ], "c"),
    ("En la capa de Interfaz de red de la pila TCP/IP, ¿cuál es el propósito principal según la arquitectura TCP/IP?", [
        "a) Incluir todos aquellos estándares y protocolos de niveles de enlace y físico capaces de transmitir paquetes IP, como Ethernet, redes Wifi, ATM, Frame Relay, X.25, e incluso palomas mensajeras (RFC 1149)",
        "b) Proporcionar una interfaz de usuario para la navegación web.",
        "c) Garantizar la entrega de datos en la red.",
        "d) Administrar los servicios de correo electrónico."
    ], "a"),
    ("¿Cuál fue la visión inicial detrás del modelo OSI (Open Systems Interconnection)?", [
        "a) Establecer un conjunto de protocolos propietarios para redes internacionales.",
        "b) Proporcionar un marco para crear un conjunto de protocolos abiertos que no dependieran de sistemas propietarios.",
        "c) Crear una red internacional basada en sistemas propietarios.",
        "d) Desarrollar una red internacional sin ningún protocolo."
    ], "b"),
    ("A pesar de sus objetivos iniciales, ¿por qué el modelo OSI llegó tarde y no pudo igualar la velocidad de adopción y expansión de Internet basada en TCP/IP?", [
        "a) Debido a la falta de apoyo de la industria de la tecnología.",
        "b) Porque OSI fue diseñado como un conjunto de protocolos propietarios.",
        "c) La velocidad de adopción de Internet basada en TCP/IP superó la de OSI.",
        "d) Porque OSI no ofrecía ventajas técnicas sobre TCP/IP."
    ], "c"),
    ("A pesar de que pocos de los protocolos desarrollados según las especificaciones OSI se utilizan ampliamente en la actualidad, ¿qué contribución importante ha realizado el modelo OSI de siete capas para el desarrollo de otros protocolos y productos en diversas redes?", [
        "a) El modelo OSI no ha tenido un impacto significativo en el desarrollo de otros protocolos o productos para redes.",
        "b) El modelo OSI ha dominado la industria de redes y ha reemplazado por completo a otros modelos.",
        "c) El modelo OSI ha sido ampliamente adoptado como el único estándar para todas las redes.",
        "d) El modelo OSI ha realizado aportes importantes para el desarrollo de otros protocolos y productos en diversas redes."
    ], "d"),
    ("Los elementos de una red de datos y telecomunicaciones son:", [
        "a) Host, medios, adaptador de red, armario de distribución, panel de parcheo, elementos de conexión y guiado, electrónica de red.",
        "b) Computadoras y routers.",
        "c) Host, cables de alimentación, y elementos de red.",
        "d) Dispositivos finales, nodos, dispositivos finales y conectores de red."
    ], "a"),
    ("En una red de datos y telecomunicaciones, ¿cuál es la descripción más adecuada de los 'hosts'?", [
        "a) Son los equipos que se conectan directamente a un segmento de red: computadoras, impresoras, escáner, otros dispositivos...",
        "b) Son los cables de alimentación utilizados para conectar los dispositivos a la red.",
        "c) Son los servidores que administran la red de datos y telecomunicaciones.",
        "d) Son los elementos de conexión utilizados para enrutar los datos en la red."
    ], "a"),
    ("¿Cuál es la función principal de los 'hosts' en una red de datos y telecomunicaciones?", [
        "a) Suministran a los usuarios conexión a la red, por medio de la cual se comparte, crea y obtiene información.",
        "b) Son cables de alimentación utilizados para conectar los dispositivos a la red.",
        "c) Son los servidores que administran la red de datos y telecomunicaciones.",
        "d) Son los elementos de conexión utilizados para enrutar los datos en la red."
    ], "a"),
    ("¿Existe una simbología estandarizada para representar los 'hosts' en una red de datos y telecomunicaciones?", [
        "a) Sí, existe una simbología estandarizada para representar los 'hosts'.",
        "b) No, no existe una simbología estandarizada para representar los 'hosts'.",
        "c) La simbología para 'hosts' varía según el fabricante de la red.",
        "d) La simbología de 'hosts' depende del tipo de dispositivo conectado."
    ], "b"),
    ("¿En qué capa específica de las 7 capas del modelo OSI se ubican los 'hosts' en una red de datos y telecomunicaciones?", [
        "a) Los 'hosts' no forman parte de ninguna capa en especial y operan dentro de las 7 capas.",
        "b) Los 'hosts' se ubican principalmente en la capa de Enlace de Datos.",
        "c) Los 'hosts' se ubican en la capa de Red del modelo OSI.",
        "d) Los 'hosts' operan exclusivamente en la capa de Aplicación del modelo OSI."
    ], "a"),
    ("En una red de datos y telecomunicaciones, ¿cuál es la función principal de los 'medios'?", [
        "a) Los medios son los que transportan la información.",
        "b) Los medios son dispositivos de almacenamiento de datos en la red.",
        "c) Los medios son servidores que gestionan la comunicación en la red.",
        "d) Los medios son cables de alimentación para dispositivos en la red."
    ], "a"),
    ("Cuando se seleccionan los 'medios' para una red de datos y telecomunicaciones, ¿qué factores se deben tener en cuenta?", [
        "a) La velocidad de la red y el tipo de hardware de los hosts.",
        "b) La simbología estandarizada y el fabricante de la red.",
        "c) La disponibilidad de servidores y la capacidad de almacenamiento.",
        "d) Se debe tener en cuenta la longitud del cable, el costo, la facilidad de instalación y la cantidad de computadoras."
    ], "d"),
    ("Dentro de los 'medios' utilizados en una red de datos y telecomunicaciones, ¿cuál de las siguientes opciones es un ejemplo de medio de transmisión?", [
        "a) Token Ring",
        "b) CPU",
        "c) DNS",
        "d) Bluetooth"
    ], "a"),
    ("Dentro de los 'medios' utilizados en una red de datos y telecomunicaciones, ¿cuál de las siguientes opciones es un ejemplo de medio de transmisión?", [
    "d) Anillo FDDI",
    "b) CPU",
    "c) DNS",
    "a) Bluetooth"
    ], "d"),
    ("Dentro de los 'medios' utilizados en una red de datos y telecomunicaciones, ¿cuál de las siguientes opciones es un ejemplo de medio de transmisión?", [
        "c) Línea Ethernet",
        "b) CPU",
        "a) DNS",
        "d) Bluetooth"
    ], "c"),
    ("¿Cuál es una forma común en la que los 'adaptadores de red' se presentan en una red de datos y telecomunicaciones?", [
        "a) Normalmente en forma de tarjeta PCI, USB, PCMCIA, etc.",
        "b) Normalmente en forma de cable de red Ethernet.",
        "c) Normalmente en forma de servidor de red.",
        "d) Normalmente en forma de software."
    ], "a"),
    ("En el contexto de redes de datos y telecomunicaciones, ¿qué siglas comúnmente se utilizan para referirse al 'adaptador de red'?", [
        "b) NIC",
        "a) CPU",
        "c) DNS",
        "d) USB"
    ], "b"),
    ("¿Cuáles son los puertos más comunes utilizados para el 'adaptador de red' en una red de datos y telecomunicaciones?", [
        "a) No hay puertos específicos para el adaptador de red.",
        "b) Par trenzado y cable coaxial.",
        "c) USB y HDMI .",
        "d) VGA y cable coaxial."
    ], "b"),
    ("¿Qué característica identifica cada 'NIC' (tarjeta de interfaz de red) al ser fabricada?", [
        "a) Cada NIC es identificada con un número de serie único.",
        "b) Cada NIC es identificada con una dirección IP única.",
        "c) Cada NIC es identificada con una dirección MAC (48 bits) única al ser fabricada.",
        "d) Cada NIC es identificada con un código de barras único."
    ], "c"),
    ("En una red de datos y telecomunicaciones, ¿cuál es una característica común de los 'armarios de distribución'?", [
        "a) Los armarios de distribución son totalmente opacos y no tienen puerta.",
        "b) Los armarios de distribución son fabricados únicamente de metal.",
        "c) Los armarios de distribución tienen puertas de cristal o material transparente.",
        "d) Los armarios de distribución son del mismo tamaño que una computadora de escritorio."
    ], "c"),
    ("¿Cuáles son algunas de las características comunes de los 'armarios de distribución' en una red de datos y telecomunicaciones?", [
        "a) Los armarios de distribución no tienen puertas ni aberturas en el techo y suelo.",
        "b) Los armarios de distribución no permiten el paso de cableado a través de ellos.",
        "c) Los armarios de distribución tienen paredes y puertas desmontables.",
        "d) Los armarios de distribución son sellados herméticamente sin ninguna abertura."
    ], "c"),
    ("¿Qué función pueden cumplir el techo y el suelo de los 'armarios de distribución' en una red de datos y telecomunicaciones?", [
        "a) El techo y el suelo son totalmente sólidos sin aberturas ni funciones específicas.",
        "b) El techo y el suelo no tienen relación con los armarios de distribución.",
        "c) Tanto el techo como el suelo pueden tener aberturas para pasar cableado a través de ellos.",
        "d) El techo y el suelo se utilizan únicamente para la ventilación de los armarios."
    ], "c"),
    ("¿Cuál de las siguientes afirmaciones describe mejor un 'armario de distribución' en una red de datos y telecomunicaciones?", [
        "a) Un armario de distribución es un producto que no se puede montar en bastidores.",
        "b) Un armario de distribución no tiene ningún bastidor en su interior.",
        "c) Un armario de distribución es un producto rackeable con cuatro bastidores internos de armazón universal de 19 pulgadas.",
        "d) Un armario de distribución es un producto que solo se utiliza en entornos de red inalámbrica."
    ], "c"),
    ("¿Cuáles son algunas de las características comunes de un 'armario de distribución' en una red de datos y telecomunicaciones?", [
        "a) Los armarios de distribución no tienen bastidores ni agujeros.",
        "b) Los armarios de distribución tienen bastidores con agujeros cada 5 cm (unidad U) y un armazón de bastidores con conexión a tierra.",
        "c) Los armarios de distribución tienen un bastidor único sin agujeros.",
        "d) Los armarios de distribución solo tienen agujeros sin bastidores."
    ], "b"),
    ("¿Cuál es una de las funciones comunes de un 'panel de parcheo' en una red de datos y telecomunicaciones?", [
        "a) Los paneles de parcheo no tienen ninguna función específica.",
        "b) Los paneles de parcheo se utilizan para organizar líneas de entrada y salida.",
        "c) Los paneles de parcheo se utilizan exclusivamente para la ventilación en los armarios de distribución.",
        "d) Los paneles de parcheo son utilizados para conectar cables de alimentación."
    ], "b"),
    ("¿Qué tipo de cables se conectan comúnmente a los 'paneles de parcheo' en una red de datos y telecomunicaciones?", [
        "a) Se conectan cables de alimentación.",
        "b) Se conectan cables de fibra óptica.",
        "c) Se conectan cables de par trenzado.",
        "d) Se conectan cables coaxiales."
    ], "c"),
    ("En una red de datos y telecomunicaciones, ¿cuántas tomas típicamente tiene un 'panel de parcheo' que ocupa 1U?", [
        "a) 24 tomas (1 fila).",
        "b) 48 tomas (2 filas).",
        "c) 72 tomas (3 filas).",
        "d) 96 tomas (4 filas)."
    ], "a"),
    ("¿Cuál es una de las características comunes de los 'paneles de parcheo' en una red de datos y telecomunicaciones en relación a la codificación de las tomas?", [
        "a) Los paneles de parcheo no utilizan ningún tipo de codificación.",
        "b) Los paneles de parcheo utilizan una codificación que no se corresponde con las tomas del otro lado del cable.",
        "c) Los paneles de parcheo utilizan una codificación que se corresponde con la toma del otro lado del cable.",
        "d) Los paneles de parcheo utilizan una codificación única para todas las tomas."
    ], "c"),
    ("¿Cuál es una de las características comunes de los 'paneles de parcheo' en una red de datos y telecomunicaciones en relación a su formato y conectores?", [
        "a) Los paneles de parcheo utilizan rosetas en lugar de regletas modulares.",
        "b) Los paneles de parcheo no utilizan ningún tipo de conector o formato específico.",
        "c) Los paneles de parcheo tienen un formato modular y utilizan regletas modulares.",
        "d) Los paneles de parcheo utilizan exclusivamente conectores USB."
    ], "c"),
    ("¿Es posible encontrar 'paneles de parcheo' en una red de datos y telecomunicaciones que estén diseñados para la conexión de cables de fibra óptica?", [
        "a) No, los paneles de parcheo nunca están diseñados para la conexión de cables de fibra óptica.",
        "b) Sí, los paneles de parcheo pueden estar diseñados para la conexión de cables de fibra óptica.",
        "c) Los paneles de parcheo solo están diseñados para cables coaxiales.",
        "d) Los paneles de parcheo solo están diseñados para cables de alimentación."
    ], "b"),
    ("¿Qué nombre se le da comúnmente a los celementos de conexión y guiado?", [
        "a) Se les llama 'tomas de usuario', 'de telecomunicaciones' o 'rosetas'.",
        "b) Se les llama 'enlaces principales' o 'conectores centrales'.",
        "c) Se les llama 'puntos de acceso' o 'routers'.",
        "d) Se les llama 'interruptores de red' o 'servidores de red'."
    ], "a"),
    ("¿Qué característica común tienen los componentes llamados 'tomas de usuario', 'de telecomunicaciones' o 'rosetas' en una red de datos y telecomunicaciones?", [
        "a) Pueden ofrecer una o más conexiones a la red.",
        "b) Solo ofrecen una única conexión a la red.",
        "c) No ofrecen ninguna conexión a la red.",
        "d) Solo ofrecen conexiones a la red de fibra óptica."
    ], "a"),
    ("¿Qué se utiliza comúnmente para conectar las 'tomas de usuario' a los armarios en una red de datos y telecomunicaciones, ya sea entre el equipo y la toma o entre un panel de parcheo y otro lugar?", [
        "d) Se utilizan latiguillos.",
        "b) Se utilizan cables de alimentación.",
        "c) Se utilizan conectores USB.",
        "a) Se utilizan cables coaxiales."
    ], "d"),
    ("En una red de datos y telecomunicaciones, ¿qué opciones tienen los administradores en cuanto a los latiguillos utilizados para conectar tomas de usuario a armarios?", [
        "a) Los latiguillos solo pueden comprarse ya hechos.",
        "b) Los latiguillos solo pueden fabricarse manualmente.",
        "c) Los latiguillos pueden comprarse ya hechos o fabricarse manualmente.",
        "d) Los latiguillos no se utilizan en redes de datos y telecomunicaciones."
    ], "c"),
    ("¿Cómo se guía comúnmente el cableado de red en una infraestructura de datos y telecomunicaciones?", [
        "a) El cableado de red no se guía a través de soportes.",
        "b) El cableado de red se guía mediante sujeciones magnéticas.",
        "c) El cableado de red se guía a través de soportes de guiado.",
        "d) El cableado de red se guía a través de canales subterráneos."
    ], "c"),
    ("¿Cuáles son algunos de los tipos comunes de 'tomas de usuario' utilizados en una red de datos y telecomunicaciones?", [
        "a) Superficie, empotrables y de suelo.",
        "b) Solamente superficie.",
        "c) Solamente empotrables.",
        "d) Solamente de suelo."
    ], "a"),
    ("¿Cuáles son algunos de los tipos comunes de 'soportes de guiado' utilizados para guiar el cableado de red en una infraestructura de datos y telecomunicaciones?", [
        "a) Canalizaciones, bandejas de guiado, guías de cable y pasahilos.",
        "b) Solamente canalizaciones.",
        "c) Solamente bandejas de guiado.",
        "d) Solamente guías de cable."
    ], "a"),
    ("Dentro de la 'electrónica de red', ¿cuáles son algunos de los componentes comunes utilizados en una red de datos y telecomunicaciones?", [
        "a) Repetidores, hubs, switches, bridges, routers y gateways.",
        "b) Repetidores, hubs, routers y gateways.",
        "c) Repetidores, hubs, swichs y routers.",
        "d) Routers, hubs y switchs."
    ], "a"),
    ("¿Cuál es una de las funciones principales de un repetidor en una red de datos y telecomunicaciones?", [
    "a) Capturar señales y almacenarlas.",
    "b) Filtrar las señales no deseadas.",
    "d) Captar una señal y enviarla amplificada.",
    "c) Transformar las señales en datos digitales."
    ], "d"),
    ("¿Qué consideración es importante al utilizar repetidores en una red para evitar problemas como 'zonas de sombra' o 'puntos muertos'?", [
        "a) Los repetidores siempre eliminan las zonas de sombra y puntos muertos automáticamente.",
        "c) No es necesario preocuparse por zonas de sombra o puntos muertos en una red con repetidores.",
        "b) Se debe planificar la ubicación de los repetidores para evitar zonas de sombra y puntos muertos.",
        "d) Los repetidores crean intencionadamente zonas de sombra y puntos muertos."
    ], "b"),
    ("¿Cuáles son los componentes principales de un repetidor inalámbrico en una red de datos y telecomunicaciones?", [
        "c) Una antena y una conexión USB.",
        "b) Un cable coaxial y una batería recargable.",
        "a) Una antena y una conexión RJ-45.",
        "d) Un conector HDMI y una fuente de alimentación externa."
    ], "a"),
    ("¿En qué capa del modelo OSI opera un repetidor en una red de datos y telecomunicaciones?", [
        "a) Capa 3",
        "b) Capa 2",
        "d) Capa 1",
        "c) Capa 4"
    ], "d"),
    ("¿Cuáles son los dos modos de funcionamiento comunes de un repetidor en una red de datos?", [
        "a) Modo de alta velocidad y modo de baja velocidad.",
        "b) Modo con alimentación por batería y modo con alimentación eléctrica.",
        "c) Modo con vínculo inalámbrico y modo con extensión cableada.",
        "d) Modo de enrutamiento y modo de conmutación."
    ], "c"),
    ("¿Cuál es una de las funciones principales de un hub (concentrador) en una red de datos?", [
        "c) Encriptar la información de la red.",
        "b) Actuar como un firewall para proteger la red.",
        "a) Vincular tramos de red y ampliar la red.",
        "d) Actuar como un enrutador para redirigir el tráfico."
    ], "a"),
    ("¿Qué tipos de conexiones pueden ser utilizados por un hub (concentrador) en una red de datos?", [
        "a) Solamente conexiones USB.",
        "b) Solamente conexiones HDMI.",
        "d) Conexiones RJ-45, coaxiales, USB, HDMI, etc.",
        "d) Conexiones inalámbricas."
    ], "c"),
    ("¿Qué función tiene la toma up-link en un hub (concentrador) en una red de datos?", [
        "a) Bloquear el tráfico no deseado.",
        "c) Conectar dispositivos móviles.",
        "b) Vincular dos hubs para extender la red (hubs en cascada).",
        "d) Actuar como un servidor de archivos."
    ], "b"),
    ("¿En qué capa del modelo OSI opera un hub (concentrador) y cómo gestiona la información que recibe?", [
        "c) Capa 3, enrutando la información a las tomas necesarias.",
        "b) Capa 2, filtrando la información antes de enviarla a las tomas.",
        "a) Capa 1, replicando la información a todas las tomas con cable.",
        "d) Capa 4, procesando la información antes de distribuirla."
    ], "a"),
    ("¿Cuál es una de las funciones principales de un switch (conmutador) en una red de datos?", [
        "a) Filtrar el tráfico de la red.",
        "b) Actuar como un firewall para proteger la red.",
        "c) Interconectar varios segmentos de red.",
        "d) Replicar todos los paquetes a todas las estaciones."
    ], "c"),
    ("¿Qué hace un switch (conmutador) para construir sus tablas con direcciones MAC de los equipos en una red?", [
        "a) Consulta una base de datos en línea.",
        "b) Solicita información a cada equipo de la red.",
        "c) Utiliza un mecanismo de autoaprendizaje.",
        "d) No necesita tablas de direcciones MAC."
    ], "c"),
    ("¿Cómo puede ser físicamente un switch (conmutador) en una red de datos y telecomunicaciones?", [
        "c) Siempre es independiente.",
        "b) Siempre es rackeable (2U).",
        "a) Puede ser rackeable (2U) o independiente.",
        "d) Solo puede ser montado en una pared."
    ], "a"),
    ("¿Qué tipos de conexiones pueden ser utilizados por un switch (conmutador) en una red de datos y telecomunicaciones?", [
        "a) Solamente conexiones coaxiales.",
        "c) Solamente conexiones de fibra óptica.",
        "b) Conexiones RJ-45, coaxiales o fibra óptica.",
        "d) Conexiones inalámbricas."
    ], "b"),
    ("¿En qué capa del modelo OSI opera un switch (conmutador) y qué función cumple en relación a los paquetes de datos?", [
        "a) Capa 3, traduce las direcciones IP a direcciones físicas.",
        "b) Capa 2, interpreta la dirección de destino de los paquetes y los remite.",
        "c) Capa 1, se encarga de la transmisión de bits individuales.",
        "d) Capa 4, administra la calidad del servicio (QoS)."
    ], "b"),
    ("¿Cuál es una de las funciones principales de un bridge (puente de red) en una red de datos?", [
        "a) Gestionar el tráfico de la red de manera centralizada.",
        "b) Actuar como un firewall para proteger la red.",
        "c) Interconectar varios segmentos de red.",
        "d) Transmitir todos los paquetes a todas las estaciones."
    ], "c"),
    ("¿Cuáles son los dos tipos principales de bridges (puentes de red) en una red de datos?", [
        "a) Bridge local y bridge remoto.",
        "c) Bridge gestionado y bridge no gestionado.",
        "b) Bridge transparente y bridge encaminado en el origen.",
        "d) Bridge de alta velocidad y bridge de baja velocidad."
    ], "b"),
    ("¿Cuál es una ventaja de un bridge (puente de red) en términos de velocidad en una red de datos?", [
        "c) El bridge siempre opera a la misma velocidad que los dispositivos de la red.",
        "b) El bridge es más lento que otros dispositivos de red.",
        "a) El bridge puede trabajar a varias velocidades, adaptándose a las necesidades de la red.",
        "d) El bridge no afecta la velocidad de la red en absoluto."
    ], "a"),
    ("¿Cuál es una de las funciones principales de un router (enrutador) en una red de datos?", [
        "a) Actuar como un switch dentro de una red local.",
        "b) Ampliar la red local conectando más dispositivos.",
        "d) Interconectar diferentes redes, ya sean LAN o WAN.",
        "c) Proporcionar una conexión a Internet mediante cable coaxial."
    ], "d"),
    ("¿Cómo puede ser físicamente un router (enrutador) en una red de datos?", [
        "a) Siempre es independiente.",
        "b) Siempre es rackeable (2U).",
        "c) Puede ser rackeable (2U) o independiente.",
        "d) Se conecta a través de conexiones coaxiales."
    ], "c"),
    ("¿Qué tipo de conexión es comúnmente utilizada por un router SoHo (independiente) para acceder a Internet?", [
        "c) Conexiones de fibra óptica.",
        "b) Conexiones inalámbricas.",
        "a) Conexiones RJ-45.",
        "d) Conexiones de cable coaxial."
    ], "c"),
    ("¿Cuáles son algunas de las características de un router rackeable en una red de datos?", [
        "a) Utiliza exclusivamente conexiones inalámbricas.",
        "b) No permite la instalación de tarjetas adicionales.",
        "c) Utiliza diferentes conexiones y velocidades, y ofrece slots para tarjetas.",
        "d) Opera solamente en la capa 1 del modelo OSI."
    ], "c"),
    ("¿En qué capa del modelo OSI opera un router (enrutador) y qué ventaja ofrece su sistema operativo (IOS)?", [
        "c) Opera en la capa 2 del modelo OSI y permite una mayor velocidad de transmisión.",
        "b) Opera en la capa 4 del modelo OSI y ofrece seguridad avanzada.",
        "a) Opera en la capa 3 del modelo OSI y el sistema operativo integra funciones de capas inferiores, permitiendo la operación con switch o bridge.",
        "d) Opera en la capa 7 del modelo OSI y proporciona servicios de aplicaciones directamente a los usuarios."
    ], "a"),
    ("¿Cuál es una de las funciones principales de un gateway (pasarela) en una red de datos y telecomunicaciones?", [
        "a) Conectar redes solo si utilizan la misma arquitectura y protocolos.",
        "b) Conectar redes solo si son LAN.",
        "c) Conectar redes independientemente de la arquitectura y protocolos.",
        "d) Controlar el tráfico de datos en una red local."
    ], "c"),
    ("¿Cómo se presenta físicamente un gateway (pasarela) comúnmente en una red de datos y telecomunicaciones?", [
        "a) Siempre es independiente y ofrece múltiples tomas RJ-45.",
        "b) Siempre es rackeable (2U) y ofrece dos tomas RJ-45.",
        "b) Puede ser independiente o rackeable y suele ofrecer dos tomas RJ-45.",
        "d) Siempre es rackeable (4U) y ofrece una sola toma RJ-45."
    ], "b"),
    ("¿En qué capa del modelo OSI opera un gateway (pasarela) y cuál es una característica especial de su funcionamiento?", [
        "a) Opera exclusivamente en la capa 1 del modelo OSI.",
        "b) Opera en la capa 3 del modelo OSI y no puede realizar funciones de capas superiores.",
        "c) Opera en la capa 4 del modelo OSI y puede realizar funciones de las capas 5, 6 y 7, así como de capas inferiores como router o switch.",
        "d) Opera en la capa 7 del modelo OSI y proporciona servicios de aplicaciones directamente a los usuarios."
    ], "c"),
    ("¿Cuál es una de las funciones de seguridad de un gateway (pasarela) y en cuántas capas del modelo OSI opera en términos de seguridad?", [
        "a) No tiene funciones de seguridad.",
        "b) Opera solo en la capa 3 para controlar el tráfico.",
        "c) Tiene función cortafuegos y opera en las 7 capas de OSI para controlar el tráfico de datos entrante y saliente.",
        "d) Opera solo en la capa 2 para filtrar paquetes de datos."
    ], "c"),
    ("¿Cuál es una de las funciones de un gateway (pasarela) como intermediario entre dos equipos y en qué capa del modelo OSI opera para realizar esta función?", [
        "a) No tiene función de intermediario.",
        "b) Opera en la capa 3 para redireccionar tráfico entre equipos.",
        "d) Tiene función proxy y opera en la capa 7 del modelo OSI como intermediario entre dos equipos.",
        "c) Opera en la capa 1 para transmitir datos entre equipos."
    ], "d"),
    ("¿Cuál es una de las funciones de un gateway (pasarela) relacionada con la seguridad y el acceso a redes privadas, y cuál es el término asociado a esta función?", [
        "a) No tiene funciones de seguridad relacionadas con el acceso a redes privadas.",
        "b) Opera en la capa 2 para proporcionar conexiones privadas.",
        "c) Tiene función VPN para permitir una conexión segura a una LAN privada desde una red pública.",
        "d) Opera en la capa 5 para garantizar la confidencialidad de los datos."
    ], "c"),
    ("¿Cuál de las siguientes afirmaciones describe una red de área personal (PAN) en términos de su área de cobertura?", [
        "a) Cubre extensiones intermedias, como una ciudad o localidad.",
        "b) Tiene una cobertura de kilómetros y suele cruzar derechos públicos de paso.",
        "c) Se utiliza para la interconexión de redes LAN en campus universitarios.",
        "d) Tiene una cobertura muy pequeña, de hasta 3 o 4 metros, para dispositivos próximos."
    ], "d"),
    ("¿Cuál de las siguientes características es típica de las redes de área local (LAN)?", [
        "a) Cobertura que abarca una ciudad o localidad.",
        "b) Propiedad de compañías de telecomunicaciones.",
        "c) Velocidades de transmisión bajas.",
        "d) Cobertura pequeña en edificios o campus, alta velocidad de transmisión."
    ], "d"),
    ("¿Cuál es una característica común de las redes de área metropolitana (MAN)?", [
        "a) Cubren extensiones intermedias, como una ciudad o localidad.",
        "b) Proporcionan alta velocidad de transmisión en campus universitarios.",
        "c) Son propiedades de organizaciones en edificios o campus pequeños.",
        "d) Cruzan derechos públicos de paso y tienen velocidades de transmisión intermedias."
    ], "a"),
    ("¿Qué característica principal distingue a las redes de área extensa (WAN) de otras redes?", [
        "a) Son propiedades de organizaciones en edificios o campus pequeños.",
        "b) Tienen velocidades de transmisión muy elevadas.",
        "c) Cubren extensiones intermedias, como una ciudad o localidad.",
        "d) Tienen una cobertura geográfica grande, cruzando derechos públicos de paso, con velocidades de transmisión inferiores."
    ], "d"),
    ("¿Cuál de las siguientes opciones describe mejor a Internet?", [
        "a) Es una red de área extensa (WAN) con alta velocidad de transmisión.",
        "b) Es propiedad de una única organización y cubre extensiones intermedias.",
        "c) Cubre extensiones de hasta 3 o 4 metros y se utiliza para interconectar dispositivos próximos.",
        "d) Es una red distribuida de dimensión mundial que utiliza las redes PAN, LAN, MAN y WAN."
    ], "d"),
    ("¿Cuál de las siguientes opciones describe cómo puede ser una red según su titularidad?", [
        "a) Red de área local (LAN)",
        "b) Red de área extensa (WAN)",
        "c) Red privada, red pública y VPN",
        "d) Red de ordenadores y red de dispositivos móviles"
    ], "c"),
    ("¿Cómo se caracteriza una red que permite a cualquier persona comunicarse, compartir información y acceder a sus servicios?", [
        "a) Red de área local (LAN)",
        "b) Red de área personal (PAN)",
        "c) Red privada",
        "d) Red pública, como Internet"
    ], "d"),
    ("¿Cuál es la principal característica de una red privada y cómo se denomina cuando ofrece servicios similares a Internet solo para sus usuarios?", [
        "a) Permite el acceso público y se llama Extranet.",
        "b) Proporciona acceso exclusivo y se llama Intranet.",
        "c) No tiene restricciones de acceso y se llama LAN.",
        "d) Se comparte con otras organizaciones y se llama WAN."
    ], "b"),
    ("¿Qué característica principal define a una Red Privada Virtual (VPN)?", [
        "a) Utiliza una red privada dedicada para la comunicación.",
        "b) No utiliza cifrado ni medidas de seguridad.",
        "c) Permite el acceso seguro a una red privada a través de Internet.",
        "d) Requiere una conexión física directa a la red privada."
    ], "c"),
    ("¿Cuál es uno de los usos comunes de una Red Privada Virtual (VPN)?", [
        "a) Transmitir datos sin cifrado a través de Internet.",
        "b) Acceder a una red pública de manera segura.",
        "c) Establecer conexiones físicas a equipos de red.",
        "d) Administrar equipos de forma remota con conexiones cifradas."
    ], "d"),
    ("¿Qué define la topología de una red?", [
        "a) La velocidad de transmisión de datos en la red.",
        "b) La dirección IP asignada a cada nodo de la red.",
        "c) La forma en que se conectan los nodos de la red.",
        "d) El tipo de cable utilizado en la red."
    ], "c"),
    ("¿Cuál es la principal diferencia entre los enlaces punto a punto y los enlaces multipunto en una red?", [
        "a) Los enlaces punto a punto son utilizados exclusivamente en redes inalámbricas.",
        "b) En los enlaces punto a punto, una única línea de comunicación es compartida por todos los nodos.",
        "c) Los enlaces multipunto conectan únicamente 2 nodos.",
        "d) En los enlaces multipunto, hay una única línea de comunicación compartida por todos los nodos, mientras que en la de punto a punto cada enlace conecta únicamente con dos nodos."
    ], "d"),
    ("¿Qué característica destaca a la topología de malla?", [
        "a) La falta de redundancia.",
        "b) Alta redundancia.",
        "c) Conexiones centralizadas.",
        "d) Baja escalabilidad"
    ], "b"),
    ("¿Cómo se complica la topología de malla al agregar nuevos nodos?", [
        "a) No se ve afectada.",
        "b) Se vuelve más eficiente.",
        "c) Requiere la reconexión con todos los nodos existentes.",
        "d) Facilita la gestión de nuevos nodos."
    ], "c"),
    ("¿Cuál de las siguientes afirmaciones describe mejor los costos asociados con la topología de malla en enlaces punto a punto?", [
        "a) Es una solución rentable para agregar nodos.",
        "b) Puede volverse costosa al agregar nuevos nodos.",
        "c) Los costos se mantienen constantes sin importar el número de nodos.",
        "d) No implica costos adicionales."
    ], "b"),
    ("¿Cómo están conectados los nodos en una topología de malla en enlaces punto a punto?", [
        "a) Cada nodo se conecta solo a un nodo central.",
        "b) Todos los nodos se conectan entre sí.",
        "c) Un único nodo actúa como intermediario para la comunicación.",
        "d) Los nodos funcionan de manera independiente sin conexiones."
    ], "b"),
    ("¿Qué caracteriza a la topología de estrella?", [
        "a) No tiene un nodo central.",
        "b) Todos los nodos se conectan entre sí directamente.",
        "c) Tiene un nodo central del que parten enlaces a todos los nodos.",
        "d) Los nodos están dispersos sin conexiones."
    ], "c"),
    ("¿Cuál es una de las principales ventajas de la topología de estrella?", [
        "a) Alta redundancia.",
        "b) Bajo costo inicial.",
        "c) No depende de un nodo central.",
        "d) Escalabilidad limitada."
    ], "b"),
    ("¿Qué ocurre si el nodo central en una topología de estrella falla?", [
        "c) La red sigue funcionando normalmente.",
        "b) La red se vuelve altamente redundante.",
        "a) La red colapsa y se vuelve muy vulnerable.",
        "d) Los otros nodos eligen un nuevo nodo central."
    ], "a"),
    ("¿Cómo se compara el costo inicial de la topología de estrella con la expansión a nuevos nodos?", [
        "a) La expansión a nuevos nodos es costosa.",
        "b) El costo inicial es bajo.",
        "c) Ambos tienen un costo alto.",
        "d) Ambos son igualmente económicos."
    ], "b"),
    ("¿Cómo se conectan las estrellas en una topología de árbol?", [
        "a) No están conectadas entre sí.",
        "b) Se conectan directamente todos con todos.",
        "c) Se conectan a través de sus nodos centrales.",
        "d) Se conectan mediante un nodo principal."
    ], "c"),
    ("¿Cómo se conectan las estrellas en una topología de árbol?", [
        "c) No están conectadas entre sí.",
        "b) Se conectan directamente todos con todos.",
        "a) Se conectan a través de sus nodos centrales.",
        "d) Se conectan mediante un nodo principal."
    ], "a"),
    ("¿Cuál es una de las situaciones en las que se emplea una topología de árbol?", [
        "a) Cuando la red se compone de una sola estrella.",
        "b) Cuando las comunicaciones se producen entre nodos distantes.",
        "c) Cuando la mayor parte de las comunicaciones se producen entre nodos próximos.",
        "d) Cuando se necesita alta redundancia."
    ], "c"),
    ("¿Qué define la topología de árbol en términos de conexiones entre nodos?", [
        "a) Una red sin nodos centrales.",
        "b) Una red altamente redundante.",
        "d) La conexión entre estrellas a través de sus nodos centrales.",
        "c) Una red en la que todos los nodos se conectan directamente."
    ], "d"),
    ("¿Cómo se transmiten los mensajes en una topología de anillo hasta llegar al destino?", [
        "a) Los mensajes saltan aleatoriamente entre nodos.",
        "b) Los mensajes se envían en múltiples direcciones simultáneamente.",
        "c) Los mensajes atraviesan todos los nodos hasta llegar al destino.",
        "d) Los mensajes son gestionados por un nodo central."
    ], "c"),
    ("¿Cuál es una de las principales vulnerabilidades de una topología de anillo?", [
        "a) Vulnerabilidad a fallos en el nodo central.",
        "b) Vulnerabilidad a fallos en la comunicación bidireccional.",
        "d) Vulnerabilidad a fallos en los nodos o los enlaces entre ellos.",
        "c) Vulnerabilidad a fallos en la comunicación unidireccional."
    ], "d"),
    ("¿Cómo se conectan los ordenadores en una topología de bus?", [
        "c) Cada ordenador se conecta a un nodo central.",
        "b) Cada ordenador se conecta con el anterior y el siguiente ordenador.",
        "a) Cada ordenador se conecta al canal de transmisión común o bus.",
        "d) Los ordenadores no están conectados entre sí."
    ], "a"),
    ("¿Cómo se comporta un mensaje enviado en una topología de bus?", [
        "a) Un mensaje enviado por un nodo solo se recibirá en el nodo destino.",
        "b) Un mensaje enviado por un nodo será recibido por todos los otros nodos.",
        "c) Un mensaje solo puede ser recibido por el nodo anterior al emisor.",
        "d) Cada nodo envía su propio mensaje independientemente."
    ], "b"),
    ("¿Quién es el encargado de determinar si un mensaje es para él en una topología de bus?", [
        "a) El nodo emisor del mensaje.",
        "b) El primer nodo de la red.",
        "c) El nodo destino del mensaje.",
        "d) Todos los nodos reciben todos los mensajes."
    ], "c"),
    ("¿Qué tipo de mecanismos son necesarios en una topología de bus?", [
        "a) Mecanismos para gestionar la comunicación bidireccional.",
        "b) Mecanismos para gestionar la comunicación punto a punto.",
        "c) Mecanismos para gestionar la transmisión a larga distancia.",
        "d) Mecanismos para gestionar cuándo se puede o no enviar un mensaje."
    ], "d"),
    ("¿Cómo es el enlace en una topología de anillo (multipunto)?", [
        "a) El enlace es abierto y la información puede ir en ambos sentidos.",
        "b) El enlace es cerrado y la información va siempre en el mismo sentido.",
        "c) El enlace es un punto central de conexión.",
        "d) El enlace cambia constantemente de dirección."
    ], "b"),
    ("¿Qué mecanismos se utilizan en una topología de anillo (multipunto) para determinar quién puede transmitir?", [
        "b) Se utiliza un nodo central para controlar la transmisión.",
        "a) Se utiliza un sistema de turnos predefinidos para transmitir (paso de testigos).",
        "c) Se permite que todos los nodos transmitan simultáneamente.",
        "d) No es necesario ningún mecanismo para determinar quién puede transmitir."
    ], "a"),
    ("¿Cómo afecta la caída de un nodo en una topología de anillo (multipunto) al resto de la red?", [
        "a) La caída de un nodo detiene por completo la red.",
        "b) La caída de un nodo afecta negativamente a la red, pero no la detiene.",
        "c) La caída de un nodo no afecta al resto de la red.",
        "d) La caída de un nodo solo afecta a los nodos cercanos."
    ], "c"),
    ("¿Cuál es la característica principal de la topología de anillo (multipunto) en términos de dirección de la información?", [
        "a) La información va en direcciones variables y cambia constantemente.",
        "b) La información va en ambos sentidos simultáneamente.",
        "c) La información va siempre en el mismo sentido.",
        "d) La información va en cualquier dirección según las necesidades."
    ], "c"),
    ("¿Cómo puede ser una red según su topología inalámbrica?", [
        "a) Topología distribuida y topología centralizada.",
        "b) Topología distribuida, topología centralizada y topología parcial.",
        "c) Topología parcial y topología total.",
        "d) Topología ascendente y topología descendente."
    ], "a"),
    ("En una topología distribuida, ¿qué función cumplen las celdas?", [
        "a) Las celdas son elementos de hardware que almacenan datos.",
        "b) Las celdas son dispositivos de almacenamiento de energía para los dispositivos inalámbricos.",
        "c) Las celdas son zonas donde la señal se emite con efectividad, definiendo áreas de cobertura.",
        "d) Las celdas son nodos centrales que gestionan todas las comunicaciones en la red."
    ], "c"),
    ("¿Cuál es la función principal de los puntos de acceso en una topología distribuida?", [
        "a) Almacenar información en la nube para su acceso remoto.",
        "b) Ampliar el rango de cobertura de la red inalámbrica.",
        "c) Gestionar el tráfico de datos en la red local.",
        "d) Proporcionar energía a los dispositivos inalámbricos."
    ], "b"),
    ("¿Qué significa el término 'itinerancia' (roaming) en el contexto de una topología distribuida?", [
        "a) La capacidad de una red inalámbrica para cambiar de un canal de transmisión a otro automáticamente.",
        "b) El proceso de enviar datos a través de múltiples nodos antes de llegar al destino final.",
        "c) La habilidad de un dispositivo para moverse entre celdas o puntos de acceso sin perder la conexión a la red.",
        "d) La administración de las direcciones IP en una red inalámbrica."
    ], "c"),
    ("¿Cuál es el requisito principal de itinerancia (roaming) en redes WLAN distribuidas?", [
        "a) El uso de celdas de gran tamaño para garantizar una cobertura completa.",
        "b) La administración de las direcciones MAC de los dispositivos.",
        "c) La capacidad de los dispositivos para moverse entre celdas o puntos de acceso sin perder la conexión.",
        "d) La utilización de cables de red en lugar de conexiones inalámbricas."
    ], "c"),
    ("¿En qué situación es más adecuada la topología centralizada?", [
        "c) Cuando se utilizan celdas de gran tamaño para garantizar una cobertura completa.",
        "b) Cuando se necesita itinerancia (roaming) entre celdas o puntos de acceso.",
        "a) Cuando hay muchas celdas e información de naturaleza variada.",
        "d) Cuando se desea una red inalámbrica con puntos de acceso en lugares estratégicos."
    ], "a"),
    ("¿Quién gestiona cada celda en una topología centralizada?", [
        "a) Los puntos de acceso (access points).",
        "b) Los dispositivos finales (clientes).",
        "c) Los routers inalámbricos.",
        "d) Los switches WLAN."
    ], "d"),
    ("En una topología centralizada de redes inalámbricas, ¿cómo se describiría la función de los puntos de acceso 'tontos'?", [
        "a) Los puntos de acceso 'tontos' gestionan activamente dispositivos conectados a la red.",
        "b) Los puntos de acceso 'tontos' dividen la red en celdas para una mejor cobertura.",
        "c) Los puntos de acceso 'tontos' permiten el movimiento entre diferentes celdas sin desconexión.",
        "d) Los puntos de acceso 'tontos' solo amplían el radio de acción y no gestionan dispositivos."
    ], "d"),
    ("¿Cómo se describe un enlace en el que la información fluye en un solo sentido?", [
        "a) Semi-duplex",
        "c) Duplex",
        "b) Simplex",
        "d) Multiplex"
    ], "b"),
    ("¿Cuál de los siguientes dispositivos de comunicación a menudo utiliza un enlace semi-duplex?", [
        "a) Teléfono",
        "b) Walkie talkie",
        "c) Radio FM",
        "d) Televisión"
    ], "b"),
    ("¿En qué tipo de enlace la transmisión de información es bidireccional y simultánea?", [
        "a) Simplex",
        "b) Semi-duplex",
        "d) Duplex (Full-duplex)",
        "c) Multiplex"
    ], "d"),
    ("¿Cómo se define la conmutación en el contexto de las redes?", [
        "c) La transmisión de datos en un solo sentido",
        "b) La conexión entre dispositivos en una misma ubicación",
        "a) La conexión que realizan nodos intermedios para establecer un camino entre un emisor y un receptor en una red",
        "d) El proceso de comunicación a larga distancia"
    ], "a"),
    ("¿Cuáles son los diferentes tipos de conmutación utilizados en las redes de comunicación?", [
        "a) Conmutación de circuitos, conmutación de mensajes y conmutación de paquetes",
        "b) Conmutación de voz, conmutación de video y conmutación de datos",
        "c) Conmutación simplex, conmutación semi-duplex y conmutación duplex",
        "d) Conmutación de tiempo, conmutación de espacio y conmutación de frecuencia"
    ], "a"),
    ("¿Cuál es una característica de la conmutación de circuitos?", [
        "a) Se divide el mensaje en paquetes pequeños para su transmisión.",
        "b) Se establece un camino físico dedicado para la transferencia del mensaje.",
        "c) Los datos se envían como mensajes completos sin división.",
        "d) Es el método comúnmente utilizado en la conmutación de paquetes."
    ], "b"),
    ("¿Cuáles son las fases en la conmutación de circuitos?", [
        "a) Inicialización y finalización del circuito.",
        "b) Envío y recepción del mensaje.",
        "c) Establecimiento del circuito, envío del mensaje y liberación del circuito.",
        "d) Conexión y desconexión de la red."
    ], "c"),
    ("¿Qué característica describe el hecho de que en la conmutación de circuitos, el circuito no se libera hasta finalizar la transmisión?", [
        "a) Sobreutilización de recursos.",
        "b) Multiplexación de circuitos.",
        "d) Infrautilización de recursos.",
        "c) Conexión de corta duración."
    ], "d"),
    ("¿Cuál es una característica de la conmutación de mensajes?", [
        "a) Se establece un camino físico para transferir el mensaje.",
        "b) No se establece una ruta física.",
        "c) Los mensajes se envían como paquetes independientes.",
        "d) La ruta se mantiene durante toda la transmisión."
    ], "b"),
    ("En la conmutación de mensajes, ¿cómo se envía el mensaje de datos?", [
        "a) Se envía como un paquete completo sin almacenamiento intermedio.",
        "b) Se envía por un camino físico preestablecido.",
        "c) Se envía el mensaje de datos entero mediante almacenamiento y envío en cada nodo.",
        "d) Se transmite en ambos sentidos simultáneamente."
    ], "c"),
    ("En la conmutación de mensajes, ¿qué se necesita en gran cantidad en los nodos?", [
        "a) Capacidad de procesamiento.",
        "b) Energía eléctrica.",
        "c) Capacidad de almacenamiento.",
        "d) Ancho de banda de red."
    ], "c"),
    ("En la conmutación de mensajes, ¿qué ocurre en caso de un error en la transmisión?", [
        "c) Se corrige automáticamente el error.",
        "b) Se descarta el mensaje completo.",
        "a) Se debe enviar el mensaje entero.",
        "d) El mensaje se divide en paquetes más pequeños para evitar errores."
    ], "a"),
    ("¿Cuál es una característica clave de la conmutación de paquetes?", [
        "a) Establece una ruta física dedicada para cada transmisión.",
        "b) Requiere una gran capacidad de almacenamiento en los nodos.",
        "c) Permite la transmisión de mensajes completos sin divisiones.",
        "d) No establece una ruta física y divide los datos en paquetes para su transmisión."
    ], "d"),
    ("¿Qué característica distingue a la conmutación de paquetes?", [
        "a) Establece una ruta física dedicada para cada transmisión.",
        "c) Requiere una gran capacidad de almacenamiento en los nodos.",
        "b) Permite que cada paquete tome un camino distinto.",
        "d) Requiere una conexión permanente durante la transmisión."
    ], "b"),
    ("¿Cuál es una ventaja de la conmutación de paquetes en comparación con la conmutación de circuitos?", [
        "a) Mayor tiempo de conmutación en cada nodo.",
        "b) Requiere una conexión permanente durante la transmisión.",
        "c) Menor tiempo de conmutación en cada nodo.",
        "d) Establece una ruta física dedicada para cada transmisión."
    ], "c"),
    ("¿Qué ventaja de la conmutación de paquetes permite que si un enlace está saturado pueda ir por otro?", [
        "a) Permite el balanceo de carga.",
        "b) Facilita la retransmisión de paquetes erróneos.",
        "c) Se ocupa completamente cada enlace de la red.",
        "d) Requiere una ruta física establecida para transferir mensajes."
    ], "a"),
    ("¿Cuál es una ventaja de la conmutación de paquetes que permite que si un enlace está saturado, los paquetes puedan ser redirigidos por otro camino disponible?", [
        "a) No permite el balanceo de carga.",
        "b) Requiere una ruta física establecida para transferir mensajes.",
        "c) Mejora el rendimiento de la red al utilizar eficazmente los enlaces disponibles.",
        "d) Facilita la retransmisión de paquetes erróneos."
    ], "c"),
    ("¿Cuál es una ventaja de la conmutación de paquetes?", [
        "a) No permite el balanceo de carga.",
        "b) Requiere una ruta física establecida para transferir mensajes.",
        "c) Mejora el rendimiento de la red, se ocupa muy poco cada enlace.",
        "d) Facilita la retransmisión de diversos paquetes erróneos."
    ], "c"),
    ("¿Por qué la conmutación de paquetes facilita la gestión de errores en la transmisión de datos en comparación con otros métodos?", [
        "a) Requiere una ruta física establecida para transferir mensajes.",
        "b) No permite el balanceo de carga.",
        "c) Mejora el rendimiento de la red al utilizar eficazmente los enlaces disponibles.",
        "d) Si hay un error, solo es necesario retransmitir el paquete erróneo, no todo el mensaje."
    ], "d"),
    ("¿Cuál es el propósito principal de la Red Telefónica Conmutada (RTC)?", [
        "a) Transmitir datos a través de fibra óptica.",
        "b) Proporcionar acceso a Internet de alta velocidad.",
        "c) La transmisión de voz mediante corriente eléctrica en un par de cables de cobre (bucle de abonado).",
        "d) Conectar redes de área local (LAN) en empresas."
    ], "c"),
    ("¿Cuál de las siguientes afirmaciones describe mejor la extensión de la Red Telefónica Conmutada (RTC)?", [
        "a) Limitada a ciertas regiones geográficas.",
        "c) Principalmente utilizada en entornos empresariales.",
        "b) Tiene cientos de millones de abonados en todo el mundo.",
        "d) Se utiliza principalmente para la transmisión de datos."
    ], "c"),
    ("¿Cuál de las siguientes opciones describe mejor la evolución de la conmutación en la Red Telefónica Conmutada (RTC)?", [
        "a) La conmutación ha seguido siendo manual y no ha experimentado cambios significativos.",
        "b) La conmutación se realizaba manualmente, pero luego se automatizó con centralitas.",
        "c) La conmutación ha avanzado hacia sistemas de conmutación por paquetes en lugar de circuitos.",
        "d) La RTC no ha experimentado cambios en su infraestructura desde su creación."
    ], "b"),
    ("¿Cuál de los siguientes servicios es uno de los principales ofrecidos por la Red Telefónica Conmutada (RTC)?", [
        "a) Servicio de correo electrónico.",
        "b) Transmisión de video en tiempo real.",
        "c) Servicio de fax.",
        "d) Transmisión de voz en tiempo real."
    ], "d"),
    ("¿Cuál de los siguientes servicios NO es uno de los ofrecidos por la Red Telefónica Conmutada (RTC)?", [
        "a) Servicio de correo electrónico.",
        "b) Llamada en espera.",
        "c) Conferencia a tres.",
        "d) Desvío de llamadas."
    ], "a"),
    ("¿Cuál de los siguientes dispositivos es responsable de realizar la modulación y desmodulación en la Red Telefónica Conmutada (RTC)?", [
        "a) Routers.",
        "b) Concentradores.",
        "c) Centralitas telefónicas.",
        "d) Módems."
    ], "d"),
    ("Según la información proporcionada, ¿qué tipo de transmisión se utiliza en la Red Telefónica Conmutada (RTC)?", [
        "a) Transmisión digital.",
        "b) Transmisión analógica.",
        "c) Transmisión por paquetes.",
        "d) Transmisión inalámbrica."
    ], "b"),
    ("Según la información proporcionada, ¿a qué velocidad máxima de transmisión de datos puede llegar utilizando el espectro de la transmisión de voz en la Red Telefónica Conmutada (RTC)?", [
        "a) 128 Kbps.",
        "b) 56 Kbps.",
        "c) 1 Gbps.",
        "d) 10 Mbps."
    ], "b"),
    



















































































































































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
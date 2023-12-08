import random

# Lista de preguntas y respuestas
preguntas = [

(
    "¿Cuál es la función principal de la capa física en el modelo OSI?",
    [
        "a) Preparar los datos para la transmisión y controlar el acceso a los medios físicos.",
        "b) Decodificar señales y convertirlas nuevamente en datos.",
        "c) Transmitir tramas a la capa de enlace de datos para su procesamiento.",
        "d) Controlar la forma en que los datos acceden a los medios físicos y prepararlos para la transmisión.",
    ],
    "b"
),
(
    "Según el modelo TCP/IP, ¿cuáles son las dos capas del modelo OSI que están tan relacionadas que son básicamente consideradas como una sola?",
    [
        "a) Capa de red y capa de transporte.",
        "b) Capa de sesión y capa de presentación.",
        "c) Capa de enlace de datos y capa física.",
        "d) Capa de aplicación y capa de transporte.",
    ],
    "c"
),
(
    "En el dispositivo emisor, ¿cuál es la función principal de la capa de enlace de datos?",
    [
        "a) Preparar los datos para la transmisión y controlar el acceso a los medios físicos.",
        "b) Decodificar señales y convertirlas nuevamente en datos.",
        "c) Transmitir tramas a la capa física para su procesamiento.",
        "d) Controlar la forma en que los datos se representan en dígitos binarios.",
    ],
    "a"
),
(
    "¿Cuál es la función principal de la capa física en el dispositivo emisor?",
    [
        "a) Preparar los datos para la transmisión y controlar el acceso a los medios físicos.",
        "b) Decodificar señales y convertirlas nuevamente en datos.",
        "c) Controlar la forma en que los datos se representan en dígitos binarios.",
        "d) Transmitir tramas a la capa de enlace de datos para su procesamiento.",
    ],
    "c"
),
(
    "¿Cuál es el proceso que realiza la capa física en el extremo receptor de una red?",
    [
        "a) Preparar los datos para la transmisión y controlar el acceso a los medios físicos.",
        "b) Decodificar señales y convertirlas nuevamente en datos para su transmisión a la capa de enlace de datos.",
        "c) Controlar la forma en que los datos se representan en dígitos binarios.",
        "d) Transmitir tramas directamente a la capa de red para su procesamiento.",
    ],
    "b"
),
(
    "¿Qué función realiza la capa física en el extremo receptor al recibir señales a través de los medios de conexión?",
    [
        "a) Decodificar señales y convertirlas en dígitos binarios.",
        "b) Controlar la forma en que los datos se representan en dígitos binarios.",
        "c) Preparar los datos para su transmisión a la capa de enlace de datos.",
        "d) Transmitir tramas directamente a la capa de red para su procesamiento.",
    ],
    "a"
),
(
    "¿Cuál es el siguiente paso que realiza la capa física después de decodificar la señal y convertirla nuevamente en datos en el extremo receptor?",
    [
        "a) Transmitir tramas directamente a la capa de red para su procesamiento.",
        "b) Controlar la forma en que los datos se representan en dígitos binarios.",
        "c) Enviar la información a la capa de transporte para su procesamiento.",
        "d) Transmitir la trama a la capa de enlace de datos para su aceptación y procesamiento.",
    ],
    "d"
),
(
    "¿Cuáles son los dos tipos principales de conexiones físicas utilizadas en redes?",
    [
        "a) Conexiones de red y conexiones inalámbricas.",
        "b) Conexiones por cable y conexiones de fibra óptica.",
        "c) Conexiones por cable y conexiones mediante ondas de radio.",
        "d) Conexiones de voz y conexiones de datos.",
    ],
    "c"
),
(
    "¿Por qué se debe establecer una conexión a una red local antes de que pueda ocurrir cualquier comunicación de red, ya sea a una impresora local en el hogar o a un sitio web en otro país?",
    [
        "a) Para garantizar la velocidad de la conexión.",
        "b) Para asegurar la privacidad de la comunicación.",
        "c) Para establecer una ruta de comunicación segura.",
        "d) Para permitir que los dispositivos se reconozcan y se comuniquen entre sí.",
    ],
    "d"
),
(
    "¿Cuáles son los dos tipos principales de conexiones físicas que se pueden establecer en una red?",
    [
        "a) Conexión de voz y conexión de datos.",
        "b) Conexión por cable y conexión mediante ondas de radio.",
        "c) Conexión de fibra óptica y conexión por satélite.",
        "d) Conexión pública y conexión privada.",
    ],
    "b"
),
(
    "¿Qué factor determina el tipo de conexión física utilizada en una red?",
    [
        "a) La velocidad de transmisión de datos.",
        "b) La ubicación geográfica de los dispositivos.",
        "c) La configuración de la red.",
        "d) El tamaño de los archivos a transmitir.",
    ],
    "c"
),
(
    "En entornos corporativos, ¿cómo suelen conectarse físicamente las PC de escritorio o portátiles a la red?",
    [
        "a) Mediante conexiones de fibra óptica.",
        "b) A través de conexiones de voz.",
        "c) Con conexiones inalámbricas exclusivamente.",
        "d) Físicamente, mediante cables, a un switch compartido.",
    ],
    "d"
),
(
    "¿Cómo se denomina la configuración en la que las PC de escritorio o portátiles se conectan físicamente mediante cables a un switch compartido, y los datos se transmiten a través de un cable físico?",
    [
        "a) Red inalámbrica.",
        "b) Red sólida",
        "c) Red de fibra óptica.",
        "d) Red cableada.",
    ],
    "d"
),
(
    "Además de las conexiones por cable, ¿qué tipo de conexiones ofrecen muchas empresas para dispositivos como PC portátiles, tablets y smartphones?",
    [
        "a) Conexiones de fibra óptica exclusivamente.",
        "b) Conexiones por satélite.",
        "c) Conexiones inalámbricas.",
        "d) Conexiones de voz.",
    ],
    "c"
),
(
    "¿Cómo se transmiten los datos en el caso de dispositivos inalámbricos según la información proporcionada?",
    [
        "a) A través de cables de fibra óptica.",
        "b) Mediante señales de voz.",
        "c) Mediante ondas de radio.",
        "d) Utilizando conexiones de satélite.",
    ],
    "c"
),
(
    "¿Por qué el uso de la conectividad inalámbrica se ha vuelto cada vez más frecuente según la información proporcionada?",
    [
        "a) Por la reducción de la velocidad de transmisión de datos.",
        "b) Por la disminución de la privacidad en las comunicaciones.",
        "c) Por las ventajas que ofrece en la oferta de servicios inalámbricos.",
        "d) Por la mayor complejidad en la configuración de redes.",
    ],
    "c"
),
(
    "En una red inalámbrica, ¿a qué deben estar conectados los dispositivos para poder ofrecer funcionalidades inalámbricas?",
    [
        "a) A un servidor central.",
        "b) A un router inalámbrico.",
        "c) A un punto de acceso inalámbrico (AP).",
        "d) A un switch compartido.",
    ],
    "c"
),
(
    "¿Cómo suelen ser los dispositivos de switch y los puntos de acceso inalámbricos dentro de una implementación de red según la información proporcionada?",
    [
        "a) Siempre están integrados en un único dispositivo.",
        "b) Son dispositivos independientes y dedicados.",
        "c) Se utilizan solo en redes de voz.",
        "d) Suelen compartir la misma infraestructura física.",
    ],
    "b"
),
(
    "¿Qué característica tienen algunos dispositivos según la información proporcionada?",
    [
        "a) Solo ofrecen conectividad por cable.",
        "b) Solo ofrecen conectividad inalámbrica.",
        "c) Ofrecen tanto conectividad por cable como inalámbrica.",
        "d) No están destinados a redes empresariales.",
    ],
    "c"
),
(
    "En muchos hogares, ¿qué tipo de dispositivos suelen implementar las personas para proporcionar conectividad tanto por cable como inalámbrica?",
    [
        "a) Switches dedicados.",
        "b) Routers de servicio integrado (ISR).",
        "c) Puntos de acceso inalámbricos exclusivamente.",
        "d) Conexiones de fibra óptica.",
    ],
    "b"
),
(
    "En muchos hogares, ¿qué tipo de dispositivos suelen implementar las personas para proporcionar conectividad tanto por cable como inalámbrica?",
    [
        "a) Switches dedicados.",
        "b) Routers de servicio integrado (ISR).",
        "c) Puntos de acceso inalámbricos exclusivamente.",
        "d) Conexiones de fibra óptica.",
    ],
    "b"
),
(
    "¿Para qué se utilizan las NIC Ethernet y las NIC WLAN según la información proporcionada?",
    [
        "a) Ambas se utilizan exclusivamente para conexiones inalámbricas.",
        "b) Ambas se utilizan exclusivamente para conexiones por cable.",
        "c) Las NIC Ethernet para conexiones por cable y las NIC WLAN para conexiones inalámbricas.",
        "d) Las NIC WLAN para conexiones por cable y las NIC Ethernet para conexiones inalámbricas.",
    ],
    "c"
),
(
    "¿Qué posibilidad tienen los dispositivos para usuarios finales en cuanto al tipo de NIC que pueden incluir según la información proporcionada?",
    [
        "a) Pueden incluir solo NIC Ethernet.",
        "b) Pueden incluir solo NIC WLAN.",
        "c) Pueden incluir ambos tipos de NIC (Ethernet y WLAN).",
        "d) No pueden incluir ninguna NIC.",
    ],
    "c"
),
(
    "¿Qué tipo de NIC suele tener una impresora de red según la información proporcionada?",
    [
        "a) Solo NIC WLAN.",
        "b) Solo NIC Ethernet.",
        "c) Ambos tipos de NIC (Ethernet y WLAN).",
        "d) Ningún tipo de NIC.",
    ],
    "b"
),
(
    "¿Qué tipo de NIC suelen contener las tabletas y los teléfonos inteligentes según la información proporcionada?",
    [
        "a) Solo NIC Ethernet.",
        "b) Solo NIC WLAN.",
        "c) Ambos tipos de NIC (Ethernet y WLAN).",
        "d) Ningún tipo de NIC.",
    ],
    "b"
),
(
    "En términos de rendimiento, ¿qué afirmación es cierta según la información proporcionada?",
    [
        "a) Todas las conexiones físicas son iguales en rendimiento.",
        "b) No hay diferencias de rendimiento entre las conexiones físicas.",
        "c) Las conexiones físicas pueden variar en rendimiento al conectarse a una red.",
        "d) El rendimiento de las conexiones físicas solo depende del tipo de dispositivo.",
    ],
    "c"
),
(
    "¿Cómo puede afectar la distancia a la que se encuentra un dispositivo inalámbrico del punto de acceso inalámbrico a su rendimiento según la información proporcionada?",
    [
        "a) La distancia no afecta al rendimiento de un dispositivo inalámbrico.",
        "b) La señal inalámbrica se fortalece a medida que el dispositivo se aleja del punto de acceso.",
        "c) La distancia puede afectar negativamente al rendimiento, debilitando la señal inalámbrica.",
        "d) La señal inalámbrica siempre permanece constante, independientemente de la distancia.",
    ],
    "c"
),
(
    "¿Qué puede significar la merma en el rendimiento de un dispositivo inalámbrico según la distancia al punto de acceso, según la información proporcionada?",
    [
        "a) Siempre implica una mejora en el ancho de banda.",
        "b) No tiene ningún impacto en la conexión inalámbrica.",
        "c) Puede significar menor ancho de banda o la ausencia absoluta de una conexión inalámbrica.",
        "d) Siempre mejora la conexión inalámbrica.",
    ],
    "c"
),
(
    "¿Qué solución se muestra en la figura para mejorar la señal inalámbrica en partes de la casa que estén demasiado alejadas del punto de acceso inalámbrico?",
    [
        "c) Desplazar el punto de acceso inalámbrico a una ubicación más central.",
        "b) Cambiar la frecuencia de la señal inalámbrica.",
        "a) Utilizar un extensor de alcance inalámbrico.",
        "d) No hay solución para mejorar la señal inalámbrica en estas situaciones.",
    ],
    "a"
),
(
    "En comparación con una conexión inalámbrica, ¿cómo se describe el impacto de una conexión por cable en el rendimiento según la información proporcionada?",
    [
        "a) Una conexión por cable siempre provoca mermas en el rendimiento.",
        "b) Una conexión por cable nunca provoca mermas en el rendimiento.",
        "c) El impacto de una conexión por cable en el rendimiento depende de la distancia.",
        "d) Una conexión por cable no provoca mermas en el rendimiento.",
    ],
    "d"
),
(
    "¿Cómo afecta el acceso a las ondas aéreas compartido por los dispositivos inalámbricos al rendimiento de la red según la información proporcionada?",
    [
        "c) El acceso compartido a las ondas aéreas mejora el rendimiento de la red inalámbrica.",
        "b) No hay impacto en el rendimiento de la red debido al acceso compartido a las ondas aéreas.",
        "a) El rendimiento de la red puede ser más lento a medida que más dispositivos inalámbricos acceden simultáneamente.",
        "d) El rendimiento de la red siempre mejora a medida que más dispositivos inalámbricos acceden simultáneamente.",
    ],
    "a"
),
(
    "¿Qué deben hacer todos los dispositivos inalámbricos en relación con el acceso a las ondas aéreas según la información proporcionada?",
    [
        "a) No es necesario que compartan el acceso a las ondas aéreas.",
        "b) Deben tener su propio punto de acceso inalámbrico.",
        "c) Deben compartir el acceso a las ondas aéreas al conectarse al mismo punto de acceso inalámbrico.",
        "d) No necesitan acceso a las ondas aéreas.",
    ],
    "c"
),
(
    "¿Qué consecuencia se menciona en relación con el rendimiento de la red cuando más dispositivos inalámbricos acceden simultáneamente, según la información proporcionada?",
    [
        "a) El rendimiento de la red siempre mejora con más dispositivos inalámbricos conectados.",
        "c) El rendimiento de la red no se ve afectado por la cantidad de dispositivos inalámbricos conectados simultáneamente.",
        "b) El rendimiento de la red puede ser más lento a medida que más dispositivos inalámbricos acceden simultáneamente.",
        "d) Solo los dispositivos conectados por cable experimentan un rendimiento más lento con la conexión simultánea de varios dispositivos.",
    ],
    "b"
),
(
    "¿Cuál es la diferencia mencionada en términos de compartir el acceso a la red entre dispositivos inalámbricos y dispositivos conectados por cable, según la información proporcionada?",
    [
        "a) Todos los dispositivos, ya sean inalámbricos o conectados por cable, comparten el acceso a la red por igual.",
        "b) Los dispositivos inalámbricos necesitan compartir el acceso a la red, a diferencia de los dispositivos conectados por cable.",
        "c) Los dispositivos inalámbricos no necesitan compartir el acceso a la red, a diferencia de los dispositivos conectados por cable.",
        "d) La necesidad de compartir el acceso a la red es la misma para todos los dispositivos, independientemente de su conexión.",
    ],
    "b"
),
(
    "Según la información proporcionada, ¿cómo se describe el canal de comunicación para cada dispositivo conectado por cable?",
    [
        "a) Todos los dispositivos conectados por cable comparten un canal de comunicación.",
        "b) Cada dispositivo conectado por cable tiene un canal de comunicación independiente a través de su propio cable Ethernet.",
        "c) Los dispositivos conectados por cable no tienen un canal de comunicación.",
        "d) El canal de comunicación para dispositivos conectados por cable depende del punto de acceso inalámbrico.",
    ],
    "b"
),
(
    "¿Por qué se destaca la importancia de tener un canal de comunicación independiente para dispositivos conectados por cable, especialmente al considerar aplicaciones que requieren más ancho de banda dedicado?",
    [
        "a) Todas las aplicaciones tienen los mismos requisitos de ancho de banda, independientemente de la conexión.",
        "b) No hay diferencia en el rendimiento entre aplicaciones que requieren más ancho de banda y otras.",
        "c) Las aplicaciones que requieren más ancho de banda no son relevantes para la calidad de la conexión.",
        "d) Algunas aplicaciones, como juegos en línea, transmisión de vídeo y conferencias de vídeo, requieren más ancho de banda dedicado, y tener un canal de comunicación independiente para dispositivos conectados por cable es crucial.",
    ],
    "d"
),
(
    "¿Cuál es la función principal de la capa física según la descripción proporcionada?",
    [
        "a) La capa física segmenta los datos de usuario y los coloca en paquetes.",
        "b) La capa física codifica las tramas y crea señales eléctricas, ópticas o de ondas de radio que representan los bits en cada trama.",
        "c) La capa física restaura las señales a sus representaciones en bits y las pasa a la capa de enlace de datos.",
        "d) La capa física encapsula los datos en forma de trama y los envía por los medios de red.",
    ],
    "b"
),
(
    "Según la descripción proporcionada, ¿cuál es el papel principal de la capa física en OSI?",
    [
        "a) La capa física segmenta los bits y los transporta a través de la red.",
        "b) La capa física proporciona los medios de transporte de los bits de la capa de enlace de datos a través de los medios de red.",
        "c) La capa física encapsula los datos en forma de trama.",
        "d) La capa física codifica las tramas para su transmisión por la red.",
    ],
    "b"
),
(
    "¿Cuál es el proceso que realiza la capa física al recibir una trama completa desde la capa de enlace de datos?",
    [
        "a) La capa física segmenta la trama en bits y la transmite por los medios de red.",
        "b) La capa física codifica la trama como una secuencia de señales y la transmite en los medios locales.",
        "c) La capa física envía la trama completa a la capa de red para su procesamiento.",
        "d) La capa física desencapsula la trama y la pasa a la capa de aplicación para su interpretación.",
    ],
    "b"
),
(
    "Cuando un dispositivo final o un dispositivo intermediario recibe los bits codificados de una trama, ¿cuál es la acción principal que realiza?",
    [
        "a) El dispositivo descarta los bits ya que no son necesarios para la operación de la red.",
        "b) Los bits se almacenan en el dispositivo sin realizar ninguna acción adicional.",
        "c) El dispositivo restaura las señales a sus representaciones en bits y pasa los bits a la capa de enlace de datos en forma de trama completa.",
        "d) El dispositivo codifica nuevamente los bits antes de pasarlos a la capa de red.",
    ],
    "c"
),
(
    "¿Cuál es la función principal de la capa física en el proceso de transporte de datos desde un nodo de origen hasta un nodo de destino?",
    [
        "a) Segmentar los datos de usuario.",
        "b) Codificar las tramas y crear señales eléctricas, ópticas o de ondas de radio.",
        "c) Colocar los datos en paquetes.",
        "d) Restaurar las señales a sus representaciones en bits y pasar los bits a la capa de enlace de datos en forma de trama completa.",
    ],
    "b"
),
(
    "En el proceso de transporte de datos, ¿cuál es el papel de la capa de transporte?",
    [
        "a) Codificar las tramas y crear señales eléctricas, ópticas o de ondas de radio.",
        "b) Segmentar los datos de usuario.",
        "c) Colocar los datos en paquetes.",
        "d) Restaurar las señales a sus representaciones en bits y pasar los bits a la capa de enlace de datos en forma de trama completa.",
    ],
    "b"
),
(
    "¿Cuál es la responsabilidad principal de la capa física en el proceso de transporte de datos?",
    [
        "a) Segmentar los datos de usuario.",
        "b) Restaurar las señales a sus representaciones en bits y pasar los bits a la capa de enlace de datos en forma de trama completa.",
        "c) Colocar los datos en paquetes.",
        "d) Codificar las tramas y crear señales eléctricas, ópticas o de ondas de radio que representan los bits en cada trama.",
    ],
    "d"
),
(
    "Después de que la capa física codifica las tramas y crea las señales, ¿qué ocurre a continuación?",
    [
        "a) Las señales se almacenan en el dispositivo sin realizar ninguna acción adicional.",
        "b) Las señales se descartan ya que no son necesarias para el funcionamiento de la red.",
        "c) Las señales se envían por los medios una a la vez.",
        "d) Las señales se restauran a sus representaciones en bits y se envían a la capa de enlace de datos en forma de trama completa.",
    ],
    "c"
),
(
    "Cuando la capa física del nodo de destino recupera las señales individuales de los medios y las restaura a sus representaciones en bits, ¿qué ocurre a continuación?",
    [
        "a) Los bits se almacenan en el dispositivo sin realizar ninguna acción adicional.",
        "b) Los bits se descartan ya que no son necesarios para el funcionamiento de la red.",
        "c) Los bits se envían a la capa de transporte para su procesamiento.",
        "d) Los bits se pasan a la capa de enlace de datos en forma de trama completa.",
    ],
    "d"
),
(
    "¿Cuáles son los tres formatos básicos de medios de red según la capa física?",
    [
        "a) Cable de cobre, cable de plástico, conexión inalámbrica.",
        "b) Cable de aluminio, cable de fibra de vidrio, conexión inalámbrica.",
        "c) Cable de cobre, cable de fibra óptica, conexión inalámbrica.",
        "d) Cable de plástico, cable de fibra de vidrio, conexión satelital.",
    ],
    "c"
),
(
    "En la capa física, ¿cómo se representan las señales en un cable de cobre?",
    [
        "a) Mediante patrones de pulsos eléctricos.",
        "b) Mediante patrones de luz.",
        "c) Mediante patrones de microondas.",
        "d) Mediante patrones de señales sonoras.",
    ],
    "a"
),
(
    "¿Cómo se representan las señales en un cable de fibra óptica en la capa física?",
    [
        "a) Mediante patrones de pulsos eléctricos.",
        "b) Mediante patrones de luz.",
        "c) Mediante patrones de microondas.",
        "d) Mediante patrones de señales sonoras.",
    ],
    "b"
),
(
    "¿Cuál es la representación de las señales en una conexión inalámbrica en la capa física?",
    [
        "a) Mediante patrones de pulsos eléctricos.",
        "b) Mediante patrones de luz.",
        "c) Mediante patrones de microondas.",
        "d) Mediante patrones de señales sonoras.",
    ],
    "c"
),
(
    "¿Quién rige todos los aspectos de las funciones de la capa física para habilitar la interoperabilidad?",
    [
        "a) El fabricante de dispositivos de red.",
        "b) El proveedor de servicios de Internet.",
        "c) Los usuarios finales.",
        "d) Los organismos de estandarización.",
    ],
    "d"
),
(
    "¿Cuál de las siguientes organizaciones NO está involucrada en el establecimiento y mantenimiento de estándares de la capa física?",
    [
        "a) Organización Internacional para la Estandarización (ISO).",
        "b) Asociación de las Industrias de las Telecomunicaciones (TIA).",
        "c) Instituto Nacional Estadounidense de Estándares (ANSI).",
        "d) Asociación Mundial de Fabricantes de Computadoras (WAMA).",
    ],
    "d"
),
(
    "¿Quiénes son los responsables del diseño y desarrollo de software para los protocolos y operaciones de las capas OSI superiores?",
    [
        "a) Ingenieros en software e informáticos.",
        "b) Ingenieros eléctricos y electrónicos.",
        "c) Reguladores gubernamentales.",
        "d) Organizaciones internacionales de cableado.",
    ],
    "a"
),
(
    "¿Qué grupo de trabajo define los servicios y protocolos del conjunto TCP/IP?",
    [
        "a) Grupo de Trabajo de Ingeniería de Internet (IETF).",
        "b) Organización Internacional para la Estandarización (ISO).",
        "c) Instituto de Ingenieros Eléctricos y Electrónicos (IEEE).",
        "d) Administración Nacional de Aeronáutica y el Espacio (NASA).",
    ],
    "a"
),
(
    "¿Qué elementos conforman la capa física, según la descripción?",
    [
        "a) Software, servicios y protocolos del conjunto TCP/IP.",
        "b) Circuitos electrónicos, medios y conectores.",
        "c) Estándares de hardware, medios, codificación y señalización.",
        "d) Organización Internacional para la Estandarización (ISO), Asociación de las Industrias de las Telecomunicaciones (TIA) y Unión Internacional de Telecomunicaciones (ITU).",
    ],
    "b"
),
(
    "¿Cuáles son algunas de las organizaciones que intervienen en el establecimiento y mantenimiento de los estándares de la capa física?",
    [
        "a) Organización Internacional para la Estandarización (ISO) y Asociación de las Industrias de las Telecomunicaciones (TIA).",
        "b) Unión Internacional de Telecomunicaciones (ITU) y Autoridades nacionales reguladoras de las telecomunicaciones.",
        "c) Instituto Nacional Estadounidense de Estándares (ANSI) y Instituto de Ingenieros Eléctricos y Electrónicos (IEEE).",
        "d) Todas las anteriores.",
    ],
    "d"
),
(
    "¿Cuáles son algunos de los grupos regionales de estandarización de cableado mencionados?",
    [
        "a) Canadian Standards Association (CSA) y European Committee for Electrotechnical Standardization (CENELEC).",
        "b) Japanese Standards Association (JSA/JIS) y Federal Communication Commission (FCC).",
        "c) Unión Internacional de Telecomunicaciones (ITU) y Asociación de Industrias Electrónicas (EIA).",
        "d) Todas las anteriores.",
    ],
    "d"
),
(
    "¿Cuáles son algunos ejemplos de componentes físicos asociados con la capa física?",
    [
        "a) Puertos e interfaces de un router Cisco 1941.",
        "b) Protocolos y servicios de red.",
        "c) Algoritmos de enrutamiento.",
        "d) Todos los anteriores.",
    ],
    "a"
),
(
    "¿Cuál es el propósito de los componentes físicos asociados con la capa física?",
    [
        "a) Gestionar protocolos y servicios de red.",
        "b) Realizar algoritmos de enrutamiento.",
        "c) Transmitir y transportar señales para representar los bits.",
        "d) Ninguna de las anteriores.",
    ],
    "c"
),
(
    "En la capa física, ¿qué especifica los componentes de hardware, como NIC, interfaces y conectores?",
    [
        "a) Protocolos de red.",
        "b) Materiales y diseño de los cables.",
        "c) Algoritmos de enrutamiento.",
        "d) Ninguna de las anteriores.",
    ],
    "b"
),
(
    "¿Cuál es un ejemplo de componentes físicos con conectores y diagramas de pines específicos derivados de los estándares?",
    [
        "a) Puertos USB de una computadora portátil.",
        "b) Conectores de auriculares de un teléfono inteligente.",
        "c) Puertos e interfaces de un router Cisco 1941.",
        "d) Conectores de alimentación de una impresora.",
    ],
    "c"
),
(
    "¿Cuál es el propósito de la codificación en una red?",
    [
        "a) Convertir una transmisión de bits en un código predefinido.",
        "b) Mejorar la velocidad de transmisión de datos.",
        "c) Reducir la interferencia electromagnética.",
        "d) Aumentar la capacidad de almacenamiento de datos.",
    ],
    "a"
),
(
    "¿Cuál es el propósito principal de la codificación en una red?",
    [
        "a) Aumentar la capacidad de almacenamiento de datos.",
        "b) Mejorar la velocidad de transmisión de datos.",
        "c) Reducir la interferencia electromagnética.",
        "d) Convertir una transmisión de bits en un código predefinido.",
    ],
    "d"
),
(
    "¿Qué función cumplen los códigos en la codificación de línea en una red?",
    [
        "a) Aumentar la capacidad de almacenamiento de datos.",
        "b) Mejorar la velocidad de transmisión de datos.",
        "c) Reducir la interferencia electromagnética.",
        "d) Proporcionar un patrón predecible reconocible por el emisor y el receptor.",
    ],
    "d"
),
(
    "En el contexto de redes, ¿cuál es el propósito principal de la codificación en la capa física?",
    [
        "a) Aumentar la capacidad de almacenamiento de datos.",
        "b) Mejorar la velocidad de transmisión de datos.",
        "c) Reducir la interferencia electromagnética.",
        "d) Representar los bits mediante un patrón de voltaje o corriente.",
    ],
    "d"
),
(
    "En la codificación Manchester, ¿cómo se representan los bits 0 y 1 respectivamente?",
    [
        "a) 0 se representa con una transición de alto a bajo, y 1 se representa con una transición de bajo a alto.",
        "b) 0 se representa con una transición de bajo a alto, y 1 se representa con una transición de alto a bajo.",
        "c) Ambos 0 y 1 se representan con una transición de alto a bajo.",
        "d) Ambos 0 y 1 se representan con una transición de bajo a alto.",
    ],
    "a"
),
(
    "En la codificación Manchester, ¿cuándo se produce la transición?",
    [
        "a) Al principio del período de bit.",
        "b) Al final del período de bit.",
        "c) En algún momento aleatorio dentro del período de bit.",
        "d) En el medio del período de bit.",
    ],
    "d"
),
(
    "¿En qué velocidad de Ethernet se utiliza comúnmente la codificación Manchester?",
    [
        "a) Ethernet 100 bps.",
        "b) Ethernet 1 Gbps.",
        "c) Ethernet 10 Gbps.",
        "d) Ethernet 10 bps.",
    ],
    "d"
),
(
    "¿Cómo afecta la velocidad de datos a la complejidad de la codificación en redes?",
    [
        "a) La velocidad de datos no afecta la complejidad de la codificación.",
        "b) A velocidades más altas, la codificación tiende a ser más simple.",
        "c) A velocidades más altas, la codificación tiende a ser más compleja.",
        "d) La complejidad de la codificación no está relacionada con la velocidad de datos.",
    ],
    "c"
),
(
    "¿Cómo se denomina el método de representación de bits en la capa física?",
    [
        "a) Señalización de datos.",
        "b) Codificación de línea.",
        "c) Modulación de onda.",
        "d) Protocolo de transmisión.",
    ],
    "b"
),
(
    "¿Cuál es la responsabilidad principal de la capa física en una red?",
    [
        "a) Procesar paquetes de datos para su transporte.",
        "b) Gestionar la conexión entre dispositivos finales.",
        "c) Generar señales inalámbricas, ópticas o eléctricas que representan los '1' y '0' en los medios.",
        "d) Encriptar y desencriptar la información transmitida.",
    ],
    "c"
),
(
    "¿Cómo se denomina el método de representación de bits en la capa física?",
    [
        "a) Codificación.",
        "b) Encriptación.",
        "c) Señalización.",
        "d) Modulación.",
    ],
    "c"
),
(
    "¿Qué deben definir los estándares de la capa física en relación con las señales?",
    [
        "c) La longitud de las señales.",
        "b) La velocidad de las señales.",
        "a) Qué tipo de señal representa un '1' y qué tipo de señal representa un '0'.",
        "d) La dirección de las señales.",
    ],
    "a"
),
(
    "En relación con la representación de bits en la capa física, ¿qué puede ser tan simple como un cambio?",
    [
        "a) La longitud de las señales.",
        "b) La velocidad de las señales.",
        "c) El tipo de señal que representa un '1' o un '0'.",
        "d) La dirección de las señales.",
    ],
    "c"
),
(
    "En relación con la transmisión de señales, ¿qué método habitual se utiliza para enviar datos?",
    [
        "a) Codificación Manchester.",
        "b) Técnicas de modulación.",
        "c) Multiplexación por división de tiempo.",
        "d) Transición de voltaje de alto a bajo.",
    ],
    "b"
),
(
    "En el contexto de la transmisión de datos, ¿cómo se define la modulación?",
    [
        "a) Es el proceso de cambiar la fase de una onda.",
        "b) Es el proceso por el cual la característica de una onda (la señal) modifica a otra onda (la portadora).",
        "c) Es el proceso de dividir el tiempo en segmentos para transmitir múltiples señales.",
        "d) Es el cambio en el nivel de una señal eléctrica o de un pulso óptico.",
    ],
    "b"
),
(
    "¿Qué determinará la naturaleza de las señales reales que representan los bits en los medios?",
    [
        "a) El estándar de la capa de enlace de datos.",
        "b) El tipo de dispositivo de red.",
        "c) El método de señalización utilizado.",
        "d) La velocidad de la conexión.",
    ],
    "c"
),
(
    "¿Cómo se mide generalmente el ancho de banda?",
    [
        "a) En voltios.",
        "b) En bits por segundo.",
        "c) En ohmios.",
        "d) En amperios.",
    ],
    "b"
),
(
    "¿Qué afirmación es cierta sobre la transferencia de bits en diferentes medios físicos?",
    [
        "a) La velocidad de transferencia de bits es siempre la misma, independientemente del medio físico.",
        "b) La transferencia de bits es más rápida en conexiones inalámbricas que en conexiones por cable.",
        "c) Los diferentes medios físicos admiten la transferencia de bits a distintas velocidades.",
        "d) La velocidad de transferencia solo depende del tipo de dispositivo utilizado.",
    ],
    "c"
),
(
    "¿Cómo se analiza por lo general la transferencia de datos en una red en términos de características?",
    [
        "a) En términos de velocidad y capacidad.",
        "b) En términos de ancho de banda y rendimiento.",
        "c) En términos de alcance y potencia de señal.",
        "d) En términos de seguridad y privacidad.",
    ],
    "b"
),
(
    "¿Cómo se define el ancho de banda en el contexto de las redes de comunicación?",
    [
        "a) La velocidad de transferencia máxima en un momento dado.",
        "b) La cantidad total de datos almacenados en un medio de conexión.",
        "c) La capacidad de un medio para transportar datos.",
        "d) La distancia máxima que puede cubrir una conexión inalámbrica.",
    ],
    "c"
),
(
    "¿Cómo se define el ancho de banda digital en el contexto de las redes de comunicación?",
    [
        "a) La velocidad de transferencia máxima en un momento dado.",
        "b) La cantidad total de datos almacenados en un medio de conexión.",
        "c) La capacidad de un medio para transportar datos.",
        "d) La cantidad de datos que pueden fluir desde un lugar hacia otro en un período de tiempo determinado.",
    ],
    "d"
),
(
    "¿En qué unidades comúnmente se mide el ancho de banda en las redes de comunicación?",
    [
        "a) Bytes por segundo (Bps).",
        "b) Kilobytes por segundo (KBps).",
        "c) Megabytes por segundo (MBps).",
        "d) Kilobits por segundo (kbps), Megabits por segundo (Mbps) o Gigabits por segundo (Gbps).",
    ],
    "d"
),
(
    "¿Por qué la velocidad a la que viajan los bits no es una medida adecuada para el ancho de banda?",
    [
        "a) Porque la velocidad de transmisión depende únicamente del medio físico.",
        "b) Porque el ancho de banda se mide en unidades distintas a la velocidad.",
        "c) Porque la electricidad siempre viaja a la misma velocidad.",
        "d) Porque la diferencia en el ancho de banda se relaciona con la cantidad de bits transmitidos por segundo, no con la velocidad a la que viajan los bits.",
    ],
    "d"
),
(
    "¿Cuáles son dos de los factores determinantes del ancho de banda práctico de una red?",
    [
        "a) El número de dispositivos conectados y la ubicación geográfica.",
        "b) La velocidad de transmisión y la capacidad de almacenamiento.",
        "c) Las propiedades de los medios físicos y las tecnologías seleccionadas para la señalización y la detección de señales de red.",
        "d) El tipo de conexión y la potencia del equipo de red.",
    ],
    "c"
),
(
    "¿Qué factores desempeñan una función al determinar el ancho de banda disponible en una red?",
    [
        "a) La ubicación geográfica y la potencia del equipo de red.",
        "b) El número de dispositivos conectados y la velocidad de transmisión.",
        "c) Las tecnologías actuales y las leyes de la física.",
        "d) El tipo de conexión y la capacidad de almacenamiento.",
    ],
    "c"
),
(
    "¿Cuál es la diferencia entre el rendimiento y el ancho de banda en una red?",
    [
        "a) El rendimiento es la medida de transferencia de bits, mientras que el ancho de banda es la capacidad máxima de un medio.",
        "b) El ancho de banda se refiere al tiempo de transferencia de datos, mientras que el rendimiento es la capacidad máxima de un medio.",
        "c) El rendimiento es la cantidad de tráfico en una red, mientras que el ancho de banda es la velocidad de transmisión de datos.",
        "d) El ancho de banda se mide en kilobits por segundo, mientras que el rendimiento se mide en megabits por segundo.",
    ],
    "a"
),
(
    "¿Cómo se define el rendimiento en el contexto de las redes de comunicación?",
    [
        "a) La capacidad máxima de un medio para transportar datos.",
        "b) La medida de transferencia de bits a través de los medios durante un período de tiempo determinado.",
        "c) La cantidad de tráfico en una red.",
        "d) La velocidad de transmisión de datos en kilobits por segundo.",
    ],
    "b"
),
(
    "¿Por qué el rendimiento generalmente no coincide con el ancho de banda especificado en las implementaciones de la capa física?",
    [
        "a) Porque el rendimiento se mide en unidades distintas al ancho de banda.",
        "b) Porque el ancho de banda no tiene impacto en el rendimiento de la red.",
        "c) Debido a la interferencia electromagnética en los medios físicos.",
        "d) Debido a diferentes factores que influyen en el rendimiento, como la cantidad de tráfico y la latencia.",
    ],
    "d"
),
(
    "¿Cuáles son algunos de los factores que influyen en el rendimiento de una red?",
    [
        "a) La capacidad de almacenamiento y la velocidad de transmisión.",
        "b) El número de dispositivos conectados y la ubicación geográfica.",
        "c) La cantidad de tráfico, el tipo de tráfico y la latencia creada por la cantidad de dispositivos de red entre origen y destino.",
        "d) La seguridad de la red y la potencia del equipo de red.",
    ],
    "c"
),
(
    "¿Cómo se define la latencia en el contexto de las redes de comunicación?",
    [
        "a) La cantidad de datos transferidos durante un período determinado.",
        "b) La velocidad de transmisión de datos entre dos puntos.",
        "c) La cantidad de tiempo, incluidas las demoras, que les toma a los datos transferirse desde un punto determinado hasta otro.",
        "d) La capacidad máxima de un medio para transportar datos.",
    ],
    "c"
),
(
    "En una internetwork o una red con múltiples segmentos, ¿qué afirmación es cierta sobre el rendimiento?",
    [
        "a) El rendimiento siempre será igual en todos los segmentos de la red.",
        "b) El rendimiento depende únicamente de la cantidad de dispositivos conectados.",
        "c) El rendimiento no puede ser más rápido que el enlace más lento de la ruta de origen a destino.",
        "d) La latencia no afecta al rendimiento en una red con múltiples segmentos.",
    ],
    "c"
),
(
    "¿Qué puede suceder en una red, incluso si la mayoría de los segmentos tienen un ancho de banda elevado?",
    [
        "a) El rendimiento será óptimo en todos los segmentos.",
        "b) La latencia no será afectada por los segmentos con rendimiento inferior.",
        "c) Solo se necesita un segmento en la ruta con un rendimiento inferior para crear un cuello de botella en el rendimiento de toda la red.",
        "d) Todos los segmentos tendrán el mismo rendimiento independientemente de su ancho de banda.",
    ],
    "c"
),
(
    "¿Cómo se puede evaluar el rendimiento de una conexión a Internet según la información proporcionada?",
    [
        "a) Mediante la latencia y la cantidad de tráfico en la red.",
        "b) A través de pruebas de velocidad en línea que revelan el rendimiento de la conexión.",
        "c) Analizando el tipo de tráfico y la capacidad de almacenamiento.",
        "d) Examinando la cantidad de dispositivos conectados en la red.",
    ],
    "b"
),
(
    "¿Qué se entiende por 'capacidad de transferencia útil' en el contexto de las redes de comunicación?",
    [
        "a) La cantidad máxima de datos que pueden fluir a través de una red en un período determinado.",
        "b) La velocidad de transmisión de datos en kilobits por segundo.",
        "c) La medida de datos utilizables transferidos durante un período determinado, sin la sobrecarga de tráfico para establecer sesiones, acuses de recibo y encapsulamientos.",
        "d) La capacidad de almacenamiento de dispositivos conectados en la red.",
    ],
    "c"
),
(
    "¿Cómo se define la capacidad de transferencia útil en el contexto de las redes de comunicación?",
    [
        "a) La cantidad máxima de datos que pueden fluir a través de una red en un período determinado.",
        "b) La velocidad de transmisión de datos en kilobits por segundo.",
        "c) La medida de datos utilizables transferidos durante un período determinado, sin la sobrecarga de tráfico para establecer sesiones, acuses de recibo y encapsulamientos.",
        "d) La capacidad de almacenamiento de dispositivos conectados en la red.",
    ],
    "c"
),
(
    "¿Qué representa la capacidad de transferencia útil en términos de rendimiento de una red?",
    [
        "a) La máxima velocidad de transmisión de datos en la red.",
        "b) El rendimiento total incluyendo la sobrecarga de tráfico para establecer sesiones, acuses de recibo y encapsulamientos.",
        "c) La capacidad de almacenamiento de dispositivos conectados en la red.",
        "d) El rendimiento sin la sobrecarga de tráfico para establecer sesiones, acuses de recibo y encapsulamientos.",
    ],
    "d"
),
(
    "¿Cuál es la función principal de la capa física en una red de comunicación?",
    [
        "a) Administrar la dirección IP de los dispositivos en la red.",
        "b) Producir la representación y agrupación de bits en voltajes, radiofrecuencia e impulsos de luz.",
        "c) Controlar la forma en que los datos acceden a los medios físicos.",
        "d) Establecer sesiones y acuses de recibo en la red.",
    ],
    "b"
),
(
    "¿Qué papel desempeñan las organizaciones que establecen estándares en el contexto de la capa física de una red de comunicación?",
    [
        "a) Administrar la dirección IP de los dispositivos en la red.",
        "b) Producir la representación y agrupación de bits en voltajes, radiofrecuencia e impulsos de luz.",
        "c) Controlar la forma en que los datos acceden a los medios físicos.",
        "d) Contribuir con la definición de las propiedades mecánicas, eléctricas y físicas de los medios disponibles para diferentes comunicaciones de datos.",
    ],
    "d"
),
(
    "¿Cuál es el propósito de las especificaciones establecidas por las organizaciones en relación con los cables y conectores en una red de comunicación?",
    [
        "a) Administrar la dirección IP de los dispositivos en la red.",
        "b) Producir la representación y agrupación de bits en voltajes, radiofrecuencia e impulsos de luz.",
        "c) Controlar la forma en que los datos acceden a los medios físicos.",
        "d) Garantizar que los cables y conectores funcionen según lo previsto mediante diferentes implementaciones de la capa de enlace de datos.",
    ],
    "d"
),
(
    "¿Qué aspectos son definidos por los estándares para los medios de cobre en una red de comunicación?",
    [
        "a) La administración de la dirección IP de los dispositivos en la red.",
        "b) La producción de la representación y agrupación de bits en voltajes, radiofrecuencia e impulsos de luz.",
        "c) La regulación de la forma en que los datos acceden a los medios físicos.",
        "d) Tipo de cableado de cobre utilizado, ancho de banda de la comunicación, tipo de conectores utilizados, diagrama de pines y códigos de colores de las conexiones a los medios, y distancia máxima de los medios.",
    ],
    "d"
),
(
    "¿Cuáles son las limitaciones principales de los medios de cobre en una red de comunicación?",
    [
        "a) Alta resistencia a la corriente eléctrica y dificultad en la instalación.",
        "b) Distancia limitada y baja interferencia de señales.",
        "c) Costo elevado y baja resistencia a la corriente eléctrica.",
        "d) Distancia limitada y susceptibilidad a interferencias, como EMI, RFI y Crosstalk.",
    ],
    "d"
),
(
    "¿Cuáles son las razones principales por las que las redes utilizan medios de cobre en lugar de otros?",
    [
        "a) Por su alta resistencia a la corriente eléctrica y facilidad de instalación.",
        "b) Debido a su costo elevado y baja resistencia a la corriente eléctrica.",
        "c) Por ser económicos, fáciles de instalar y tener baja resistencia a la corriente eléctrica.",
        "d) Por su alta resistencia a la corriente eléctrica y baja interferencia de señales.",
    ],
    "c"
),
(
    "¿Cuáles son las limitaciones principales de los medios de cobre en una red de comunicación?",
    [
        "a) Alta resistencia a la corriente eléctrica y dificultad en la instalación.",
        "b) Distancia limitada y baja interferencia de señales.",
        "c) Costo elevado y baja resistencia a la corriente eléctrica.",
        "d) Distancia limitada y susceptibilidad a interferencias, como EMI, RFI y Crosstalk.",
    ],
    "d"
),
(
    "¿Cómo se transmiten los datos en cables de cobre en una red de comunicación?",
    [
        "a) Como ondas de radio.",
        "b) A través de impulsos eléctricos.",
        "c) Utilizando señales de luz.",
        "d) Mediante señales magnéticas.",
    ],
    "b"
),
(
    "¿Cuál es el requisito clave para que un detector en la interfaz de red de un dispositivo de destino reciba una señal en una red de comunicación?",
    [
        "a) La velocidad de transmisión.",
        "b) La codificación de la señal.",
        "c) La longitud del cable de cobre.",
        "d) La cantidad de dispositivos conectados a la red.",
    ],
    "b"
),
(
    "¿Qué concepto se utiliza para describir el fenómeno en el que una señal se deteriora a medida que viaja a mayores distancias en un cable de cobre?",
    [
        "a) Interferencia electromagnética.",
        "b) Atenuación de señal.",
        "c) Crosstalk.",
        "d) Ancho de banda.",
    ],
    "b"
),
(
    "¿Por qué es necesario que los medios de cobre sigan limitaciones estrictas de distancia en una red de comunicación?",
    [
        "a) Para evitar interferencia electromagnética.",
        "b) Para garantizar la seguridad de la red.",
        "c) Debido a la atenuación de señal a mayores distancias.",
        "d) Para facilitar la instalación de cables.",
    ],
    "c"
),
(
    "¿Cuáles son las dos fuentes principales de interferencia que afectan los valores de temporización y voltaje de los pulsos eléctricos en los cables de cobre?",
    [
        "a) Interferencia de señales digitales y señales analógicas.",
        "b) Interferencia electromagnética (EMI) y crosstalk.",
        "c) Atenuación de señal y ruido eléctrico.",
        "d) Interferencia de radiofrecuencia (RFI) y ruido térmico.",
    ],
    "b"
),
(
    "¿Cómo pueden afectar la interferencia electromagnética (EMI) y la interferencia de radiofrecuencia (RFI) a los medios de cobre?",
    [
        "a) Mejoran la calidad de la señal de datos.",
        "b) No tienen ningún impacto en la transmisión de datos.",
        "c) Pueden distorsionar y dañar las señales de datos en los medios de cobre.",
        "d) Aumentan la velocidad de transmisión de datos.",
    ],
    "c"
),
(
    "¿Cuáles son posibles fuentes de interferencia electromagnética (EMI) y radiofrecuencia (RFI) que pueden afectar a los medios de cobre?",
    [
        "a) Ondas de luz, ondas de radio o huracanes",
        "b) Motores eléctricos, ondas de radio o luces fluorescentes,",
        "c) Agua potable, luces de neón y vapores.",
        "d) Alimentos sólidos",
    ],
    "b"
),
(
    "¿Cómo se define el crosstalk en el contexto de los medios de cobre?",
    [
        "a) Una conexión de red inalámbrica",
        "b) Una perturbación causada por campos electromagnéticos o magnéticos de una señal a un hilo adyacente",
        "c) Una forma de codificación de datos",
        "d) Un tipo de conexión por cable",
    ],
    "b"
),
(
    "¿Cómo puede afectar el crosstalk a los circuitos telefónicos?",
    [
        "a) Mejora la calidad de la voz en la conversación",
        "b) No tiene impacto en los circuitos telefónicos",
        "c) Puede provocar que se escuche parte de otra conversación de voz de un circuito adyacente",
        "d) Aumenta la velocidad de transmisión de datos",
    ],
    "c"
),
(
    "¿Cómo puede la corriente eléctrica en un hilo afectar a otro hilo adyacente en términos de crosstalk?",
    [
        "a) La corriente eléctrica no tiene impacto en hilos adyacentes",
        "b) Crea un campo magnético que puede afectar un hilo adyacente, causando crosstalk",
        "c) Reduce la interferencia electromagnética en hilos cercanos",
        "d) Aumenta la velocidad de transmisión de datos en el hilo adyacente",
    ],
    "b"
),
(
    "¿Qué medida se toma para contrarrestar los efectos negativos de la EMI y la RFI en algunos cables de cobre?",
    [
        "a) Aumentar la distancia de transmisión",
        "b) Utilizar cables más delgados",
        "c) Empaquetar los cables con un blindaje metálico y proporcionar una conexión a tierra adecuada",
        "d) Reducir la velocidad de transmisión",
    ],
    "c"
),
(
    "¿Cómo contrarrestan algunos tipos de cables de cobre los efectos negativos del crosstalk de manera eficaz?",
    [
        "a) Aumentar la distancia entre los cables",
        "b) Utilizar cables con aislamiento más grueso",
        "c) Trenzar pares de hilos de circuitos opuestos",
        "d) Aplicar un blindaje metálico alrededor de cada hilo",
    ],
    "c"
),
(
    "¿Cómo se puede limitar la susceptibilidad de los cables de cobre al ruido electrónico?",
    [
        "a) Seleccionando un tipo o categoría de cable adecuado al entorno de red",
        "b) Diseñando la infraestructura de cables para atraer fuentes de interferencia",
        "c) Utilizando técnicas de cableado que descuiden el manejo y la terminación de los cables",
        "d) Aumentando la longitud de los cables para reducir la interferencia",
    ],
    "a"
),
(
    "¿Qué factor es crucial para limitar la susceptibilidad de los cables de cobre al ruido electrónico?",
    [
        "a) Longitud de los cables",
        "b) Color de los cables",
        "c) Elección del tipo o categoría de cable adecuado al entorno de red",
        "d) Conexión a tierra del cable",
    ],
    "c"
),
(
    "¿Qué aspecto del cableado ayuda a evitar interferencias en la estructura del edificio?",
    [
        "a) Longitud de los cables",
        "b) Diseño de una infraestructura de cables",
        "c) Color de los cables",
        "d) Tipo de conectores utilizados",
    ],
    "b"
),
(
    "¿Qué aspecto del cableado contribuye a reducir la susceptibilidad al ruido electrónico mediante el uso de técnicas adecuadas?",
    [
        "a) Longitud de los cables",
        "b) Marca del cable",
        "c) Uso de técnicas de manejo y terminación apropiadas",
        "d) Número de conectores en la red",
    ],
    "c"
),
(
    "¿Cuáles son los tres tipos principales de medios de cobre utilizados en las redes?",
    [
        "a) Cable de fibra óptica, cable coaxial y par trenzado no blindado (UTP)",
        "b) Par trenzado no blindado (UTP), par trenzado blindado (STP) y coaxial",
        "c) Cable coaxial, par trenzado no blindado (UTP) y par trenzado blindado (STP)",
        "d) Cable de red cruzado, cable coaxial y cable de par trenzado apantallado (FTP)",
    ],
    "b"
),
(
    "¿Para qué se utilizan los cables de par trenzado en una red y cuáles son sus dispositivos complementarios?",
    [
        "a) Los cables de par trenzado se utilizan para la transmisión de datos inalámbrica y sus dispositivos complementarios son repetidores y puentes.",
        "b) Los cables de par trenzado se utilizan para la conexión de dispositivos de almacenamiento y sus dispositivos complementarios son hubs y switches.",
        "c) Los cables de par trenzado se utilizan para interconectar nodos en una LAN, y sus dispositivos complementarios son switches, routers y puntos de acceso inalámbrico.",
        "d) Los cables de par trenzado se utilizan exclusivamente para conexiones telefónicas, y sus dispositivos complementarios son teléfonos y centrales telefónicas.",
    ],
    "c"
),
(
    "¿Cuál es el propósito principal de los switches en una red y cómo difieren de los routers?",
    [
        "a) Los switches se utilizan para conectar redes LAN, mientras que los routers se utilizan para redes WAN.",
        "b) Los switches y routers cumplen la misma función en una red y son intercambiables.",
        "c) Los switches se utilizan para segmentar una red en dominios de colisión, mientras que los routers se utilizan para interconectar redes y enrutar datos entre ellas.",
        "d) Los switches y routers son términos que se utilizan indistintamente para describir el mismo dispositivo de red.",
    ],
    "c"
),
(
    "¿Por qué es importante seguir los estándares de cableado en las conexiones de red?",
    [
        "a) Los estándares de cableado son solo recomendaciones y no afectan el rendimiento de la red.",
        "b) No es necesario seguir estándares de cableado, ya que todas las conexiones de red son similares.",
        "c) Los estándares de cableado garantizan la interoperabilidad y el rendimiento óptimo de las conexiones de red.",
        "d) Los estándares de cableado solo son relevantes para las conexiones inalámbricas y no para las conexiones por cable.",
    ],
    "c"
),
(
    "¿Por qué es importante seguir los estándares de la capa física en cuanto a los conectores utilizados en redes?",
    [
        "a) Los estándares de la capa física no son relevantes para la elección de conectores en redes.",
        "b) El uso de conectores no estandarizados mejora la flexibilidad de la red.",
        "c) Los estándares garantizan la interoperabilidad y facilitan la conexión y desconexión de dispositivos en la red.",
        "d) La elección de conectores no afecta el rendimiento de la red.",
    ],
    "c"
),
(
    "En el contexto de redes de computadoras, ¿cuál es la función principal de los conectores RJ-45?",
    [
        "a) Proporcionar energía a los dispositivos de red.",
        "b) Transmitir datos entre dispositivos de red.",
        "c) Actuar como un firewall para proteger la red.",
        "d) Administrar la asignación de direcciones IP.",
    ],
    "b"
),







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
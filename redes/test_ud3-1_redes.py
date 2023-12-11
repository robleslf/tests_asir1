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
(
    "¿Cuál es la principal característica del cable de par trenzado no blindado (UTP) utilizado en redes LAN?",
    [
        "a) El cable UTP tiene un revestimiento metálico para proteger contra interferencias.",
        "b) El cable UTP consta de dos pares de hilos codificados por colores.",
        "c) El cable UTP está diseñado para interconectar hosts de red con dispositivos finales como computadoras y impresoras.",
        "d) El cable UTP consta de cuatro pares de hilos codificados por colores que están trenzados entre sí para proteger contra interferencias y se termina con conectores RJ-45.",
    ],
    "d"
),
(
    "¿Cuál es la afirmación correcta sobre el cableado de par trenzado no blindado (UTP) en redes?",
    [
        "a) El UTP es un medio de red poco común y raramente se utiliza.",
        "b) El UTP es el medio de red más común y ampliamente utilizado.",
        "c) El UTP solo se utiliza para conectar dispositivos finales, como computadoras y impresoras.",
        "d) El UTP se utiliza exclusivamente en redes LAN de alta velocidad.",
    ],
    "b"
),
(
    "¿Para qué se utiliza comúnmente el cableado UTP terminado con conectores RJ-45?",
    [
        "a) Exclusivamente para conectar computadoras y dispositivos finales.",
        "b) Para la interconexión de hosts de red con dispositivos intermediarios como switches y routers.",
        "c) Solo en redes LAN de alta velocidad.",
        "d) Principalmente para conectar servidores en entornos empresariales.",
    ],
    "b"
),
(
    "¿Cómo está compuesto el cable UTP utilizado en redes LAN?",
    [
        "a) El cable UTP tiene solo dos pares de hilos sin codificación de colores.",
        "b) El cable UTP consta de seis pares de hilos con codificación de colores.",
        "c) El cable UTP consta de cuatro pares de hilos codificados por colores y trenzados entre sí, con un revestimiento de plástico flexible para protección contra daños físicos menores.",
        "d) El cable UTP tiene un único par de hilos sin ninguna codificación de colores.",
    ],
    "c"
),
(
    "¿Cuál es el propósito principal del trenzado de los hilos en el cable UTP utilizado en redes?",
    [
        "a) Mejorar la velocidad de transmisión de datos.",
        "b) Facilitar la identificación de los hilos.",
        "c) Proteger contra daños físicos.",
        "d) Ayudar a proteger contra interferencias de señales de otros hilos.",
    ],
    "d"
),
(
    "¿Cuál es el propósito principal de los códigos por colores en el cable UTP?",
    [
        "a) Decoración estética del cable.",
        "b) Facilitar la identificación del fabricante del cable.",
        "c) Identificar los pares individuales con sus alambres y ayudar en la terminación de cables.",
        "d) Indicar la velocidad máxima de transmisión del cable.",
    ],
    "c"
),
(
    "¿Cuál es una característica distintiva del cable de par trenzado blindado (STP) en comparación con el cable UTP?",
    [
        "a) El STP es más económico que el UTP.",
        "b) El STP proporciona una mejor protección contra ruido y utiliza conectores RJ-11.",
        "c) El STP es más fácil de instalar que el UTP.",
        "d) El STP utiliza conectores RJ-45 y combina técnicas de blindaje para contrarrestar EMI y RFI, además de trenzado de hilos para contrarrestar crosstalk.",
    ],
    "d"
),
(
    "¿Cuál es una ventaja principal del par trenzado blindado (STP) en comparación con el cable UTP?",
    [
        "a) Mayor velocidad de transmisión.",
        "b) Mayor distancia de transmisión.",
        "c) Mejor protección contra ruido, especialmente EMI y RFI.",
        "d) Menor costo de instalación.",
    ],
    "c"
),
(
    "¿Cuál es una desventaja principal del cable de par trenzado blindado (STP) en comparación con el cable UTP?",
    [
        "a) Mayor velocidad de transmisión.",
        "b) Mayor facilidad de instalación.",
        "c) Menor costo.",
        "d) Mayor costo y dificultad de instalación.",
    ],
    "d"
),
(
    "¿Qué tipo de conector comparten los cables de par trenzado blindado (STP) y no blindado (UTP)?",
    [
        "a) Conector RJ-11.",
        "b) Conector RJ-45.",
        "c) Conector USB.",
        "d) Conector HDMI.",
    ],
    "b"
),
(
    "¿Cuáles son las técnicas combinadas utilizadas en el cable de par trenzado blindado (STP) para contrarrestar interferencias?",
    [
        "a) Trenzado de hilos y conectores blindados.",
        "b) Blindaje de hoja metálica y conectores RJ-11.",
        "c) Trenzado de hilos para contrarrestar crosstalk y blindaje para contrarrestar EMI y RFI.",
        "d) Trenzado de hilos y cables coaxiales.",
    ],
    "c"
),
(
    "¿Cómo se terminan comúnmente los cables de par trenzado blindado (STP) para obtener los máximos beneficios del blindaje?",
    [
        "a) Con conectores RJ-11 estándar.",
        "b) Con conectores de datos STP blindados especiales.",
        "c) Con conectores USB.",
        "d) Con conectores HDMI.",
    ],
    "b"
),
(
    "¿Por qué es importante conectar correctamente a tierra el blindaje de un cable de par trenzado blindado (STP)?",
    [
        "a) Para mejorar la velocidad de transmisión.",
        "b) Para facilitar la instalación del cable.",
        "c) Para prevenir la interferencia magnética.",
        "d) Para evitar que el blindaje actúe como antena y capture señales no deseadas.",
    ],
    "d"
),
(
    "¿Cómo está configurado el cable de par trenzado blindado (STP) que se describe?",
    [
        "a) Dos pares de hilos con blindaje de hoja metálica.",
        "b) Tres pares de hilos con malla tejida.",
        "c) Cuatro pares de hilos con blindaje de hoja metálica y malla tejida o hoja metálica adicional.",
        "d) Cinco pares de hilos sin blindaje.",
    ],
    "c"
),
(
    "¿Cuáles son los componentes principales de un cable coaxial?",
    [
        "a) Dos conductores de cobre y una capa de aislamiento plástico.",
        "b) Un conductor de cobre y una capa de aislamiento plástico flexible.",
        "c) Un conductor de aluminio y una malla de cobre tejida.",
        "d) Un conductor de cobre, una capa de aislamiento plástico, una malla de cobre tejida o una hoja metálica y un revestimiento protector.",
    ],
    "d"
),
(
    "¿Cuál es la característica que da nombre al cable coaxial?",
    [
        "a) La presencia de una capa de aislamiento plástico.",
        "b) La malla de cobre tejida o la hoja metálica.",
        "c) El hecho de que hay dos conductores que comparten el mismo eje.",
        "d) El revestimiento protector que cubre el cable.",
    ],
    "c"
),
(
    "¿Cuáles son los componentes principales de un cable coaxial?",
    [
        "a) Conductor de aluminio, capa de aislamiento plástico y revestimiento protector.",
        "b) Conductor de cobre, capa de aislamiento plástico flexible y malla de cobre tejida o hoja metálica.",
        "c) Dos conductores de cobre y una capa de aislamiento plástico.",
        "d) Conductor de aluminio y revestimiento protector.",
    ],
    "b"
),
(
    "¿Cuál es el propósito del conductor de cobre en un cable coaxial?",
    [
        "a) Actuar como una capa de aislamiento.",
        "b) Transmitir las señales electrónicas.",
        "c) Proporcionar flexibilidad al cable.",
        "d) Funcionar como un revestimiento protector.",
    ],
    "b"
),
(
    "¿Cuál es la función de la capa de aislamiento plástico flexible en un cable coaxial?",
    [
        "a) Transmitir señales electrónicas.",
        "b) Proporcionar flexibilidad al cable.",
        "c) Actuar como un conductor adicional.",
        "d) Rodear al conductor de cobre para aislarlo.",
    ],
    "d"
),
(
    "¿Cuál es el propósito de la malla de cobre tejida o la hoja metálica sobre el material aislante en un cable coaxial?",
    [
        "a) Actuar como un conductor adicional.",
        "b) Transmitir señales electrónicas.",
        "c) Proporcionar flexibilidad al cable.",
        "d) Actuar como segundo hilo en el circuito y blindaje para reducir interferencias electromagnéticas externas.",
    ],
    "d"
),
(
    "¿Cuál es el propósito del revestimiento que cubre la totalidad del cable coaxial?",
    [
        "a) Transmitir señales electrónicas.",
        "b) Actuar como conductor adicional.",
        "c) Proporcionar flexibilidad al cable.",
        "d) Evitar daños físicos menores al cable.",
    ],
    "d"
),
(
    "¿Cuál es la afirmación correcta sobre los conectores de cable coaxial?",
    [
        "a) Todos los conectores de cable coaxial son iguales.",
        "b) Solo hay un tipo de conector para cable coaxial.",
        "c) Existen diferentes tipos de conectores para cable coaxial.",
        "d) Los conectores de cable coaxial no son necesarios.",
    ],
    "c"
),
(
    "Aparte de las instalaciones de Ethernet modernas, ¿cuáles son algunos de los usos adaptados del cable coaxial?",
    [
        "a) No tiene otros usos aparte de las instalaciones de Ethernet.",
        "b) Se utiliza solo en instalaciones de Internet por cable.",
        "c) Conecta dispositivos Bluetooth en instalaciones inalámbricas.",
        "d) Conecta antenas a dispositivos inalámbricos y se utiliza en instalaciones de Internet por cable.",
    ],
    "d"
),
(
    "¿Cuál es uno de los roles del cable coaxial en instalaciones inalámbricas?",
    [
        "a) Transmitir señales de fibra óptica.",
        "b) Conectar dispositivos Bluetooth.",
        "c) Conectar antenas a dispositivos inalámbricos.",
        "d) Proporcionar energía eléctrica a dispositivos inalámbricos.",
    ],
    "c"
),
(
    "Además de conectar antenas a dispositivos inalámbricos, ¿cuál es otro papel del cable coaxial en instalaciones inalámbricas?",
    [
        "a) Transmitir señales de fibra óptica.",
        "b) Transportar energía de radiofrecuencia (RF) entre antenas y equipos de radio.",
        "c) Conectar dispositivos Bluetooth.",
        "d) Proporcionar energía eléctrica a dispositivos inalámbricos.",
    ],
    "b"
),
(
"En instalaciones de Internet por cable, ¿cómo se utiliza el cable coaxial según la descripción dada?",
    [
        "a) Se reemplaza completamente por cables de fibra óptica.",
        "b) No se utiliza en instalaciones de Internet por cable.",
        "c) Se utiliza para conectar dispositivos Bluetooth.",
        "d) Se reemplaza parcialmente y se admite elementos de amplificación con cables de fibra óptica.",
    ],
    "d"
),
(
    "A pesar de las mejoras en las infraestructuras, ¿qué tipo de cableado sigue siendo comúnmente utilizado en las instalaciones del cliente para la conexión a Internet por cable?",
    [
        "a) Cable de fibra óptica.",
        "b) Cable UTP.",
        "c) Cable coaxial.",
        "d) Cable de par trenzado blindado.",
    ],
    "c"
),
(
    "¿Cuál es uno de los peligros potenciales asociados con los medios de cobre en las redes, especialmente en situaciones donde se conectan dispositivos con diferentes potenciales de conexión a tierra?",
    [
        "a) Peligro de inundación.",
        "b) Peligro de explosión.",
        "c) Peligro eléctrico y de incendio.",
        "d) Peligro biológico.",
    ],
    "c"
),
(
    "¿Por qué podría existir el peligro de incendio en los medios de cobre utilizados en redes?",
    [
        "a) Debido a la oxidación de los cables.",
        "b) Por la exposición al agua.",
        "c) Debido a la inflamabilidad y la producción de emanaciones tóxicas del revestimiento y aislamiento de los cables al calentarse o quemarse.",
        "d) Por la conexión a tierra incorrecta.",
    ],
    "c"
),
(
    "¿Quién o qué entidad puede estipular estándares de seguridad para las instalaciones de hardware y cableado?",
    [
        "a) Los fabricantes de hardware.",
        "b) Los usuarios finales de la red.",
        "c) Las organizaciones o autoridades edilicias.",
        "d) Los proveedores de servicios de internet.",
    ],
    "c"
),
(
    "¿Cuál es uno de los problemas potenciales relacionados con los peligros eléctricos del cableado de cobre?",
    [
        "a) Conductividad mejorada.",
        "b) Reducción de riesgos eléctricos.",
        "c) Conducción no deseada de electricidad.",
        "d) Mejora en la eficiencia energética.",
    ],
    "c"
),
(
    "¿Qué riesgo eléctrico se menciona como ejemplo cuando un dispositivo de red está defectuoso?",
    [
        "a) Mayor eficiencia energética.",
        "b) Conducción segura de corriente.",
        "c) Riesgo de que el chasis de otros dispositivos conduzca corriente.",
        "d) Ausencia de peligros eléctricos.",
    ],
    "c"
),
(
    "¿Cuál es un posible problema asociado al cableado de red en términos de niveles de voltaje?",
    [
        "a) Mayor eficiencia energética.",
        "b) Conexión segura a tierra.",
        "c) Posibilidad de niveles de voltaje no deseados.",
        "d) Ausencia de problemas eléctricos.",
    ],
    "c"
),
(
    "¿Cuándo pueden surgir posibles problemas eléctricos al utilizar cableado de cobre para conectar redes en diferentes edificios o pisos?",
    [
        "a) Solo cuando hay tormentas eléctricas.",
        "b) No hay posibilidad de problemas eléctricos.",
        "c) En situaciones donde los edificios o pisos tienen instalaciones de energía diferentes.",
        "d) Solo en edificios de gran altura.",
    ],
    "c"
),
(
    "¿En qué situación el cableado de cobre puede conducir voltajes provocados por descargas eléctricas a los dispositivos de red?",
    [
        "a) Solo durante tormentas eléctricas.",
        "b) Cuando los dispositivos de red están apagados.",
        "c) Si el cableado de cobre está instalado correctamente.",
        "d) En situaciones donde se producen descargas eléctricas.",
    ],
    "d"
),
(
    "¿Cuáles son las posibles consecuencias de las corrientes y voltajes no deseados en el cableado de cobre?",
    [
        "a) Daño a los dispositivos de red y a las PC conectadas.",
        "b) Mejora del rendimiento de los dispositivos de red.",
        "c) Mayor eficiencia energética en la red.",
        "d) Ninguna consecuencia, ya que el cableado de cobre es seguro.",
    ],
    "a"
),
(
    "¿Por qué es importante seguir las especificaciones relevantes y los códigos de edificación al instalar el cableado de cobre?",
    [
        "a) Para aumentar el costo de instalación.",
        "b) Para prevenir situaciones peligrosas y perjudiciales.",
        "c) Para reducir la eficiencia energética de la red.",
        "d) Para no seguir estándares y códigos.",
    ],
    "b"
),
(
    "¿Por qué es importante seguir prácticas de cableado adecuadas para evitar posibles peligros eléctricos y de incendio?",
    [
        "a) Solo por estética.",
        "b) Para cumplir con estándares de seguridad y prevenir daños.",
        "c) No es necesario seguir prácticas específicas de cableado.",
        "d) Para aumentar la complejidad de la red.",
    ],
    "b"
),
(
    "¿Cuántos pares de hilos codificados por colores tiene el cableado de par trenzado no blindado (UTP)?",
    [
        "a) Dos pares.",
        "b) Tres pares.",
        "c) Cuatro pares.",
        "d) Cinco pares.",
    ],
    "c"
),
(
    "¿Cómo limitan el efecto negativo del crosstalk en los cables UTP?",
    [
        "a) Utilizando blindaje metálico.",
        "b) Cambiando el número de vueltas por par de hilos.",
        "c) Aumentando el tamaño del cable.",
        "d) Separando los hilos por una distancia mayor.",
    ],
    "b"
),
(
    "¿Qué ventaja se menciona sobre el tamaño del cable UTP?",
    [
        "a) Es grande y fácil de manejar.",
        "b) Puede ser una desventaja durante la instalación.",
        "c) Su tamaño pequeño puede ser una ventaja durante la instalación.",
        "d) No se menciona ninguna ventaja relacionada con el tamaño.",
    ],
    "c"
),
(
    "¿Cuántos pares de hilos codificados por colores tiene el cableado de par trenzado no blindado (UTP)?",
    [
        "a) Dos pares.",
        "b) Tres pares.",
        "c) Cuatro pares.",
        "d) Cinco pares.",
    ],
    "c"
),
(
    "¿Cuál es la función principal de la trenza entre los hilos en el cable UTP?",
    [
        "a) Proporcionar rigidez al cable.",
        "b) Reducir interferencias electromagnéticas y de radiofrecuencia.",
        "c) Aumentar la velocidad de transmisión.",
        "d) Evitar cortocircuitos.",
    ],
    "b"
),
(
    "¿Qué característica diferencia a los cables UTP del blindaje utilizado para contrarrestar EMI y RFI?",
    [
        "a) Los cables UTP no están afectados por EMI y RFI.",
        "b) Los cables UTP no utilizan blindaje para contrarrestar EMI y RFI.",
        "c) Los cables UTP no dependen únicamente de su trenzado interno para contrarrestar EMI y RFI.",
        "d) Los cables UTP no necesitan protección contra EMI y RFI.",
    ],
    "b"
),
(
    "¿Cómo los diseñadores de cables UTP limitan el efecto negativo del crosstalk?",
    [
        "a) Utilizando blindaje para cada par de hilos.",
        "b) Aplicando campos magnéticos adicionales para contrarrestar el crosstalk.",
        "c) Implementando la anulación al emparejar los hilos en un circuito.",
        "d) Aumentando la longitud total de los cables UTP.",
    ],
    "c"
),
(
    "¿Qué técnica utilizan los diseñadores para mejorar el efecto de anulación en los cables UTP?",
    [
        "a) Cambiando la codificación de colores de los hilos.",
        "b) Incrementando la resistencia eléctrica de los hilos.",
        "c) Cambiando el número de vueltas por par de hilos.",
        "d) Aplicando un recubrimiento metálico en la superficie externa de los cables.",
    ],
    "c"
),
(
    "¿Cómo se logra la anulación en los cables UTP para contrarrestar el crosstalk?",
    [
        "a) Mediante la aplicación de campos magnéticos adicionales.",
        "b) Al aumentar la resistencia eléctrica de los hilos.",
        "c) Emparejando los hilos en un circuito para que los campos magnéticos sean opuestos.",
        "d) Utilizando blindaje en cada hilo para evitar interferencias.",
    ],
    "c"
),
(
    "¿Qué sucede cuando los campos magnéticos generados por dos hilos en un circuito UTP son opuestos?",
    [
        "a) Se produce interferencia electromagnética (EMI).",
        "b) Se anulan mutuamente, contrarrestando cualquier señal de EMI y RFI externa.",
        "c) Los hilos se enredan, causando cortocircuitos.",
        "d) Aumenta la resistencia eléctrica en el circuito.",
    ],
    "b"
),
(
    "¿Cómo contribuye el cambio en el número de vueltas por par de hilos en un cable UTP a la reducción del crosstalk?",
    [
        "a) Aumenta el crosstalk, causando interferencia en las señales.",
        "b) Disminuye la resistencia eléctrica del cable.",
        "c) Mejora el efecto de anulación entre los campos magnéticos de los hilos.",
        "d) No tiene ningún impacto en el rendimiento del cable.",
    ],
    "c"
),
(
    "¿Por qué es importante seguir especificaciones precisas en cuanto al número de vueltas o trenzas por metro en cables UTP?",
    [
        "a) Para aumentar la resistencia eléctrica del cable.",
        "b) Para reducir la flexibilidad del cable.",
        "c) Para mejorar la eficiencia de transmisión y reducir el crosstalk.",
        "d) No tiene impacto en el rendimiento del cable UTP.",
    ],
    "c"
),
(
    "¿Por qué se observa que el par naranja y naranja/blanco está menos trenzado que el par azul y azul/blanco en la figura? xdddddddddddd",
    [
        "a) Es un error en la fabricación del cable.",
        "b) No hay razón específica para la diferencia de trenzado.",
        "c) La diferencia de trenzado afecta positivamente a la transmisión de datos.",
        "d) La diferencia de trenzado afecta negativamente a la transmisión de datos."
    ],
    "c"
),
(
    "¿Cuál es la principal estrategia de los cables UTP para limitar la degradación de la señal y proporcionar un autoblindaje eficaz de los pares de hilos?",
    [
        "a) Utilizan un revestimiento externo de metal para el blindaje.",
        "b) Dependan de la anulación producida por los pares de hilos trenzados.",
        "c) Incorporan materiales aislantes especiales.",
        "d) Utilizan conectores RJ-45 blindados."
    ],
    "b"
),
(
    "¿Qué estándar establece los estándares comerciales de cableado para las instalaciones LAN y es el estándar de mayor uso en entornos de cableado LAN?",
    [
        "a) IEEE",
        "b) TIA/EIA-568",
        "c) Cat5",
        "d) Cat6"
    ],
    "b"
),
(
    "¿Qué elementos define el estándar TIA/EIA-568?",
    [
        "a) Tipos de cables, longitudes del cable y conectores",
        "b) Terminación de los cables y métodos para realizar pruebas de cable",
        "c) Todos los anteriores",
        "d) Ninguno de los anteriores"
    ],
    "c"
),
(
    "¿Quién define las características eléctricas del cableado de cobre?",
    [
        "a) TIA/EIA",
        "b) IEEE",
        "c) ISO",
        "d) ANSI"
    ],
    "b"
),
(
    "¿Cómo se dividen los cables UTP según su capacidad para transportar datos y velocidades?",
    [
        "a) Por colores",
        "b) Por marcas",
        "c) Por categorías",
        "d) Por longitud"
    ],
    "c"
),
(
    "¿En qué tipo de instalaciones se utiliza comúnmente el cable de Categoría 5 (Cat5)?",
    [
        "a) Gigabit Ethernet",
        "b) FastEthernet 100BASE-TX",
        "c) Fibra óptica",
        "d) 10BASE-T"
    ],
    "b"
),
(
    "¿Cuál es el propósito principal de diseñar cables de categorías superiores?",
    [
        "a) Reducir el costo de producción.",
        "b) Mejorar la flexibilidad del cable.",
        "c) Admitir velocidades superiores de transmisión de datos.",
        "d) Facilitar la instalación en entornos húmedos."
    ],
    "c"
),
(
    "¿Qué categoría de cable es mínimamente aceptable para las actuales tecnologías Ethernet de velocidades en gigabits?",
    [
        "a) Cat5",
        "b) Cat5e",
        "c) Cat6",
        "d) Cat6a"
    ],
    "b"
),
(
    "¿Cuál es el tipo de cable recomendado para nuevas instalaciones edilicias?",
    [
        "a) Cat5",
        "b) Cat5e",
        "c) Cat6",
        "d) Cat6a"
    ],
    "c"
),
(
    "¿Cómo se refieren algunos fabricantes a los cables que exceden las especificaciones de la categoría 6a?",
    [
        "a) Cables de Categoría 6a+",
        "b) Cables de Categoría 7",
        "c) Cables de Categoría 6b",
        "d) Cables de Categoría 6a mejorados"
    ],
    "b"
),
(
    "¿Para qué se utiliza con mayor frecuencia el cable de Categoría 3 (UTP)?",
    [
        "a) Transmisión de datos a alta velocidad",
        "b) Comunicación de voz",
        "c) Líneas telefónicas",
        "d) b y c son correctas."
    ],
    "d"
),
(
"¿Cuál es una característica de los cables de Categoría 5 o 5e (UTP)?",
    [
        "a) Utilizado para la transmisión de voz",
        "b) Utilizado para la trasmisión de video",
        "c) Utilizado para la transmisión de radio",
        "d) Utilizado para la transmisión de datos"
    ],
    "d"
),
(
"¿Cuál es una característica de los cables de Categoría 5 o 5e (UTP)?",
    [
        "a) Los cables Cat5 admiten velocidades de 100 Mbps y pueden admitir velocidades de 1000 Mbps, pero esto no se recomienda.",
        "b) Los cables Cat5 admiten velocidades de 100 Mbps y pueden admitir velocidades de 1000 Mbps, que es lo recomendable.",
        "c) Los cables Cat5 admiten velocidades de 10 Mbps y pueden admitir velocidades de 100 Mbps, pero esto no se recomienda.",
        "d) Los cables Cat5 admiten velocidades de 10 Mbps y pueden admitir velocidades de 100 Mbps, pero esto no se recomienda."
    ],
    "a"
),
(
    "¿Cuál es una característica de los cables de Categoría 6 (UTP)?",
    [
        "a) Limitado a velocidades de 100 Mbps",
        "b) No se recomienda para velocidades superiores a 1 Gbps",
        "c) No utilizado para la transmisión de datos",
        "d) Cuenta con un separador entre cada par de cables para velocidades más elevadas"
    ],
    "d"
),
(
    "¿Cuál es una característica de los cables de Categoría 6 (UTP)?",
    [
        "a) Utilizado para la transmisión entre dispositivos antiguos.",
        "b) Utilizado para la transmisión de video.",
        "c) Utilizado para la transmisión de audio.",
        "d) Utilizado para la transmisión de datos."
    ],
    "d"
),
(
    "¿Cuál es una característica de los cables de Categoría 6 (UTP)?",
    [
        "a) Cuenta con un separador agregado entre cada par de cables para permitir que funcione a velocidades más elevadas.",
        "b) Cuenta con un separador agregado entre cada cable para permitir que funcione a velocidades más elevadas.",
        "c) Cuenta con un separador agregado entre cada par de cables para permitir que funcione sin interferencias.",
        "d) Cuenta con un separador agregado entre cada cable para permitir que funcione sin interferencias."
    ],
    "a"
),
(
    "¿Cuál es una característica de los cables de Categoría 6 (UTP)?",
    [
        "a) Admite velocidades desde 100 Mbps hasta 10 Gbps, aunque esta última no se recomienda.",
        "b) Admite velocidades desde 1000 Mbps hasta 10 Gbps, aunque esta última no se recomienda.",
        "c) Admite velocidades desde 100 Mbps hasta 10 Gbps, siendo esta última la recomendada.",
        "d) Admite velocidades desde 1000 Mbps hasta 10 Gbps, siendo esta última la recomendada."
    ],
    "b"
),
(
    "¿Cuál es el conector comúnmente utilizado para terminar los cables UTP?",
    [
        "a) RJ-11",
        "b) RJ-45",
        "c) USB",
        "d) HDMI"
    ],
    "b"
),
(
    "¿Cuál de las siguientes afirmaciones sobre los cables de categoría 6 (UTP) es correcta?",
    [
        "a) Se utiliza para la comunicación de voz.",
        "b) Admite velocidades de hasta 100 Mbps.",
        "c) No cuenta con un separador agregado entre cada par de cables.",
        "d) Admite velocidades desde 1000 Mbps hasta 10 Gbps."
    ],
    "d"
),
(
    "¿Cómo suelen terminarse los cables UTP en el contexto de las redes?",
    [
        "a) Con conectores USB.",
        "b) Con conectores VGA.",
        "c) Con conectores RJ-45.",
        "d) Con conectores HDMI.",
    ],
    "c"
),
(
    "¿Para qué especificaciones de capa física se utiliza comúnmente el conector RJ-45, incluyendo una importante como Ethernet?",
    [
        "a) Exclusivamente para USB.",
        "b) Principalmente para VGA.",
        "c) Mayormente para HDMI.",
        "d) Comúnmente para Ethernet y otras especificaciones de capa física.",
    ],
    "d"
),
(
    "¿Qué describe el estándar TIA/EIA-568 en el contexto de cables Ethernet?",
    [
        "a) Las especificaciones de USB.",
        "b) La evolución histórica de los cables de red.",
        "c) Las asignaciones de códigos por colores de los hilos y el diagrama de pines de los cables Ethernet.",
        "d) La función de los conectores HDMI en la red.",
    ],
    "c"
),
(
    "En el contexto de conexiones de red, ¿cuál es la función del conector RJ-45?",
    [
        "a) Es el componente hembra en dispositivos de red.",
        "b) Es el componente macho en el extremo del cable.",
        "c) Es el conector utilizado exclusivamente para HDMI.",
        "d) Es el componente utilizado en paneles de conexiones de red.",
    ],
    "b"
),
(
    "¿Por qué es fundamental asegurar terminaciones de calidad superior al trabajar con cables de cobre en redes?",
    [
        "a) Para evitar la pérdida de señal y la generación de ruido en el circuito de comunicación.",
        "b) Porque cada terminación incorrecta representa una fuente potencial de mejora del rendimiento.",
        "c) Solo se aplica a tecnologías de red futuras.",
        "d) No afecta al funcionamiento de la capa física de la red.",
    ],
    "a"
),
(
    "¿Cuáles son las posibles consecuencias al realizar la terminación de un cableado de cobre de manera incorrecta?",
    [
        "a) Pérdida de señal y generación de ruido en el circuito de comunicación.",
        "b) Mejora del rendimiento de la capa física de la red.",
        "c) Garantía de un funcionamiento óptimo en tecnologías de red actuales y futuras.",
        "d) Ausencia de impacto en el rendimiento de la capa física.",
    ],
    "a"
),
(
    "¿Qué representa cada cable cuando las terminaciones se realizan de manera incorrecta?",
    [
        "a) Una fuente de mejora del rendimiento de la capa física.",
        "b) Una garantía de funcionamiento óptimo en tecnologías de red actuales y futuras.",
        "c) Una posible fuente de degradación del rendimiento de la capa física.",
        "d) Un componente independiente del rendimiento de la red.",
    ],
    "c"
),
(
    "¿Por qué es esencial que todas las terminaciones de medios de cobre sean de calidad superior?",
    [
        "a) Para asegurar una conexión segura entre servidores y clientes.",
        "b) Porque garantiza la compatibilidad con tecnologías de red actuales y futuras.",
        "c) Solo es relevante para redes antiguas.",
        "d) No afecta el rendimiento de la capa física de la red.",
    ],
    "b"
),
(
    "¿Cuál es la principal aplicación de un cable directo de Ethernet?",
    [
        "a) Conectar dispositivos similares, como dos switches.",
        "b) Interconectar un host con un switch y un switch con un router.",
        "c) Exclusivamente utilizado para conexiones de consola en dispositivos Cisco.",
        "d) Conectar un router a un switch.",
    ],
    "b"
),
(
    "¿Por qué es necesario que los cables UTP estén correctamente terminados?",
    [
        "a) Para garantizar la compatibilidad con dispositivos y tecnologías de red actuales y futuras.",
        "b) Para evitar la pérdida de señal y la introducción de ruido.",
        "c) Para proteger los cables de daños físicos.",
        "d) Para mejorar el rendimiento de la red.",
    ],
    "b",
),
(
    "¿Cuál es la razón principal por la que los alambres individuales de un cable UTP deben conectarse en diferente orden para distintos grupos de pins en conectores RJ45?",
    [
        "a) Para facilitar el proceso de terminación.",
        "b) Por motivos estéticos.",
        "c) Para adaptarse a diferentes configuraciones de red.",
        "d) Para garantizar la correcta conexión y funcionamiento según las convenciones de cableado.",
    ],
    "d"
),
(
    "¿Cuál es la principal aplicación de un cable cruzado Ethernet?",
    [
        "a) Interconectar un host con un switch.",
        "b) Conectar dispositivos similares, como dos switches o dos routers.",
        "c) Exclusivamente utilizado para conexiones de consola en dispositivos Cisco.",
        "d) Interconectar un switch con un router.",
    ],
    "b"
),
(
    "¿Cuáles son los principales tipos de cable que se obtienen al utilizar las convenciones específicas de cableado?",
    [
        "a) Cable directo de Ethernet, cable cruzado de Ethernet, cable mixto de Ethernet, Cable de consola.",
        "b) Cable directo de Ethernet, cable cruzado de Ethernet, Cable de consola.",
        "c) Cable directo de Ethernet, cable mixto de Ethernet, Cable de consola.",
        "d) Cable directo de Ethernet y cable indirecto de Ethernet.",
    ],
    "b"
),
(
    "¿Cuál es la principal función de un cable directo de Ethernet?",
    [
        "a) Conectar dispositivos similares, como dos switches.",
        "b) Interconectar un host con un switch y un switch con un router.",
        "c) Exclusivamente utilizado para conexiones de consola en dispositivos Cisco.",
        "d) Interconectar un router con un switch.",
    ],
    "b"
),
(
    "¿Cuál es el propósito principal de un cable cruzado Ethernet?",
    [
        "a) Interconectar un host con un switch y un switch con un router.",
        "b) Conectar dispositivos similares, como dos switches o dos routers.",
        "c) Exclusivamente utilizado para conexiones de consola en dispositivos Cisco.",
        "d) Interconectar un router con un switch.",
    ],
    "b"
),
(
    "¿Cuál es la función principal de un cable de consola en el contexto de redes?",
    [
        "a) Interconectar un host con un switch y un switch con un router.",
        "b) Conectar dispositivos similares, como dos switches o dos routers.",
        "c) Exclusivamente utilizado para conexiones de consola en dispositivos Cisco.",
        "d) Interconectar un router con un switch.",
    ],
    "c"
),
(
    "¿Cuál es el resultado probable de usar incorrectamente un cable de conexión cruzada o de conexión directa entre dispositivos?",
    [
        "a) Daño inmediato a los dispositivos conectados.",
        "b) Mejora de la conectividad y la comunicación entre dispositivos.",
        "c) Sin impacto en la conectividad o comunicación entre dispositivos.",
        "d) Falta de conectividad y comunicación entre dispositivos.",
    ],
    "d"
),
(
    "¿Cuál es la primera medida recomendada para resolver problemas de conectividad en un laboratorio si no se logra la conexión entre dispositivos?",
    [
        "a) Cambiar inmediatamente los cables de conexión.",
        "b) Reiniciar todos los dispositivos.",
        "c) Verificar que las conexiones de los dispositivos sean correctas.",
        "d) Reemplazar los dispositivos con problemas.",
    ],
    "c"
),
(
    "Después de la instalación de cables UTP, ¿cuáles son los parámetros que se deben probar utilizando un comprobador de cables?",
    [
        "a) Color de los cables y grosor del aislamiento.",
        "b) Marca y modelo de los conectores utilizados.",
        "c) Mapa de cableado, longitud del cable, pérdida de señal y crosstalk.",
        "d) Nivel de voltaje y corriente en el cableado.",
    ],
    "c"
),
(
    "¿Por qué se recomienda revisar minuciosamente que se cumplan todos los requisitos de instalación de UTP después de la instalación?",
    [
        "a) Para aumentar el rendimiento de la capa física.",
        "b) Por razones estéticas y organizativas.",
        "c) Para verificar la marca y modelo de los conectores utilizados.",
        "d) Para asegurar un funcionamiento óptimo y evitar problemas en la red.",
    ],
    "d"
),
(
    "¿Cuáles son las propiedades distintivas del cableado de fibra óptica en comparación con los cables de cobre?",
    [
        "a) Menor ancho de banda y mayor susceptibilidad a interferencias electromagnéticas.",
        "b) Mayor atenuación de señal y menor distancia de transmisión.",
        "c) Mayor capacidad de transmisión a distancias más extensas y total inmunidad a EMI y RFI.",
        "d) Menor flexibilidad y mayor grosor que un cable de cobre estándar.",
    ],
    "c"
),
(
    "¿Cuál es una de las principales ventajas de la fibra óptica en términos de transmisión de datos?",
    [
        "a) Mayor susceptibilidad a interferencias electromagnéticas.",
        "b) Menor capacidad de transmisión a distancias extensas.",
        "c) Transmisión de datos a través de distancias más extensas y a anchos de banda mayores que cualquier otro medio de red.",
        "d) Limitada inmunidad a las interferencias de radiofrecuencia.",
    ],
    "c"
),
(
    "En comparación con los cables de cobre, ¿cuál es una característica distintiva del cable de fibra óptica?",
    [
        "a) Mayor susceptibilidad a interferencias electromagnéticas.",
        "b) Transmisión de señales con mayor atenuación.",
        "c) Limitada inmunidad a las interferencias de radiofrecuencia.",
        "d) Transmite señales con menos atenuación y es totalmente inmune a EMI y RFI.",
    ],
    "d"
),
(
    "¿Cuál es uno de los usos principales del cable de fibra óptica en el contexto de las redes?",
    [
        "a) Conectar dispositivos de red utilizando señales eléctricas.",
        "b) Proporcionar servicios de banda ancha a hogares y pequeñas empresas.",
        "c) Conectar dispositivos similares, como dos switches.",
        "d) Interconectar dispositivos de red utilizando luz para la transmisión de datos.",
    ],
    "d"
),
(
    "¿Cómo se describe la fibra óptica en términos de su estructura física?",
    [
        "a) Gruesa y rígida, similar a un cable de cobre estándar.",
        "b) Flexible, extremadamente delgada y transparente, no mucho más gruesa que un cabello humano.",
        "c) Similar en grosor a un cable de alimentación eléctrica.",
        "d) Opaca y rígida, como un tubo de metal.",
    ],
    "b"
),
(
    "¿Cómo se codifican los bits en la fibra óptica para la transmisión de datos?",
    [
        "a) Mediante impulsos eléctricos.",
        "b) A través de señales de radiofrecuencia.",
        "c) Utilizando impulsos de luz.",
        "d) Codificación magnética.",
    ],
    "c"
),
(
    "¿Cómo se describe la función principal del cable de fibra óptica en la transmisión de datos?",
    [
        "a) Como un conductor de electricidad.",
        "b) Como una antena receptora de señales de radio.",
        "c) Actúa como una guía de ondas o una 'tubería de luz' para transmitir la luz entre los dos extremos con una pérdida mínima de la señal.",
        "d) Funciona como un generador de campos magnéticos.",
    ],
    "c"
),
(
    "Según la analogía proporcionada, ¿cómo se describe básicamente el funcionamiento de un cable de fibra óptica?",
    [
        "a) Como un rollo de toallas de papel con un puntero magnético.",
        "b) Como un conductor de electricidad recubierto de material reflectante.",
        "c) Como una tubería de luz con un pequeño puntero láser para enviar señales de Código Morse a la velocidad de la luz.",
        "d) Como un generador de campos eléctricos con tecnologías avanzadas de emisión y recepción.",
    ],
    "c"
),
(
    "En la actualidad, ¿cuáles son algunos de los usos del cableado de fibra óptica en distintas industrias?",
    [
        "a) Principalmente en la construcción de edificios y estructuras.",
        "b) Exclusivamente en la industria de la moda.",
        "c) En redes empresariales, Fibre-to-the-Home (FTTH), redes de largo alcance y redes por cable submarinas.",
        "d) Limitado a aplicaciones científicas en laboratorios.",
    ],
    "c"
),
(
    "En redes empresariales, ¿cuál es uno de los principales propósitos de utilizar fibra óptica?",
    [
        "a) Únicamente para aplicaciones de iluminación en edificios de oficinas.",
        "b) Principalmente para conectar dispositivos dentro de una sola habitación.",
        "c) Para aplicaciones de cableado troncal y la interconexión de dispositivos de infraestructura.",
        "d) Exclusivamente para transmisión de señales de radiofrecuencia.",
    ],
    "c"
),
(
    "En la implementación de Fibre-to-the-Home (FTTH), ¿cuál es el propósito principal de utilizar fibra óptica?",
    [
        "a) Exclusivamente para transmisión de señales de televisión por cable.",
        "b) Principalmente para la iluminación en hogares y pequeñas empresas.",
        "c) Para proporcionar servicios de banda ancha siempre activos a hogares y pequeñas empresas.",
        "d) Limitada a aplicaciones científicas en laboratorios domésticos.",
    ],
    "c"
),
(
    "En redes de largo alcance, ¿cuál es el papel principal de la fibra óptica según la información proporcionada?",
    [
        "a) Principalmente para transmisión de señales de radio de largo alcance.",
        "b) Limitada a conexiones locales dentro de una misma ciudad.",
        "c) Utilizada por proveedores de servicios para conectar países y ciudades.",
        "d) Exclusivamente para transmisión de datos a corta distancia.",
    ],
    "c"
),
(
    "En redes por cable submarinas, ¿cuál es uno de los requisitos clave para las soluciones de fibra óptica?",
    [
        "a) Limitada a distancias cortas debido a las limitaciones del agua.",
        "b) Principalmente utilizada para comunicaciones locales entre islas.",
        "c) Proporcionar soluciones confiables de alta velocidad y alta capacidad en entornos submarinos adversos por distancias transoceánicas.",
        "d) Exclusivamente para transmisión de señales de audio submarinas.",
    ],
    "c"
),
(
    "¿Cuál es la composición básica de la fibra óptica en términos de sus componentes?",
    [
        "a) Tres tipos de vidrio (núcleo, revestimiento y blindaje), cada uno con una función específica.",
        "b) Un solo tipo de vidrio con múltiples capas para mayor resistencia.",
        "c) Dos tipos de vidrio (núcleo y revestimiento) y un blindaje exterior de protección.",
        "d) Principalmente compuesta por plástico para mayor flexibilidad.",
    ],
    "c"
),
(
    "¿Cuáles son los componentes principales de la fibra óptica según su diseño?",
    [
        "a) Tres tipos de vidrio (núcleo, revestimiento y blindaje), cada uno con una función específica.",
        "b) Un solo tipo de vidrio con múltiples capas para mayor resistencia.",
        "c) Dos tipos de vidrio (núcleo y revestimiento) y un blindaje exterior de protección.",
        "d) Principalmente compuesta por plástico para mayor flexibilidad.",
    ],
    "c"
),
(
    "A pesar de ser delgada y susceptible a dobleces marcados, ¿qué característica la hace fuerte según las propiedades del vidrio del núcleo y del revestimiento?",
    [
        "a) Un blindaje externo de metal que proporciona resistencia adicional.",
        "b) Su composición de plástico altamente flexible.",
        "c) Las propiedades del núcleo y un revestimiento resistente.",
        "d) Su capacidad para resistir cambios bruscos de temperatura.",
    ],
    "c"
),
(
    "¿Cuál es una de las características destacadas de la fibra óptica en términos de durabilidad y despliegue en condiciones ambientales adversas?",
    [
        "a) Propensa a daños en entornos con variaciones de temperatura.",
        "c) Limitada a implementaciones en interiores y ambientes controlados.",
        "b) Alta durabilidad y capacidad de implementación en redes en condiciones adversas en todo el mundo.",
        "d) Necesita protección adicional para resistir condiciones climáticas extremas.",
    ],
    "b"
),
(
    "¿Cuáles son las dos fuentes principales de generación de pulsos de luz para representar datos en los medios de fibra óptica?",
    [
        "a) Luz solar y luz artificial.",
        "c) Láseres y lámparas incandescentes.",
        "b) Láseres y diodos emisores de luz (LED).",
        "d) Láseres y fluorescentes.",
    ],
    "b"
),
(
    "En sistemas de fibra óptica, ¿qué función desempeñan los dispositivos electrónicos semiconductores conocidos como 'fotodiodos'?",
    [
        "a) Generar pulsos de luz para representar datos.",
        "b) Transmitir señales de voltaje a través de la fibra óptica.",
        "d) Detectar los pulsos de luz y convertirlos en voltajes.",
        "c) Amplificar la señal luminosa en la fibra óptica.",
    ],
    "d"
),
(
    "¿Cuál es una precaución importante al manejar la luz del láser transmitida a través del cableado de fibra óptica?",
    [
        "x) No hay precauciones necesarias, ya que la luz del láser no representa peligro.",
        "y) Es necesario usar gafas de sol al trabajar con cables de fibra óptica.",
        "z) La luz del láser puede dañar el ojo humano, por lo que se debe tener precaución y evitar mirar dentro del extremo de una fibra óptica activa.",
        "w) Se recomienda mirar directamente a la luz del láser para verificar su funcionamiento.",
    ],
    "z"
),
(
    "¿Cuáles son las dos clasificaciones principales de cables de fibra óptica en función del tamaño del núcleo y las tecnologías de transmisión utilizadas?",
    [
        "a) Fibra óptica monocapa y fibra óptica multimodo.",
        "b) Fibra óptica de baja atenuación y fibra óptica de alta atenuación.",
        "c) Fibra óptica de transmisión única y fibra óptica de transmisión múltiple.",
        "d) Fibra óptica monomodo y fibra óptica multimodo.",
    ],
    "d"
),
(
    "¿Cuál es una característica principal de la fibra óptica monomodo (SMF) en términos del tamaño del núcleo y la tecnología de transmisión?",
    [
        "a) Tiene un núcleo grande y utiliza tecnología láser costosa.",
        "b) Tiene un núcleo pequeño y emplea tecnología láser costosa para enviar un único haz de luz.",
        "c) Tiene un núcleo grande y utiliza emisores LED para la transmisión de datos.",
        "d) Tiene un núcleo pequeño y utiliza emisores LED para la transmisión de datos.",
    ],
    "b"
),
(
    "¿En qué situaciones se utiliza comúnmente la fibra óptica monomodo (SMF) debido a sus características de transmisión?",
    [
        "a) En redes LAN para distancias cortas.",
        "b) En aplicaciones de corta distancia como conexiones entre dispositivos en una misma habitación.",
        "c) En situaciones de larga distancia que abarcan cientos de kilómetros, como aplicaciones de TV por cable y telefonía de larga distancia.",
        "d) En redes de área metropolitana (MAN) para conexiones de mediana distancia.",
    ],
    "c"
),
(
    "¿Cuál es una característica principal de la fibra óptica multimodo (MMF) en términos del tamaño del núcleo y la tecnología de transmisión?",
    [
        "a) Tiene un núcleo pequeño y emplea tecnología láser costosa para enviar un único haz de luz.",
        "b) Tiene un núcleo grande y utiliza tecnología láser costosa.",
        "c) Tiene un núcleo grande y utiliza emisores LED para enviar pulsos de luz.",
        "d) Tiene un núcleo pequeño y utiliza emisores LED para enviar pulsos de luz.",
    ],
    "c"
),
(
    "¿Cómo ingresa la luz a la fibra óptica multimodo (MMF) en términos de ángulos y tecnología de transmisión?",
    [
        "a) La luz de un LED ingresa a la fibra en un único ángulo, utilizando tecnología láser.",
        "b) La luz de un LED ingresa a la fibra en diferentes ángulos, utilizando tecnología láser.",
        "c) La luz de un láser ingresa a la fibra en diferentes ángulos, utilizando emisores LED.",
        "d) La luz de un láser ingresa a la fibra en un único ángulo, utilizando emisores LED.",
    ],
    "b"
),
(
    "¿Por qué la fibra óptica multimodo (MMF) se utiliza comúnmente en redes LAN?",
    [
        "a) Por su capacidad para transmitir a largas distancias.",
        "b) Porque utiliza tecnología láser de alto rendimiento.",
        "d) Debido a su capacidad para transmitir a cortas distancias con emisores LED de bajo costo.",
        "c) Por su inmunidad total a las interferencias electromagnéticas (EMI).",
    ],
    "d"
),
(
    "¿Cuál es el ancho de banda típico que proporciona la fibra óptica multimodo (MMF) a través de longitudes de enlace de hasta 550 m?",
    [
        "a) 1 Gbps",
        "b) 10 Gbps",
        "c) 100 Gbps",
        "d) 1 Tbps",
    ],
    "b"
),
(
    "¿Cuál es una de las diferencias destacadas entre la fibra óptica multimodo y monomodo?",
    [
        "a) La potencia eléctrica.",
        "b) La dispersión.",
        "c) El voltaje.",
        "d) La resistencia eléctrica.",
    ],
    "b"
),
(
    "En el contexto de la fibra óptica, ¿cómo se define la dispersión?",
    [
        "a) La dispersión se refiere a la pérdida de potencia de la señal.",
        "b) La dispersión se refiere a la velocidad de transmisión de datos.",
        "c) La dispersión se refiere a la extensión de los pulsos de luz con el tiempo.",
        "d) La dispersión no tiene impacto en la transmisión de datos.",
    ],
    "c"
),
(
    "En la fibra óptica, ¿cómo afecta la dispersión a la pérdida de potencia de la señal?",
    [
        "a) La dispersión no tiene impacto en la pérdida de potencia.",
        "b) Cuanta más dispersión, menor es la pérdida de potencia.",
        "c) Cuanta más dispersión, mayor es la pérdida de potencia.",
        "d) La dispersión y la pérdida de potencia son independientes.",
    ],
    "c"
),
(
    "¿Cuál es la principal diferencia entre los tipos de conectores de fibra óptica?",
    [
        "a) La velocidad de transmisión que admiten.",
        "b) La longitud de los cables a los que pueden estar conectados.",
        "c) Las dimensiones y los métodos de acoplamiento.",
        "d) El número de fibras que pueden transportar simultáneamente.",
    ],
    "c"
),
(
    "¿Cómo termina el extremo de una fibra óptica?",
    [
        "a) Con un conector de fibra óptica.",
        "b) Con un conector RJ-45.",
        "c) Con un conector Willhemson.",
        "d) Con cualquiera de las anteriores.",
    ],
    "a"
),
(
    "¿Cuál de las siguientes afirmaciones es correcta con respecto a los conectores de fibra óptica?",
    [
        "a) Solo hay un tipo de conector de fibra óptica.",
        "b) La variedad de conectores de fibra óptica es limitada.",
        "c) No existen conectores específicos para fibra óptica.",
        "d) Existe una variedad de conectores de fibra óptica.",
    ],
    "d"
),
(
    "¿Cuáles son las principales diferencias entre los tipos de conectores de fibra óptica?",
    [
        "a) Las diferencias principales son solo en los materiales utilizados.",
        "b) Las dimensiones son las únicas diferencias significativas.",
        "c) Los métodos de acoplamiento son los únicos aspectos distintivos.",
        "d) Las diferencias principales son las dimensiones y los métodos de acoplamiento.",
    ],
    "d"
),
(
    "¿Cómo toman las empresas decisiones sobre qué tipos de conectores de fibra óptica utilizarán?",
    [
        "a) De acuerdo con la disponibilidad en el mercado.",
        "b) Basándose únicamente en consideraciones de costos.",
        "c) Sin tener en cuenta los equipos existentes.",
        "d) Las empresas deciden qué tipos de conectores utilizarán según sus equipos.",
    ],
    "d"
),
(
    "¿Por qué se requieren dos fibras para realizar una operación full duplex en sistemas de fibra óptica?",
    [
        "a) Para duplicar la velocidad de transmisión.",
        "b) Porque la luz solo puede viajar en una dirección a través de la fibra óptica.",
        "c) Para simplificar la instalación y reducir costos.",
        "d) Porque la luz no puede viajar a través de la fibra óptica.",
    ],
    "b"
),
(
    "¿Cómo se configuran los cables de conexión de fibra óptica en términos de número de fibras y conectores?",
    [
        "a) Forman un haz de una sola fibra con conectores múltiples.",
        "b) Son cables individuales sin conectores.",
        "c) Forman un haz de dos cables de fibra óptica con un par de conectores de fibra monomodo estándar.",
        "d) Utilizan conectores de fibra multimodo exclusivamente.",
    ],
    "c"
),
(
    "¿Cómo se denomina un conector que permite la transmisión y recepción en un único conector en el contexto de fibra óptica?",
    [
        "a) Conector único",
        "b) Conector múltiple",
        "c) Conector dúplex",
        "d) Conector monomodo",
    ],
    "c"
),
(
    "Hablamos de conectores de fibra óptica. ¿Cómo se caracterizan los conectores de punta directa (ST) en términos de su mecanismo de bloqueo?",
    [
        "a) Utilizan un mecanismo de bloqueo tipo tornillo.",
        "b) No tienen un mecanismo de bloqueo.",
        "c) Se bloquean mediante un mecanismo tipo bayoneta de giro.",
        "d) Utilizan un mecanismo de bloqueo magnético.",
    ],
    "c"
),
(
    "¿Cuál es una característica histórica de los conectores de punta directa (ST)?",
    [
        "a) Son de diseño moderno.",
        "b) No tienen un mecanismo de bloqueo.",
        "c) Utilizan un mecanismo tipo escopeta de feria.",
        "d) Fueron uno de los primeros tipos de conectores utilizados.",
    ],
    "d"
),
(
    "¿Cómo se conoce comúnmente al conector suscriptor (CS) y qué tipo de mecanismo utiliza para asegurar la inserción correcta?",
    [
        "a) Conector redondo con mecanismo de clic.",
        "b) Conector cuadrado con mecanismo de bayoneta.",
        "c) Conector estándar con mecanismo magnético.",
        "d) Conector LAN y WAN con mecanismo de inserción/extracción.",
    ],
    "d"
),
(
    "¿Cómo se conoce ocasionalmente al conector suscriptor (CS)?",
    [
        "a) Conector redondo",
        "b) Conector cuadrado",
        "c) Conector estándar",
        "d) Conector magnético",
    ],
    "b"
),
(
    "¿Para qué tipo de redes se utiliza comúnmente el conector suscriptor (CS), y qué mecanismo emplea para asegurar la inserción correcta?",
    [
        "a) Para redes locales (LAN) y utiliza un mecanismo de clic.",
        "b) Para redes anchas (WAN) y utiliza un mecanismo magnético.",
        "c) Para redes LAN y WAN, utiliza un mecanismo de inserción/extracción.",
        "d) Para redes privadas y utiliza un mecanismo tipo bayoneta.",
    ],
    "c"
),
(
    "¿Qué tipo de fibra óptica es compatible con el conector suscriptor (CS)?",
    [
        "a) Solo fibra óptica multimodo.",
        "b) Solo fibra óptica monomodo.",
        "c) Ambos, fibra óptica multimodo y monomodo.",
        "d) No es compatible con ninguna fibra óptica.",
    ],
    "c"
),
(
    "¿Cómo se describe el conector Lucent (LC) simplex (WSA) en comparación con el conector SC?",
    [
        "a) Es una versión más grande del conector SC.",
        "b) Es una versión del conector SC diseñada exclusivamente para uso local.",
        "c) Es una versión pequeña del conector SC.",
        "d) No tiene relación con el conector SC.",
    ],
    "c"
),
(
    "¿Cómo se refiere a veces al conector Lucent (LC) simplex (WSA) en términos de tamaño?",
    [
        "c) Conector grande",
        "b) Conector de uso exclusivamente local",
        "a) Conector pequeño",
        "d) Conector remoto",
    ],
    "a"
),
(
    "¿Qué característica contribuye al creciente aumento de popularidad del conector Lucent (LC) simplex (WSA)?",
    [
        "a) Su velocidad de transmisión",
        "b) Su resistencia al desgaste",
        "c) Su tamaño reducido",
        "d) Su compatibilidad con la fibra óptica monomodo",
    ],
    "c"
),
(
    "¿Cómo se caracteriza un conector LC multimodo dúplex en comparación con un conector LC simplex?",
    [
        "a) Tiene un tamaño más grande.",
        "b) Utiliza un conector magnético.",
        "c) Es idéntico en tamaño y diseño.",
        "d) Utiliza un conector dúplex.",
    ],
    "d"
),
(
    "¿Cuál es la función principal de los cables de conexión de fibra óptica en un entorno de infraestructura?",
    [
        "a) Proporcionar energía a los dispositivos conectados.",
        "b) Interconectar dispositivos de infraestructura.",
        "c) Transmitir datos de forma inalámbrica.",
        "d) Garantizar la seguridad de la red.",
    ],
    "b"
),
(
    "¿Cuál es la función principal de los cables de conexión de fibra óptica en un entorno de infraestructura?",
    [
        "a) Proporcionar energía a los dispositivos conectados.",
        "b) Interconectar dispositivos de infraestructura.",
        "c) Transmitir datos de forma inalámbrica.",
        "d) Garantizar la seguridad de la red.",
    ],
    "b"
),
(
    "En el contexto de los cables de conexión de fibra óptica, ¿cómo se utiliza el código de colores para distinguir entre cables monomodo y multimodo?",
    [
        "a) No se utiliza ningún código de colores.",
        "b) Se utiliza el color para indicar la velocidad de transmisión.",
        "c) Los cables monomodo y multimodo no se distinguen por colores.",
        "d) El código de colores se utiliza para distinguir entre cables monomodo y multimodo.",
    ],
    "d"
),
(
    "En el contexto de los cables de conexión de fibra óptica, ¿cuál es la asociación de colores para distinguir entre cables monomodo y multimodo?",
    [
        "a) Amarillo para monomodo y naranja para multimodo.",
        "b) Amarillo para multimodo y naranja para monomodo.",
        "c) No hay una distinción de colores para cables monomodo y multimodo.",
        "d) Amarillo para ambos tipos de cables.",
    ],
    "a"
),
(
    "¿Cuál es una práctica recomendada para proteger los cables de fibra óptica cuando no se están utilizando?",
    [
        "a) Almacenarlos en una bolsa de papel.",
        "b) Mantenerlos al aire libre para una mejor ventilación.",
        "c) Envolverlos en tela para mayor protección.",
        "d) Protegerlos con un pequeño capuchón de plástico.",
    ],
    "d"
),
(
    "En el contexto de la prueba de cables de fibra óptica, ¿cuál es uno de los métodos rápidos y sencillos para detectar problemas en la fibra?",
    [
        "a) Utilizar un Reflectómetro óptico de dominio de tiempo (OTDR).",
        "b) Realizar una prueba de campo iluminando un extremo con una linterna potente.",
        "c) Separar los extremos del cable y observar visualmente.",
        "d) Medir la temperatura del cable con un termómetro infrarrojo.",
    ],
    "b"
),
(
    "¿Por qué la terminación y el empalme del cableado de fibra óptica requieren equipo y capacitación especiales?",
    [
        "a) Porque la fibra óptica es un material muy costoso.",
        "b) Porque la fibra óptica no necesita equipo especial para su terminación.",
        "c) Debido a que la fibra óptica es un material fácil de manipular.",
        "d) Porque la terminación incorrecta puede provocar disminución en las distancias de señalización o falla total en la transmisión.",
    ],
    "d"
),
(
    "¿Cuál es el impacto de una terminación incorrecta en los medios de fibra óptica?",
    [
        "a) Aumenta las distancias de señalización.",
        "b) No afecta la transmisión de la señal.",
        "c) Produce una disminución en las distancias de señalización.",
        "d) Mejora la calidad de la transmisión.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cuáles son tres tipos comunes de errores de empalme y terminación de fibra óptica?",
    [
        "a) Desgaste, oxidación y torsión.",
        "b) Desalineación, separación de los extremos y acabado final.",
        "c) Superposición, interferencia y resonancia.",
        "d) Calentamiento, congelamiento y exposición a la luz solar.",
    ],
    "b"
),
(
    "Según la información proporcionada, ¿cómo se define la desalineación en el contexto de la fibra óptica?",
    [
        "a) Un exceso de alineación en los medios de fibra óptica.",
        "b) Una alineación perfecta en los medios de fibra óptica.",
        "c) Una falta de alineación precisa al unir los medios de fibra óptica.",
        "d) Un proceso de alineación automática de los medios de fibra óptica.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cómo se describe la separación de los extremos en el contexto de la fibra óptica?",
    [
        "a) Una conexión perfecta entre los medios de fibra óptica.",
        "b) Una falta de contacto completo de los medios en el empalme.",
        "c) Un exceso de contacto en el empalme de los medios de fibra óptica.",
        "d) Un proceso automático de unión de los extremos de la fibra óptica.",
    ],
    "b"
),
(
    "Según la información proporcionada, ¿cómo se define el acabado final en el contexto de la fibra óptica?",
    [
        "a) Los extremos de los medios están perfectamente pulidos sin ninguna suciedad.",
        "b) Los extremos de los medios no están pulidos y presentan suciedad en la terminación.",
        "c) El proceso de pulido automático de los extremos de los medios.",
        "d) La terminación de los extremos no afecta la calidad de la fibra óptica.",
    ],
    "b"
),
(
    "Según la información proporcionada, ¿cuál es un método rápido y sencillo para realizar una prueba de campo en una fibra óptica?",
    [
        "a) Utilizar un Reflectómetro óptico de dominio de tiempo (OTDR).",
        "b) Medir la temperatura de la fibra con un termómetro infrarrojo.",
        "c) Iluminar un extremo con una linterna potente mientras se observa el otro extremo.",
        "d) Sumergir la fibra en agua para verificar su resistencia al líquido.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cuál es el dispositivo recomendado para probar cada segmento del cable de fibra óptica?",
    [
        "a) Linterna potente.",
        "b) Termómetro infrarrojo.",
        "c) Reflectómetro óptico de dominio de tiempo (OTDR).",
        "d) Medidor de señal de radiofrecuencia.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cómo funciona un Reflectómetro óptico de dominio de tiempo (OTDR) al probar un cable de fibra óptica?",
    [
        "a) Genera impulsos eléctricos para medir la conductividad del cable.",
        "b) Introduce un impulso de luz de prueba en el cable y mide la retrodispersión y el reflejo de la luz detectados en función del tiempo.",
        "c) Utiliza ondas de sonido para evaluar la integridad del cable.",
        "d) Emite señales de radio para analizar la transmisión del cable.",
    ],
    "b"
),
(
    "Según la información proporcionada, ¿cuál es una función del Reflectómetro óptico de dominio de tiempo (OTDR) al detectar fallas en un cable de fibra óptica?",
    [
        "a) Emitir un sonido de alerta al encontrar una falla.",
        "b) Calcular la velocidad de transmisión del cable.",
        "c) Medir la temperatura del cable durante la falla.",
        "d) Calcular la distancia aproximada en la que se detectan las fallas en toda la longitud del cable.",
    ],
    "d"
),
(
    "Según la información proporcionada, ¿cuál es una ventaja clave de la fibra óptica sobre el cobre?",
    [
        "a) Mayor conductividad eléctrica.",
        "b) Inmunidad a la interferencia electromagnética.",
        "c) Baja pérdida de señal en longitudes cortas.",
        "d) Mayor capacidad de conducción de corriente eléctrica no deseada.",
    ],
    "b"
),
(
    "Según la información proporcionada, ¿por qué la fibra óptica es inmune a la interferencia electromagnética?",
    [
        "a) Debido a que las fibras de vidrio son conductores eléctricos.",
        "b) Debido a que las fibras de vidrio no son conductores eléctricos.",
        "c) Debido a que la fibra óptica utiliza cables más gruesos.",
        "d) Debido a que la fibra óptica conduce corriente eléctrica no deseada.",
    ],
    "b"
),
(
    "Según la información proporcionada, ¿cuáles son características clave de las fibras ópticas en comparación con los medios de cobre?",
    [
        "a) Las fibras ópticas son más gruesas y tienen una alta pérdida de señal.",
        "b) Las fibras ópticas son más delgadas y tienen una pérdida de señal relativamente baja.",
        "c) Las fibras ópticas son menos flexibles y solo se pueden utilizar en distancias cortas.",
        "d) Las fibras ópticas tienen una pérdida de señal más alta y son menos eficientes en distancias largas.",
    ],
    "b"
),
(
    "Según la información proporcionada, ¿qué afirmación es cierta con respecto a las especificaciones de la capa física de la fibra óptica?",
    [
        "a) Las especificaciones de la capa física de la fibra óptica solo admiten longitudes de unos pocos metros.",
        "b) Las especificaciones de la capa física de la fibra óptica no están relacionadas con la longitud del cable.",
        "c) Las especificaciones de la capa física de la fibra óptica pueden admitir longitudes que alcanzan varios kilómetros.",
        "d) Las especificaciones de la capa física de la fibra óptica limitan su uso a distancias cortas.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cuál es un uso común de la fibra óptica en entornos empresariales?",
    [
        "a) Uso exclusivo en conexiones de corta distancia.",
        "b) Uso en conexiones de baja velocidad.",
        "c) Principalmente utilizado como cableado troncal para conexiones punto a punto con mucho tráfico entre servicios de distribución de datos.",
        "d) Limitado a la conexión de edificios en pequeños entornos empresariales.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cuál es una razón clave por la cual la fibra óptica es considerada ideal para su uso en entornos empresariales?",
    [
        "a) Conduce electricidad eficientemente.",
        "b) Presenta una pérdida de señal alta.",
        "c) No es adecuada para conexiones punto a punto.",
        "d) No conduce electricidad y tiene una pérdida de señal baja.",
    ],
    "d"
),
(
    "Según la información proporcionada, ¿cómo se transportan las señales electromagnéticas en los medios inalámbricos?",
    [
        "a) Mediante cables de fibra óptica.",
        "b) A través de señales eléctricas.",
        "c) Utilizando frecuencias de radio y de microondas.",
        "d) Con cables de cobre.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cómo se representan los dígitos binarios en las comunicaciones de datos mediante medios inalámbricos?",
    [
        "a) A través de cables coaxiales.",
        "b) Mediante señales eléctricas directas.",
        "c) Utilizando señales de infrarrojos.",
        "d) Mediante frecuencias de radio y de microondas.",
    ],
    "d"
),
(
    "Según la información proporcionada, ¿cuál es una característica destacada de los medios inalámbricos en términos de movilidad?",
    [
        "a) Los medios inalámbricos tienen una movilidad limitada.",
        "b) La movilidad de los medios inalámbricos es comparable a la de los medios con cables.",
        "c) Los medios inalámbricos proporcionan las mejores opciones de movilidad de todos los medios.",
        "d) La movilidad de los medios inalámbricos es más lenta que la de los medios con cables.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cuál es una tendencia destacada relacionada con la cantidad de dispositivos habilitados para tecnología inalámbrica?",
    [
        "a) La cantidad de dispositivos inalámbricos está disminuyendo.",
        "b) La cantidad de dispositivos inalámbricos permanece constante.",
        "c) La cantidad de dispositivos inalámbricos sigue en aumento.",
        "d) Los dispositivos inalámbricos ya no se utilizan.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿qué relación existe entre el aumento de opciones de ancho de banda de red y la popularidad de la tecnología inalámbrica en redes empresariales?",
    [
        "a) El aumento del ancho de banda no afecta la popularidad de la tecnología inalámbrica.",
        "b) A medida que aumentan las opciones de ancho de banda, la tecnología inalámbrica pierde popularidad.",
        "c) La tecnología inalámbrica es independiente del ancho de banda de red.",
        "d) A medida que aumentan las opciones de ancho de banda de red, la tecnología inalámbrica adquiere popularidad rápidamente en redes empresariales.",
    ],
    "d"
),
(
    "Según la información proporcionada, ¿cuáles son algunas de las áreas de importancia para la tecnología inalámbrica?",
    [
        "a) La tecnología inalámbrica no se ve afectada por interferencias.",
        "b) La seguridad no es un problema en las redes inalámbricas.",
        "c) La tecnología inalámbrica no tiene limitaciones en la cobertura efectiva.",
        "d) La tecnología inalámbrica puede ser afectada por interferencias, tiene limitaciones en la cobertura efectiva y presenta desafíos en seguridad y medio compartido.",
    ],
    "d"
),
(
    "Según la información proporcionada, ¿cuál es una consideración importante en el área de cobertura de las tecnologías inalámbricas?",
    [
        "a) Las tecnologías inalámbricas tienen una cobertura ilimitada en cualquier entorno.",
        "b) La cobertura efectiva de las tecnologías inalámbricas puede ser limitada por materiales de construcción, estructuras y terreno local.",
        "c) La cobertura de las tecnologías inalámbricas siempre es constante sin importar el entorno.",
        "d) Los materiales de construcción y la estructura no afectan la cobertura de las tecnologías inalámbricas.",
    ],
    "b"
),
(
    "Según la información proporcionada, ¿cuál es un desafío importante relacionado con la interferencia en la tecnología inalámbrica?",
    [
        "a) La tecnología inalámbrica no es vulnerable a interferencias.",
        "b) Dispositivos como teléfonos inalámbricos, luces fluorescentes y hornos microondas no afectan la tecnología inalámbrica.",
        "c) La interferencia no es un problema común en las redes inalámbricas.",
        "d) La tecnología inalámbrica es vulnerable a interferencias de dispositivos comunes, lo que puede afectar su rendimiento.",
    ],
    "d"
),
(
    "Según la información proporcionada, ¿cuál es un desafío significativo en términos de seguridad para la comunicación inalámbrica?",
    [
        "a) La comunicación inalámbrica siempre es segura y no requiere medidas adicionales.",
        "b) La seguridad en la comunicación inalámbrica se garantiza a través de hilos físicos.",
        "c) La falta de hilos físicos en la cobertura de la comunicación inalámbrica facilita el acceso no autorizado a la red.",
        "d) Solo los dispositivos autorizados pueden acceder a la comunicación inalámbrica, independientemente de la presencia de hilos físicos.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿por qué la seguridad de la red es un componente principal en la administración de redes inalámbricas?",
    [
        "a) La seguridad no es importante en las redes inalámbricas.",
        "b) La administración de redes inalámbricas no involucra cuestiones de seguridad.",
        "c) La seguridad de la red es crítica debido a la falta de hilos físicos en la comunicación inalámbrica.",
        "d) La seguridad de la red no está relacionada con la administración de redes inalámbricas.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cuál es una característica importante del medio compartido en WLAN (redes locales inalámbricas)?",
    [
        "a) En WLAN, ambos dispositivos pueden enviar o recibir a la vez debido a su operación en duplex.",
        "b) En WLAN, solo un dispositivo puede enviar o recibir debido a su operación en simplex.",
        "c) Ninguna de las anteriores.",
        "d) En WLAN, solo un dispositivo puede enviar o recibir a la vez debido a su operación en half-duplex.",
    ],
    "d"
),
(
    "Según la información proporcionada, ¿cuál es una consecuencia del medio compartido en WLAN cuando más usuarios necesitan acceso simultáneo?",
    [
        "a) Todos los usuarios obtienen el mismo ancho de banda sin importar la cantidad de usuarios simultáneos.",
        "b) Cuantos más usuarios necesitan acceso simultáneo, cada uno obtendrá más ancho de banda.",
        "c) El medio compartido en WLAN no afecta el ancho de banda, independientemente del número de usuarios simultáneos.",
        "d) Cuantos más usuarios necesitan acceso simultáneo, cada uno obtendrá menos ancho de banda debido a la compartición del medio inalámbrico.",
    ],
    "d"
),
(
    "Según la información proporcionada, ¿cuál es la tendencia general en las implementaciones de redes en cuanto a la elección de medios de capa física?",
    [
        "a) La tecnología inalámbrica es la única opción popular para la conectividad de escritorio.",
        "b) El cobre y la fibra óptica son los medios de capa física menos populares para las implementaciones de redes.",
        "c) Aunque la tecnología inalámbrica es popular, el cobre y la fibra óptica siguen siendo los medios más populares para las implementaciones de redes.",
        "d) La tecnología inalámbrica ha reemplazado completamente al cobre y la fibra óptica en las implementaciones de redes.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿qué aspectos cubren los estándares de IEEE y del sector de las telecomunicaciones en las comunicaciones inalámbricas de datos?",
    [
        "a) Solo la capa física de las comunicaciones inalámbricas de datos.",
        "b) Solo la capa de enlace de datos de las comunicaciones inalámbricas de datos.",
        "c) Ambas la capa física y la capa de enlace de datos en las comunicaciones inalámbricas de datos.",
        "d) Ninguna de las anteriores.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿qué aspectos abarcan las especificaciones de la capa física en los estándares de comunicaciones inalámbricas?",
    [
        "a) Solo codificación de señales de datos a señales de radio.",
        "b) Solo frecuencia e intensidad de la transmisión.",
        "c) Codificación de señales de datos a señales de radio, frecuencia e intensidad de la transmisión, requisitos de recepción y decodificación de señales, y diseño y construcción de antenas.",
        "d) Ninguna de las anteriores.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿qué afirmación es correcta sobre Wi-Fi?",
    [
        "a) Wi-Fi es un estándar de comunicación inalámbrica desarrollado por IEEE.",
        "b) Wi-Fi es una marca comercial de Bluetooth.",
        "c) Wi-Fi es una marca comercial de Wi-Fi Alliance.",
        "d) Wi-Fi no está asociado con ninguna organización o entidad.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿con qué tipo de dispositivos se utiliza la tecnología Wi-Fi?",
    [
        "a) Solo con dispositivos Bluetooth.",
        "b) Con cualquier dispositivo inalámbrico, independientemente del estándar.",
        "c) Solo con dispositivos WLAN basados en los estándares IEEE 802.11.",
        "d) No se utiliza con ningún tipo de dispositivo.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cuáles son los dispositivos necesarios para una LAN inalámbrica?",
    [
        "a) Solo routers inalámbricos.",
        "b) Solo adaptadores NIC inalámbricos.",
        "c) Solo puntos de acceso inalámbrico (AP).",
        "d) Puntos de acceso inalámbrico (AP) y adaptadores NIC inalámbricos.",
    ],
    "d"
),
(
    "Según la información proporcionada, ¿para qué se utiliza comúnmente la tecnología inalámbrica de datos?",
    [
        "a) Exclusivamente para conexiones punto a punto.",
        "b) Únicamente en entornos cerrados.",
        "c) Para permitir a los dispositivos conectarse en forma inalámbrica a través de una LAN.",
        "d) Solo en redes de área extensa (WAN).",
    ],
    "c"
),
(
    "¿Qué dispositivos necesita una LAN inalámbrica?",
    [
        "a) Un punto de acceso inalámbrico y adaptadores NIC inalámbricos.",
        "b) Un punto de acceso inalámbrico y adaptadores NIC, los cuales no tienen por qué ser inalámbricos.",
        "c) Punto de acceso, antena de carga y adaptadores NIC.",
        "d) Un adaptador NIC, sin que tenga por qué ser inalámbrico.",
    ],
    "a"
),
(
    "Según la información proporcionada, ¿cuál es la función principal de un Punto de Acceso Inalámbrico (AP) en una LAN inalámbrica?",
    [
        "a) Concentrar las señales inalámbricas de los usuarios.",
        "b) Proporcionar capacidad de comunicación inalámbrica a cada host de la red.",
        "c) Integrar funciones de router, switch y punto de acceso en un solo dispositivo.",
        "d) Conectar la infraestructura de red existente basada en fibra óptica.",
    ],
    "a"
),
(
    "Según la información proporcionada, ¿qué tipo de infraestructura de red conecta un Punto de Acceso Inalámbrico (AP) en una LAN inalámbrica?",
    [
        "a) Fibra óptica.",
        "b) Coaxial.",
        "c) Ethernet basado en cobre.",
        "d) Redes de área amplia (WAN).",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿qué funciones integran los routers inalámbricos domésticos y de pequeñas empresas en un solo dispositivo?",
    [
        "a) Solo funciones de router.",
        "b) Solo funciones de switch.",
        "c) Solo funciones de punto de acceso.",
        "d) Funciones de router, switch y punto de acceso.",
    ],
    "d"
),
(
    "Según la información proporcionada, ¿cuál es la función principal de los Adaptadores NIC Inalámbricos en una LAN inalámbrica?",
    [
        "a) Proporcionar funciones de router.",
        "b) Establecer conexiones con la infraestructura de red basada en fibra óptica.",
        "c) Suministrar energía eléctrica a dispositivos inalámbricos.",
        "d) Proporcionar capacidad de comunicación inalámbrica a cada host de la red.",
    ],
    "d"
),
(
    "Según la evolución de la tecnología, ¿qué consecuencia positiva se menciona en relación con la aparición de estándares WLAN basados en Ethernet?",
    [
        "a) Limitación en la variedad de dispositivos compatibles.",
        "b) Reducción de la movilidad en las conexiones inalámbricas.",
        "c) Mayor diversidad y compatibilidad de dispositivos WLAN.",
        "d) Incremento en la complejidad y dificultad de configuración.",
    ],
    "c"
),
(
    "¿Por qué se destaca la importancia de tener precaución al comprar dispositivos inalámbricos?",
    [
        "a) Para aumentar el costo de adquisición.",
        "b) Garantizar la incompatibilidad entre dispositivos.",
        "c) Asegurar la interoperabilidad y compatibilidad de los dispositivos inalámbricos.",
        "d) Reducir la diversidad de dispositivos en una red.",
    ],
    "c"
),
(
    "¿Cuáles son los beneficios destacados de las tecnologías inalámbricas de comunicación de datos?",
    [
        "a) Mayor costo debido a la necesidad de cableado extenso.",
        "b) Limitación en la movilidad del host.",
        "c) Ahorro en el costoso cableado de las instalaciones y mayor conveniencia en la movilidad del host.",
        "d) Complejidad adicional en la administración de la red.",
    ],
    "c"
),
(
    "¿Qué necesitan desarrollar y aplicar los administradores de red para proteger las LAN inalámbricas del daño y el acceso no autorizado?",
    [
        "a) Procesos y políticas de seguridad relajadas.",
        "b) Mayor apertura en la configuración de la red.",
        "c) Políticas de seguridad solo para LAN con cable.",
        "d) Procesos y políticas de seguridad rigurosas.",
    ],
    "d"
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
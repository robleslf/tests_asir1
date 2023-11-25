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
    ("¿Qué indica la tasa de transferencia en el contexto de las comunicaciones?", [
    "a) La cantidad de datos que se pueden transmitir por unidad de tiempo.",
    "b) La distancia que pueden cubrir las señales de transmisión.",
    "c) La calidad de la conexión física entre dispositivos.",
    "d) La capacidad de almacenamiento de los dispositivos de red."
    ], "a"),
    ("¿Cómo se define la tasa de transferencia máxima en el contexto de las comunicaciones?", [
    "a) Como la cantidad máxima de datos que se pueden transmitir por unidad de tiempo.",
    "b) Como la velocidad mínima requerida para la transmisión de datos.",
    "c) Como la calidad de la conexión física entre dispositivos.",
    "d) Como la capacidad de almacenamiento de los dispositivos de red."
], "a"),
("¿Cuál es la tasa de transferencia máxima del estándar 802.11n, según lo discutido en temas anteriores?", [
    "a) 100 Mbps.",
    "b) 300 Mbps.",
    "c) 600 Mbps.",
    "d) 1000 Mbps."
], "c"),
("¿Qué factores afectan la tasa de transferencia máxima en una comunicación, según se menciona en el fragmento?", [
    "a) La longitud del cable y el número de dispositivos conectados a la red.",
    "b) El tipo de conector y el voltaje de la red eléctrica.",
    "c) El ancho de banda analógico, la potencia del señal, la potencia del ruido en el canal y la codificación del canal.",
    "d) La cantidad de bits por segundo que pueden ser transmitidos por el medio físico."
], "c"),
("¿Cómo se define la tasa de transferencia real en el contexto de las comunicaciones?", [
    "a) La velocidad máxima teórica del canal de transmisión.",
    "b) La velocidad mínima requerida para la transmisión de datos.",
    "c) La velocidad que percibe el usuario durante transmisiones habituales.",
    "d) La capacidad de almacenamiento de los dispositivos de red."
], "c"),
("¿Cuál es la tasa de transferencia máxima del estándar 10BASE2 (802.3a)?", [
    "a) 100 Mbps.",
    "b) 50 Mbps.",
    "c) 10 Mbps.",
    "d) 1 Gbps."
], "c"),
("¿Cuál es la tasa de transferencia máxima del estándar 10BASE5?", [
    "c) 100 Mbps.",
    "b) 50 Mbps.",
    "a) 10 Mbps.",
    "d) 1 Gbps."
], "a"),
("¿Cuál es la tasa de transferencia máxima del estándar 10BASE-T (802.3i)?", [
    "a) 100 Mbps.",
    "c) 50 Mbps.",
    "b) 10 Mbps.",
    "d) 1 Gbps."
], "b"),
("¿Cuál es la tasa de transferencia máxima del estándar 100BASE-TX (802.3u)?", [
    "a) 100 Mbps.",
    "b) 50 Mbps.",
    "c) 10 Mbps.",
    "d) 1 Gbps."
], "a"),
("¿Cuál es la tasa de transferencia máxima del estándar 100BASE-F (802.3u)?", [
    "a) 100 Mbps.",
    "b) 50 Mbps.",
    "c) 10 Mbps.",
    "d) 1 Gbps."
], "a"),
("¿Cuál es la tasa de transferencia máxima del estándar 1000BASE-T (802.3ab)?", [
    "a) 100 Mbps.",
    "b) 500 Mbps.",
    "c) 1 Gbps.",
    "d) 10 Gbps."
], "c"),
("¿Cuál es la tasa de transferencia máxima del estándar 1000BASE-F (802.3z)?", [
    "a) 100 Mbps.",
    "b) 500 Mbps.",
    "c) 1 Gbps.",
    "d) 10 Gbps."
], "c"),
("¿Cuál es la tasa de transferencia máxima del estándar 10GBASE-T (802.3an)?", [
    "a) 1 Gbps.",
    "b) 5 Gbps.",
    "c) 10 Gbps.",
    "d) 100 Gbps."
], "c"),
("¿Cómo se define la ganancia de un sistema en el contexto de señales electromagnéticas?", [
    "a) La velocidad de transmisión de datos.",
    "b) La relación entre la distancia entre el emisor y el receptor.",
    "d) La proporción entre las potencias de salida y entrada, en términos de energía por unidad de tiempo.",
    "c) La capacidad de almacenamiento de los dispositivos de red."
], "d"),
("La ganancia de un sistema puede ser positiva (amplificación) o negativa (atenuación). ¿Cómo se caracteriza una ganancia positiva y una ganancia negativa en este contexto?", [
    "a) Una ganancia positiva implica una pérdida de energía, mientras que una ganancia negativa implica una amplificación de la señal.",
    "b) Una ganancia positiva implica una amplificación de la señal, mientras que una ganancia negativa implica una pérdida de energía.",
    "c) Ambas ganancias, positiva y negativa, implican una pérdida de energía.",
    "d) Ambas ganancias, positiva y negativa, implican una amplificación de la señal."
], "b"),
("¿Cómo se expresa la ganancia?", [
    "a) En Hz.",
    "b) En dB.",
    "c) En A.",
    "d) En W."
], "b"),
("El logaritmo decimal de la relación entre la potencia de salida y entrada, conocido como Bel en honor a Graham Bell, inventor/patentador del teléfono. ¿Cuál es la unidad derivada de Bel que comúnmente se utiliza para medir la ganancia en sistemas de comunicación?", [
    "a) Hertz (Hz).",
    "b) Vatio (W).",
    "c) Decibelio (dB).",
    "d) Newton (N)."
], "c"),
("La décima parte del Bel, comúnmente utilizada para medir ganancias en sistemas de comunicación, se conoce como decibelio (dB). ¿Cómo se define el decibelio en términos de la relación entre la potencia de salida y la potencia de entrada?", [
    "a) dB = 10 · log (Potencia de salida - Potencia de entrada)",
    "b) dB = log10 (Potencia de salida / Potencia de entrada)",
    "c) dB = log2 (Potencia de salida / Potencia de entrada)",
    "d) dB = 10 · log (Potencia de salida / Potencia de entrada)"
], "d"),
("Como es sabido, el logaritmo en base 10 es la inversa de la operación matemática de potenciación. Por ejemplo, ¿cómo se expresa el logaritmo en base 10 de 1000?", [
    "a) log10(1000) = 1",
    "b) log10(1000) = 2",
    "c) log10(1000) = 3",
    "d) log10(1000) = 4"
], "c"),
("¿Cuál es la razón principal para el uso del logaritmo en el contexto de la ganancia de sistemas de comunicación?", [
    "a) Para aumentar la complejidad de los cálculos.",
    "b) Para simplificar las unidades y emplear valores menores.",
    "c) Para complicar la representación de la ganancia.",
    "d) Para cambiar la escala de los valores."
], "b"),
("¿Cuál es la razón principal para el uso del logaritmo en el contexto de la ganancia de sistemas de comunicación?", [
    "a) Para aumentar la complejidad de los cálculos.",
    "b) Para simplificar las unidades y emplear valores menores.",
    "c) Para complicar la representación de la ganancia.",
    "d) Para cambiar la escala de los valores."
], "b"),
("Si un medio no pierde ni gana potencia (Potencia Salida / Potencia Entrada = 1), ¿cómo se reflejaría esto en la expresión logarítmica y en la medida de ganancia en decibelios (dB)?", [
    "a) log(1) = 1, ganancia = 1 dB.",
    "b) log(1) = 0, ganancia = 0 dB.",
    "c) log(1) = 10, ganancia = 10 dB.",
    "d) log(1) = -1, ganancia = -1 dB."
], "b"),
("Si un amplificador amplifica la potencia de entrada en 100 veces, ¿cómo se expresaría la ganancia en decibelios (dB) según la fórmula logarítmica?", [
    "a) 5 dB.",
    "b) 10 dB.",
    "c) 20 dB.",
    "d) 100 dB."
], "c"),
("En el caso de pérdida de potencia, si la potencia de salida es la mitad de la potencia de entrada, ¿cómo se expresaría la ganancia (o pérdida) en decibelios (dB) según la fórmula logarítmica?", [
    "a) -1 dB.",
    "b) -3 dB.",
    "c) -6 dB.",
    "d) -9 dB."
], "b"),
("Supongamos que tenemos un cable que pierde 1 dB por kilómetro. Si el cable tiene 4 kilómetros de longitud, ¿cuánta pérdida de decibelios tendríamos? Luego, si tenemos un amplificador que proporciona una ganancia de 20 dB, ¿cuál sería el resultado final de la ganancia o pérdida en decibelios?", [
    "a) Pérdida de 4 dB, ganancia de 20 dB; resultado final: 16 dB.",
    "b) Pérdida de 4 dB, ganancia de 20 dB; resultado final: 24 dB.",
    "c) Pérdida de 4 dB, ganancia de 20 dB; resultado final: 4 dB.",
    "d) Pérdida de 4 dB, ganancia de 20 dB; resultado final: 20 dB."
], "a"),
("Dentro de los tipos de transmisión, ¿qué clasificación podemos hacer?", [
    "a) Secuencia dos bits, simultaneidad en la emisión-recepción, sincronismo.",
    "b) Frecuencia, amplitud, duración.",
    "c) Voltaje, resistencia, corriente.",
    "d) Longitud de onda, potencia, velocidad."
], "a"),
("Dentro de la secuencia de bits, ¿cuáles son las dos modalidades principales de transmisión?", [
    "a) Serie y paralelo.",
    "b) Sincrónica y asíncrona.",
    "c) Analógica y digital.",
    "d) Unipolar y bipolar."
], "a"),
("En la transmisión en serie, ¿cómo se envían los bits de una palabra?", [
    "a) Consecutivamente, uno tras otro, por una única línea de datos.",
    "b) Simultáneamente, todos al mismo tiempo, por diferentes líneas de datos.",
    "c) En bloques, agrupados por su valor, por diferentes líneas de datos.",
    "d) Aleatoriamente, sin un orden específico, por una única línea de datos."
], "a"),
("En la transmisión en paralelo, ¿cómo se envían los bits de una palabra?", [
    "a) Consecutivamente, uno tras otro, por una única línea de datos.",
    "b) Simultáneamente, todos al mismo tiempo, por diferentes líneas de datos.",
    "c) En bloques, agrupados por su valor, por diferentes líneas de datos.",
    "d) Aleatoriamente, sin un orden específico, por una única línea de datos."
], "b"),
("En cuanto a la simultaneidad en la emisión-recepción, ¿cuáles son las tres modalidades principales de transmisión?", [
    "a) Simplex, semi-duplex (half-duplex), dúplex (full-duplex).",
    "b) Serie, paralelo, dúplex (full-dúplex).",
    "c) Simples, semi-duplex, dúplex, full-dúplex",
    "d) Simplex (semi- dúplex), dúplex (full-dúplex)."
], "a"),
("En la modalidad de transmisión 'Simplex', ¿cómo se lleva a cabo la transmisión de datos?", [
    "a) En ambos sentidos simultáneamente.",
    "b) En un único sentido.",
    "c) En ambos sentidos, pero no simultáneamente.",
    "d) En diferentes líneas de datos."
], "b"),
("En la modalidad de transmisión 'Semi-duplex (half-duplex)', ¿cómo se realiza la transmisión de datos?", [
    "a) En ambos sentidos simultáneamente.",
    "b) En un único sentido.",
    "c) En ambos sentidos, pero no simultáneamente.",
    "d) En diferentes líneas de datos."
], "c"),
("En la modalidad de transmisión 'Dúplex (full-dúplex)', ¿cómo se lleva a cabo la transmisión de datos?", [
    "a) En ambos sentidos simultáneamente.",
    "b) En un único sentido.",
    "c) En ambos sentidos, pero no simultáneamente.",
    "d) En diferentes líneas de datos."
], "a"),
("En el contexto de la transmisión de datos, ¿cómo se define el 'Sincronismo'?", [
    "a) Es el proceso de envío de bits de manera consecutiva.",
    "b) Es el proceso de informar al receptor sobre el inicio y fin de un bloque de bits, así como la duración de cada bit.",
    "c) Es el proceso de transmitir datos en ambos sentidos simultáneamente.",
    "d) Es el proceso de agrupar bits por su valor y enviarlos en bloques."
], "b"),
("En el contexto de la sincronización en la transmisión de datos, ¿cuáles son las tres formas principales de sincronización?", [
    "a) Sincronización de frecuencia, sincronización de amplitud, sincronización de duración.",
    "b) Sincronización de bit, sincronización de palabra, sincronización de bloque.",
    "c) Sincronización de voltaje, sincronización de resistencia, sincronización de corriente.",
    "d) Sincronización de serie, sincronización de paralelo, sincronización de dúplex."
], "b"),
("¿Cómo se define la 'Sincronización de bit' en la transmisión de datos?", [
    "a) Es el reconocimiento de la frecuencia de cada bit.",
    "b) Es el reconocimiento del inicio y fin de cada bit.",
    "c) Es el reconocimiento del voltaje de cada bit.",
    "d) Es el reconocimiento del valor de cada bit."
], "b"),
("¿Cómo se define la 'Sincronización de palabra' en la transmisión de datos?", [
    "a) Es el reconocimiento de la frecuencia de cada palabra.",
    "b) Es el reconocimiento del inicio y fin de cada palabra.",
    "c) Es el reconocimiento del voltaje de cada palabra.",
    "d) Es el reconocimiento del valor de cada palabra."
], "b"),
("¿Cómo se define la 'Sincronización de bloque' en la transmisión de datos?", [
    "a) Es el reconocimiento de la frecuencia de cada bloque.",
    "b) Es el reconocimiento del inicio y fin de cada bloque.",
    "c) Es el reconocimiento del voltaje de cada bloque.",
    "d) Es el reconocimiento del valor de cada bloque."
], "b"),
("En función de cómo se establece el sincronismo, ¿cuáles son los dos tipos de transmisión que podemos distinguir?", [
    "a) Transmisión digital y transmisión analógica.",
    "b) Transmisión serie y transmisión paralelo.",
    "c) Transmisión asíncrona y transmisión síncrona.",
    "d) Transmisión unipolar y transmisión bipolar."
], "c"),
("¿Cuál fue el primer tipo de transmisión en utilizarse, y cuál es un ejemplo de su aplicación?", [
    "a) Transmisión digital, Ethernet.",
    "b) Transmisión paralelo, USB.",
    "c) Transmisión asíncrona, HDMI.",
    "d) Transmisión síncrona, RS-232."
], "c"),
("En la transmisión asíncrona, ¿cómo se produce el proceso de sincronización?", [
    "a) Para cada letra (bit) que se transmite.",
    "b) Para cada palabra (byte) que se transmite.",
    "c) Simultáneamente para todos los bits de una palabra.",
    "d) No hay sincronización en la transmisión asíncrona."
], "b"),
("En el contexto de la transmisión asíncrona, ¿qué se envía junto con los bits de la palabra para indicar el inicio y el final de la palabra?", [
    "a) Bits de paridad.",
    "b) Bits de inicio y de parada.",
    "c) Bits de control.",
    "d) Bits de sincronización."
], "b"),
("En la transmisión asíncrona, ¿qué requisitos deben cumplir el emisor y el receptor?", [
    "a) Deben trabajar a diferentes frecuencias.",
    "b) Deben tener relojes desincronizados.",
    "c) Deben trabajar a la misma frecuencia y tener los relojes sincronizados.",
    "d) No es necesario que trabajen a la misma frecuencia ni que tengan los relojes sincronizados."
], "c"),
("Si enviamos palabras de 5 bits de información junto con 1 bit de inicio y 1 bit de fin, ¿cuál sería la eficiencia del código, considerando que se transmiten 7 bits en total?", [
    "a) 50%",
    "b) 60%",
    "c) 71%",
    "d) 80%"
], "c"),
("En la transmisión síncrona, ¿cómo se envía el sincronismo con respecto a los datos?", [
    "a) Paralelamente con cada byte.",
    "b) Secuencialmente antes de cada byte.",
    "c) Paralelamente con los datos, pero NO en cada byte.",
    "d) No se envía sincronismo en la transmisión síncrona."
], "c"),
("En la transmisión síncrona, ¿cómo se indica la duración de cada uno de los bits?", [
    "a) No se indica la duración de los bits.",
    "b) Se envía una señl periódica de sincronización junto con los datos.",
    "c) Se envía un bit especial al inicio de cada palabra para indicar la duración.",
    "d) Se utiliza un código especial al final de cada byte para señalar la duración."
], "b"),
("En comparación con las transmisiones asíncronas, ¿cómo afecta el hecho de que la transmisión síncrona no emplea señales de inicio y fin en cada palabra/byte a la velocidad de transmisión?", [
    "a) Las transmisiones síncronas son más lentas.",
    "b) Las transmisiones síncronas son más rápidas.",
    "c) No hay diferencia en la velocidad entre transmisiones síncronas y asíncronas.",
    "d) Depende de la longitud de las palabras/bytes transmitidos."
], "b"),
("En la transmisión síncrona, ¿cómo se envía la señal de sincronización en relación con la señal de datos?", [
    "a) En cables diferentes.",
    "b) Por el mismo cable.",
    "c) En la misma señal.",
    "d) Depende de la distancia entre el emisor y el receptor."
], "c"),
("En la trama IEEE 802.3 de Ethernet, ¿cuál es la función de los primeros 7 bytes (56 bits) de sincronización?", [
    "a) Indican el inicio de la trama.",
    "b) Contienen información de control de flujo.",
    "c) Establecen la velocidad de transmisión.",
    "d) Todos los bits alternos 0, 1, 0, 1, ... para sincronización."
], "d"),
("¿Cómo se definen las perturbaciones en el contexto de la transmisión de datos?", [
    "a) Son acciones que mejoran la calidad del sistema de transmisión.",
    "b) Son acciones externas que no afectan al sistema de transmisión.",
    "c) Son acciones tanto externas como internas que provocan que la señal recibida no sea exactamente igual al emitido por el emisor.",
    "d) Son acciones que solo afectan al sistema de transmisión en modo síncrono."
], "c"),
("En relación con las perturbaciones y la transmisión de datos, ¿cómo afecta una perturbación que no modifica sustancialmente la señal enviada?", [
    "a) Provoca errores de transmisión.",
    "b) Garantiza una transmisión libre de errores.",
    "c) No tiene ningún efecto en la transmisión.",
    "d) Aumenta la velocidad de transmisión."
], "b"),
("¿Cuáles son algunas de las perturbaciones posibles en la transmisión de datos y cómo se define el indicador de esta perturbación?", [
    "a) Distorsión, intermodulación, ecos, diafonías, ruido, atenuación y modularización.",
    "b) Distorsión, intermodulación, ecos, atenuación y modularización.",
    "c) Distorsión, diafonías, ruido, atenuación y modularización.",
    "d) Distorsión, intermodulación, ecos, diafonías, ruido y atenuación."
], "d"),
("¿Cómo se caracteriza la distorsión en la transmisión de datos?", [
    "a) Por variaciones solo en amplitud.",
    "b) Por variaciones solo en frecuencia.",
    "c) Por variaciones tanto en amplitud como en frecuencia, generalmente causadas por el efecto del ruido.",
    "d) Por variaciones en la velocidad de transmisión."
], "c"),
("¿Cómo se define la intermodulación en la transmisión de datos?", [
    "c) Es la variación de amplitud de la seña emitido.",
    "b) Es la variación de frecuencia de la seña emitido.",
    "a) Es la llegada de otras señales a distintas frecuencias junto con la señal emitido.",
    "d) Es la variación de velocidad de transmisión de la señal."
], "a"),
("En relación con los ecos en la transmisión de datos, ¿a partir de cuándo es apreciable en el receptor?", [
    "a) A partir de los 10 ms.",
    "b) A partir de los 100 ms.",
    "c) A partir de 1 s.",
    "d) A partir de 1 ms."
], "a"),
("¿Cómo se caracteriza la diafonía en la transmisión de datos?", [
    "a) Se produce entre cables de diferentes materiales.",
    "b) Se produce en líneas de transmisión ópticas.",
    "c) Se produce en líneas metálicas homogéneas, donde acoplamientos entre dos o varios cables en el mismo conducto afectan al otro cable sumándose a la otra señal.",
    "d) Se produce solo en transmisiones inalámbricas."
], "c"),
("En términos de transmisión de datos, ¿cómo se define el ruido?", [
    "a) Es la variación de amplitud de la señal recibido.",
    "b) Es la variación de frecuencia de la señal recibido.",
    "c) Es la interferencia que recibe el medio de transmisión de distintos elementos externos, añadiendo una señal conocida y no deseada.",
    "d) Es la atenuación de la señal transmitido."
], "c"),
("¿Cómo afectará el ruido al sistema de transmisión según la potencia de la señal?", [
    "a) Ambas son correctas.",
    "b) Dependiendo de la potencia de la señal, el ruido afectará más o menos.",
    "c) Ambas son incorrectas.",
    "d) El ruido no tiene relación con la potencia de la señal."
], "b"),
("En el contexto de la transmisión de datos, ¿cómo se define el indicador de la perturbación por ruído?", [
    "a) Se mide en decibelios.",
    "b) Se representa como la variación de frecuencia entre señal y ruido.",
    "c) Se expresa como la relación de potencia entre señal y ruido, definido como PotenciaSeñal / PotenciaRuido.",
    "d) Se calcula como la variación de amplitud entre señal y ruido."
], "c"),
("En relación con la atenuación en la transmisión de datos, ¿cómo se manifiesta este fenómeno?", [
    "a) La atenuación no afecta a la potencia del sinal.",
    "b) La atenuación provoca un aumento de la potencia del sinal a medida que aumenta la distancia de transmisión.",
    "c) La atenuación implica una pérdida de potencia (amplitud) a medida que aumenta la distancia de transmisión, con un efecto proporcional a la longitud del medio de transmisión.",
    "d) La atenuación solo ocurre en transmisiones inalámbricas."
], "c"),
("¿Qué sucede a partir de cierta distancia en la atenuación de la transmisión de datos y cómo se puede abordar este problema?", [
    "a) La atenuación no tiene impacto en la transmisión a larga distancia.",
    "b) La atenuación aumenta la potencia del sinal a medida que la distancia crece.",
    "c) A partir de cierta distancia, el sinal se vuelve tan fuerte que no se necesita repetidores ni amplificadores intermedios.",
    "d) A partir de cierta distancia, el sinal se debilita y no se puede interpretar la información, requiriendo el uso de repetidores y amplificadores intermedios."
], "d"),
("En relación con la atenuación en la transmisión de datos, ¿cómo se relaciona este fenómeno con la longitud del medio de transmisión?", [
    "c) La atenuación es inversamente proporcional a la longitud del medio de transmisión.",
    "b) La atenuación no está relacionada con la longitud del medio de transmisión.",
    "a) La atenuación tiene un efecto proporcional a la longitud del medio de transmisión.",
    "d) La atenuación aumenta a medida que disminuye la longitud del medio de transmisión."
], "a"),
("En el contexto de la atenuación en la transmisión de datos, ¿por qué a partir de cierta distancia la señal se vuelve tan débil que no se puede interpretar la información?", [
    "a) La atenuación no afecta la interpretación de la información a larga distancia.",
    "b) A mayor distancia, la atenuación disminuye, fortaleciendo la señal.",
    "c) La atenuación causa interferencias en la señal a medida que la distancia aumenta.",
    "d) A medida que la distancia aumenta, la atenuación debilita la señal, requiriendo repetidores y amplificadores intermedios para interpretar la información."
], "d"),
("¿Cuál es el objetivo principal de la multiplexación en la transmisión de datos?", [
    "a) Transmitir información de una única fuente o emisor por canal.",
    "b) Transmitir información de distintas fuentes o emisores por un mismo canal.",
    "c) Evitar la transmisión de información de diferentes emisores.",
    "d) Reducir la velocidad de transmisión de datos."
], "b"),
("¿Cuál es la base fundamental para la multiplexación en las comunicaciones?", [
    "a) Utilizar la capacidad del medio al 100% en todas las comunicaciones.",
    "b) Aprovechar al máximo la capacidad del medio de transmisión.",
    "c) Limitar la cantidad de información transmitida por canal.",
    "d) Garantizar que cada comunicación tenga su propio canal dedicado."
], "b"),
("¿Cuáles son los dos tipos principales de multiplexación?", [
    "a) Multiplexación por división de espacio y Multiplexación por división de potencia.",
    "b) Multiplexación por división de tiempo y Multiplexación por división en frecuencias.",
    "c) Multiplexación por división de señal y Multiplexación por división de velocidad.",
    "d) Multiplexación por división de canales y Multiplexación por división de codificación."
], "b"),
("¿En qué situación se utiliza la Multiplexación por División de Tiempo (TDM) según la información proporcionada?", [
    "a) Cuando la velocidad del medio (canal) es igual a la velocidad de los datos a transmitir.",
    "b) Únicamente se utiliza cuando la velocidad del medio es inferior a la velocidad de los datos.",
    "c) Cuando la velocidad del medio (canal) es superior a la velocidad de los datos a ser transmitidos.",
    "d) Se aplica solo en casos de comunicaciones inalámbricas."
], "c"),

("¿Cuándo sería apropiado utilizar la Multiplexación por División de Tiempo (TDM) según la situación planteada?", [
    "a) Cuando la velocidad de los emisores y receptores es igual a la velocidad del canal.",
    "b) Únicamente se utiliza cuando la velocidad de los emisores y receptores es mayor que la velocidad del canal.",
    "c) Cuando la velocidad de los emisores y receptores es menor que la velocidad del canal.",
    "d) Se aplica solo en casos de comunicaciones con igual velocidad en todos los componentes."
], "c"),
("En el contexto de la Multiplexación por División de Tiempo (TDM), ¿cómo se asigna el tiempo del canal a cada fuente de baja velocidad?", [
    "a) Todas las fuentes comparten el tiempo del canal simultáneamente.",
    "c) Cada fuente de baja velocidad recibe su propio canal dedicado.",
    "b) A cada fuente de baja velocidad se le asigna un fragmento de tiempo del canal.",
    "d) El tiempo del canal se asigna solo a las fuentes de alta velocidad."
], "b"),
("¿Cómo funciona la Multiplexación por División en Frecuencias (FDM)?", [
    "a) Cada fuente de datos tiene su propia canal dedicada.",
    "b) La canal se divide en segmentos de tiempo asignados a cada fuente.",
    "c) La canal se divide en bandas de frecuencia y estas se asignan a cada fuente de datos.",
    "d) Todas las fuentes comparten la misma banda de frecuencia simultáneamente."
], "c"),
("¿Cuál es la necesidad en el receptor al utilizar Multiplexación por División en Frecuencias (FDM)?", [
    "a) Utilizar un filtro de tiempo para distinguir las diferentes fuentes de emisión.",
    "b) No se requiere ningún filtro en el receptor.",
    "c) Emplear un filtro de amplitud para separar las señales de las diferentes fuentes.",
    "d) Es necesario emplear un filtro de frecuencias para distinguir las diferentes fuentes de emisión."
], "d"),
("¿Cuál es un ejemplo práctico de la aplicación de la Multiplexación por División en Frecuencias (FDM)?", [
    "a) La utilización de filtros de tiempo en emisoras de radio.",
    "b) La transmisión de señales sin la necesidad de asignar frecuencias específicas a cada emisora.",
    "c) En las emisiones de radio, cada emisora ocupa una posición en el dial o rango de frecuencias diferente.",
    "d) Todas las emisoras de radio comparten la misma frecuencia simultáneamente."
], "c"),
("¿Cuáles son algunos de los equipos necesarios para transmitir datos digitales sobre líneas de comunicación?", [
    "a) Antenas y amplificadores.",
    "b) Teclados y ratones.",
    "c) Módems, tarjetas de red, codificadores, decodificadores, etc.",
    "d) Pantallas y altavoces."
], "c"),
("¿Cuándo es posible enviar una señal sin modificaciones sobre el medio de transmisión?", [
    "a) Solo si la frecuencia de la señal es igual a la frecuencia de la onda del medio de transmisión.",
    "b) Siempre es posible enviar una señal sin modificaciones.",
    "c) Solo si la longitud de onda de la señal es menor que la del medio de transmisión.",
    "d) Si la frecuencia de la señal es mayor que la frecuencia de la onda del medio de transmisión."
], "a"),
("¿Cómo se denomina a la técnica en la que la frecuencia de la señal que se quiere transmitir coincide con la frecuencia de la onda empleada por el medio de transmisión?", [
    "a) Banda ancha.",
    "b) Banda lateral.",
    "c) Banda estrecha.",
    "d) Banda base."
], "d"),
("En el contexto de transmisión de señales, ¿qué técnica se utiliza cuando las frecuencias no coinciden, y es necesario adaptar la señal para que cumpla ciertas condiciones?", [
    "a) Banda base.",
    "b) Banda lateral.",
    "c) Banda ancha.",
    "d) Banda estrecha."
], "c"),
("¿Cómo se define la técnica de transmisión en Banda Base en el contexto de las comunicaciones?", [
    "a) Transmisión de señales sin modificaciones.",
    "b) Transmisión de señales adaptadas a diferentes frecuencias.",
    "c) Técnicas de transmisión en las que las frecuencias del medio coinciden con las frecuencias del sinal a transmitir.",
    "d) Transmisión de señales con cambios en la amplitud."
], "c"),
("¿Cuál es el propósito principal de las diferentes técnicas de codificación en las comunicaciones?", [
    "a) Modificar la frecuencia de la señal para una mejor transmisión.",
    "b) Facilitar la adaptación del sinal al medio de transmisión.",
    "c) Establecer un acuerdo entre emisor y receptor para intercambiar mensajes.",
    "d) Aumentar la potencia de la señal durante la transmisión."
], "c"),
("¿Cuál es el objetivo principal de los métodos de codificación en términos de mejorar la sincronización entre el emisor y el receptor?", [
    "a) Aumentar la velocidad de transmisión.",
    "b) Reducir la potencia de la señal.",
    "c) Mejorar la sincronización y aumentar la fiabilidad de la transmisión.",
    "d) Adaptar la señal al medio de transmisión."
], "c"),
("¿Qué método de codificación utilizaba Ethernet clásica para lograr la sincronización sin depender de un reloj externo?", [
    "a) PSG y PSG diferencial.",
    "b) Manchester y Manchester Diferencial.",
    "c) Bayern y Bayern Diferencial.",
    "d) Liverpool y Liverpool Diferencial."
], "b"),
("En el método de codificación Manchester, ¿cómo se representa el '0' y el '1' en términos de transiciones de voltaje?", [
    "a) '0' tiene una transición de – a + y '1' tiene una transición de + a -.",
    "b) '0' tiene una transición de + a - y '1' tiene una transición de – a +.",
    "c) Ambos '0' y '1' tienen una transición de + a -.",
    "d) Ambos '0' y '1' tienen una transición de – a +."
], "b"),
("En el método Manchester Diferencial de codificación, ¿cómo se distingue entre '0' y '1' en términos de transiciones de voltaje?", [
    "a) '0' tiene una transición + a – tanto al principio como en la mitad del intervalo, y '1' tiene cualquier transición de voltaje pero solo en la mitad del intervalo.",
    "b) '0' tiene una transición + a – en la mitad del intervalo, y '1' tiene una transición + a – tanto al principio como en la mitad del intervalo.",
    "c) '0' tiene cualquier transición de voltaje pero solo en la mitad del intervalo, y '1' tiene una transición + a – tanto al principio como en la mitad del intervalo.",
    "d) '0' tiene cualquier transición de voltaje pero solo en la mitad del intervalo, y '1' tiene cualquier transición de voltaje pero solo en la mitad del intervalo."
], "a"),
("En la transmisión en Banda Ancha, ¿cómo se define esta técnica en relación con las frecuencias de la onda en el medio y las frecuencias de la señal que se desea transmitir?", [
    "a) Las frecuencias de la onda en el medio coinciden con las frecuencias de la señal que se desea transmitir.",
    "b) Las frecuencias de la onda en el medio no coinciden con las frecuencias de la señal que se desea transmitir.",
    "c) Las frecuencias de la onda en el medio son inversamente proporcionales a las frecuencias de la señal que se desea transmitir.",
    "d) Las frecuencias de la onda en el medio son directamente proporcionales a las frecuencias de la señal que se desea transmitir."
], "b"),
("En el contexto de la transmisión, ¿cuáles son los elementos principales involucrados?", [
    "a) Receptor y transmisor.",
    "b) Portadora y moduladora.",
    "c) Frecuencia y amplitud.",
    "d) Analógico y digital."
], "b"),
("En el proceso de transmisión, ¿cómo se define la 'portadora'?", [
    "a) Es el medio físico de transmisión.",
    "b) Es la información que se desea transmitir.",
    "c) Es el canal por el cual se envía la señal.",
    "d) Es la señal del medio que transporta la información."
], "d"),
("En el contexto de la transmisión en banda ancha, ¿cómo se define la 'moduladora' según la información proporcionada?", [
    "a) Es la señal del medio que transporta la información.",
    "b) Es la información que se desea transmitir.",
    "c) Es el canal por el cual se envía la señal.",
    "d) Es la señal que modifica algún parámetro de la portadora y contiene la información."
], "d"),

# Seguir en página 9 copiando el apartado de portadora analóxica.






































































































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
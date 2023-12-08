import random

# Lista de preguntas y respuestas
preguntas = [
(
    "¿Cuál es la función principal de los conectores externos en un sistema informático?",
    [
        "a) Conectar componentes internos de la placa base.",
        "b) Proporcionar energía a la CPU.",
        "c) Facilitar la conexión de periféricos y dispositivos externos.",
        "d) Regular la temperatura interna del equipo.",
    ],
    "c"
),
(
    "¿Cuál es la función principal de los conectores externos en un sistema informático?",
    [
        "a) Conectar componentes internos del equipo.",
        "b) Proporcionar energía al dispositivo.",
        "c) Interconectar distintos dispositivos y periféricos externos.",
        "d) Regular la temperatura interna del sistema.",
    ],
    "c"
),
(
    "¿Cuál es una ventaja importante de que los conectores estén estandarizados en los sistemas informáticos?",
    [
        "a) Aumenta la complejidad de las conexiones.",
        "b) Facilita la interoperabilidad entre dispositivos de diferentes fabricantes.",
        "c) Limita las opciones de conectividad.",
        "d) Reduce la velocidad de transferencia de datos.",
    ],
    "b"
),
(
    "¿Cuál de las siguientes afirmaciones sobre el conector USB es correcta?",
    [
        "a) El USB 2.0 es más rápido que el USB 3.0.",
        "b) La característica Plug and Play no está presente en los dispositivos USB.",
        "c) El USB 3.0 es más lento que su antecesor, el USB 2.0.",
        "d) Todos los USB tienen la característica Plug and Play.",
    ],
    "d"
),
(
    "¿Cuáles son algunas de las características del conector USB según la información proporcionada?",
    [
        "a) Complejidad y falta de resistencia.",
        "b) Resistencia y simplicidad.",
        "c) Complejidad y baja fiabilidad.",
        "d) Fiabilidad y falta de resistencia.",
    ],
    "b"
),
(
    "Según la información proporcionada, ¿quién inventó el conector USB?",
    [
        "a) AMD.",
        "b) Microsoft.",
        "c) Intel.",
        "d) Apple.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿qué significa la característica 'Plug and Play' en los conectores USB?",
    [
        "a) Requiere instalación de controladores antes de conectar dispositivos.",
        "b) Los dispositivos USB deben reiniciarse después de la conexión.",
        "c) Los dispositivos USB se conectan y funcionan automáticamente sin necesidad de instalación adicional.",
        "d) 'Plug and Play' no es una característica de los conectores USB."
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cuántas veces más rápido es el USB 3.0 en comparación con su antecesor, el USB 2.0?",
    [
        "a) Cinco veces más rápido.",
        "b) Diez veces más rápido.",
        "c) Dos veces más rápido.",
        "d) Veinte veces más rápido."
    ],
    "b"
),
(
    "Según la información proporcionada, ¿qué significa la retrocompatibilidad de los dispositivos USB?",
    [
        "a) Los dispositivos USB pueden conectarse a dispositivos más antiguos.",
        "b) Los dispositivos USB solo pueden conectarse a puertos USB 3.0.",
        "c) Los dispositivos USB no son compatibles con versiones anteriores.",
        "d) La velocidad de los dispositivos USB no se ve afectada por la retrocompatibilidad."
    ],
    "a"
),
(
    "¿Cuál es una ventaja de los puertos USB 3.0 sobre los USB 2.0, según la información proporcionada?",
    [
        "a) Los puertos USB 3.0 no requieren retrocompatibilidad.",
        "b) Los puertos USB 3.0 son diez veces más rápidos que los USB 2.0.",
        "c) Los puertos USB 3.0 no son compatibles con dispositivos más antiguos.",
        "d) La velocidad de los puertos USB 2.0 es igual a la de los USB 3.0."
    ],
    "b"
),
(
    "¿Qué sucede al conectar un dispositivo USB 2.0 a un puerto USB 3.0?",
    [
        "a) No es posible realizar esta conexión debido a la incompatibilidad.",
        "b) El dispositivo funcionará sin problemas y aprovechará todas las ventajas del conector USB 3.0.",
        "c) El dispositivo funcionará sin problemas, aunque no aprovechará las ventajas del conector USB 3.0.",
        "d) El dispositivo presentará problemas de funcionamiento y no será reconocido por el sistema.",
    ],
    "c"
),
(
    "¿Cuál es la relación entre los conectores tipo A y B en USB 3.0 con respecto a los conectores A y B en USB 2.0?",
    [
        "a) No hay relación entre los conectores de USB 3.0 y USB 2.0.",
        "b) Los conectores tipo A y B en USB 3.0 son incompatibles con los conectores A y B en USB 2.0.",
        "c) Los conectores tipo A y B en USB 3.0 son parecidos y retrocompatibles con los conectores A y B en USB 2.0.",
        "d) Los conectores tipo A y B en USB 3.0 tienen un diseño completamente diferente a los conectores A y B en USB 2.0.",
    ],
    "c"
),
(
    "¿Cuál es la característica distintiva del conector micro-B en USB 3.0 y en qué dispositivos es comúnmente utilizado?",
    [
        "a) El conector micro-B en USB 3.0 no tiene características distintivas.",
        "b) El conector micro-B en USB 3.0 es exclusivamente utilizado en dispositivos de audio.",
        "d) El conector micro-B en USB 3.0 es muy utilizado en dispositivos como discos duros externos.",
        "c) El conector micro-B en USB 3.0 es incompatible con cualquier tipo de dispositivo externo.",
    ],
    "d"
),
(
    "¿Cuál es la característica principal de la especificación USB 3.1 (SuperSpeed USB 10Gbps)?",
    [
        "a) Ofrece la misma velocidad que USB 3.0.",
        "b) Proporciona un modo a 5 Gbps gracias a una mejor codificación de datos.",
        "c) Ofrece un modo a 10 Gbps gracias a una mejor y más eficiente codificación de datos.",
        "d) No es retrocompatible con las versiones anteriores de USB.",
    ],
    "c"
),
(
    "¿Cuál es el nombre completo de la nueva especificación de USB que ofrece una velocidad de 10 Gbps?",
    [
        "a) USB 3.0",
        "b) SuperSpeed USB 5Gbps",
        "c) USB 3.1",
        "d) SuperSpeed USB 10Gbps",
    ],
    "d"
),
(
    "¿Cómo logra la especificación USB 3.1 ofrecer un modo a 10 Gbps?",
    [
        "c) Aumenta el número de pines en el conector USB.",
        "b) Mejora la eficiencia energética del sistema.",
        "a) Gracias a una mejor y más eficiente codificación de datos.",
        "d) Implementa una conexión inalámbrica de alta velocidad.",
    ],
    "a"
),
(
    "¿Cómo se compara la velocidad de la especificación USB 3.1 con respecto al USB 3.0?",
    [
        "a) Ofrece la misma velocidad que USB 3.0.",
        "b) Tiene el doble de velocidad que USB 3.0.",
        "c) Es más lenta que USB 3.0.",
        "d) No tiene relación con la velocidad de USB 3.0.",
    ],
    "b"
),
(
    "¿Qué beneficio adicional ofrece la especificación USB 3.1 además de mejorar el rendimiento?",
    [
        "a) No tiene beneficios adicionales.",
        "b) Aumenta el consumo de energía.",
        "c) Mejora la eficiencia energética, reduciendo el gasto eléctrico.",
        "d) No afecta el consumo de energía del sistema.",
    ],
    "c"
),
(
    "¿Qué característica distingue al conector Thunderbolt y cuál es su ventaja principal en términos de velocidad de transmisión?",
    [
        "a) Su capacidad exclusiva para transmitir datos.",
        "b) La conexión óptica que utiliza, transmitiendo datos por pulsos de luz en lugar de pulsos eléctricos, lo que aumenta la velocidad.",
        "c) La capacidad de transmitir solo video y audio, pero no datos.",
        "d) Fue inventado por Apple en lugar de Intel.",
    ],
    "b"
),
(
    "¿En qué tipo de ordenadores se encuentra comúnmente el puerto de comunicaciones Thunderbolt?",
    [
        "a) Solo en computadoras Windows.",
        "b) Exclusivamente en computadoras Apple, como MacBooks e iMacs.",
        "c) En todos los dispositivos electrónicos, independientemente de la marca.",
        "d) Principalmente en computadoras de escritorio.",
    ],
    "b"
),
(
    "¿Cuáles son las capacidades de transmisión del conector Thunderbolt?",
    [
        "a) Solo transmite datos.",
        "b) Puede transmitir únicamente vídeo y audio, pero no datos.",
        "c) Tiene la capacidad de transmitir tanto vídeo y audio como datos.",
        "d) No tiene capacidades de transmisión.",
    ],
    "c"
),
(
    "¿Quién fue el inventor del conector Thunderbolt?",
    [
        "a) Fue desarrollado por Apple.",
        "b) Fue inventado por Microsoft.",
        "c) Fue inventado por Intel.",
        "d) Fue una colaboración entre Apple y Microsoft.",
    ],
    "c"
),
(
    "¿Cuál es la principal razón de la velocidad del conector Thunderbolt?",
    [
        "c) Su conexión inalámbrica.",
        "b) La transmisión de pulsos eléctricos.",
        "a) Su conexión óptica, transmitiendo datos por pulsos de luz en lugar de pulsos eléctricos.",
        "d) La colaboración entre Apple e Intel.",
    ],
    "a"
),
(
    "¿Qué tipo de periféricos pueden conectarse generalmente al puerto Thunderbolt debido a su velocidad?",
    [
        "a) Únicamente dispositivos de baja velocidad.",
        "b) Exclusivamente dispositivos inalámbricos.",
        "c) Cualquier periférico, pero generalmente está diseñado para dispositivos rápidos como monitores de alta definición y discos duros externos.",
        "d) Solo dispositivos de Apple.",
    ],
    "c"
),
(
    "¿Cuántos dispositivos se pueden conectar en cadena al puerto Thunderbolt en serie?",
    [
        "a) Hasta tres dispositivos.",
        "b) Hasta cuatro dispositivos.",
        "c) Hasta cinco dispositivos.",
        "d) Hasta seis dispositivos.",
    ],
    "d"
),
(
    "¿Puede un portátil acceder a un disco duro externo incluso si este no está conectado directamente a él, sino de forma indirecta a través de la cadena de dispositivos Thunderbolt?",
    [
        "a) No, la conexión indirecta impide el acceso al disco duro externo.",
        "b) Sí, el portátil puede acceder al disco duro externo aunque esté conectado indirectamente a través de Thunderbolt.",
        "c) Solo si el disco duro externo está conectado directamente al portátil.",
        "d) Depende del tipo de portátil utilizado.",
    ],
    "b"
),
(
    "¿Cuántas veces más rápido es el puerto Thunderbolt en comparación con el puerto USB 3.0 al trabajar con dos canales simultáneos?",
    [
        "a) Dos veces más rápido.",
        "b) Tres veces más rápido.",
        "c) Cuatro veces más rápido.",
        "d) Cinco veces más rápido.",
    ],
    "c"
),
(
    "En una placa base típica, ¿cuáles son las funciones de las entradas de color verde, azul y rosa en los conectores de sonido?",
    [
        "a) Verde: Entrada de línea. Azul: Salida de línea. Rosa: Micrófono.",
        "b) Verde: Micrófono. Azul: Altavoces. Rosa: Salida de línea.",
        "d) Verde: Salida de línea. Azul: Entrada de línea. Rosa: Micrófono.",
        "c) Verde: Salida de línea. Azul: Micrófono. Rosa: Entrada de línea.",
    ],
    "d"
),
(
    "¿Qué función comúnmente realiza un jack de sonido externo en la mayoría de los dispositivos?",
    [
        "a) Solo funciona como salida de línea para altavoces.",
        "b) Hace exclusivamente las funciones de entrada de micrófono.",
        "c) Tiene solo funciones de entrada de línea.",
        "d) Normalmente actúa como salida de línea y a veces también como entrada de micrófono.",
    ],
    "d"
),
(
    "En placas con sistema de sonido 5.1 envolvente, ¿cuáles son las funciones de los conectores de color gris, negro y naranja?",
    [
        "a) Gris: Micrófono. Negro: Salida de línea para altavoces delanteros. Naranja: Entrada de línea.",
        "b) Gris: Salida de línea para altavoces delanteros. Negro: Salida de línea para altavoces traseros. Naranja: Salida de línea para subwoofer o altavoz central.",
        "c) Gris: Entrada de línea. Negro: Salida de línea para altavoces delanteros. Naranja: Salida de línea para altavoces traseros.",
        "d) Gris: Salida de línea para altavoces delanteros. Negro: Salida de línea para altavoces traseros. Naranja: Salida de línea para el subwoofer (subgrave) o altavoz central.",
    ],
    "d"
),
(
    "¿Cuál de los siguientes enunciados describe correctamente al puerto VGA?",
    [
        "a) Es el más reciente de todos los puertos de monitor.",
        "b) Tiene conexiones digitales y es similar al HDMI.",
        "c) Es el más antiguo de todos, con 15 pines, y utiliza una señal analógica.",
        "d) Tiene un conector de color azul y solo puede usarse con monitores antiguos.",
    ],
    "c"
),
(
    "¿Cuáles son las características principales del puerto VGA (Video Graphics Array)?",
    [
        "a) Es el más reciente de todos, con conexiones digitales y un conector azul.",
        "b) Tiene 15 pines, es analógico, y su conector es normalmente de color azul.",
        "c) Es un puerto exclusivamente digital similar al HDMI.",
        "d) Utiliza una conexión USB y es compatible solo con monitores modernos.",
    ],
    "b"
),
(
    "¿Cuál de las siguientes afirmaciones describe correctamente al conector DVI (Digital Visual Interface)?",
    [
        "a) Es un conector analógico con mejor calidad que el VGA.",
        "b) Todos los monitores actuales son analógicos, por lo que el DVI es necesario para la conversión digital-analógica.",
        "c) Es un conector digital diseñado para obtener mejor calidad en monitores digitales, y su color normalmente es blanco.",
        "d) Su diseño permite realizar la conversión digital-analógica sin pérdida de calidad en la imagen.",
    ],
    "c"
),
(
    "¿Cuál es la característica principal del conector DVI (Digital Visual Interface) en términos de su señal?",
    [
        "a) Es un conector analógico.",
        "b) Es un conector híbrido que admite tanto señales analógicas como digitales.",
        "c) Es un conector digital.",
        "d) Es un conector exclusivamente analógico.",
    ],
    "c"
),
(
    "¿Cómo se compara la calidad del conector DVI con el conector VGA?",
    [
        "a) El conector DVI tiene menor calidad que el VGA.",
        "b) La calidad es similar entre ambos conectores.",
        "c) El conector DVI obtiene mejor calidad que el VGA.",
        "d) No hay diferencia de calidad entre ambos conectores.",
    ],
    "c"
),
(
    "¿Cómo se compara la calidad del conector DVI con el conector VGA?",
    [
        "c) El conector DVI tiene menor calidad que el VGA.",
        "b) La calidad es similar entre ambos conectores.",
        "a) El conector DVI obtiene mejor calidad que el VGA.",
        "d) Depende del fabricante.",
    ],
    "a"
),
(
    "¿Por qué se afirma que no tiene sentido realizar la conversión digital-analógica en los monitores actuales al usar el conector DVI?",
    [
        "a) Todos los monitores actuales son exclusivamente analógicos.",
        "b) La conversión digital-analógica es más eficiente que la conversión analógico-digital.",
        "c) Todos los monitores actuales son digitales, por lo que no es necesario realizar la conversión digital-analógica.",
        "d) La conversión analógico-digital es más eficiente que la conversión digital-analógica.",
    ],
    "c"
),
(
    "¿Cuál es el objetivo principal del diseño del conector DVI en relación con la calidad de imagen en los monitores digitales?",
    [
        "a) Obtener una calidad de imagen inferior en comparación con otros conectores.",
        "b) Diseñado exclusivamente para monitores analógicos.",
        "c) Mejorar la calidad de imagen en monitores digitales.",
        "d) Proporcionar una conexión híbrida para admitir tanto monitores digitales como analógicos.",
    ],
    "c"
),
(
    "¿Cuál es el color típicamente asociado con el conector DVI?",
    [
        "a) Rojo.",
        "b) Negro.",
        "c) Blanco.",
        "d) Azul.",
    ],
    "c"
),
(
    "¿Cuál de las siguientes afirmaciones describe correctamente al conector HDMI (High Definition Multimedia Interface)?",
    [
        "a) Es un conector analógico con menor sofisticación que el DVI.",
        "b) Puede transmitir solo video, no tiene capacidad de audio.",
        "c) Es un conector digital más sofisticado que el DVI, capaz de transmitir video y sonido.",
        "d) Tiene una velocidad de transmisión de hasta 1Gbps.",
    ],
    "c"
),
(
    "¿Cuál es la principal característica del conector HDMI (High Definition Multimedia Interface)?",
    [
        "a) Es un conector analógico.",
        "b) Puede transmitir solo video, no tiene capacidad de audio.",
        "c) Es un conector digital más sofisticado que el DVI, capaz de transmitir video y sonido.",
        "d) Tiene una velocidad de transmisión de hasta 10Gbps.",
    ],
    "c"
),
(
    "¿Cuál es la naturaleza principal del conector HDMI (High Definition Multimedia Interface)?",
    [
        "a) Es un conector analógico.",
        "c) Es un conector híbrido que admite señales analógicas y digitales.",
        "b) Es un conector digital.",
        "d) Puede transmitir solo audio, no tiene capacidad de video.",
    ],
    "b"
),
(
    "¿Cuál es la velocidad máxima de transmisión de video y sonido que puede alcanzar el conector HDMI?",
    [
        "a) Hasta 1Gbps.",
        "b) Hasta 2.5Gbps.",
        "c) Hasta 5Gbps.",
        "d) Hasta 10Gbps.",
    ],
    "c"
),
(
    "¿Cuál es la función principal del conector ATX en una computadora?",
    [
        "a) Conectar discos duros y unidades SSD a la placa base.",
        "b) Suministrar energía a la placa base.",
        "c) Proporcionar energía al procesador.",
        "d) Conectar dispositivos de almacenamiento a la fuente de alimentación.",
    ],
    "b"
),
(
    "¿Cuántos pines tiene el conector ATX utilizado para suministrar energía a la placa base?",
    [
        "a) 12 pines.",
        "b) 20 pines.",
        "c) 24 pines.",
        "d) 30 pines.",
    ],
    "c"
),
(
    "¿Cómo se establece la conexión física entre la placa base y la fuente de alimentación mediante el conector ATX?",
    [
        "a) Ambos tienen conectores ATX hembra.",
        "c) Ambos tienen conectores ATX macho.",
        "b) La placa base tiene un conector ATX hembra, mientras que la fuente de alimentación tiene un conector ATX macho.",
        "d) La placa base tiene un conector ATX macho, mientras que la fuente de alimentación tiene un conector ATX hembra.",
    ],
    "b"
),
(
    "¿Cuántos pines tiene el conector ATX en la actualidad y cuántos tenía en equipos muy antiguos?",
    [
        "a) 20 pines en la actualidad, 24 pines en equipos muy antiguos.",
        "b) 24 pines en la actualidad, 20 pines en equipos muy antiguos.",
        "c) 24 pines tanto en la actualidad como en equipos muy antiguos.",
        "d) 20 pines tanto en la actualidad como en equipos muy antiguos.",
    ],
    "b"
),
(
    "¿Cuál es la función principal del conector ATX 12V de 4 y 8 pines en una computadora?",
    [
        "a) Conectar discos duros y unidades SSD a la placa base.",
        "b) Suministrar energía a la placa base.",
        "c) Proporcionar energía al procesador, con variantes de 4 y 8 pines.",
        "d) Conectar dispositivos de almacenamiento a la fuente de alimentación.",
    ],
    "c"
),
(
    "¿Cuál es la función principal del conector ATX 12V en relación con el procesador?",
    [
        "a) Conectar dispositivos de almacenamiento a la placa base.",
        "b) Suministrar energía a la placa base.",
        "c) Proporcionar energía al procesador.",
        "d) Conectar dispositivos externos a la fuente de alimentación.",
    ],
    "c"
),
(
    "¿Dónde se encuentra ubicada la clavija hembra del conector ATX 12V en la placa base?",
    [
        "a) Lejos del procesador.",
        "b) En el extremo opuesto de la placa base.",
        "c) Cercana al procesador.",
        "d) En la parte superior de la placa base.",
    ],
    "c"
),
(
    "¿Cuántas variantes de conectores existen para el conector ATX 12V en términos de cantidad de pines?",
    [
        "a) Solo existe una variante de 4 pines.",
        "b) Solo existe una variante de 8 pines.",
        "c) Existen variantes de 4 y de 8 pines.",
        "d) Existen variantes de 6 y de 12 pines.",
    ],
    "c"
),
(
    "¿Cuál es la función adicional de los conectores de 8 pines en comparación con los de 4 pines en el conector ATX 12V?",
    [
        "a) Proporcionar una conexión más segura.",
        "b) No hay diferencia en la función entre los conectores de 4 y 8 pines.",
        "c) Aportar una mayor cantidad de energía al procesador.",
        "d) Reducir la velocidad del procesador para un mejor rendimiento energético.",
    ],
    "c"
),
(
    "¿Cuál es la función principal del puerto SATA en una computadora?",
    [
        "a) Conectar dispositivos de sonido a la placa base.",
        "b) Suministrar energía a la placa base.",
        "c) Conectar discos duros, unidades SSD y antiguos lectores ópticos a la placa base.",
        "d) Conectar dispositivos de red a la placa base.",
    ],
    "c"
),
(
    "¿Para qué tipo de dispositivos se utilizaban comúnmente los puertos SATA, incluyendo lectores ópticos obsoletos?",
    [
        "a) Para dispositivos de impresión.",
        "b) Para cámaras digitales.",
        "c) Para conectar discos duros, unidades SSD y lectores ópticos obsoletos a la placa base.",
        "d) Exclusivamente para dispositivos de red.",
    ],
    "c"
),
(
    "¿Cuál es la principal diferencia de velocidad entre los dispositivos NVMe con puerto M.2 y las unidades SSD SATA?",
    [
        "a) Los dispositivos NVMe son más lentos que las unidades SSD SATA.",
        "b) No hay diferencia significativa de velocidad entre ellos.",
        "c) Los dispositivos NVMe con puerto M.2 son hasta seis veces más rápidos que las unidades SSD SATA.",
        "d) Los dispositivos NVMe con puerto M.2 son el doble de rápidos que las unidades SSD SATA.",
    ],
    "c"
),
(
    "¿Cómo se relaciona el puerto M.2 con los puertos SATA en términos de evolución?",
    [
        "a) El puerto M.2 es una versión más antigua que los puertos SATA.",
        "b) Ambos son tecnologías independientes sin relación alguna.",
        "c) El puerto M.2 es la evolución de los puertos SATA.",
        "d) Los puertos SATA son una versión mejorada del puerto M.2.",
    ],
    "c"
),
(
    "¿Cómo se relaciona el puerto M.2 con los puertos SATA en términos de evolución?",
    [
        "a) El puerto M.2 es una versión más antigua que los puertos SATA.",
        "b) Ambos son tecnologías independientes sin relación alguna.",
        "c) El puerto M.2 es la evolución de los puertos SATA.",
        "d) Los puertos SATA son una versión mejorada del puerto M.2.",
    ],
    "c"
),
(
    "¿En qué modo funcionan los dispositivos NVMe con puerto M.2?",
    [
        "a) En modo USB.",
        "b) En modo Thunderbolt.",
        "d) En modo PCI Express, con una diferencia significativa de velocidad.",
        "c) En modo SATA, con la misma velocidad que los dispositivos convencionales.",
    ],
    "d"
),
(
    "¿Cuánto más rápido puede ser un dispositivo NVMe en comparación con una unidad SSD SATA?",
    [
        "a) El doble de rápido.",
        "b) Cuatro veces más rápido.",
        "c) Seis veces más rápido.",
        "d) Diez veces más rápido.",
    ],
    "c"
),
(
    "¿Cuáles son los dos tipos de conectores para ventiladores que pueden tener las placas base?",
    [
        "a) CPU Flan y Cha Flan.",
        "b) JACK Chan y CPU Chan.",
        "c) CPU Fan y CHA Fan.",
        "d) Solo ventiladores controlados por la fuente de alimentación.",
    ],
    "c"
),
(
    "¿Cómo se describen comúnmente los conectores CPU Fan en términos de pines y funcionalidad?",
    [
        "a) Conectores de 2 pines sin control de velocidad.",
        "b) Conectores de 3 pines con control de velocidad.",
        "c) Conectores de 4 pines con opción PWM de control de velocidad.",
        "d) Conectores de 4 pines sin opción de control de velocidad.",
    ],
    "c"
),
(
    "¿Cuál es la principal ventaja de la opción PWM de control de velocidad en los conectores CPU Fan?",
    [
        "a) No afecta la velocidad del ventilador.",
        "b) Adaptar la velocidad del ventilador al rendimiento del disco duro.",
        "c) Adaptar la velocidad del ventilador al rendimiento del microprocesador.",
        "d) Controlar la velocidad del ventilador automáticamente sin intervención del usuario.",
    ],
    "c"
),
(
    "¿Cómo se describe el conector CHA Fan en términos de su conexión y control?",
    [
        "a) Es un conector obligatorio para todos los ventiladores en la placa base.",
        "b) Es un conector opcional que controla automáticamente la velocidad de los ventiladores.",
        "c) Es un conector opcional utilizado para conectar y controlar ventiladores por la placa base.",
        "d) Es un conector reservado exclusivamente para ventiladores de la CPU.",
    ],
    "c"
),
(
    "¿Cuál es la función principal de los puertos USB externos en las cajas de computadoras?",
    [
        "a) Controlar la velocidad del procesador.",
        "b) Permitir la expansión de posibilidades de conexión externa.",
        "c) Facilitar la conexión de dispositivos de sonido.",
        "d) Exclusivamente para la conexión de unidades de disco duro externas.",
    ],
    "b"
),
(
    "¿Cuál es el propósito principal de los puertos externos en las cajas de computadoras, además de la placa base?",
    [
        "a) Mejorar la velocidad de la memoria RAM.",
        "b) Facilitar la conexión de dispositivos de red.",
        "c) Permitir al equipo más posibilidades de expansión.",
        "d) Exclusivamente para la conexión de monitores externos.",
    ],
    "c"
),
(
    "¿Por qué en ocasiones los puertos externos en las cajas de computadoras son más accesibles para dispositivos como pendrives o tarjetas de memoria?",
    [
        "a) Porque solo admiten este tipo de dispositivos.",
        "b) Por razones estéticas.",
        "c) Para limitar el acceso a dispositivos externos.",
        "d) Para facilitar la conexión de dispositivos portátiles como pendrives o tarjetas de memoria.",
    ],
    "d"
),
(
    "¿Cuál es la función principal de los conectores del Front Panel en una computadora?",
    [
        "a) Controlar la velocidad del procesador.",
        "c) Permitir la conexión de dispositivos externos.",
        "b) Conectar cables y botones relacionados con la operación básica de la computadora, como encendido, reinicio y actividad del disco duro.",
        "d) Exclusivamente para la conexión de dispositivos de audio externos.",
    ],
    "b"
),
(
    "¿Cuáles son algunas de las conexiones que se pueden realizar a través de los conectores del Front Panel?",
    [
        "a) Conectar dispositivos de red externos.",
        "b) Conectar dispositivos USB externos.",
        "c) Conectar el cable de encendido, el botón de reset, el LED de actividad del disco duro y el LED de actividad del equipo.",
        "d) Exclusivamente para la conexión de dispositivos de almacenamiento externos.",
    ],
    "c"
),
(
    "¿Cuál es la función principal del conector interno PC speaker en una placa base?",
    [
        "a) Reproducir música y sonidos durante el uso normal de la computadora.",
        "b) Conectar dispositivos de almacenamiento externos.",
        "c) Permitir la conexión de altavoces externos.",
        "d) Emitir pitidos durante el arranque para indicar la presencia o ausencia de errores según el POST.",
    ],
    "d"
),
(
    "¿Cuál es la finalidad principal del conector interno PC speaker y cómo se utiliza en la placa base?",
    [
        "a) Reproducir música durante el uso normal de la computadora.",
        "b) Emitir pitidos durante el arranque para indicar la presencia o ausencia de errores según el POST.",
        "c) Conectar altavoces externos para mejorar la calidad del sonido.",
        "d) Transmitir datos entre la placa base y dispositivos de almacenamiento externos.",
    ],
    "b"
),
(
    "¿Cuándo se utiliza principalmente el speaker conectado al conector interno PC speaker en la placa base?",
    [
        "a) Durante el uso normal de la computadora.",
        "b) Exclusivamente para reproducir música y sonidos.",
        "c) Solamente durante el arranque para que el POST avise de la ausencia o presencia de errores.",
        "d) En situaciones de alta carga de procesamiento para mejorar la calidad del sonido.",
    ],
    "c"
),
(
    "¿Cuál es la función principal de los pitidos emitidos por el speaker conectado al conector interno PC speaker durante el arranque?",
    [
        "a) Proporcionar un sonido agradable durante el inicio de la computadora.",
        "b) Indicar errores en el sistema operativo.",
        "c) Emitir pitidos para realizar diagnósticos de la placa base durante el arranque.",
        "d) Reproducir música de fondo durante la carga del sistema.",
    ],
    "c"
),
(
    "¿Cuál es la función principal de los conectores de sonido interno en una computadora?",
    [
        "c) Proporcionar energía a los altavoces externos.",
        "b) Conectar dispositivos de almacenamiento externos.",
        "a) Permitir la conexión de entradas y salidas de audio de la caja del equipo.",
        "d) Exclusivamente para la conexión de micrófonos externos.",
    ],
    "a"
),
(
    "¿Por qué es importante la estructura y el material del chasis en un equipo microinformático?",
    [
        "a) Únicamente para mejorar la estética del equipo.",
        "b) Para proporcionar una mayor capacidad de almacenamiento.",
        "c) Para amortiguar las vibraciones y prevenir daños mecánicos a componentes como discos duros o lectores ópticos.",
        "d) Exclusivamente para facilitar el ensamblaje de componentes internos.",
    ],
    "c"
),
(
    "¿Cuál es la principal razón por la que la estructura y el material de la caja son importantes en un equipo microinformático?",
    [
        "a) Únicamente para mejorar la estética del equipo.",
        "b) Para proporcionar una mayor capacidad de almacenamiento.",
        "c) Para prevenir daños mecánicos a componentes como discos duros o lectores ópticos al amortiguar las vibraciones.",
        "d) Exclusivamente para facilitar el transporte del equipo.",
    ],
    "c"
),
(
    "¿Cuáles son los materiales comunes utilizados en la fabricación de las cajas de equipos microinformáticos?",
    [
        "a) Exclusivamente chapa troquelada.",
        "b) Chapa troquelada y plástico en el frontal.",
        "c) Únicamente aluminio.",
        "d) Aluminio y plástico en el frontal.",
    ],
    "b"
),
(
    "¿Cuál es una característica principal de la chapa troquelada utilizada en las cajas de equipos microinformáticos?",
    [
        "a) Ofrece una gran rigidez y resistencia.",
        "b) Es un material costoso pero muy liviano.",
        "c) Proporciona mucha rigidez y es económico.",
        "d) No es adecuada para la fabricación de cajas debido a su fragilidad.",
    ],
    "c"
),
(
    "¿Cuáles son las ventajas de las cajas de aluminio en comparación con las de chapa troquelada?",
    [
        "a) Son más pesadas pero ofrecen mayor resistencia.",
        "b) Son menos rígidas y más costosas.",
        "c) Son más rígidas y livianas que la chapa troquelada.",
        "d) Ofrecen la misma rigidez que la chapa troquelada pero a un costo menor.",
    ],
    "c"
),
(
    "¿Cuál es una característica económica de las cajas de aluminio en comparación con otras opciones?",
    [
        "c) Son más económicas que las cajas de chapa troquelada.",
        "b) Tienen un costo similar al de las cajas de plástico.",
        "a) Son más caras en comparación con otras opciones.",
        "d) Ofrecen una excelente relación calidad-precio.",
    ],
    "a"
),
(
    "¿Cuáles son algunos de los formatos más usuales de cajas de equipos microinformáticos?",
    [
        "a) Mini, Micro y Mega.",
        "b) Pequeño, Mediano y Grande.",
        "c) Estándar, Pequeño y Grande.",
        "d) Formato estándar, Formato más pequeño y Formato grande.",
    ],
    "d"
),
(
    "¿Cuáles son las principales ventajas de las cajas ATX y micro-ATX en comparación con otros formatos?",
    [
        "a) Son menos comunes y difíciles de encontrar.",
        "b) Pueden albergar una variedad de formatos de placa base, incluyendo ATX y micro-ATX.",
        "c) Ocupan más espacio pero son más fáciles de mantener.",
        "d) Tienen una fuente de alimentación complicada de reemplazar.",
    ],
    "b"
),
(
    "¿Cuáles son los formatos de cajas más utilizados en formato estándar?",
    [
        "a) Formatos Mini y Mega.",
        "b) Cajas estándar y especializadas.",
        "c) Cajas ATX y micro-ATX.",
        "d) Formatos Pequeño y Grande.",
    ],
    "c"
),
(
    "¿Cuál es una de las principales ventajas de las cajas ATX y micro-ATX?",
    [
        "a) Son más pesadas y robustas.",
        "b) Tienen un diseño más moderno.",
        "c) Pueden albergar una variedad de formatos de placa base, incluyendo ATX y micro-ATX.",
        "d) Son más económicas pero menos versátiles.",
    ],
    "c"
),
(
    "¿Cuál es una de las consideraciones al elegir cajas micro-ATX en términos de la fuente de alimentación?",
    [
        "a) Siempre utilizan fuentes de alimentación ATX.",
        "b) Tienen una fuente de alimentación más fácil de reemplazar que las cajas ATX.",
        "c) Ocupan menos espacio pero pueden tener una fuente de alimentación complicada de reemplazar.",
        "d) No son compatibles con fuentes de alimentación ATX.",
    ],
    "c"
),
(
    "¿Cuál es el formato más pequeño de cajas de equipos microinformáticos?",
    [
        "a) Micro-ATX.",
        "b) Mini-ITX.",
        "c) Mega-ATX.",
        "d) Nano-ATX.",
    ],
    "b"
),
(
    "¿Qué tipo de placas base suelen soportar las cajas mini-ITX, y cuál es una característica común de estas cajas?",
    [
        "a) Suelen soportar placas base ATX, y tienen una fuente de alimentación de alta potencia.",
        "b) Suelen soportar placas base Mini-ATX, y tienen una fuente de alimentación de alta potencia.",
        "c) Suelen soportar placas base micro-ATX, y tienen una fuente de alimentación de alta potencia.",
        "d) Suelen soportar placas base mini-ITX, y tienen una fuente de alimentación de poca potencia.",
    ],
    "d"
),
(
    "¿Cuál es uno de los motivos comunes para elegir cajas mini-ITX?",
    [
        "a) Para tener una fuente de alimentación de alta potencia.",
        "b) Para soportar placas base ATX.",
        "c) Para facilitar el montaje de unidades ópticas.",
        "d) Para lograr un formato reducido, siendo compatibles con placas base mini-ITX.",
    ],
    "d"
),
(
    "¿Cuál es una característica típica de la fuente de alimentación en las cajas mini-ITX?",
    [
        "a) Tienen una fuente de alimentación de alta potencia.",
        "b) Utilizan fuentes de alimentación ATX estándar.",
        "c) Suelen tener una fuente de alimentación de poca potencia, alrededor de 15 vatios.",
        "d) Son compatibles únicamente con fuentes de alimentación de más de 500 vatios.",
    ],
    "c"
),
(
    "¿Cuál es una ventaja de algunos modelos de cajas mini-ITX?",
    [
        "a) Son más pesados que otras cajas, lo que mejora su estabilidad.",
        "b) No permiten el montaje en la parte trasera del monitor.",
        "c) Tienen un diseño exclusivo que no se adapta a la mayoría de los entornos de trabajo.",
        "d) Se pueden atornillar en la parte trasera del monitor, liberando espacio en el área de trabajo.",
    ],
    "d"
),
(
    "¿Cuál es una característica de las cajas picoITX?",
    [
        "a) Son más grandes que las cajas mini-ITX.",
        "b) Tienen un formato poco común en barebones.",
        "c) Suelen ser menos eficientes en términos de espacio.",
        "d) Son cajas mucho más pequeñas y son comunes en barebones.",
    ],
    "d"
),
(
    "¿Qué se entiende por barebone en el contexto de los sistemas informáticos?",
    [
        "a) Un sistema completamente ensamblado y listo para usar.",
        "b) Una caja de computadora sin componentes internos.",
        "c) Un PC completamente construido con todos los componentes necesarios.",
        "d) Un PC parcialmente construido, con los mínimos componentes imprescindibles (caja + fuente de alimentación + placa base).",
    ],
    "d"
),
(
    "En el contexto de barebones, ¿qué aspecto es responsabilidad del usuario?",
    [
        "a) La fabricación de la caja.",
        "b) La instalación de la fuente de alimentación.",
        "c) Elegir y ajustar los componentes como CPU, RAM y HDD según sus necesidades.",
        "d) Configurar el sistema operativo.",
    ],
    "c"
),
(
    "¿Cuándo se suelen utilizar las cajas E-ATX o Extended ATX?",
    [
        "a) En sistemas compactos y de formato reducido.",
        "b) Principalmente en computadoras personales de uso diario.",
        "c) En servidores o en situaciones donde se necesita mucho espacio.",
        "d) Exclusivamente en equipos de juegos.",
    ],
    "c"
),
(
    "¿Cuándo se suelen utilizar las cajas E-ATX o Extended ATX?",
    [
        "a) En sistemas compactos y de formato reducido.",
        "b) Principalmente en computadoras personales de uso diario.",
        "c) En servidores o en situaciones donde se necesita mucho espacio.",
        "d) Exclusivamente en equipos de juegos.",
    ],
    "c"
),
(
    "¿Cuál es una de las ventajas principales de las cajas E-ATX o Extended ATX?",
    [
        "c) Reducción del consumo de energía.",
        "b) Mayor facilidad de transporte.",
        "a) Mejora en la ventilación y espacio extra para una ubicación más correcta de los componentes.",
        "d) Menor costo en comparación con otros tipos de cajas.",
    ],
    "a"
),
(
    "¿Por qué la placa base es considerada un componente fundamental en un sistema informático?",
    [
        "a) Por su capacidad para almacenar grandes cantidades de datos.",
        "b) Por su capacidad para procesar información a alta velocidad.",
        "c) Generalmente, una buena placa base asegura un sistema eficiente.",
        "d) Por su capacidad para ejecutar software de manera eficiente.",
    ],
    "c"
),
(
    "¿Cuál es la razón principal por la cual una buena placa base puede asegurar un sistema eficiente?",
    [
        "a) Aumenta la capacidad de almacenamiento.",
        "b) Mejora la velocidad de procesamiento.",
        "c) Facilita la conexión de periféricos externos.",
        "d) Generalmente, una buena placa base asegura un sistema eficiente.",
    ],
    "d"
),
(
    "¿Por qué en ocasiones es preferible invertir en una mejor placa base en lugar de un microprocesador más potente?",
    [
        "a) La placa base tiene un impacto directo en la velocidad de procesamiento.",
        "b) Una mejor placa base mejora la capacidad de almacenamiento.",
        "c) El microprocesador no afecta significativamente el rendimiento del sistema.",
        "d) Una buena placa base es esencial para la conectividad de periféricos externos.",
    ],
    "a"
),
(
    "¿Por qué en ocasiones es preferible invertir en una mejor placa base en lugar de un microprocesador más potente?",
    [
        "a) La placa base tiene un impacto directo en la velocidad de procesamiento.",
        "b) Una mejor placa base mejora la capacidad de almacenamiento.",
        "c) El microprocesador no afecta significativamente el rendimiento del sistema.",
        "d) Una buena placa base es esencial para la conectividad de periféricos externos.",
    ],
    "a"
),
(
    "¿Cuál es la ventaja de la localización de los componentes en una placa base ATX?",
    [
        "a) Mejora la capacidad de almacenamiento.",
        "b) Facilita la conexión de periféricos externos.",
        "c) Optimiza la ventilación de la caja del equipo.",
        "d) Permite una mayor velocidad de procesamiento.",
    ],
    "c"
),
(
    "¿Qué es el factor de forma de una placa base?",
    [
        "a) La velocidad máxima de procesamiento.",
        "b) La capacidad de almacenamiento.",
        "c) El tamaño y disposición de los componentes en la placa.",
        "d) La cantidad de puertos USB disponibles.",
    ],
    "c"
),
(
    "¿Qué significa la sigla ATX en el contexto de las placas base?",
    [
        "a) Advanced Technology Xtended.",
        "b) Average Technology eXpanded.",
        "c) Advanced Technical eXperience.",
        "d) All-Time Xtreme.",
    ],
    "a"
),
(
    "¿Qué formato de placa base se sigue utilizando desde hace mucho tiempo?",
    [
        "a) ATX (Advanced Technology Xtended).",
        "b) ATX (Average Technology eXpanded).",
        "c) ARX (Advanced Reduced eXperience).",
        "d) ARX (Advanced  Recursive Xtended.",
    ],
    "a"
),
(
    "¿Cuál es la principal diferencia entre los formatos micro-ATX y mini-ITX?",
    [
        "a) El micro-ATX es más grande que el mini-ITX.",
        "b) El mini-ITX es más grande que el micro-ATX.",
        "c) El micro-ATX tiene más conectores USB.",
        "d) El mini-ITX es más adecuado para servidores.",
    ],
    "a"
),
(
    "¿En qué situaciones es más adecuado utilizar el formato mini-ITX en lugar de micro-ATX?",
    [
        "a) Cuando se necesita mayor capacidad de expansión.",
        "b) Cuando se requiere un menor tamaño y la reducción es prioritaria.",
        "c) Cuando se desea un rendimiento superior.",
        "d) Cuando se utiliza la placa base para servidores.",
    ],
    "b"
),
(
    "¿Cuál es la finalidad de situar la fuente de alimentación encima del microprocesador en una placa base ATX?",
    [
        "a) Mejorar la estética de la placa base.",
        "b) Facilitar el acceso a la fuente de alimentación.",
        "c) Optimizar la ventilación de la caja.",
        "d) Reducir el tamaño de la placa base.",
    ],
    "c"
),
(
    "¿Cuál es el beneficio de situar las unidades de almacenamiento cerca de los puertos SATA en una placa base ATX?",
    [
        "a) Facilitar el acceso a las unidades de almacenamiento.",
        "b) Reducir la longitud de los cables SATA y formar una maraña de cables.",
        "c) Mejorar la velocidad de transferencia de datos.",
        "d) Incrementar la capacidad de almacenamiento.",
    ],
    "b"
),
(
    "¿Cuál es el principal beneficio de los formatos nano-ITX y pico-ITX en comparación con otros formatos más grandes?",
    [
        "a) Mayor capacidad de almacenamiento.",
        "b) Menor consumo de energía.",
        "c) Reducción significativa del espacio.",
        "d) Mejor capacidad de ventilación.",
    ],
    "c"
),
(
    "¿Qué tipo de memoria se utiliza comúnmente en placas base con formatos nano-ITX o pico-ITX debido a su espacio reducido?",
    [
        "a) DDR2",
        "b) DDR3",
        "c) DDR4",
        "d) SO-DIMM",
    ],
    "d"
),
(
    "¿Qué significan las siglas SO-DIMM en el contexto de la memoria utilizada en placas base con formatos nano-ITX o pico-ITX?",
    [
        "a) Single Outline Dual In-Line Memory Module",
        "b) Small Outline Dual In-Line Memory Module",
        "c) Slim Outline Dual In-Line Memory Module",
        "d) System Outline Dual In-Line Memory Module",
    ],
    "b"
),
(
    "¿Cuál es una de las características destacadas del diseño de las memorias RAM SO-DIMM utilizadas en arquitecturas destinadas a ordenadores portátiles?",
    [
        "a) Tamaño grande",
        "b) Diseño asimétrico",
        "c) Equilibrio y compacidad",
        "d) Elevada velocidad",
    ],
    "c"
),
(
    "¿Qué significa la sigla SoC en el contexto de los smartphones?",
    [
        "a) Sistema Operativo Común",
        "b) Sistema de Organización Central",
        "c) Sistema Operativo Centralizado",
        "d) Sistema en un Chip",
    ],
    "d"
),
(
    "¿Cuál de los siguientes elementos es común tanto en un smartphone como en un portátil?",
    [
        "a) Ratón",
        "b) Teclado físico",
        "c) Placa base",
        "d) Unidad de CD/DVD",
    ],
    "c"
),
(
    "¿Cuáles son algunos de los elementos comunes entre un smartphone y un portátil?",
    [
        "a) Elementos únicos, no comparten ningún componente.",
        "b) Comparten únicamente la pantalla.",
        "c) Comparten la placa base, batería, y sistema de carga, entre otros elementos.",
        "d) Solo comparten el sistema operativo.",
    ],
    "c"
),
(
    "¿Qué significa la sigla SoC en el contexto de los smartphones?",
    [
        "a) Sistema Operativo Compartido.",
        "b) Servicio de Operación Continua.",
        "c) Sistema en un Chip (System on a Chip).",
        "d) Software Orientado a Comunicaciones.",
    ],
    "c"
),
(
    "¿Qué es el socket o zócalo de la CPU y cuál es su función principal en la placa base?",
    [
        "a) Un puerto de conexión para el teclado.",
        "b) Un conector para la tarjeta de video.",
        "c) El lugar donde se coloca el microprocesador en la placa base.",
        "d) Un dispositivo de almacenamiento externo.",
    ],
    "c"
),
(
    "¿Cuáles son los dos tipos de zócalos comúnmente utilizados para colocar el microprocesador en la placa base?",
    [
        "a) Zócalo A y Zócalo B.",
        "b) Zócalo X y Zócalo Y.",
        "c) Zócalo PGA y Zócalo LGA.",
        "d) Zócalo USB y Zócalo HDMI.",
    ],
    "c"
),
(
    "¿Cómo se compone el socket PGA en términos de conectores o contactos y dónde residen las patillas o pines?",
    [
        "a) Una matriz de pines en el socket y conectores en el microprocesador.",
        "b) Una matriz de conectores o contactos en el socket y patillas en el microprocesador.",
        "c) Patillas en el socket y conectores en el microprocesador.",
        "d) Conectores en ambos, tanto el socket como el microprocesador.",
    ],
    "b"
),
(
    "¿Cómo se caracteriza la composición del socket PGA en términos de su estructura?",
    [
        "a) Una matriz de patillas en el socket y conectores en el microprocesador.",
        "b) Una matriz de conectores o contactos en el socket.",
        "c) Una matriz de conectores en el microprocesador.",
        "d) Una matriz de patillas en ambos, tanto el socket como el microprocesador.",
    ],
    "b"
),
(
    "¿Dónde residen las patillas o pines en el caso del socket PGA?",
    [
        "a) En una matriz en el socket.",
        "b) En una matriz en el microprocesador.",
        "c) En la parte superior del socket.",
        "d) En la parte inferior del socket.",
    ],
    "b"
),
(
    "¿Qué tipo de socket se utiliza comúnmente para los procesadores AMD?",
    [
        "a) LGA",
        "b) PGA",
        "c) USB",
        "d) HDMI",
    ],
    "b"
),
(
    "¿Qué tipo de socket se utiliza comúnmente para los procesadores AMD?",
    [
        "a) LGA",
        "b) PGA",
        "c) USB",
        "d) HDMI",
    ],
    "b"
),
(
    "¿Cómo se caracteriza la ubicación de los pines en el caso del socket LGA?",
    [
        "a) Los pines están en el microprocesador.",
        "b) Los pines están en una serie de contactos en el socket.",
        "c) Los pines están en el socket, mientras que el microprocesador tiene una serie de contactos.",
        "d) Los pines y los contactos se distribuyen por igual entre el socket y el microprocesador.",
    ],
    "c"
),
(
    "¿Cómo afecta la disposición de los pines en los sockets LGA a su delicadeza?",
    [
        "a) No afecta su delicadeza.",
        "b) Los hace menos delicados.",
        "c) Los hace más delicados.",
        "d) No hay diferencia en la delicadeza entre los sockets LGA y PGA.",
    ],
    "c"
),
(
    "¿Qué tipo de socket es comúnmente utilizado por los microprocesadores Intel?",
    [
        "a) PGA",
        "b) LGA",
        "c) USB",
        "d) HDMI",
    ],
    "b"
),
(
    "¿Qué significa la sigla ZIF en el contexto de los zócalos de la CPU?",
    [
        "a) Zócalo Inteligente y Fácil.",
        "b) Zona de Interconexión Flexible.",
        "c) Zero Insertion Force (Fuerza de Inserción Cero).",
        "d) Zócalo Inalámbrico y Flexible.",
    ],
    "c"
),
(
    "¿Cuál es la característica principal de los zócalos ZIF en términos de fijación del microprocesador a la placa base?",
    [
        "a) Requieren una presión significativa para la fijación.",
        "b) Utilizan fuerza magnética para la fijación.",
        "c) No necesitan realizar presión para fijar el microprocesador.",
        "d) Son exclusivos para microprocesadores de baja potencia.",
    ],
    "c"
),
(
    "¿Cuál es la función de la patilla en los zócalos ZIF y cómo afecta al proceso de fijación del microprocesador?",
    [
        "a) La patilla proporciona energía al microprocesador.",
        "b) La patilla facilita la conexión de periféricos externos.",
        "c) La patilla permite la fijación sin necesidad de aplicar presión sobre el microprocesador.",
        "d) La patilla controla la temperatura del microprocesador.",
    ],
    "c"
),
(
    "¿Qué significa el acrónimo BIOS y cuál es su función principal en un sistema informático?",
    [
        "a) Basic Input Output System; controla el sistema operativo.",
        "b) Basic Input Output System; realiza funciones básicas de entrada/salida antes de que el sistema operativo tome el control.",
        "c) Basic Input Output Service; gestiona servicios básicos del sistema operativo.",
        "d) Basic Input Output Service; realiza operaciones avanzadas de entrada/salida.",
    ],
    "b"
),
(
    "¿Cuál es una de las funciones clave de la BIOS en relación con los componentes básicos del equipo?",
    [
        "a) Controlar el rendimiento del microprocesador.",
        "b) Realizar operaciones avanzadas de memoria.",
        "c) Identificar y proporcionar referencias iniciales de los componentes básicos al sistema operativo.",
        "d) Gestionar servicios de red del sistema operativo.",
    ],
    "c"
),
(
    "¿Por qué es importante tener precaución al realizar modificaciones en la BIOS y qué recomendación se da en caso de realizar cambios?",
    [
        "a) No es necesario tener precaución, ya que la BIOS es robusta.",
        "b) Es importante para mejorar el rendimiento del sistema operativo.",
        "c) Se recomienda realizar varios cambios a la vez para obtener resultados más rápidos.",
        "d) Es crucial tener precaución, ya que cambios incorrectos pueden causar mal funcionamiento, y se aconseja realizar un cambio a la vez y verificar el funcionamiento o, en caso de problemas, restablecer los parámetros por defecto.",
    ],
    "d"
),
(
    "¿Cuál es el riesgo principal al cambiar valores en la BIOS sin comprender completamente su significado?",
    [
        "a) Mejora del rendimiento del equipo.",
        "b) Posible incompatibilidad con el sistema operativo.",
        "c) No hay riesgos, ya que la BIOS se ajusta automáticamente.",
        "d) Mayor estabilidad del sistema.",
    ],
    "b"
),
(
    "¿Cuál es la recomendación principal en cuanto al procedimiento al realizar cambios en la BIOS?",
    [
        "a) Realizar múltiples cambios simultáneamente para ahorrar tiempo.",
        "b) Hacer solo un cambio a la vez y verificar el correcto funcionamiento.",
        "c) No es necesario comprobar el funcionamiento después de realizar cambios.",
        "d) Modificar varios parámetros al mismo tiempo para obtener mejores resultados.",
    ],
    "b"
),
(
    "¿Cuál es la precaución específica recomendada al modificar parámetros en la BIOS?",
    [
        "a) Modificar tantos parámetros como sea posible de una vez.",
        "b) No es necesario tener precaución, ya que la BIOS ajusta automáticamente los cambios.",
        "c) Cambiar varios parámetros al mismo tiempo para obtener mejores resultados.",
        "d) Evitar modificar muchos parámetros de manera simultánea.",
    ],
    "d"
),
(
    "En caso de problemas después de realizar modificaciones en la BIOS, ¿cuál es una posible solución recomendada?",
    [
        "a) Desconectar la alimentación del equipo.",
        "b) Ignorar los problemas y continuar con el uso normal del equipo.",
        "c) Realizar cambios adicionales para corregir los problemas.",
        "d) Ejecutar la opción de 'restablecer los parámetros por defecto' en la BIOS.",
    ],
    "d"
),
(
    "¿Cómo suele venir configurada por defecto la BIOS y cuándo se recomienda modificar dicha configuración?",
    [
        "a) Siempre viene desconfigurada por defecto.",
        "b) Viene configurada por defecto y generalmente no es necesario modificarla, salvo en casos excepcionales.",
        "c) Solo se configura por defecto en equipos antiguos.",
        "d) Debe ser modificada inmediatamente después de adquirir el equipo.",
    ],
    "b"
),
(
    "¿Qué modificación en la BIOS es comúnmente realizada para cambiar la secuencia de arranque de un equipo?",
    [
        "a) Cambiar la velocidad del procesador.",
        "b) Ajustar la resolución de pantalla.",
        "c) Modificar la configuración de red.",
        "d) Cambiar la secuencia de arranque.",
    ],
    "d"
),
(
    "¿Cuándo es necesario cambiar la secuencia de arranque en la BIOS?",
    [
        "a) Solo en casos de fallos en el sistema operativo.",
        "b) Cuando se quiere ajustar la velocidad de arranque.",
        "c) Siempre que se adquiere un nuevo equipo.",
        "d) Cuando se necesita arrancar el equipo desde otro dispositivo que no está contemplado previamente en la configuración de la BIOS, como un pendrive o un lector óptico.",
    ],
    "d"
),
(
    "¿Cuál es el propósito principal de cambiar la secuencia de arranque en la BIOS?",
    [
        "a) Aumentar la velocidad del sistema operativo.",
        "b) Mejorar la calidad de la pantalla de inicio.",
        "c) Es una acción innecesaria y no afecta al rendimiento del equipo.",
        "d) Especificar el orden en el que el sistema carga el sistema operativo, permitiendo arrancar desde diferentes dispositivos como un pendrive, lector óptico o la red.",
    ],
    "d"
),
(
    "¿Qué define la secuencia de arranque en la BIOS de un equipo?",
    [
        "a) La velocidad del sistema operativo.",
        "b) El idioma predeterminado del sistema operativo.",
        "c) El orden que el sistema sigue para cargar el sistema operativo.",
        "d) La cantidad de memoria RAM disponible.",
    ],
    "c"
),
(
    "¿Cuáles son algunas de las opciones comunes desde las cuales un equipo puede arrancar según la configuración de la secuencia de arranque en la BIOS?",
    [
        "a) Solo desde el disco duro.",
        "b) Exclusivamente desde un pendrive.",
        "c) Desde un lector óptico o desde la red.",
        "d) Únicamente desde la unidad SSD.",
    ],
    "c"
),
(
    "¿En qué situación es comúnmente necesario arrancar un equipo desde un lector óptico o desde la red, según la configuración de la secuencia de arranque en la BIOS?",
    [
        "a) Únicamente cuando se quiere mejorar el rendimiento del sistema operativo.",
        "b) En casos de fallos en el disco duro.",
        "c) Normalmente, cuando se desea instalar un sistema operativo.",
        "d) Nunca es necesario arrancar desde el lector óptico o desde la red.",
    ],
    "c"
),
(
    "¿Por qué es necesario cambiar la secuencia de arranque en la BIOS cuando se quiere instalar o reemplazar el sistema operativo?",
    [
        "a) Para ajustar la resolución de la pantalla.",
        "b) Como una práctica recomendada para mejorar el rendimiento del sistema operativo.",
        "c) Únicamente cuando se desea cambiar el idioma predeterminado del sistema operativo.",
        "d) Para permitir el arranque desde el medio (por ejemplo, un pendrive o un lector óptico) donde se encuentra el instalador del sistema operativo.",
    ],
    "d"
),
(
    "¿Cómo se puede acceder y modificar fácilmente la secuencia de arranque en muchas BIOS?",
    [
        "a) A través de un menú desplegable en el escritorio del sistema operativo.",
        "b) Mediante el Panel de Control del sistema operativo.",
        "c) Haciendo doble clic en el dispositivo deseado desde el explorador de archivos.",
        "d) Solo a través de herramientas especializadas de terceros.",
    ],
    "c"
),
(
    "¿Cuál es uno de los mensajes comunes que aparece durante el arranque para indicar la opción de acceder a la BIOS, y qué tecla suele utilizarse para ello?",
    [
        "a) 'Press Enter to Enter BIOS Setup', tecla 'Enter'.",
        "b) 'Press Del to Enter BIOS Setup', tecla 'Delete'.",
        "c) 'Press F2 to Enter BIOS Setup', tecla 'F2'.",
        "d) 'Press Ctrl to Enter BIOS Setup', tecla 'Ctrl'.",
    ],
    "b"
),
(
    "Durante el arranque de un ordenador, ¿qué mensaje suele aparecer para indicar cómo acceder a la BIOS y qué tecla se debe pulsar?",
    [
        "a) 'Loading Operating System...'",
        "b) 'Press Enter to Start'",
        "c) 'Press Del to Enter BIOS Setup', 'Press F2 to Enter BIOS Setup', ...",
        "d) No hay mensajes durante el arranque.",
    ],
    "c"
),
(
    "¿Por qué es importante actuar rápidamente cuando aparece el mensaje para acceder a la BIOS durante el arranque de un sistema?",
    [
        "a) Para evitar daños en el sistema operativo.",
        "b) No es importante actuar rápidamente; se puede acceder a la BIOS en cualquier momento durante el arranque.",
        "c) Porque los sistemas dan poco tiempo antes de continuar la secuencia de arranque.",
        "d) No hay necesidad de acceder a la BIOS durante el arranque.",
    ],
    "c"
),
(
    "Una vez dentro de la BIOS, ¿cuáles son las opciones comunes para seleccionar el dispositivo desde el cual arrancar el sistema?",
    [
        "a) No se puede seleccionar el dispositivo de arranque desde la BIOS.",
        "b) Solo se puede hacer doble clic sobre el dispositivo deseado.",
        "c) Se pueden hacer doble clic o modificar la secuencia de arranque.",
        "d) Solo se permite modificar la secuencia de arranque.",
    ],
    "c"
),
(
    "En las BIOS antiguas, ¿dónde podría aparecer la opción de configuración del arranque, como 'Boot', 'Advanced Setup' o 'Advanced Features'?",
    [
        "a) Nunca se incluye en las BIOS antiguas.",
        "b) Siempre se encuentra en la opción 'Boot'.",
        "c) Puede aparecer bajo la opción de menú 'Boot', 'Advanced Setup' o 'Advanced Features'.",
        "d) Exclusivamente bajo la opción 'Advanced Setup'.",
    ],
    "c"
),
(
    "¿Qué objetivo se persigue al modificar la configuración de prioridades en la BIOS, especialmente en relación con el arranque del sistema?",
    [
        "a) No hay necesidad de modificar las prioridades en la BIOS.",
        "b) Colocar todos los dispositivos en igual prioridad.",
        "c) Establecer como primera opción factible el dispositivo desde donde se desea arrancar.",
        "d) Mantener la configuración predeterminada de prioridades.",
    ],
    "c"
),
(
    "Después de realizar cambios en la BIOS y guardarlos, ¿qué sucede con la secuencia de arranque y desde dónde inicia el sistema?",
    [
        "a) La secuencia de arranque se reinicia automáticamente.",
        "b) No es necesario guardar cambios en la BIOS; el sistema arranca desde cualquier dispositivo al reiniciar.",
        "c) Se debe reiniciar manualmente la secuencia de arranque.",
        "d) Se sale de la BIOS continuando la secuencia de arranque y el sistema arranca desde el dispositivo elegido.",
    ],
    "d"
),
(
    "¿Por qué es importante tener en cuenta que las BIOS pueden ser diferentes unas de otras?",
    [
        "a) Todas las BIOS son idénticas, por lo que no es necesario considerar diferencias.",
        "b) Las diferencias entre las BIOS no afectan la configuración del sistema.",
        "c) Las opciones en las BIOS pueden diferir, por lo que es necesario elegir la opción correcta para cada caso.",
        "d) No es necesario adaptarse a las opciones específicas de cada BIOS.",
    ],
    "c"
),
(
    "¿Cuáles son dos de los fabricantes más destacados de BIOS en el mercado?",
    [
        "a) HP y Dell.",
        "b) ASUS y MSI.",
        "c) AMI (American Megatrends Incorporated) y AWARD-Phoenix.",
        "d) IBM y Lenovo.",
    ],
    "c"
),
(
    "A pesar de las diferencias en los menús según la marca, ¿cómo tiende a ser la similitud en el manejo y los parámetros de las BIOS?",
    [
        "a) Cada marca tiene un manejo y parámetros completamente únicos.",
        "b) No hay similitud en el manejo y parámetros entre las diferentes marcas de BIOS.",
        "c) Aunque los menús pueden ser distintos dependiendo de la marca, el manejo y los distintos parámetros suelen ser muy similares.",
        "d) Solo las BIOS de la misma marca comparten similitudes en manejo y parámetros.",
    ],
    "c"
),
(
    "¿Cómo afecta el conocimiento del funcionamiento de la BIOS a la capacidad de un técnico para modificar parámetros, incluso en BIOS de diferentes marcas?",
    [
        "a) No hay relación entre el conocimiento de la BIOS y la capacidad de modificar parámetros.",
        "b) Un técnico solo puede modificar parámetros en BIOS de la misma marca.",
        "c) Aunque el contenido de la BIOS de diferentes marcas sea distinto, un técnico que conoce el funcionamiento de la BIOS no debería tener problema para modificar los parámetros de cualquier BIOS.",
        "d) Un técnico solo puede modificar parámetros en BIOS de marcas específicas.",
    ],
    "c"
),
(
    "¿Cómo se describe mejor la naturaleza de la BIOS y dónde se almacenan sus datos?",
    [
        "a) La BIOS es un hardware y sus datos se almacenan en la memoria RAM.",
        "b) La BIOS es un software y sus datos se almacenan en una memoria flash EEPROM o memoria ROM de lectura y escritura cuyos datos almacenan en una memoria CMOS.",
        "c) La BIOS es un sistema operativo y sus datos se almacenan en el disco duro.",
        "d) La BIOS es un programa almacenado en una memoria CMOS.",
    ],
    "b"
),
(
    "¿Cómo se describe mejor la memoria CMOS en relación con su tipo y características?",
    [
        "a) La memoria CMOS es un tipo de memoria RAM alimentada por una pila, pero consume mucha energía.",
        "b) La memoria CMOS es un tipo de memoria ROM alimentada por una pila y consume poca energía.",
        "c) La memoria CMOS es un tipo de memoria flash EEPROM alimentada por una pila y consume poca energía.",
        "d) La memoria CMOS es un tipo de memoria RAM alimentada por una pila y consume muy poca energía.",
    ],
    "d"
),
(
    "¿Cuál es la función principal de la pila, por ejemplo, modelo CR-2032, que está alojada en la placa y alimenta la memoria CMOS?",
    [
        "a) Proporcionar energía a la CPU.",
        "b) Alimentar la memoria RAM.",
        "c) Alimentar la memoria flash EEPROM.",
        "d) Alimentar la memoria CMOS y mantener ajustes como la hora, y cuando se agota, el sistema muestra mensajes como 'CMOS Checksum Invalid' y pierde el ajuste de la hora.",
    ],
    "d"
),
(
    "¿Dónde se encuentra comúnmente la opción para restablecer los valores por defecto en cualquier BIOS del mercado?",
    [
        "a) La opción para restablecer los valores por defecto no está disponible en ninguna BIOS.",
        "b) Siempre se encuentra en la sección 'Advanced Settings'.",
        "c) Puede encontrarse en cualquier sección del menú de configuración de la BIOS.",
        "d) Se encuentra comúnmente dentro del menú de configuración y puede variar de una BIOS a otra.",
    ],
    "d"
),
(
    "En caso de no poder cargar los valores por defecto desde el menú de la BIOS debido a una contraseña, ¿cuáles son las opciones adicionales disponibles?",
    [
        "a) No hay opciones adicionales disponibles; la contraseña es irrompible.",
        "b) Puentear el jumper Clear CMOS o CLRCMOS y encender el equipo o quitar la pila de la BIOS durante unos 10 segundos.",
        "c) Quitar la memoria CMOS y reiniciar el sistema.",
        "d) Enviar la placa base a reparación para desbloquear la contraseña.",
    ],
    "b"
),
(
    "Cuando no se puede cargar los valores por defecto desde el menú de la BIOS debido a una contraseña, ¿cuál es una opción adicional para lograrlo?",
    [
        "a) Desmontar la placa base y reemplazar el jumper Clear CMOS.",
        "b) Ignorar la contraseña y continuar con la configuración actual.",
        "c) Puentear el jumper Clear CMOS y encender el equipo.",
        "d) Esperar a que la contraseña expire automáticamente.",
    ],
    "c"
),
(
    "¿Cuál es la segunda opción para cargar los valores por defecto en la BIOS cuando no se puede hacer desde el menú y hay una contraseña?",
    [
        "a) Enviar la placa base a reparación para desbloquear la contraseña.",
        "b) Ignorar la contraseña y continuar con la configuración actual.",
        "c) Quitar la pila de la BIOS durante aproximadamente 10 segundos y volverla a colocar.",
        "d) Desmontar la placa base y reemplazar la memoria CMOS.",
    ],
    "c"
),
(
    "¿Cómo afecta la ausencia de corriente a la memoria CMOS de la BIOS y qué resultado se obtiene cuando se restablecen los valores por defecto?",
    [
        "c) La memoria CMOS se daña sin corriente, y los valores por defecto no se restablecen.",
        "b) Sin corriente, la memoria CMOS retiene la información y no se restablecen los valores por defecto.",
        "a) Sin corriente, la memoria CMOS de la BIOS pierde información y se restablecen los valores por defecto.",
        "d) La memoria CMOS es independiente de la corriente y siempre mantiene la información.",
    ],
    "a"
),
(
    "¿Cuál es la precaución importante al retirar la pila de la BIOS?",
    [
        "a) Se puede utilizar cualquier objeto, ya que la pila es resistente.",
        "b) Utilizar solo objetos metálicos para evitar dañar la pila.",
        "c) Retirar la pila sin precauciones adicionales.",
        "d) Habrá que hacerlo con la capucha de un bolígrafo o algún utensilio de plástico, nunca con un destornillador u objeto metálico.",
    ],
    "d"
),
(
    "¿Cómo se define comúnmente el chipset en una placa base y qué indica el nombre clave asignado al chip principal?",
    [
        "a) El chipset es una parte externa a la placa base y no influye en su funcionamiento.",
        "b) El chipset es un solo microprocesador en la placa base sin funciones específicas.",
        "c) El chipset es un grupo de microprocesadores en la placa base, y su nombre clave (por ejemplo, H110, Z270, B250) indica la funcionalidad y tecnología que posee.",
        "d) El chipset es un componente opcional y no es esencial para el funcionamiento de la placa base.",
    ],
    "c"
),
(
    "¿Cuál es la función principal del chipset en una placa base?",
    [
        "a) Realizar funciones de conectividad con el exterior, como Bluetooth y USB.",
        "b) Proporcionar alimentación a los elementos del sistema informático.",
        "c) Gestionar la velocidad de la unidad SSD y la tarjeta gráfica.",
        "d) Comunicar los elementos de un sistema informático (unidad SSD, memoria, microprocesador, tarjeta gráfica, ...) y realizar funciones de conectividad con el exterior (Bluetooth, Ethernet, USB, ...).",
    ],
    "d"
),
(
    "¿Qué aspectos del sistema informático dependen del tipo de chipset en una placa base?",
    [
        "a) La marca del procesador.",
        "b) La capacidad de almacenamiento de la memoria.",
        "d) La frecuencia del FSB (Front Side Bus), el adaptador gráfico...",
        "c) El color del adaptador gráfico.",
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
    equivalencia =f (puntuacion / total_preguntas) * escala_maxima
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
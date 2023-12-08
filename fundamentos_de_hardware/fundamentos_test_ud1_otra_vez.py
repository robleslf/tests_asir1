import random

# Lista de preguntas y respuestas
preguntas = [
    (
    "¿Cuál es el enfoque lógico en el funcionamiento de un ordenador o sistema microinformático?",
    [
        "a) Coincide siempre con la organización física o comercial.",
        "b) Se basa en la historia y evolución del hardware.",
        "c) Está relacionado con el almacenamiento de programas en la UCP.",
        "d) Depende exclusivamente de la arquitectura física.",
    ],
    "c"
),
(
    "¿Cuál es el aspecto principal del funcionamiento de un ordenador o sistema microinformático desde el punto de vista lógico?",
    [
        "a) La coincidencia constante con la organización física o comercial.",
        "b) La relación directa con la historia y evolución del hardware.",
        "c) La independencia de la organización lógica con respecto a la organización física o comercial.",
        "d) La exclusiva dependencia de la arquitectura física.",
    ],
    "c"
),
(
    "¿Quién estableció en 1945 un nuevo modelo básico de arquitectura de computadoras, introduciendo la Unidad Central de Proceso (UCP) para el almacenamiento de programas?",
    [
        "a) Alan Turing",
        "b) John von Neumann",
        "c) Ada Lovelace",
        "d) Charles Babbage",
    ],
    "b"
),
(
    "Según John von Neumann, ¿cuáles son los principales componentes de un equipo o sistema informático?",
    [
        "a) Teclado, ratón y pantalla.",
        "b) CPU, GPU y RAM.",
        "c) Periféricos de entrada, CPU y periféricos de salida.",
        "d) Almacenamiento, sistema operativo y aplicaciones.",
    ],
    "c"
),
(
    "¿Cuál es un ejemplo de periférico que puede actuar tanto como periférico de entrada como de salida, según la nota proporcionada?",
    [
        "a) Teclado",
        "b) Ratón",
        "c) Pantallas táctiles",
        "d) Impresora",
    ],
    "c"
),
(
    "¿Cuáles son los componentes principales de una CPU (Central Process Unit), según la descripción proporcionada?",
    [
        "a) Solo una unidad de control.",
        "b) Solo una unidad aritmética.",
        "c) Una memoria y una unidad de control.",
        "d) Una memoria y un procesador con una unidad aritmética y una unidad de control.",
    ],
    "d"
),
(
    "¿Cuál es la función principal de la memoria en una CPU, según la descripción?",
    [
        "a) Ejecutar órdenes de programas.",
        "b) Realizar operaciones matemáticas y lógicas.",
        "c) Almacenar datos y programas.",
        "d) Controlar la entrada y salida de periféricos.",
    ],
    "c"
),
(
    "¿Cuál es la función principal del procesador en una CPU, según la descripción?",
    [
        "c) Almacenar datos y programas.",
        "b) Realizar operaciones matemáticas y lógicas.",
        "a) Ejecutar órdenes de programas y procesar información de periféricos de entrada.",
        "d) Controlar la entrada y salida de periféricos.",
    ],
    "a"
),
(
    "¿Cuáles son las principales componentes del procesador según la descripción proporcionada?",
    [
        "a) Solo la unidad de control.",
        "b) Solo la unidad aritmética.",
        "c) La unidad aritmética y la unidad de control.",
        "d) La memoria y la unidad de control.",
    ],
    "c"
),
(
    "¿Cuál es la función principal de la unidad aritmética en un procesador?",
    [
        "a) Almacenar datos y programas.",
        "b) Controlar la entrada y salida de periféricos.",
        "c) Realizar operaciones matemáticas y lógicas.",
        "d) Ejecutar órdenes de programas.",
    ],
    "c"
),
(
    "¿Cuál es el papel principal de la unidad de control en un procesador, según la descripción?",
    [
        "a) Realizar operaciones matemáticas y lógicas.",
        "b) Controlar la entrada y salida de periféricos.",
        "c) Ejecutar órdenes de programas.",
        "d) Ser el verdadero 'cerebro' del sistema.",
    ],
    "d"
),
(
    "¿Cuál es una característica principal de los microprocesadores CISC (Complex Instruction Set Computer), según la descripción proporcionada?",
    [
        "a) Utilización inicial.",
        "b) Juego de instrucciones reducido.",
        "c) Unidad de control muy rápida.",
        "d) Ejecución de instrucciones en un solo ciclo de reloj.",
    ],
    "a"
),
(
    "¿Cómo se describen las instrucciones de los microprocesadores CISC (Complex Instruction Set Computer), según la información proporcionada?",
    [
        "a) Instrucciones simples y básicas.",
        "b) Instrucciones complejas y muy potentes.",
        "c) Instrucciones limitadas y específicas.",
        "d) Instrucciones rápidas y eficientes.",
    ],
    "b"
),
(
    "Según la información proporcionada, ¿qué se menciona sobre la naturaleza de las instrucciones en los microprocesadores CISC?",
    [
        "a) Todas las instrucciones son esenciales y no se pueden simplificar.",
        "b) Muchas de ellas se pueden realizar de manera más sencilla con otras instrucciones.",
        "c) Cada instrucción es única y no se puede reducir.",
        "d) Las instrucciones son simples y directas, sin redundancias.",
    ],
    "b"
),
(
    "¿Qué característica destacada se menciona sobre la creación de instrucciones en los microprocesadores CISC?",
    [
        "a) Todas las instrucciones están predefinidas y no se pueden modificar.",
        "b) La creación de nuevas instrucciones es imposible.",
        "c) Se pueden crear nuevas instrucciones según sea necesario.",
        "d) Las instrucciones son estáticas y no se pueden cambiar.",
    ],
    "c"
),
(
    "En el contexto histórico de los microprocesadores CISC, ¿cómo se describe la relación entre la velocidad de la memoria y la unidad de control?",
    [
        "a) La memoria era más rápida que la unidad de control.",
        "b) La velocidad de la memoria y la unidad de control era la misma.",
        "c) La memoria era mucho más lenta que la unidad de control.",
        "d) La memoria y la unidad de control eran independientes en velocidad.",
    ],
    "c"
),
(
    "En el contexto histórico de los microprocesadores CISC, ¿cómo se describe la ejecución de operaciones en términos de ciclos de reloj?",
    [
        "a) Cada operación requería múltiples ciclos de reloj.",
        "b) Todas las operaciones se podían realizar en un solo ciclo de reloj.",
        "c) Los ciclos de reloj eran irrelevantes para la ejecución de operaciones.",
        "d) Solo las operaciones complejas necesitaban más de un ciclo de reloj.",
    ],
    "b"
),
(
    "Con el tiempo, ¿qué sucedió con la velocidad de la memoria en comparación con la unidad de control en los microprocesadores CISC?",
    [
        "a) Permaneció constante.",
        "b) La velocidad de la memoria siempre fue más lenta.",
        "c) La unidad de control siempre fue más lenta.",
        "d) La velocidad de la memoria aumentó e incluso superó a la de la unidad de control.",
    ],
    "d"
),
(
    "¿Cómo afectaba el gran número y la complejidad de instrucciones en los microprocesadores CISC a la velocidad de las CPU, según la información proporcionada?",
    [
        "a) Aceleraba la velocidad de las CPU.",
        "b) No tenía impacto en la velocidad de las CPU.",
        "c) Hacía que las CPU fueran lentas.",
        "d) Facilitaba la ejecución eficiente de instrucciones.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿qué evento dio lugar al paso de la arquitectura CISC a RISC?",
    [
        "a) La mejora continua en la velocidad de la memoria.",
        "b) La simplificación de las instrucciones CISC.",
        "c) El aumento en la complejidad de las instrucciones CISC.",
        "d) Los problemas de velocidad causados por el gran número y complejidad de instrucciones CISC.",
    ],
    "d"
),
(
    "¿Cuál es una característica principal de los microprocesadores RISC (Reduced Instruction Set Computer), según la descripción proporcionada?",
    [
        "a) Juego de instrucciones muy amplio.",
        "b) Unidad de control lenta que requiere múltiples ciclos de reloj por instrucción.",
        "c) Juego de instrucciones muy reducido.",
        "d) Unidad de control que ejecuta múltiples instrucciones en un solo ciclo de reloj.",
    ],
    "c"
),
(
    "¿Cuál es una característica destacada de la unidad de control en los microprocesadores RISC, según la descripción?",
    [
        "a) Requiere múltiples ciclos de reloj por instrucción.",
        "b) Ejecuta instrucciones en varios ciclos de reloj.",
        "c) Es lenta y tiene un juego de instrucciones complejo.",
        "d) Puede ejecutar una instrucción en un solo ciclo de reloj.",
    ],
    "d"
),
(
    "¿Cuál es una diferencia clave entre las arquitecturas RISC y CISC, según la información proporcionada?",
    [
        "a) Las instrucciones en RISC son más complejas que en CISC.",
        "b) La velocidad total del sistema es mayor en CISC que en RISC.",
        "c) Una instrucción CISC puede transformarse en varias RISC, y aún así, la velocidad total del sistema es mayor en RISC.",
        "d) La mayoría de las instrucciones en RISC son complejas, mientras que en CISC son simples.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cuál es una característica común de la mayoría de las instrucciones en una CPU, en contraste entre RISC y CISC?",
    [
        "a) La mayoría de las instrucciones en RISC son complejas.",
        "b) La mayoría de las instrucciones en CISC son complejas.",
        "c) La mayoría de las instrucciones en ambas arquitecturas son complejas.",
        "d) La mayoría de las instrucciones que se ejecutan en una CPU son simples y no complejas.",
    ],
    "d"
),
(
    "¿Cómo se describe la memoria que alberga la CPU, según la información proporcionada?",
    [
        "c) Está formada por instrucciones complejas.",
        "b) Está compuesta por una unidad de control rápida.",
        "a) Está formada por una serie de celdillas o biestables con 2 estados (0 ó 1).",
        "d) Está compuesta por instrucciones simples y directas.",
    ],
    "a"
),
(
    "¿Cuál es la función principal de las celdillas o biestables en la memoria de la CPU, según la información proporcionada?",
    [
        "a) Almacenar instrucciones complejas.",
        "b) Almacenar instrucciones simples y directas.",
        "c) Albergar múltiples bits de información.",
        "d) Almacenar un bit, siendo el elemento básico de información.",
    ],
    "d"
),
(
    "Según la información proporcionada, ¿cuáles son los dos valores posibles que pueden tener los bits en la memoria de la CPU?",
    [
        "a) 0 y 2.",
        "b) 1 y 3.",
        "c) 0 y 1: Ausencia o presencia de energía.",
        "d) Ninguna de las anteriores.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cómo se accede a un conjunto de celdillas o biestables en la memoria de la CPU?",
    [
        "a) A través de instrucciones complejas.",
        "b) Directamente desde la unidad de control.",
        "c) Mediante un conjunto de direcciones.",
        "d) Accediendo individualmente a cada celdilla.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cuáles son los modos de acceso posibles a la memoria en la CPU?",
    [
        "a) Solo en modo lectura.",
        "b) Solo en modo escritura.",
        "c) Accesos solo directos desde la unidad de control.",
        "d) Accesos en modo lectura y escritura.",
    ],
    "d"
),
(
    "¿Cuál es la función principal de las celdillas o biestables en la memoria de la CPU, según la información proporcionada?",
    [
        "a) Solo almacenan datos.",
        "b) Solo almacenan instrucciones.",
        "c) Almacenan tanto datos como instrucciones de la máquina.",
        "d) No tienen una función específica.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cómo se agrupan las instrucciones en la CPU?",
    [
        "a) Las instrucciones no se agrupan.",
        "b) Se agrupan por la velocidad de ejecución.",
        "c) Se agrupan por la complejidad.",
        "d) Se agrupan en programas.",
    ],
    "d"
),
(
    "¿Cómo se describe un programa, según la información proporcionada?",
    [
        "a) Un programa es un conjunto de instrucciones desordenadas.",
        "b) Un programa se organiza por la complejidad de las instrucciones.",
        "c) Un programa es un conjunto de instrucciones almacenadas de forma secuencial.",
        "d) Un programa se ejecuta simultáneamente en múltiples ciclos de reloj.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿dónde están almacenados los programas?",
    [
        "a) En la unidad de control.",
        "b) En la memoria secundaria.",
        "c) En la memoria caché.",
        "d) En la memoria principal.",
    ],
    "d"
),
(
    "Según la información proporcionada, ¿dónde residen los datos de los programas y cómo se accede a ellos?",
    [
        "a) Los datos residen en la memoria secundaria y se accede directamente desde la unidad de control.",
        "b) Los datos residen en la memoria caché y se accede directamente desde la unidad aritmética.",
        "c) Los datos residen en la memoria principal y se accede cuando sea necesario, ya sea en modo escritura o lectura.",
        "d) Los datos residen en la unidad de control y se accede simultáneamente con la ejecución de instrucciones.",
    ],
    "c"
),
(
    "¿Cómo se denomina comúnmente la memoria que se describe como 'Random Access Memory' en inglés y 'memoria de acceso aleatorio' en castellano?",
    [
        "a) ROM (Read-Only Memory).",
        "b) Flash Memory.",
        "c) Cache Memory.",
        "d) RAM (Random Access Memory).",
    ],
    "d"
),
(
    "Según la información proporcionada, ¿cómo se describe la estructura de la memoria RAM?",
    [
        "a) Consiste en un único bloque continuo de almacenamiento.",
        "b) Está formada por clusters interconectados.",
        "c) Se compone de una serie de celdas.",
        "d) Está organizada en capas jerárquicas.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cómo se describen las características de las celdas en la memoria RAM?",
    [
        "a) Cada celda contiene instrucciones complejas.",
        "b) Cada celda almacena datos en formato de texto.",
        "c) Cada celda contiene una serie de bits o celdillas.",
        "d) Cada celda almacena únicamente el valor '1'.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿qué valores puede almacenar cada bit en una celda de la memoria RAM?",
    [
        "a) Puede almacenar los valores '0' y '1'.",
        "b) Solo el valor '1'.",
        "c) Puede almacenar el valor '0', '1', o nada.",
        "d) Solo valores numéricos enteros.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cuál es la relación entre celdas, biestables y bytes en la memoria RAM?",
    [
        "a) 1 celda = 1 byte = 1 bit.",
        "b) 1 celda = 8 bytes = 1 bit.",
        "c) 1 celda = 1 byte = 8 bits.",
        "d) 1 celda = 1 bit = 1 byte.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cómo se describe la ubicación de las celdas en la memoria RAM?",
    [
        "c) Las celdas no tienen una dirección específica.",
        "b) Cada celda tiene múltiples direcciones.",
        "a) Tienen una dirección determinada.",
        "d) La dirección de las celdas es variable.",
    ],
    "a"
),
(
    "Según la información proporcionada, ¿cuál es la unidad mínima de memoria que puede leerse o escribirse de forma completa?",
    [
        "a) El bit.",
        "b) La palabra de memoria.",
        "c) El biestable.",
        "d) La celda.",
    ],
    "d"
),
(
    "Según la información proporcionada, ¿cómo se describe el tiempo que tarda el sistema en leer o escribir en las celdas de la memoria?",
    [
        "a) El tiempo varía para cada celda.",
        "b) El tiempo es diferente para lectura y escritura.",
        "c) El tiempo es el mismo para cualquiera de las celdas.",
        "d) El tiempo es más rápido para las celdas en la memoria secundaria.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cuántos bits constituyen un byte en cada celda de la memoria RAM?",
    [
        "a) 1 bit.",
        "b) 4 bits.",
        "c) 8 bits.",
        "d) 16 bits.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cómo se describe la cantidad de celdas y direcciones en esta memoria?",
    [
        "a) La memoria tiene N celdas y 2N direcciones.",
        "c) La memoria tiene 2N celdas y N direcciones.",
        "b) La memoria tiene 2N-1 celdas y cada una con una dirección en memoria.",
        "d) La memoria tiene N-1 celdas y 2N direcciones.",
    ],
    "b"
),
(
    "Según la información proporcionada, ¿cómo se expresa la dirección de una celda de memoria y qué indica?",
    [
        "a) Se expresa con un número decimal e indica el contenido de la celda.",
        "b) Se expresa con un número hexadecimal e indica la posición en la memoria.",
        "c) Se expresa con un número binario e indica en qué lugar se encuentran los datos.",
        "d) La dirección de una celda no se expresa numéricamente.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cómo se describe el contenido de una celda de memoria?",
    [
        "a) Es siempre un número decimal.",
        "b) Es una cadena de texto que indica la función de la celda.",
        "c) Se trata del contenido que hay en una dirección de memoria.",
        "d) La memoria no tiene un contenido específico.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cómo se diferencia la dirección de una celda de su contenido?",
    [
        "a) La dirección y el contenido son siempre iguales.",
        "b) La dirección se expresa en binario y el contenido en decimal.",
        "c) La dirección se expresa en hexadecimal y el contenido en binario.",
        "d) No hay una relación directa entre la dirección de una celda y su contenido.",
    ],
    "d"
),
(
    "En el ejemplo dado de la diapositiva 11, ¿cómo se expresa la dirección de la segunda celda y cuál es su contenido?",
    [
        "a) Dirección: 1, Contenido: 1 bit.",
        "b) Dirección: 0000000000000001, Contenido: 1 byte / 8 bits.",
        "c) Dirección: 2, Contenido: 8 bytes / 64 bits.",
        "d) Dirección: 0000000000000010, Contenido: 2 bytes / 16 bits.",
    ],
    "b"
),
(
    "Según la información proporcionada, ¿cómo afecta el número de bits utilizados para direccionar una celda de memoria a su capacidad?",
    [
        "a) No hay relación entre el número de bits y la capacidad de memoria.",
        "b) Cuantos más bits se utilicen, menor será la capacidad de memoria.",
        "c) Cuantos más bits se utilicen, mayor será la capacidad de memoria.",
        "d) El número de bits no afecta a la capacidad de memoria.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cómo se relaciona el número de bits en una dirección de memoria con el espacio de direcciones disponible?",
    [
        "a) Cuantos más bits, menor es el espacio de direcciones.",
        "b) Cuantos más bits, mayor es el espacio de direcciones.",
        "c) No hay relación entre el número de bits y el espacio de direcciones.",
        "d) El espacio de direcciones siempre es igual a 2N.",
    ],
    "b"
),
(
    "Según la información proporcionada, ¿cómo se describe el espacio de direcciones con una dirección de memoria de N bits?",
    [
        "a) El espacio de direcciones es siempre igual a 2N.",
        "b) Cuantos más bits, menor es el espacio de direcciones.",
        "c) Cuantos más bits, mayor es el espacio de direcciones.",
        "d) El espacio de direcciones siempre es igual a 2^(2N).",
    ],
    "a"
),
(
    "Según la información proporcionada, ¿cómo se define el tiempo de acceso a la memoria y en qué unidad se suele medir?",
    [
        "a) El tiempo de acceso es el tiempo que tarda la CPU en realizar operaciones de memoria.",
        "b) El tiempo de acceso es el tiempo que tarda la memoria en hacer operaciones de lectura o escritura.",
        "c) El tiempo de acceso se mide en milisegundos.",
        "d) El tiempo de acceso es el tiempo que tarda la memoria en procesar instrucciones de la CPU.",
    ],
    "b"
),
(
    "Además, según la información proporcionada, ¿en qué unidad se suele medir el tiempo de acceso a la memoria?",
    [
        "a) Milisegundos.",
        "b) Microsegundos.",
        "c) Nanosegundos.",
        "d) Segundos.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cuánto representa un nanosegundo en términos de segundos?",
    [
        "a) 0.000001 segundos.",
        "b) 0.000000001 segundos.",
        "c) 0.00000001 segundos.",
        "d) 0.0000001 segundos.",
    ],
    "b"
),
(
    "En los discos duros, según la información proporcionada, ¿cómo se mide el tiempo de acceso y en qué unidad?",
    [
        "a) Se mide en nanosegundos.",
        "b) Se mide en milisegundos.",
        "c) Se mide en microsegundos.",
        "d) Se mide en picosegundos.",
    ],
    "b"
),
(
    "En los discos duros, según la información proporcionada, ¿cómo se mide el tiempo de acceso y en qué unidad?",
    [
        "a) Se mide en nanosegundos.",
        "b) Se mide en milisegundos.",
        "c) Se mide en microsegundos.",
        "d) Se mide en picosegundos.",
    ],
    "b"
),
(
    "Según la información proporcionada, ¿cuáles son las dos operaciones principales que se pueden realizar con la memoria?",
    [
        "a) Leer y escribir.",
        "b) Sumar y restar.",
        "c) Copiar y pegar.",
        "d) Borrar y mover.",
    ],
    "a"
),
(
    "Según la información proporcionada, ¿qué implica la operación de lectura en la memoria?",
    [
        "a) Modificar el valor de una celda de memoria.",
        "b) Obtener el contenido de una celda concreta.",
        "c) Escribir en una dirección de memoria.",
        "d) Realizar operaciones matemáticas con datos de la memoria.",
    ],
    "b"
),
(
    "Según la información proporcionada, ¿qué característica tiene la operación de lectura en relación con el valor de la celda?",
    [
        "a) La lectura siempre modifica el valor de la celda.",
        "b) La lectura no afecta el valor de la celda, que permanece inalterado.",
        "c) La lectura duplica el valor de la celda.",
        "d) La lectura borra el contenido de la celda.",
    ],
    "b"
),
(
    "Según la información proporcionada, ¿qué implica la operación de almacenamiento en la memoria?",
    [
        "a) Obtener el contenido de una celda concreta.",
        "b) Modificar el valor de una celda de memoria.",
        "c) Realizar operaciones matemáticas con datos de la memoria.",
        "d) Duplicar el valor de la celda de memoria.",
    ],
    "b"
),
(
    "Según la información proporcionada, ¿cómo se describe la operación de almacenamiento en relación con el contenido de un registro y una celda concreta?",
    [
        "a) La operación de almacenamiento no está relacionada con registros.",
        "b) La operación de almacenamiento duplica el contenido de un registro.",
        "c) La operación de almacenamiento consiste en volcar el contenido de un registro en una celda concreta.",
        "d) La operación de almacenamiento borra el contenido de un registro.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cómo afecta la operación de escritura al valor de la celda en memoria?",
    [
        "a) La escritura no tiene ningún efecto en el valor de la celda.",
        "b) La escritura duplica el valor de la celda.",
        "c) La escritura modifica el valor de la celda.",
        "d) La escritura solo borra el contenido de la celda.",
    ],
    "c"
),
(
    "¿Cómo funciona la operación de lectura -dirección-?",
    [
        "a) Se decodifica la dirección, se carga la dirección en el registro de direcciones y se copia el contenido de la celda de memoria en el registro de datos.",
        "b) Se copia el contenido de la celda de memoria en el registro de datos, se carga la dirección en el registro de direcciones y se decodifica la dirección.",
        "d) Se carga la dirección en el registro de direcciones, se decodifica la dirección y se copia el contenido de la celda de memoria en el registro de datos.",
        "c) Se carga la dirección en el registro de direcciones, se copia el contenido de la celda de memoria en el registro de datos y se decodifica la dirección.",
    ],
    "d"
),
(
    "¿Cómo funciona la operación de escritura -dirección, valor-?",
    [
        "a) Se decodifica la dirección, se carga la dirección en el registro de direcciones, se carga el valor en el registro de datos y se copia el contenido del registro de datos en la celda de memoria seleccionada.",
        "b) Se copia el contenido del registro de datos en la celda de memoria seleccionada, se carga la dirección en el registro de direcciones, se carga el valor en el registro de datos y se decodifica la dirección.",
        "c) Se carga la dirección en el registro de direcciones, se carga el valor en el registro de datos, se decodifica la dirección y se copia el contenido del registro de datos en la celda de memoria seleccionada.",
        "d) Se carga la dirección en el registro de direcciones, se decodifica la dirección, se carga el valor en el registro de datos y se copia el contenido del registro de datos en la celda de memoria seleccionada.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cuál es la función principal del subsistema de entrada/salida en un sistema informático?",
    [
        "a) Controlar las operaciones de la CPU.",
        "b) Gestionar el sistema de memoria.",
        "c) Permitir al sistema comunicarse con dispositivos externos como pantallas, teclados e impresoras.",
        "d) Realizar operaciones matemáticas.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿qué función realiza el subsistema de entrada/salida en relación con los dispositivos externos?",
    [
        "a) Realizar operaciones matemáticas con dispositivos externos.",
        "b) Controlar las operaciones de la CPU.",
        "c) Gestionar el sistema de memoria.",
        "d) Controlar los dispositivos que permiten al sistema comunicarse con el exterior, como pantalla, teclado, impresora y ratón.",
    ],
    "d"
),
(
    "Según la información proporcionada, ¿qué función cumple el subsistema de entrada/salida en relación con el almacenamiento de información en dispositivos secundarios como discos duros?",
    [
        "a) Controlar las operaciones de la CPU en dispositivos de almacenamiento secundario.",
        "b) Realizar operaciones matemáticas en dispositivos de almacenamiento secundario.",
        "c) Gestionar el sistema de memoria para dispositivos de almacenamiento secundario.",
        "d) Permitir al sistema almacenar información en dispositivos de almacenamiento secundario como discos duros.",
    ],
    "d"
),
(
    "¿Cuál es la función principal de la ALU (Unidad Aritmético-Lógica) en un sistema informático?",
    [
        "a) Gestionar el sistema de memoria.",
        "b) Controlar dispositivos de entrada/salida.",
        "c) Realizar operaciones aritméticas y lógicas como sumas, restas, comparaciones y operaciones lógicas.",
        "d) Decodificar direcciones de memoria.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cómo está estructurada la ALU (Unidad Aritmético-Lógica)?",
    [
        "a) Solo consiste en un conjunto de registros que almacenan resultados intermedios.",
        "c) Consiste únicamente en un conjunto de circuitos para realizar operaciones.",
        "b) Está compuesta por un conjunto de circuitos para realizar operaciones y una serie de registros que almacenan resultados intermedios.",
        "d) Su estructura se basa en la gestión del sistema de memoria.",
    ],
    "b"
),
(
    "Según la información proporcionada, ¿por qué la ALU (Unidad Aritmético-Lógica) necesita un BUS?",
    [
        "a) Para gestionar el sistema de memoria.",
        "b) Para realizar operaciones aritméticas y lógicas.",
        "c) Únicamente para almacenar resultados intermedios en los registros.",
        "d) Para interconectar los registros con la circuitería que realiza las operaciones.",
    ],
    "d"
),
(
    "¿Cuántos operandos puede tomar la ALU (Unidad Aritmético-Lógica) y qué tipo de operaciones puede realizar?",
    [
        "a) Toma un único operando y realiza operaciones aritméticas únicamente.",
        "b) Toma hasta dos operandos y realiza operaciones aritméticas y lógicas.",
        "c) Puede tomar operandos ilimitados y realiza operaciones aritméticas y lógicas.",
        "d) No puede procesar operandos, solo realiza operaciones de memoria.",
    ],
    "b"
),
(
    "Según la información proporcionada, ¿dónde suele almacenar la ALU (Unidad Aritmético-Lógica) el resultado de las operaciones?",
    [
        "a) En una memoria secundaria.",
        "b) En un registro llamado acumulador (ACC).",
        "c) En un conjunto de registros intermedios.",
        "d) No almacena resultados, solo realiza operaciones en tiempo real.",
    ],
    "b"
),
(
    "Según la información proporcionada, ¿cuál es la función principal de la Unidad de Control en un sistema informático?",
    [
        "a) Realizar operaciones aritméticas y lógicas.",
        "b) Gestionar el sistema de memoria.",
        "c) Almacenar resultados en registros.",
        "d) Ejecutar, una a una, las instrucciones de los programas almacenados en memoria.",
    ],
    "d"
),
(
    "Según la información proporcionada, ¿cómo se define un programa en el contexto de la Unidad de Control?",
    [
        "a) Como un conjunto de operaciones aritméticas.",
        "b) Como un conjunto de registros de memoria.",
        "c) Como un conjunto de instrucciones almacenadas en memoria.",
        "d) Como un conjunto de datos procesados por la ALU.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cómo se denominan las instrucciones que están en binario y son entendidas por la máquina?",
    [
        "a) Instrucciones de bajo nivel.",
        "b) Instrucciones de ensamblador.",
        "c) Instrucciones máquina.",
        "d) Instrucciones de alto nivel.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cuál es el papel principal de la Unidad de Control en relación con las instrucciones?",
    [
        "a) Almacenar instrucciones en memoria.",
        "b) Ejecutar operaciones aritméticas.",
        "c) Gestionar registros de memoria.",
        "d) Ir ejecutando, una a una, las instrucciones almacenadas en memoria.",
    ],
    "d"
),
(
    "¿Cuáles son los pasos que la Unidad de Control sigue para ejecutar una instrucción, según la información proporcionada?",
    [
        "a) 1. Ejecutar la instrucción, 2. Leer la instrucción de memoria, 3. Decodificarla., 4. Continuar ejecutando instrucciones hasta que se encuentre con una instrucción de fin.",
        "b) 1. Leer la instrucción de memoria, 2. Decodificarla, 3. Ejecutarla., 4. Continuar ejecutando instrucciones hasta que se encuentre con una instrucción de fin.",
        "c) 1. Decodificarla, 2. Ejecutarla, 3. Leer la instrucción de memoria., 4. Continuar ejecutando instrucciones hasta que se encuentre con una instrucción de fin.",
        "d) 1. Ejecutarla, 2. Decodificarla, 3. Leer la instrucción de memoria., 4. Continuar ejecutando instrucciones hasta que se encuentre con una instrucción de fin.",
    ],
    "b"
),
(
    "Según la información proporcionada, ¿a qué componentes la Unidad de Control envía señales durante la ejecución de instrucciones?",
    [
        "a) Solo a la memoria.",
        "b) Solo a la ALU (Unidad Aritmético-Lógica).",
        "c) A la ALU, la memoria y el subsistema de entrada/salida.",
        "d) A la memoria y al subsistema de entrada/salida.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cómo se compone una instrucción en lenguaje máquina o binaria?",
    [
        "a) Un solo campo que contiene el código de operación.",
        "b) Dos campos: el código de operación y los valores o direcciones de memoria.",
        "c) Tres campos: el código de operación, los valores y las direcciones de memoria.",
        "d) Cuatro campos: el código de operación, los valores, las direcciones de memoria y la descripción de la operación.",
    ],
    "b"
),
(
    "Según la información proporcionada, ¿cuál es una de las razones clave para el éxito de la informática móvil?",
    [
        "a) La conexión a plataformas en la nube.",
        "b) La mejora en la productividad.",
        "c) La potencia de los microprocesadores (SoC) para pequeños dispositivos.",
        "d) La adopción de la arquitectura x86 desde 1978.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿qué aspectos contribuyen a hacer de la informática móvil una nueva forma de trabajo?",
    [
        "a) La potencia de cálculo y la adopción de la arquitectura x86.",
        "b) La mejora en la productividad y la conexión a plataformas en la nube.",
        "c) La potencia de cálculo y la irrupción de smartphones y tabletas.",
        "d) La adopción de la arquitectura ARM y la mejora en el servicio al cliente.",
    ],
    "b"
),
(
    "Según la información proporcionada, ¿cuáles son algunos de los beneficios de la informática móvil?",
    [
        "a) Aumento de la potencia de cálculo y mejora en la conexión a plataformas en la nube.",
        "b) Mejora en la productividad y adopción de la arquitectura x86.",
        "c) Aumento de la eficiencia y mejora en el servicio al cliente.",
        "d) Adopción de la arquitectura ARM y mayor capacidad de almacenamiento.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cuál es un factor decisivo para el éxito de la informática móvil?",
    [
        "a) La adopción de la arquitectura x86 en dispositivos móviles.",
        "b) La conectividad a plataformas en la nube.",
        "c) La potencia de los nuevos microprocesadores (SoC) para pequeños dispositivos.",
        "d) La disponibilidad de smartphones y tabletas.",
    ],
    "c"
),
(
    "Según la información proporcionada, ¿cuál ha sido un cambio significativo en la arquitectura de microprocesadores debido a la irrupción de smartphones y tabletas?",
    [
        "a) La continuación de la arquitectura x86 en dispositivos móviles.",
        "b) El aumento en la complejidad de la arquitectura x86.",
        "c) La adopción masiva de la arquitectura ARM en dispositivos móviles.",
        "d) El uso exclusivo de microprocesadores CISC en smartphones y tabletas.",
    ],
    "c"
),
(
    "¿Cuál fue uno de los objetivos principales del diseño inicial de la arquitectura ARM?",
    [
        "c) Priorizar la potencia de cálculo y velocidad.",
        "b) Establecer una arquitectura exclusiva para dispositivos de alta capacidad de procesamiento.",
        "a) Centrarse en dispositivos de muy poca capacidad de procesamiento y bajo consumo.",
        "d) Competir directamente con la arquitectura x86 en términos de rendimiento.",
    ],
    "a"
),
(
    "Según la información proporcionada, ¿qué ventaja ofrece la arquitectura ARM en comparación con x86 en términos de funcionalidades adicionales?",
    [
        "a) La arquitectura ARM se centra exclusivamente en el procesamiento de datos.",
        "b) La arquitectura x86 es más eficiente en el procesamiento gráfico.",
        "c) La arquitectura ARM permite a los microprocesadores gestionar características adicionales como bluetooth, entrada/salida y procesamiento gráfico.",
        "d) La arquitectura x86 es más eficaz en el manejo de funciones de entrada/salida.",
    ],
    "c"
),
(
    "¿Cuál de las siguientes afirmaciones es correcta sobre ARM según la información proporcionada?",
    [
        "a) ARM es una empresa independiente que no está vinculada a ninguna corporación.",
        "b) ARM fue adquirida por NVIDIA en septiembre de 2020 por 40.000 millones de dólares.",
        "c) ARM es actualmente propiedad de Intel.",
        "d) La adquisición de ARM por parte de NVIDIA no ha tenido lugar.",
    ],
    "b"
),
(
    "Según la información proporcionada, ¿en qué tipo de dispositivos se puede encontrar actualmente la arquitectura ARM?",
    [
        "a) Exclusivamente en ordenadores de alta potencia.",
        "b) Solo en dispositivos de almacenamiento secundario.",
        "d) Principalmente en microprocesadores de menor tamaño y bajo consumo, como los de dispositivos de electrónica portátil e integrada.",
        "c) Únicamente en dispositivos de realidad virtual.",
    ],
    "d"
),
(
    "¿Dónde se puede encontrar actualmente la arquitectura ARM según la información proporcionada?",
    [
        "a) Exclusivamente en dispositivos de realidad virtual.",
        "b) Principalmente en microprocesadores de menor tamaño y bajo consumo, como los de dispositivos de electrónica portátil e integrada.",
        "c) Únicamente en ordenadores de alta potencia.",
        "d) Solo en dispositivos de almacenamiento secundario.",
    ],
    "b"
),
(
    "¿Cuáles son algunas de las características de la arquitectura ARM según la información proporcionada?",
    [
        "a) Se encuentra exclusivamente en dispositivos de alta potencia.",
        "b) Está presente solo en dispositivos de almacenamiento secundario.",
        "c) Se encuentra en microprocesadores de menor tamaño y bajo consumo, con un coste reducido.",
        "d) Únicamente se utiliza en ordenadores de escritorio.",
    ],
    "c"
),
(
    "¿Cuál es uno de los beneficios de la arquitectura ARM según la información proporcionada?",
    [
        "a) Se destaca por su alta potencia de procesamiento.",
        "b) Está diseñada exclusivamente para aplicaciones de alto rendimiento.",
        "c) Es ideal para aplicaciones que no requieren mucha potencia.",
        "d) Solo se utiliza en dispositivos de escritorio.",
    ],
    "c"
),
(
    "¿Qué tipo de arquitectura utiliza el microprocesador de los iPhones (AX), según la información proporcionada?",
    [
        "a) x86",
        "b) ARM",
        "c) RISC",
        "d) CISC",
    ],
    "b"
),
(
    "¿Cuál es la arquitectura comúnmente utilizada en la mayoría de los microprocesadores de los móviles Android?",
    [
        "a) x86",
        "b) ARM",
        "c) RISC",
        "d) CISC",
    ],
    "b"
),
(
    "¿Cuál es uno de los fabricantes de procesadores comúnmente presentes en los dispositivos móviles, incluyendo muchos de los móviles Android?",
    [
        "a) Konami",
        "b) Qualcomm",
        "c) Kellogs",
        "d) SEGA",
    ],
    "b"
),
(
    "¿En qué tipo de dispositivos se está empezando a utilizar la arquitectura ARM, incluyendo algunos ordenadores portátiles que ofrecen un rendimiento notable y una duración de batería impresionante?",
    [
        "a) Solo en smartphones",
        "b) Exclusivamente en dispositivos de electrónica portátil",
        "c) Únicamente en sistemas de entretenimiento",
        "d) También en ordenadores personales",
    ],
    "d"
),
(
    "¿Cuál es una de las ventajas destacadas de los ordenadores portátiles con CPU de arquitectura ARM, cuando se combinan con un sistema operativo adecuado?",
    [
        "a) Rendimiento excepcional en tareas de alta demanda",
        "b) Mayor consumo de energía en comparación con otras arquitecturas",
        "c) Duración de la batería impresionante",
        "d) Dependencia total de la conexión a la nube",
    ],
    "c"
),
(
    "¿Por qué los procesadores con arquitectura ARM son a menudo considerados ideales para ordenadores orientados al mundo ofimático?",
    [
        "a) Mayor complejidad y potencia de cálculo",
        "b) Baja duración de la batería",
        "c) Elevado consumo de energía",
        "d) Simplicidad y eficiencia energética",
    ],
    "d"
),
(
    "¿Cuál fue la principal razón para que Apple migrara de procesadores Intel x86 a sus propios procesadores Apple Silicon basados en la arquitectura ARM?",
    [
        "a) Mayor potencia de cálculo de los procesadores ARM",
        "b) Colaboración estratégica con ARM",
        "c) Mejor eficiencia energética y rendimiento en tareas específicas",
        "d) Precio más bajo de los procesadores ARM",
    ],
    "c"
),
(
    "¿Cuál es una de las principales ventajas de la arquitectura ARM en dispositivos móviles?",
    [
        "a) Mayor potencia de cálculo",
        "b) Mayor consumo de energía",
        "c) Tamaño más grande",
        "d) Bajo consumo de energía y tamaño reducido",
    ],
    "d"
),
(
    "¿En qué tipo de dispositivos cotidianos se utilizan microprocesadores con arquitectura ARM?",
    [
        "a) Supercomputadoras",
        "b) Refrigeradores",
        "c) Ordenadores de a bordo de coches y barcos",
        "d) Equipos de minería de criptomonedas",
    ],
    "c"
),
(
    "¿Cómo se les denomina a los microprocesadores basados en arquitectura ARM que integran en un solo chip funciones como CPU, GPU, controladores de memoria, y otros componentes?",
    [
        "c) CPU",
        "b) GPU",
        "a) System on a Chip (SoC)",
        "d) FPGA",
    ],
    "a"
),
(
    "¿Cómo ha evolucionado la capacidad de procesamiento de los System on a Chip (SoC) a lo largo del tiempo?",
    [
        "a) Ha disminuido en términos de rendimiento",
        "b) Ha permanecido constante sin cambios significativos",
        "c) Ha aumentado, permitiendo realizar funciones más complejas",
        "d) No ha experimentado cambios",
    ],
    "c"
),
(
    "¿Cómo influye el número de núcleos en la velocidad y capacidad de procesamiento de un System on a Chip (SoC)?",
    [
        "a) No tiene ninguna influencia en el rendimiento",
        "b) Cuantos más núcleos, mayor velocidad y capacidad de procesamiento",
        "c) Cuantos más núcleos, menor velocidad y capacidad de procesamiento",
        "d) La velocidad y capacidad de procesamiento dependen solo de la eficiencia, no del número de núcleos",
    ],
    "b"
),
(
    "¿Cuál es la función principal de un coprocesador en un System on a Chip (SoC)?",
    [
        "a) Realizar todas las operaciones del procesador principal",
        "b) Reducir la eficiencia del procesador principal",
        "c) Ayudar al procesador principal en ciertos tipos de operaciones de manera eficiente",
        "d) Aumentar el consumo de energía del procesador principal",
    ],
    "c"
),
(
    "¿Cuál es una característica clave de los coprocesadores en un System on a Chip (SoC)?",
    [
        "a) Realizan el trabajo de manera menos eficiente que el procesador principal",
        "b) Consumen más energía que el procesador principal",
        "c) Realizan el trabajo de forma más eficiente y consumiendo menos energía que el procesador principal",
        "d) No contribuyen al rendimiento del SoC",
    ],
    "c"
),
(
    "¿Cuál es la función principal de la GPU (Graphics Processing Unit) en un System on a Chip (SoC)?",
    [
        "a) Realizar operaciones matemáticas de coma flotante exclusivamente",
        "b) Descargar trabajo de la CPU mejorando el rendimiento del sistema",
        "c) Procesar únicamente información gráfica estática",
        "d) Aumentar el consumo de energía del SoC",
    ],
    "b"
),
(
    "¿Cuál es una de las principales diferencias entre un System on a Chip (SoC) eficiente y uno mediocre?",
    [
        "a) El tamaño físico del SoC",
        "b) La cantidad de núcleos de la CPU",
        "c) La presencia y calidad de la GPU (Graphics Processing Unit)",
        "d) El tipo de memoria RAM utilizada",
    ],
    "c"
),
(
    "¿Cuál es la misión principal de la GPU (Graphics Processing Unit) en un System on a Chip (SoC)?",
    [
        "a) Realizar operaciones matemáticas de coma flotante",
        "b) Descargar a la CPU del procesamiento gráfico para mejorar el rendimiento del sistema",
        "c) Ejecutar instrucciones de la Unidad de Control",
        "d) Gestionar la memoria principal del SoC",
    ],
    "b"
),
(
    "¿En qué tipo de operaciones se especializa principalmente la GPU (Graphics Processing Unit) en un System on a Chip (SoC)?",
    [
        "a) Operaciones lógicas",
        "b) Operaciones matemáticas de enteros",
        "c) Operaciones matemáticas de coma flotante y procesamiento de gráficos",
        "d) Operaciones de entrada/salida",
    ],
    "c"
),
(
    "¿Cuál es la principal diferencia entre una GPU (Graphics Processing Unit) y una CPU (Central Processing Unit)?",
    [
        "a) La GPU está diseñada para el procesamiento general de datos, mientras que la CPU está especializada en gráficos.",
        "b) La CPU es más eficiente en operaciones matemáticas de coma flotante, mientras que la GPU se especializa en operaciones lógicas.",
        "c) La GPU está diseñada para el procesamiento de gráficos y operaciones matemáticas de coma flotante, mientras que la CPU maneja tareas generales.",
        "d) La CPU y la GPU son intercambiables y pueden realizar las mismas tareas.",
    ],
    "c"
),
(
    "¿Por qué las GPU actuales, a pesar de su gran potencia de cálculo, no pueden reemplazar completamente a las CPU?",
    [
        "a) Las GPU son menos eficientes en el procesamiento de gráficos.",
        "c) Las CPU son más eficientes en operaciones matemáticas de coma flotante.",
        "b) Las GPU están diseñadas exclusivamente para tareas específicas, mientras que las CPU manejan una variedad de tareas generales.",
        "d) Las GPU son más caras que las CPU.",
    ],
    "b"
),
(
    "¿De qué depende la potencia gráfica del SOC?",
    [
        "a) De la CPU.",
        "b) De la GPU.",
        "c) De la GC.",
        "d) De la ALU.",
    ],
    "b"
),
(
    "¿Cómo afecta tener una GPU más evolucionada a la gestión de pantallas con mayor resolución?",
    [
        "a) La GPU no tiene impacto en la resolución de la pantalla.",
        "b) Una GPU más evolucionada permite gestionar pantallas con mayor resolución de manera más eficiente.",
        "c) La resolución de la pantalla solo depende de la CPU.",
        "d) Una GPU más evolucionada reduce la calidad de la pantalla.",
    ],
    "b"
),
(
    "¿Qué otro factor determina la evolución de un SOC?",
    [
        "a) La litografía o tecnología de fabricación.",
        "b) La orografía o tecnología de procesador.",
        "c) La nanografía o tecnología de procesador.",
        "d) La litografía o tecnología de procesamiento.",
    ],
    "b"
),
(
    "¿Cómo influye el tamaño de la tecnología de fabricación en la evolución de un microprocesador?",
    [
        "a) Un mayor tamaño de tecnología de fabricación mejora el rendimiento del microprocesador.",
        "b) La tecnología de fabricación no tiene impacto en la evolución de un microprocesador.",
        "c) Cuanto más pequeña sea la tecnología de fabricación, más evolucionado estará dicho microprocesador.",
        "d) Un microprocesador evoluciona independientemente de su tecnología de fabricación.",
    ],
    "c"
),
(
    "¿Cómo afecta una tecnología de fabricación menor en un microprocesador?",
    [
        "a) Aumenta el gasto energético y reduce la concentración de transistores.",
        "b) No tiene impacto en el rendimiento del microprocesador.",
        "c) Disminuye el gasto energético y permite una mayor concentración de transistores en el mismo espacio.",
        "d) Una tecnología de fabricación menor no afecta al microprocesador.",
    ],
    "c"
),
(
    "¿Qué indica la tecnología de fabricación en un SoC?",
    [
        "a) La velocidad del procesador.",
        "b) El tamaño de las puertas lógicas en los circuitos.",
        "c) El número de núcleos en el microprocesador.",
        "d) La capacidad de almacenamiento de la memoria RAM.",
    ],
    "b"
),
(
    "¿Qué significa una tecnología de fabricación de 14 nanómetros en un SoC?",
    [
        "a) Indica el número de transistores (14) en el microprocesador.",
        "b) Representa la velocidad del procesador.",
        "c) Significa que las puertas lógicas tienen un tamaño aproximado de 14 nanómetros.",
        "d) Es una medida de la capacidad de la memoria RAM.",
    ],
    "c"
),
(
    "¿Qué característica destaca a los chips neuromórficos en comparación con los microprocesadores convencionales?",
    [
        "a) Capacidad para realizar billones de operaciones por segundo.",
        "b) Reconocimiento de patrones y procesamiento de imágenes similar al cerebro humano.",
        "c) Velocidad de procesamiento superior a los microprocesadores convencionales.",
        "d) Capacidad para reconocer a una persona por su manera de caminar.",
    ],
    "b"
),
(
    "¿Cuál es una de las limitaciones actuales de los ordenadores en comparación con el cerebro humano?",
    [
        "a) Incapacidad para realizar billones de operaciones por segundo.",
        "b) Dificultad para procesar imágenes de manera eficiente.",
        "c) Falta de capacidad para reconocer patrones y personas por su manera de caminar.",
        "d) Las mismas limitaciones emocionales que tu ex.",
    ],
    "c"
),
(
    "¿Qué presentó Google en 2012 en relación con el reconocimiento en vídeos?",
    [
        "a) Un nuevo modelo de procesador.",
        "b) Un software capaz de reconocer gatos en vídeos.",
        "c) Un avance en la eficiencia de los procesadores.",
        "d) Una tecnología de fabricación para microchips neuromórficos.",
    ],
    "b"
),
(
    "¿Cuántos procesadores necesitaba Google para ejecutar el software capaz de reconocer gatos en vídeos en 2012?",
    [
        "a) 8,000 procesadores.",
        "b) 12,000 procesadores.",
        "c) 16,000 procesadores.",
        "d) 20,000 procesadores.",
    ],
    "c"
),
(
    "En términos de energía, ¿cuántas veces más eficiente es el cerebro humano en comparación con cualquier procesador u ordenador?",
    [
        "a) Miles de veces.",
        "b) Cientos de miles de veces.",
        "c) Millones de veces.",
        "d) Miles de millones de veces.",
    ],
    "c"
),
(
    "¿Qué papel desempeñan los microchips neuromórficos?",
    [
        "a) Aumentar la velocidad de procesamiento.",
        "b) Optimizar la eficiencia energética.",
        "c) Mejorar la capacidad de almacenamiento.",
        "d) Ampliar la conectividad de red.",
    ],
    "b"
),
(
    "¿Cuál es una característica destacada de los microchips neuromórficos?",
    [
        "a) Aumentan significativamente la velocidad de procesamiento.",
        "b) Optimizan la eficiencia energética.",
        "c) Mejoran la capacidad de almacenamiento.",
        "d) Amplían la conectividad de red.",
    ],
    "b"
),
(
    "¿Cuál es una aplicación potencial de los microchips neuromórficos?",
    [
        "a) Aumentar la velocidad de procesamiento en computadoras personales.",
        "b) Implantar microchips en retinas artificiales para personas con ceguera.",
        "c) Mejorar la capacidad de almacenamiento en dispositivos móviles.",
        "d) Ampliar la conectividad de red en sistemas de comunicación.",
    ],
    "b"
),
(
    "¿Cuál es el secreto fundamental que hace eficientes a los microchips neuromórficos?",
    [
        "b) Su capacidad para realizar operaciones matemáticas complejas.",
        "a) La organización similar al cerebro para tareas rápidas y eficientes.",
        "c) El uso de la arquitectura x86 en su diseño.",
        "d) Su capacidad para almacenar grandes cantidades de datos.",
    ],
    "a"
),
(
    "¿Qué ventaja clave proporciona la organización y funciones neuronales de los microchips neuromórficos?",
    [
        "a) Mayor capacidad de almacenamiento de datos.",
        "b) Mayor velocidad de procesamiento.",
        "c) Eficiencia energética y capacidad para tareas sensoriales.",
        "d) Mayor compatibilidad con arquitecturas x86.",
    ],
    "c"
),
(
    "¿Cuántas conexiones neuronales puede activar un cerebro en un segundo?",
    [
        "a) Cien mil millones.",
        "b) Un millón.",
        "c) Diez cuadrillones.",
        "d) Mil millones.",
    ],
    "c"
),
(
    "¿Cuántos Pentium y cuántos megavatios de electricidad se necesitarían para igualar la capacidad de cálculo de un cerebro en un segundo?",
    [
        "a) Un millón de Pentium y unos cientos de megavatios.",
        "b) Mil millones de Pentium y unos pocos megavatios.",
        "c) Cien mil millones de Pentium y unos cientos de megavatios.",
        "d) Un millón de Pentium y unos pocos megavatios.",
    ],
    "a"
),
(
    "¿Qué se está haciendo actualmente para acercarse a la capacidad de cálculo del cerebro humano?",
    [
        "a) Utilizando un millón de Pentium y megavatios de electricidad.",
        "b) Replicando microchips que copian la organización y funciones neuronales.",
        "c) Creando chips neuromórficos sin basarse en la estructura cerebral.",
        "d) Desarrollando software más eficiente para la inteligencia artificial.",
    ],
    "b"
),
(
    "¿Cuál es una posible aplicación exitosa de los chips neuromórficos en el futuro?",
    [
        "a) Replicar exactamente la capacidad de cálculo de un Pentium.",
        "b) Desarrollar sistemas de reconocimiento facial más avanzados.",
        "c) Mejorar la eficiencia energética de los procesadores actuales.",
        "d) Tratar datos sensoriales y darles sentido.",
    ],
    "d"
),
(
    "¿Qué técnicas de inteligencia artificial utilizan los procesadores?",
    [
        "a) Ingeniería genética y biotecnología.",
        "b) Astronomía y astrofísica.",
        "c) Machine learning, deep learning y neural networks.",
        "d) Química orgánica y teoría de números.",
    ],
    "c"
),
(
    "En términos de inteligencia artificial, ¿qué significa 'Machine Learning'?",
    [
        "a) Aprendizaje automático.",
        "b) Aprendizaje multinivel.",
        "c) Aprendizaje profundo.",
        "d) Aprendizaje mecánico.",
    ],
    "a"
),
(
    "En términos de inteligencia artificial, ¿qué significa 'Deep Learning'?",
    [
        "a) Aprendizaje automático.",
        "b) Aprendizaje multinivel.",
        "c) Aprendizaje profundo.",
        "d) Redes nuronales.",
    ],
    "c"
),
(
    "En términos de inteligencia artificial, ¿qué significa 'Neuronal Networks'?",
    [
        "a) Aprendizaje automático.",
        "b) Aprendizaje multinivel.",
        "c) Aprendizaje profundo.",
        "d) Redes neuronales.",
    ],
    "d"
),
(
    "¿Cuál de las siguientes técnicas NO es una disciplina de la inteligencia artificial?",
    [
        "a) Machine learning.",
        "b) Deep learning.",
        "c) Circuitos integrados.",
        "d) Neural networks.",
    ],
    "c"
),
(
    "En el contexto de inteligencia artificial, ¿por qué se afirma que cuanto mejor sea el algoritmo y más entrenado esté, mejor eficiencia tendrá?",
    [
        "a) Porque al aumentar la complejidad del algoritmo se mejora la eficiencia.",
        "b) Porque un algoritmo bien diseñado y entrenado puede realizar tareas de forma más rápida y precisa.",
        "c) Porque el entrenamiento del algoritmo no tiene impacto en su eficiencia.",
        "d) Porque la eficiencia de un algoritmo no depende de su diseño o entrenamiento.",
    ],
    "b"
),
(
    "¿Cuál de las siguientes afirmaciones es correcta?",
    [
        "a) Machine learning es una rama del deep learning.",
        "b) Deep learning es una rama del machine learning.",
        "c) Machine learning y deep learning son dos disciplinas completamente independientes.",
        "d) Ninguna de las anteriores.",
    ],
    "b"
),
(
    "¿Cuál de las siguientes afirmaciones es correcta sobre Machine Learning?",
    [
        "a) Machine Learning no tiene relación con la inteligencia artificial.",
        "b) Los sistemas de Machine Learning no requieren datos de referencia clasificados.",
        "c) Machine Learning permite que los sistemas aprendan por sí mismos.",
        "d) Machine Learning solo funciona en hardware y no en software.",
    ],
    "c"
),
(
    "¿Cuál es un requisito clave para que un sistema de Machine Learning pueda aprender?",
    [
        "a) No necesita datos de referencia clasificados.",
        "b) Debe tener una serie de datos de referencia previamente clasificados.",
        "c) Puede aprender sin ningún tipo de datos.",
        "d) La clasificación previa de datos no es relevante para el aprendizaje en Machine Learning.",
    ],
    "b"
),
(
    "¿Qué puede hacer un sistema de Machine Learning una vez que ha sido parametrizado con datos clasificados?",
    [
        "a) No puede realizar ninguna tarea adicional.",
        "b) Solo puede clasificar los datos previamente utilizados en el aprendizaje.",
        "c) Puede clasificar nuevos datos que no ha visto durante el aprendizaje.",
        "d) Debe ser reentrenado cada vez que se presentan nuevos datos.",
    ],
    "c"
),
(
    "En el ejemplo de detección de caras humanas mediante Machine Learning, ¿qué tarea puede realizar el sistema después de ser entrenado?",
    [
        "a) Solo puede detectar caras humanas en las fotografías utilizadas durante el entrenamiento.",
        "b) No puede realizar ninguna tarea adicional.",
        "c) Puede detectar caras humanas en nuevas fotografías que no ha visto durante el entrenamiento.",
        "d) Necesita ser reentrenado cada vez que se presentan nuevas fotografías.",
    ],
    "c"
),
(
    "¿Qué característica destacada tienen los sistemas que utilizan deep learning o aprendizaje profundo?",
    [
        "a) Utilizan algoritmos que imitan el funcionamiento de un cerebro.",
        "b) Requieren un entrenamiento manual constante.",
        "c) Solo pueden ejecutarse en supercomputadoras.",
        "d) No pueden integrarse en dispositivos como los smartphones.",
    ],
    "a"
),
(
    "¿Cuál es la función principal de las redes neuronales en los sistemas que utilizan deep learning o aprendizaje profundo?",
    [
        "a) Imitar el funcionamiento de un corazón.",
        "b) Simular el comportamiento de un software convencional.",
        "c) Emular el funcionamiento de un cerebro.",
        "d) Sustituir completamente a los algoritmos tradicionales.",
    ],
    "c"
),
(
    "¿Qué ha permitido la evolución de los procesadores en relación con los algoritmos de machine learning y deep learning?",
    [
        "a) Su eliminación completa de los dispositivos.",
        "b) Su integración en dispositivos normales como los smartphones.",
        "c) La restricción de su uso exclusivo en supercomputadoras.",
        "d) El desarrollo de algoritmos más simples sin necesidad de procesadores avanzados.",
    ],
    "b"
),
(
    "¿Cómo afectará el uso de motores neurales en los chips al procesamiento de inteligencia artificial?",
    [
        "a) No tendrá impacto en el procesamiento de inteligencia artificial.",
        "b) Aumentará la dependencia de la fuerza bruta con la CPU o GPU.",
        "c) Hará que muchos procesadores utilicen la inteligencia artificial de manera más eficiente.",
        "d) Reducirá la eficacia de la inteligencia artificial en los procesadores.",
    ],
    "c"
),
(
    "¿Cuál es la función principal de la unidad de control (UC) en un microprocesador?",
    [
        "a) Almacenar datos en la memoria principal.",
        "b) Realizar operaciones aritméticas y lógicas.",
        "c) Ejecutar programas y activar la circuitería para realizar operaciones.",
        "d) Gestionar los dispositivos de entrada/salida.",
    ],
    "c"
),
(
    "¿Qué función principal cumple la memoria en un sistema informático?",
    [
        "a) Realizar operaciones aritméticas y lógicas.",
        "b) Almacenar el código del programa y los datos.",
        "c) Ejecutar programas y activar la circuitería.",
        "d) Gestionar dispositivos de entrada/salida.",
    ],
    "b"
),
(
    "¿Cuál es la función principal de la ALU (Unidad Aritmético-Lógica) en un sistema informático?",
    [
        "a) Almacenar el código del programa y los datos.",
        "b) Ejecutar operaciones aritméticas y lógicas.",
        "c) Gestionar dispositivos de entrada/salida.",
        "d) Activar la circuitería para realizar operaciones.",
    ],
    "b"
),
(
    "¿Qué función cumple el buffer llamado ACC en una ALU (Unidad Aritmético-Lógica)?",
    [
        "a) Almacenar el código del programa.",
        "b) Almacenar los datos del programa.",
        "c) Almacenar el resultado de las operaciones realizadas.",
        "d) Gestionar dispositivos de entrada/salida.",
    ],
    "c"
),
(
    "¿Cuál es la función de los registros (A-J) en un microprocesador?",
    [
        "a) Almacenar el código del programa.",
        "b) Almacenar los datos del programa.",
        "c) Almacenar resultados intermedios de las operaciones.",
        "d) Gestionar dispositivos de entrada/salida.",
    ],
    "c"
),
(
    "¿Cuál es la función del buffer de teclado en un microprocesador?",
    [
        "a) Almacenar el código del programa.",
        "b) Almacenar los datos del programa.",
        "c) Almacenar resultados intermedios de las operaciones.",
        "d) Almacenar pulsaciones de teclas para su posterior procesamiento.",
    ],
    "d"
),
(
    "¿Cuál es la función de la memoria de vídeo en un microprocesador?",
    [
        "a) Almacenar el código del programa.",
        "b) Almacenar los datos del programa.",
        "c) Almacenar resultados intermedios de las operaciones.",
        "d) Permitir la comunicación con el exterior y mostrar datos en pantalla.",
    ],
    "d"
),
(
    "¿Qué realiza la instrucción 'SUMA ACC RX' en un microprocesador?",
    [
        "a) Almacena el contenido del acumulador en el registro RX.",
        "b) Resta el contenido del registro RX al acumulador.",
        "c) Multiplica el contenido del acumulador por el registro RX.",
        "d) Suma el contenido del acumulador y el registro RX, almacenando el resultado en el acumulador.",
    ],
    "d"
),

(
    "¿Qué realiza la instrucción 'RESTA RX ACC' en un microprocesador?",
    [
        "a) Almacena el contenido del acumulador en el registro RX.",
        "b) Resta el contenido del registro RX al acumulador, almacenando el resultado en el acumulador.",
        "c) Multiplica el contenido del acumulador por el registro RX.",
        "d) Suma el contenido del acumulador y el registro RX.",
    ],
    "b"
),
(
    "¿Qué realiza la instrucción 'READ RX' en un microprocesador?",
    [
        "a) Realiza una operación de suma entre el contenido del registro RX y el acumulador.",
        "b) Lee un dato desde el teclado y lo almacena en el registro RX.",
        "c) Copia el contenido del acumulador en el registro RX.",
        "d) Resta el contenido del acumulador al registro RX.",
    ],
    "b"
)












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
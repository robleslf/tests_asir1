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
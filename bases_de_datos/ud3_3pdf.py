import random

# Lista de preguntas y respuestas
preguntas = [
    ("¿Cuál es el objetivo del desarrollo de un esquema de base de datos relacional, según el texto?", [
    "a) Crear una representación inexacta de los datos.",
    "b) Generar datos sin restricciones.",
    "c) Crear una representación precisa y adecuada de los datos, sus relaciones y restricciones.",
    "d) Desarrollar un esquema sin representación de datos."
], "c"),
("¿Quién desarrolló el Modelo Relacional, un modelo lógico de datos para representar información mediante esquemas?", [
    "a) Alan Turing.",
    "b) Richard Stallman.",
    "c) Edgar F. Codd.",
    "d) Tim Berners-Lee."
], "c"),
("¿Cómo perciben los usuarios la base de datos relacional en términos de estructura fundamental del modelo?", [
    "a) Como una colección de tablas con gran uniformidad.",
    "b) Como una colección de gráficos con diversidad.",
    "c) Como una serie de documentos con complejidad.",
    "d) Como una colección de registros con independencia física."
], "a"),
("¿Qué característica del modelo relacional permite realizar el diseño y la evaluación mediante métodos sistemáticos basados en abstracciones?", [
    "a) Independencia física.",
    "b) Sólida fundamentación teórica.",
    "c) Independencia lógica.",
    "d) Sencillez y uniformidad."
], "b"),
("¿Qué característica del modelo relacional proporciona una gran independencia respecto a la forma en que los datos están almacenados?", [
    "a) Independencia física.",
    "b) Sólida fundamentación teórica.",
    "c) Independencia lógica.",
    "d) Sencillez y uniformidad."
], "a"),
("¿Cuál de las siguientes afirmaciones destaca la característica del modelo relacional que implica que las modificaciones en el modelo no deben afectar a las vistas o aplicaciones definidas para la base de datos?", [
    "a) Sencillez y uniformidad.",
    "b) Independencia física.",
    "c) Sólida fundamentación teórica.",
    "d) Independencia lógica."
], "d"),
("¿Cuál de los siguientes elementos es el central en el modelo relacional?", [
    "a) Conjunto.",
    "b) Tabla.",
    "c) Registro.",
    "d) Vista."
], "b"),
("¿Cómo se caracterizan las relaciones en el modelo relacional?", [
    "a) Conjuntos unidimensionales.",
    "b) Tablas bidimensionales.",
    "c) Registros multidimensionales.",
    "d) Vistas matriciales."
], "b"),
("¿Cómo se componen las tuplas en una relación del modelo relacional?", [
    "a) Por un solo valor.",
    "b) Por el conjunto de valores de todos los atributos de un mismo elemento.",
    "c) Por una lista de identificadores.",
    "d) Por el promedio de los valores de los atributos."
], "b"),
("En el modelo relacional, ¿cuáles son los dos componentes principales de una relación?", [
    "b) Atributos y Tuplas.",
    "a) Intensión y Extensión.",
    "c) Claves primarias y Claves foráneas.",
    "d) Entidades y Atributos."
], "a"),
("¿Qué representa la intensión o variable de relación en el modelo relacional?", [
    "a) La estructura estática de la relación.",
    "b) La parte dinámica de la relación.",
    "c) Las operaciones de manipulación de datos.",
    "d) La extensión de la relación."
], "a"),
("¿Qué representa la intensión o variable de relación en el modelo relacional?", [
    "a) La estructura abstracta de datos y las restricciones de integridad de la misma.",
    "b) La parte dinámica de la relación.",
    "c) Las operaciones de manipulación de datos.",
    "d) La extensión de la relación."
], "a"),
("¿Cuál es la función principal de la extensión o relación propiamente dicha en el modelo relacional?", [
    "a) Representa la aserción implícita en un predicado específico sobre una parte concreta del modelo.",
    "b) Define la estructura abstracta de datos y las restricciones de integridad de la misma.",
    "c) Es la parte estática y definitoria de la relación.",
    "d) Es el conjunto de tuplas que satisfacen el esquema de relación en un instante dado."
], "d"),
("¿Cómo podemos identificar la extensión o relación propiamente dicha en el modelo relacional?", [
    "a) Es la parte estática y definitoria de la relación.",
    "b) Se representa mediante una matriz bidimensional.",
    "c) Define la estructura abstracta de datos y las restricciones de integridad de la misma.",
    "d) Podemos identificarla con el valor que toma la variable de relación en un instante dado."
], "d"),
("¿Cómo se denomina al número de tuplas de una relación en un instante dado en el modelo relacional?", [
    "a) Variable de relación.",
    "b) Cardinalidad de la relación.",
    "c) Extensión de la relación.",
    "d) Variable de tupla."
], "b"),
("¿Cómo se denomina al número de columnas o atributos de una relación en el modelo relacional?", [
    "a) Cardinalidad de la relación.",
    "b) Extensión de la relación.",
    "c) Grado de la relación.",
    "d) Variable de relación."
], "c"),
("En el contexto del modelo relacional, ¿cómo se define el dominio de un atributo?", [
    "a) Como el conjunto de tuplas de una relación.",
    "b) Como la cardinalidad de una relación.",
    "c) Como el conjunto de valores atómicos posibles de un atributo.",
    "d) Como el número de columnas o atributos de una relación."
], "c"),
("En el modelo relacional, ¿cómo está ligado cada atributo a un dominio?", [
    "a) Cada atributo puede tener varios dominios asociados.",
    "b) Un dominio puede estar asociado a varios atributos.",
    "c) Cada atributo está ligado a un determinado dominio.",
    "d) Un dominio representa el uso de varios atributos en una relación."
], "c"),
("¿Cómo pueden estar definidos los dominios en el modelo relacional?", [
    "a) Solo por intensión.",
    "b) Solo por extensión.",
    "c) Por intensión o por extensión.",
    "d) No están definidos en el modelo relacional."
], "c"),
("¿Cómo se definen las claves candidatas en una relación del modelo relacional?", [
    "a) Son conjuntos de atributos que identifican sin ambigüedad y de forma única cada tupla.",
    "b) Son conjuntos de atributos que pueden identificar sin ambigüedad cada tupla.",
    "c) Son conjuntos de atributos que identifican de forma única cada tupla.",
    "d) Son conjuntos de atributos que identifican sin ambigüedad cada tupla."
], "a"),
("¿Qué se entiende por atributos clave en una relación del modelo relacional?", [
    "a) Atributos que no forman parte de ninguna clave candidata.",
    "b) Atributos que pueden formar parte de alguna clave candidata.",
    "c) Atributos que forman parte de alguna clave candidata.",
    "d) Atributos que forman parte de la clave principal."
], "c"),
("¿Cómo se denomina la clave candidata que se especifica como clave principal o clave primaria en el esquema de una relación?", [
    "a) Clave única",
    "b) Clave secundaria",
    "c) Clave foránea",
    "d) Clave principal"
], "d"),
("¿Cómo se denominan las claves candidatas que no son especificadas como clave principal en el esquema de una relación?", [
    "a) Claves secundarias",
    "b) Claves primarias",
    "c) Claves únicas",
    "d) Claves alternativas"
], "d"),
("¿Cuál es la función de las claves foráneas en el modelo relacional de datos?", [
    "a) Identifican de forma única cada tupla de la relación.",
    "b) Establecen relaciones entre diferentes relaciones.",
    "c) Son atributos opcionales en una relación.",
    "d) Definen la estructura de una relación."
], "b"),
("¿Qué proporcionan las claves primarias y las claves alternativas al modelo relacional?", [
    "a) La intensión y extensión de la relación.",
    "b) Mecanismos para representar las (inter)relaciones entre los objetos del problema.",
    "c) Los valores de los atributos de la relación.",
    "d) La cardinalidad y el grado de la relación."
], "b"),
("¿Cuál es una característica inherente al modelo relacional respecto al orden de los elementos?", [
    "a) El orden de las tuplas y atributos es siempre relevante.",
    "b) El orden de las tuplas es relevante pero no el de los atributos.",
    "c) No se define ningún orden en los elementos de una relación.",
    "d) El orden de los atributos es relevante pero no el de las tuplas."
], "c"),
("¿Qué afirmación es correcta sobre la existencia de la clave primaria en una relación del modelo relacional?", [
    "a) No es obligatoria la existencia de la clave primaria.",
    "b) Puede haber dos tuplas iguales en una relación.",
    "c) La existencia de la clave primaria es opcional.",
    "d) En toda relación es obligatoria la existencia de la clave primaria."
], "d"),
("¿Cuál de las siguientes afirmaciones es correcta sobre los valores de los atributos en una tupla del modelo relacional?", [
    "a) Cada atributo puede tomar múltiples valores en una tupla.",
    "b) No hay restricciones en los valores de los atributos en una tupla.",
    "c) Cada atributo de una tupla solo puede tomar un único valor.",
    "d) Los valores de los atributos en una tupla no están relacionados con el dominio."
], "c"),
("En el modelo relacional, ¿qué significa que el valor de un atributo en una tupla sea nulo?", [
    "a) Significa que el atributo no está definido en la relación.",
    "b) Significa que el atributo no puede tomar valores.",
    "c) Significa que el valor del atributo está presente pero no se conoce.",
    "d) Significa la ausencia de valor para ese atributo en esa tupla."
], "d"),
("Según la regla de integridad de clave en el modelo relacional, ¿cuál es la afirmación correcta?", [
    "a) Todos los atributos de una relación pueden tomar valores nulos.",
    "b) Los atributos clave pueden tomar valores nulos en algunas tuplas.",
    "c) Los atributos clave no pueden tomar valores nulos en ninguna tupla.",
    "d) La presencia de valores nulos en los atributos clave es opcional."
], "c"),
("La integridad referencial en el modelo relacional permite:", [
    "a) Que las claves foráneas de una relación puedan referenciar cualquier tupla de la relación padre.",
    "b) Que las claves foráneas de una relación puedan referenciar una tupla válida de la relación padre.",
    "c) Que las claves foráneas de una relación no estén relacionadas con ninguna tupla de la relación padre.",
    "d) Que las claves foráneas de una relación no tengan restricciones."
], "b"),
("En el modelo relacional, ¿qué permite al usuario especificar operaciones cuando se produce el borrado o modificación de una tupla en la relación padre?", [
    "a) Clave primaria.",
    "b) Integridad referencial.",
    "c) Clave candidata.",
    "d) Dominio."
], "b"),
("En el contexto de integridad referencial en el modelo relacional, ¿qué sucede en una operación de borrado o modificación en cascada?", [
    "a) Se crea una nueva tupla.",
    "b) Se actualizan todas las tuplas relacionadas en la relación hija.",
    "c) Se produce un error.",
    "d) Se borra la tupla en la relación hija."
], "b"),
("En el contexto de integridad referencial en el modelo relacional, ¿qué sucede en una operación de borrado o modificación restringido?", [
    "a) Se crea una nueva tupla.",
    "b) Se actualizan todas las tuplas relacionadas en la relación hija.",
    "c) Se produce un error.",
    "d) No se permite el borrado o modificación de las tuplas de la relación padre."
], "d"),
("En el contexto de integridad referencial en el modelo relacional, ¿qué sucede en una operación de borrado o modificación con puesta a nulos?", [
    "a) Se crea una nueva tupla.",
    "b) Se actualizan todas las tuplas relacionadas en la relación hija.",
    "c) Se pone a nulo el valor de los atributos clave ajena en la relación hija.",
    "d) No se permite el borrado o modificación de las tuplas de la relación padre."
], "c"),
("En el contexto de integridad referencial en el modelo relacional, ¿qué sucede en una operación de borrado o modificación con puesta a un valor por defecto?", [
    "a) Se crea una nueva tupla.",
    "b) Se actualizan todas las tuplas relacionadas en la relación hija.",
    "c) Se ponen a un valor por defecto los atributos clave ajena en la relación hija.",
    "d) No se permite el borrado o modificación de las tuplas de la relación padre."
], "c"),
("En el contexto de integridad referencial en el modelo relacional, ¿qué tipo de integridad referencial implica que los atributos clave foránea pueden tener valores nulos?", [
    "a) Integridad referencial simple.",
    "b) Integridad referencial compuesta.",
    "c) Integridad referencial con puesta a nulos.",
    "d) Integridad referencial con puesta a un valor por defecto."
], "c"),
("¿Cuál de las siguientes afirmaciones es correcta en relación con las restricciones en el modelo relacional?", [
    "a) Las restricciones solo se aplican a las relaciones hijas.",
    "b) Las restricciones no afectan la integridad del modelo.",
    "c) Las restricciones solo se aplican a las claves primarias.",
    "d) Las restricciones garantizan la integridad del modelo."
], "d"),
("¿Cuál de las siguientes afirmaciones describe correctamente las restricciones de verificación (CHECK) en el modelo relacional?", [
    "a) Las restricciones de verificación solo se aplican a los valores nulos.",
    "b) Las restricciones de verificación especifican condiciones para los valores de ciertos atributos.",
    "c) Las restricciones de verificación solo se aplican a las claves foráneas.",
    "d) Las restricciones de verificación no afectan la validez del modelo."
], "b"),
("¿Qué afirmación describe correctamente las aserciones (ASSERTIONS) en el modelo relacional?", [
    "a) Las aserciones solo se aplican a los atributos clave.",
    "b) Las aserciones permiten especificar condiciones entre elementos de distintas relaciones.",
    "c) Las aserciones solo se aplican a las restricciones de verificación.",
    "d) Las aserciones no afectan la integridad del modelo relacional."
], "b"),
("¿Cuál de las siguientes afirmaciones es correcta acerca de los disparadores (TRIGGER) en el modelo relacional?", [
    "a) Los disparadores solo se utilizan para la inserción de datos.",
    "b) Los disparadores están soportados en SQL-92.",
    "c) Los disparadores se utilizan exclusivamente para la modificación de datos.",
    "d) Los disparadores permiten especificar condiciones y acciones para cuando se efectúen eventos específicos."
], "d"),
("¿Cómo se describe el grafo relacional en el modelo relacional?", [
    "a) Como un conjunto de tablas con claves primarias y foráneas.",
    "b) Como un grafo dirigido cuyos nodos son relaciones con sus atributos.",
    "c) Como un conjunto de tuplas con sus valores en la base de datos.",
    "d) Como un conjunto de operaciones SQL para manipular datos."
], "b"),
("¿Cómo se describe el grafo relacional en el modelo relacional?", [
    "a) Como un conjunto de tablas con claves primarias y foráneas.",
    "b) Como un grafo dirigido cuyos nodos son relaciones con sus atributos.",
    "c) Como un conjunto de tuplas con sus valores en la base de datos.",
    "d) Como un conjunto de operaciones SQL para manipular datos."
], "b"),
("¿Cómo se representan las restricciones de clave ajena en el grafo relacional?", [
    "a) Mediante colores en las relaciones.",
    "b) Como nodos adicionales.",
    "c) A través de arcos entre las relaciones.",
    "d) Mediante líneas conectando los atributos de las relaciones."
], "c"),
("¿Qué información se añade a cada arco en un grafo relacional para mantener la integridad referencial?", [
    "a) Nombres de las relaciones.",
    "b) Tipos de datos de los atributos.",
    "c) Opciones de borrado y modificación.",
    "d) Nombres de los atributos."
], "c"),
("¿Cómo se representan los nombres de las tablas en un modelo relacional?", [
    "a) En mayúsculas.",
    "b) En minúsculas.",
    "c) En formato mixto (mayúsculas y minúsculas).",
    "d) No hay una convención específica."
], "a"),
("¿Cómo se presenta la información de una relación en el modelo relacional?", [
    "a) Solo el nombre de la relación.",
    "b) Solo los atributos entre paréntesis.",
    "c) El nombre de la relación seguido de sus atributos entre paréntesis.",
    "d) El nombre de la relación y atributos en líneas separadas."
], "c"),
("¿Cómo se representan las claves primarias en el modelo relacional?", [
    "a) En negrita.",
    "b) Subrayadas.",
    "c) Con un color diferente.",
    "d) Entre paréntesis."
], "b"),
("¿Cómo se representan las claves alternativas en el modelo relacional?", [
    "a) En negrita.",
    "b) Subrayadas.",
    "c) Con un color diferente.",
    "d) Entre paréntesis."
], "a"),
("¿Cómo se representan las claves ajenas en el grafo relacional?", [
    "a) En cursiva y con una flecha.",
    "b) Con un color diferente.",
    "c) Subrayadas.",
    "d) Entre paréntesis."
], "a"),
("¿Cómo se representan los atributos que pueden tomar valores nulos en el grafo relacional?", [
    "a) Subrayados.",
    "b) Con un asterisco.",
    "c) En negrita.",
    "d) Entre paréntesis."
], "b"),
("¿Cuáles son las opciones para la integridad referencial en el grafo relacional?", [
    "a) I:C, I:R, I:N, I:D.",
    "b) R:C, R:R, R:N, R:D.",
    "c) B:C, B:R, B:N, B:D, M:C, M:R, M:N, M:D.",
    "d) C:B, R:B, N:B, D:B, C:M, R:M, N:M, D:M."
], "c"),
("¿Cómo se puede representar la información en una base de datos mediante el modelo relacional?", [
    "a) Por medio de un conjunto de objetos y un conjunto de relaciones.",
    "b) Por medio de un conjunto de relaciones y un conjunto de reglas de integridad.",
    "c) Por medio de un conjunto de tablas y un conjunto de atributos.",
    "d) Por medio de un conjunto de tuplas y un conjunto de dominios."
], "b"),
("¿Cómo es aconsejable abordar el diseño de una base de datos en el modelo relacional?", [
    "a) Obteniendo el esquema relacional directamente del modelo E/R.",
    "b) Realizando el proceso de diseño conceptual en el modelo E/R y luego transformándolo en un esquema relacional.",
    "c) Obteniendo el esquema relacional directamente de la observación del universo del discurso.",
    "d) Transformando directamente el modelo E/R en un esquema relacional sin fase de diseño conceptual."
], "b"),
("¿Cuáles son los posibles problemas que pueden surgir en las relaciones obtenidas directamente de la observación del mundo real o de la transformación del esquema E/R en el modelo relacional?", [
    "a) Fallos en la percepción del universo del discurso.",
    "b) Fallos en el diseño del esquema E/R.",
    "c) Fallos en el paso al modelo relacional.",
    "d) Todas las anteriores."
], "d"),
("¿Cuáles son problemas que pueden surgir en las relaciones obtenidas directamente de la observación del mundo real o de la transformación del esquema E/R en el modelo relacional?", [
    "a) Incapacidad para almacenar ciertos hechos.",
    "b) Redundancias y posibilidad de inconsistencias.",
    "c) Ambigüedades.",
    "d) Pérdida de información.",
    "e) Pérdida de dependencias funcionales.",
    "f) Existencia de valores nulos.",
    "g) Aparición de estados no válidos.",
    "h) Todas las anteriores."
], "h"),
("¿Por qué es importante analizar el esquema relacional para evitar problemas como la pérdida de información y la aparición de estados no válidos en el mundo real?", [
    "a) Para aumentar la complejidad del modelo.",
    "b) Para asegurar la consistencia de la base de datos.",
    "c) Para favorecer la redundancia de datos.",
    "d) Para simplificar el diseño de la base de datos."
], "b"),
("¿Cuál es el propósito principal de aplicar las formas normales a bases de datos ya implantadas en forma de relaciones?", [
    "a) Aumentar la complejidad de las relaciones.",
    "b) Garantizar la consistencia de la base de datos.",
    "c) Favorecer la redundancia de datos.",
    "d) Simplificar el diseño de la base de datos."
], "b"),
("¿Cuántas formas normales existen según el contexto presentado?", [
    "a) Cuatro formas normales.",
    "b) Cinco formas normales.",
    "c) Seis formas normales.",
    "d) Siete formas normales."
], "c"),
("¿Qué implicación tiene el cumplimiento de una forma normal con respecto a las anteriores?", [
    "a) El cumplimiento de una forma normal implica automáticamente el cumplimiento de todas las anteriores.",
    "b) El cumplimiento de una forma normal no tiene relación con las anteriores.",
    "c) Cumplir con una forma normal significa que las anteriores no son necesarias.",
    "d) Es posible cumplir con una forma normal sin cumplir con las anteriores."
], "a"),
("¿Qué se puede afirmar sobre la descomposición de un esquema relacional que se encuentra en una FN pero no cumple la siguiente?", [
    "a) No es posible realizar una descomposición sin pérdida.",
    "b) La descomposición siempre resulta en pérdida de información.",
    "c) Existe siempre una descomposición sin pérdida que permite normalizar el esquema a esa FN.",
    "d) La descomposición solo es posible si se cumplen todas las formas normales anteriores."
], "c"),
("¿Es posible llevar un esquema relacional hasta la 5FN?", [
    "a) Sí, siempre es posible.",
    "b) No, solo se puede llegar hasta la 4FN.",
    "c) Depende del tamaño de la base de datos.",
    "d) Solo si se cumplen todas las formas normales anteriores."
], "a"),
("¿Qué suele ocurrir al realizar descomposiciones para llevar un esquema a formas normales superiores?", [
    "a) Se eliminan restricciones existentes.",
    "b) No se producen cambios en las restricciones.",
    "c) Aparecen nuevas restricciones en las nuevas relaciones descompuestas.",
    "d) Todas las restricciones desaparecen."
], "c"),
("¿Cuáles de las siguientes formas normales son suficientes en la mayoría de los casos para normalizar los esquemas de relación?", [
    "a) Las dos primeras",
    "b) Las cuatro primeras",
    "c) Las tres primeras",
    "d) Es necesario que cumplan todas"
], "b"),
("¿Cuándo se dice que una relación está en la Primera Forma Normal (1FN)?", [
    "a) Cuando todos los atributos son duplicados.",
    "b) Cuando existen atributos duplicados.",
    "c) Cuando no existen atributos duplicados y cada atributo toma un único valor.",
    "d) Cuando los atributos toman múltiples valores."
], "c"),
("En la Primera Forma Normal (1FN), ¿cada atributo tiene asociado un dominio del cual toma un valor en cada tupla?", [
    "a) No, cada atributo toma múltiples valores en cada tupla.",
    "b) Sí, cada atributo toma un único valor en cada tupla.",
    "c) No, los atributos pueden tomar varios valores en cada tupla.",
    "d) Sí, los atributos pueden tomar múltiples valores en cada tupla."
], "b"),
("¿Es cierto que cualquier variable de relación se encuentra por definición en la Primera Forma Normal (1FN)?", [
    "a) Sí, es cierto.",
    "b) No, la 1FN es una característica opcional del modelo relacional.",
    "c) Sí, pero solo si se aplica la normalización correctamente.",
    "d) No, es falso."
], "a"),
("¿Es cierto que las tuplas pueden no cumplir la Primera Forma Normal (1FN) a diferencia de las variables de relación?", [
    "a) Sí, es cierto.",
    "b) No, las tuplas siempre cumplen la 1FN.",
    "c) Depende del SGBD utilizado.",
    "d) No, es falso."
], "a"),
("¿Cuáles son los dos tipos fundamentales de dependencias en el modelo relacional, utilizadas para definir las formas normales?", [
    "a) Dependencias lineales y dependencias circulares.",
    "b) Dependencias jerárquicas y dependencias de unión.",
    "c) Dependencias funcionales y dependencias de unión.",
    "d) Dependencias de inclusión y dependencias de exclusión."
], "c"),
("¿Cómo se define una dependencia funcional en el contexto del modelo relacional?", [
    "a) Es una relación entre atributos de diferentes relaciones.",
    "b) Es una relación entre atributos de una misma relación.",
    "c) Es una relación entre claves primarias y claves ajenas.",
    "d) Es una relación entre dominios y atributos."
], "b"),
("¿Cuándo se considera que una dependencia funcional es elemental?", [
    "a) Cuando tiene varios atributos en el lado derecho.",
    "b) Cuando tiene un atributo en el lado derecho.",
    "c) Cuando tiene atributos en ambos lados.",
    "d) Cuando no tiene atributos en ninguno de los lados."
], "b"),
("¿Cómo se caracteriza una dependencia funcional completa?", [
    "a) Cuando el valor de algunos atributos de la parte derecha no está determinado por el valor de todos los atributos de la parte izquierda.",
    "b) Cuando el valor de cada atributo de la parte derecha está determinado por el valor de todos los atributos de la parte izquierda.",
    "c) Cuando no hay una relación clara entre los atributos de la parte izquierda y los de la parte derecha.",
    "d) Cuando no hay una relación clara entre los atributos de la parte derecha y los de la parte izquierda."
], "b"),
("¿Cómo se llama al conjunto de atributos de una relación del cual depende funcionalmente de forma completa algún otro atributo de la misma relación?", [
    "a) Dependiente funcional.",
    "b) Conjunto funcional.",
    "c) Determinante funcional.",
    "d) Atributo dependiente."
], "c"),
("¿Cómo se llama al conjunto de atributos X+ con respecto a un conjunto de dependencias funcionales F, que incluye todos los atributos que son determinados funcionalmente por X?", [
    "a) Conjunto de cierre.",
    "b) Conjunto de dependencia.",
    "c) Cierre transitivo.",
    "d) Conjunto extendido."
], "a"),
("¿Qué condición debe cumplir el cierre transitivo de un conjunto de atributos para que este conjunto sea clave candidata de una relación?", [
    "a) Debe contener todos los atributos de la relación.",
    "b) Debe ser el conjunto vacío.",
    "c) Debe ser un conjunto unitario.",
    "d) Debe ser igual al conjunto original."
], "a"),
("¿Por qué un conjunto de atributos no puede ser clave candidata si existe un subconjunto que también cumple con el cierre transitivo?", [
    "a) Porque el cierre transitivo solo puede aplicarse al conjunto completo.",
    "b) Porque se generarían dependencias funcionales redundantes.",
    "c) Porque contradice las reglas de normalización.",
    "d) Porque los subconjuntos siempre son superiores en términos de clave candidata."
], "b"),
("¿Qué representa el cierre de un conjunto de dependencias funcionales?", [
    "a) Todas las dependencias funcionales originales.",
    "b) Solo las dependencias funcionales elementales.",
    "c) Todas las dependencias funcionales que son consecuencia del conjunto original.",
    "d) Solo las dependencias funcionales completas."
], "c"),
("¿Cómo se define el recubrimiento minimal (o no redundante) de un conjunto de dependencias funcionales?", [
    "a) Con dependencias funcionales redundantes.",
    "b) Sin dependencias funcionales elementales.",
    "c) Sin dependencias funcionales completas.",
    "d) Con dependencias funcionales elementales, completas y sin redundancias."
], "d"),
("¿Cómo se define el recubrimiento o cobertura minimal (o no redundante) de un conjunto de dependencias funcionales?", [
    "a) Con dependencias funcionales redundantes.",
    "b) Sin dependencias funcionales elementales.",
    "c) Sin dependencias funcionales completas.",
    "d) Con dependencias funcionales elementales, completas y sin redundancias."
], "d"),
("¿Cuáles son los atributos que formarían parte de todas las claves posibles de una relación al seguir el proceso descrito?", [
    "a) Los atributos que solo figuran en la parte derecha de las DF.",
    "b) Los atributos que solo figuran en la parte izquierda de las DF.",
    "c) Todos los atributos de la relación.",
    "d) Los atributos que no están presentes en las DF."
], "b"),
("¿Qué se puede decir acerca de los atributos que figuran tanto en la parte izquierda de una DF como en la parte derecha de otra DF en el proceso de hallar las claves candidatas?", [
    "a) No pueden formar parte de ninguna clave.",
    "b) Deben formar parte de todas las claves posibles.",
    "c) Pueden formar parte de alguna clave.",
    "d) No son relevantes en el proceso de encontrar claves candidatas."
], "c"),
("En el proceso de hallar las claves candidatas de una relación, ¿qué se puede decir acerca de los atributos que solo figuran en la parte derecha de las DF en el recubrimiento minimal?", [
    "a) Son parte de todas las claves posibles.",
    "b) Pueden formar parte de alguna clave.",
    "c) No son relevantes en el proceso de encontrar claves candidatas.",
    "d) No son parte de ninguna clave."
], "d"),
("En el proceso de hallar las claves candidatas de una relación, ¿qué se puede decir acerca de los atributos que solo figuran en la parte izquierda de las DF en el recubrimiento minimal?", [
    "a) Son parte de todas las claves posibles.",
    "b) Pueden formar parte de alguna clave.",
    "c) No son relevantes en el proceso de encontrar claves candidatas.",
    "d) No son parte de ninguna clave."
], "a"),
("¿Hasta qué forma normal se utiliza como base las dependencias funcionales en el proceso de normalización?", [
    "a) 1FN",
    "b) 2FN",
    "c) 3FN",
    "d) FNBC"
], "d"),
("¿Cuál es la condición adicional para que una relación esté en 2FN?", [
    "a) No debe tener atributos duplicados.",
    "b) Cada atributo no clave debe tener dependencia funcional completa respecto de las claves.",
    "c) Los atributos deben ser atómicos y univaluados.",
    "d) Ninguna de las anteriores."
], "b"),
("¿Cómo se puede expresar la condición para que una relación esté en 2FN?", [
    "a) Debe estar en 1FN y tener claves primarias.",
    "b) Debe estar en 1FN y cada atributo no clave debe depender completamente de las claves.",
    "c) Los atributos deben ser atómicos y univaluados.",
    "d) Ninguna de las anteriores."
], "b"),
("¿Cuál es la condición para que una relación cumpla con la Tercera Forma Normal (3FN)?", [
    "a) Debe estar en 1FN y tener claves primarias.",
    "b) Debe estar en 2FN y cada atributo no clave debe depender completamente de las claves.",
    "c) Debe estar en 2FN y ningún atributo no clave debe depender funcionalmente de otros atributos no clave.",
    "d) Ninguna de las anteriores."
], "c"),
("En el contexto de la Tercera Forma Normal (3FN), ¿qué significa que no pueden existir dependencias entre los atributos que no forman parte de una clave de la relación R?", [
    "a) Pueden existir dependencias funcionales entre cualquier par de atributos de la relación.",
    "b) Solo pueden existir dependencias funcionales entre atributos que forman parte de una clave de la relación.",
    "c) Los atributos no clave no pueden tener valores determinados por otros atributos no clave.",
    "d) La relación debe tener un atributo clave para cumplir con la 3FN."
], "c"),
("¿Cuál es la diferencia principal entre la Forma Normal de Boyce-Codd (FNBC) y la Tercera Forma Normal (3FN)?", [
    "a) La FNBC permite dependencias entre atributos que no forman parte de una clave.",
    "b) La FNBC es menos estricta en términos de dependencias funcionales.",
    "c) La FNBC es más estricta en términos de dependencias funcionales.",
    "d) No hay diferencia significativa entre ambas."
], "c"),
("¿Quiénes formularon en principio la redefinición de la Tercera Forma Normal (3FN) que más adelante se convirtió en la Forma Normal de Boyce-Codd (FNBC)?", [
    "a) Codd y Date.",
    "b) Boyce y Date.",
    "c) Boyce y Codd.",
    "d) Boyce-Codd y Pascal."
], "c"),
("¿Qué condición debe cumplir una relación para estar en la Forma Normal de Boyce-Codd (FNBC)?", [
    "a) Estar en 1FN y tener dependencias de unión.",
    "b) Estar en 2FN y tener dependencias multivaluadas.",
    "c) Estar en 1FN y tener cada determinante funcional como clave candidata.",
    "d) Estar en 3FN y tener dependencias transitivas."
], "c"),
("¿Qué acción se debe realizar para eliminar atributos multivaluados y transformarlos en entidades débiles dependientes en el contexto de la normalización del esquema E-R?", [
    "a) Eliminar la entidad por completo.",
    "b) Transformarlos en entidades fuertes independientes.",
    "c) Transformarlos en entidades débiles dependientes.",
    "d) Conservar los atributos multivaluados sin cambios."
], "c"),
("¿Qué acción se debe realizar para transformar tipos de entidad a relaciones en el contexto de la normalización del esquema E-R?", [
    "a) Eliminar los tipos de entidad.",
    "b) Conservar los tipos de entidad sin cambios.",
    "c) Transformar los tipos de entidad a relaciones.",
    "d) Transformar los tipos de entidad a atributos."
], "c"),
("En la transformación de tipos de interrelación binarias uno a uno en el contexto de la normalización del esquema E-R, ¿qué acción se realiza?", [
    "a) Eliminar una de las tablas.",
    "b) Mantener una sola tabla.",
    "c) Crear dos tablas y propagar la clave.",
    "d) Convertir la relación en un atributo."
], "c"),
("En la transformación de tipos de interrelación binarias uno a uno en el contexto de la normalización del esquema E-R, ¿qué opción se aplica si solo uno de los dos tipos de entidades tiene cardinalidad mínima cero?", [
    "a) Propagar la clave hacia el lado de cardinalidad mínima cero.",
    "b) Convertir cada tipo de entidad en una tabla y propagar la clave hacia el lado de cardinalidad mínima cero.",
    "c) Convertir cada tipo de entidad en una tabla y propagar la clave hacia el lado de cardinalidad mínima uno.",
    "d) Hacer una tabla nueva para evitar valores nulos."
], "b"),
("En la transformación de tipos de interrelación binarias uno a uno en el contexto de la normalización del esquema E-R, ¿qué opción se aplica si ambos tipos de entidades tienen cardinalidad mínima uno?", [
    "a) Propagar la clave hacia el lado de cardinalidad mínima cero.",
    "b) Convertir cada tipo de entidad en una tabla y propagar la clave hacia el lado de cardinalidad mínima cero.",
    "c) Convertir cada tipo de entidad en una tabla y propagar la clave hacia el lado de cardinalidad mínima uno.",
    "d) Hacer una tabla nueva para evitar valores nulos."
], "a"),
("En la transformación de tipos de interrelación binarias uno a uno en el contexto de la normalización del esquema E-R, ¿qué opción se aplica si ambos tipos de entidades tienen cardinalidad mínima uno y hay dependencia en identificación con el mismo identificador principal en ambos tipos de relaciones?", [
    "a) Propagar la clave hacia el lado de cardinalidad mínima cero.",
    "b) Convertir cada tipo de entidad en una tabla y propagar la clave hacia el lado de cardinalidad mínima cero.",
    "c) Convertir cada tipo de entidad en una tabla y propagar la clave hacia el lado de cardinalidad mínima uno.",
    "d) Convertir ambos tipos de entidad en una única tabla."
], "d"),
("En la transformación de tipos de interrelación binarias uno a uno en el contexto de la normalización del esquema E-R, ¿qué opción se aplica si solo uno de los dos tipos de entidades tiene cardinalidad mínima cero?", [
    "a) Propagar la clave hacia el lado de cardinalidad mínima cero.",
    "b) Convertir cada tipo de entidad en una tabla y propagar la clave hacia el lado de cardinalidad mínima cero.",
    "c) Convertir cada tipo de entidad en una tabla y propagar la clave hacia el lado de cardinalidad mínima uno.",
    "d) Convertir ambos tipos de entidad en una única tabla."
], "b"),
("En la transformación de tipos de interrelación binarias uno a uno en el contexto de la normalización del esquema E-R, ¿qué opción se aplica si ambos tipos de entidades tienen cardinalidad mínima cero?", [
    "a) Propagar la clave hacia el lado de cardinalidad mínima cero.",
    "b) Convertir cada tipo de entidad en una tabla y propagar la clave hacia el lado de cardinalidad mínima cero.",
    "c) Convertir cada tipo de entidad en una tabla y propagar la clave hacia el lado de cardinalidad mínima uno.",
    "d) Crear una tabla nueva (tres tablas en total) para evitar la existencia de demasiados valores nulos."
], "d"),
("En la transformación de tipos de interrelación binarias uno a muchos en el contexto de la normalización del esquema E-R, ¿cómo se aplicaría la propagación de la clave?", [
    "a) Hacia el lado uno.",
    "b) Hacia el lado muchos.",
    "c) Hacia ambos lados.",
    "d) Hacia ninguno de los lados."
], "b"),
("En la transformación de tipos de interrelación binarias uno a muchos con una cardinalidad mínima cero en la entidad del lado uno (0,1)  ¿cómo se gestionaría la presencia de valores nulos ?", [
    "a) Generando dos tablas, una por cada tipo de entidad.",
    "b) Generando tres tablas, una por cada tipo de entidad y otra adicional con los identificadores y atributos de la interrelación.",
    "c) Generando una única tabla con los identificadores de ambas entidades.",
    "d) Generando una tabla única con todos los atributos."
], "b"),
("En la transformación de tipos de interrelación binarias uno a muchos, ¿cómo se determina la clave principal en la tabla resultante?", [
    "a) Utilizando el identificador principal del tipo de entidad con cardinalidad mínima.",
    "b) Utilizando el identificador principal del tipo de entidad con cardinalidad máxima.",
    "c) Utilizando un identificador nuevo específico para la tabla de interrelación.",
    "d) Utilizando un identificador compuesto de ambos tipos de entidad."
], "b"),
("En la transformación de tipos de interrelación binarias muchos a muchos, ¿cómo se determina la clave principal en la tabla resultante?", [
    "a) Utilizando el identificador principal del tipo de entidad con cardinalidad mínima.",
    "b) Utilizando el identificador principal del tipo de entidad con cardinalidad máxima.",
    "c) Utilizando un identificador nuevo específico para la tabla de interrelación.",
    "d) Utilizando un identificador compuesto de ambos tipos de entidad."
], "c"),
("Los tipos de interrelación binarias muchos a muchos se transforman siempre en tres tablas, una por cada tipo de entidad y otra con los identificadores de ambas entidades y los atributos (si los hay) de la interrelación; ¿Cuál es la clave principal de la tercera tabla?", [
    "a) La clave principal estará compuesta por los identificadores principales de ambos tipos de entidades.",
    "b) La clave principal estará compuesta solo por el identificador principal de uno de los tipos de entidades.",
    "c) La clave principal estará compuesta solo por el identificador principal del otro tipo de entidad.",
    "d) La clave principal será cada una de los identificadores principales de ambos tipos de entidades más todos los atributos de la interrelación."
], "a"),
("Los tipos de interrelación en los que intervienen más de dos tipos de entidad, ...", [
    "a)  ...se transforman de la misma forma que los tipos de interrelación binarias (0,1).",
    "b)  ...se transforman de la misma forma que los tipos de interrelación binarias muchos a muchos.",
    "c)  ...se transforman de la misma forma que los tipos de interrelación binarias (0,n).",
    "d) Yo q cojones se tio xd."
], "b"),
("En el contexto de la transformación de tipos de interrelación reflexiva en un esquema E-R, ¿cómo se manejan las interrelaciones reflexivas del tipo 1:N?", [
    "a) Se genera una única tabla para el tipo de entidad con el identificador principal como clave foránea.",
    "b) Se crean dos tablas, una para el tipo de entidad y otra para el tipo de interrelación, duplicando el identificador principal.",
    "c) Se transforman de la misma forma que los tipos de interrelación binarias muchos a muchos.",
    "d) Se generan tablas separadas para cada tipo de entidad."
], "a"),
("Cuando hay propagación de la clave en la transformación de tipos de interrelación, ¿qué sucede con los atributos de las interrelaciones?", [
    "a) Se eliminan.",
    "b) Se propagan también.",
    "c) Se convierten en claves primarias.",
    "d) Se duplican en ambas tablas resultantes."
], "b"),
("En la transformación de relaciones jerárquicas de generalización – especialización, ¿cuántas formas existen de realizar la transformación?", [
    "a) Una forma.",
    "b) Dos formas.",
    "c) Tres formas.",
    "d) Cuatro formas."
], "c"),
("En la transformación de relaciones jerárquicas de generalización – especialización, ¿cuál es una de las formas de realizar la transformación?", [
    "a) Transformando el tipo de entidad padre en una relación y colgando de ella los atributos comunes y no comunes de todos los tipos de entidad hijo.",
    "b) Creando una relación para el tipo de entidad padre, con los atributos comunes, y otra relación para cada uno de los tipos de entidad hijo.",
    "c) Creando una relación para cada uno de los tipos de entidad hijo y poniendo en cada una de ellas todos los atributos comunes del tipo de entidad padre.",
    "d) Todas las anteriores."
], "d"),
("En la transformación de relaciones jerárquicas de generalización – especialización, ¿qué consideración se debe tener respecto a las dependencias en identificación y en existencia?", [
    "a) Deben transformarse para evitar la existencia de valores nulos en la clave foránea de la relación proveniente del tipo de entidad débil.",
    "b) Deben ignorarse en la transformación.",
    "c) Deben mantenerse igual en la transformación.",
    "d) Depende del tipo de entidad débil."
], "a")





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
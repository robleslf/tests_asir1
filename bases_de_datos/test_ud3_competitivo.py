import random

# Lista de preguntas y respuestas
preguntas = [
("¿Cuál es la naturaleza del modelo relacional en el contexto de la representación de la estructura lógica de un sistema según la información proporcionada?", [
    "a) Es una representación gráfica.",
    "b) Es una representación de la estructura física del sistema.",
    "c) Es una representación de la estructura lógica del sistema.",
    "d) Es una representación de la interfaz de usuario."
], "c"),
("¿Cuál es el elemento principal del modelo relacional según la información proporcionada?", [
    "a) Atributo.",
    "b) Entidad.",
    "c) Relación.",
    "d) Instancia."
], "c"),
("¿Cómo se representa cada relación en el modelo relacional según la información proporcionada?", [
    "a) Con un grafo direccional.",
    "b) Con una lista enlazada.",
    "c) Con una tabla bidimensional.",
    "d) Con un árbol binario."
], "c"),
("¿Cómo se distingue la relación en el modelo relacional de la relación en el modelo entidad-relación?", [
    "a) Por la cantidad de datos almacenados.",
    "b) Por la estructura bidimensional.",
    "c) Por la presencia de una tabla enlazada.",
    "d) Por su naturaleza conceptual o lógica."
], "d"),
("¿Cómo se relaciona una relación en el modelo relacional con las entidades o asociaciones del modelo E-R?", [
    "a) No hay relación entre ambas.",
    "b) Una relación en el modelo relacional es siempre una entidad en el modelo E-R.",
    "c) Una relación en el modelo relacional puede representar una entidad o asociación del modelo E-R.",
    "d) Las relaciones en ambos modelos son idénticas."
], "c"),
("¿Cuál es la equivalencia de las tuplas en una relación del modelo relacional con el modelo E-R?", [
    "a) Las tuplas no tienen equivalencia en el modelo E-R.",
    "b) Cada tupla equivale a una entidad del modelo E-R.",
    "c) Las tuplas equivalen a las asociaciones del modelo E-R.",
    "d) Las tuplas equivalen a las ocurrencias del modelo E-R."
], "d"),
("¿Cuál es la función de los atributos en una relación del modelo relacional?", [
    "a) Representan las ocurrencias del modelo E-R.",
    "b) Representan las entidades del modelo E-R.",
    "c) Representan las propiedades de los elementos.",
    "d) Equivalen a las asociaciones del modelo E-R."
], "c"),
("¿Cómo podemos definir una relación en el modelo relacional?", [
    "a) Por la cantidad de tuplas que contiene.",
    "b) Por la cantidad de atributos que posee.",
    "c) Por su extensión o su intensión.",
    "d) Por su grado o cardinalidad."
], "c"),
("¿Qué representa la extensión en el contexto de una relación en el modelo relacional?", [
    "a) La cantidad de tuplas de la relación.",
    "b) La cantidad de atributos de la relación.",
    "c) La secuencia de tuplas que componen la relación en un momento dado.",
    "d) El grado o cardinalidad de la relación."
], "c"),
("¿Qué representa la intensión en el contexto de una relación en el modelo relacional?", [
    "a) La cantidad de tuplas de la relación.",
    "b) La secuencia de tuplas que componen la relación en un momento dado.",
    "c) Las características que deben cumplir los elementos para pertenecer a la relación.",
    "d) El grado o cardinalidad de la relación."
], "c"),
("¿Cómo se define la intensión en el contexto del modelo relacional?", [
    "a) Por la cantidad de tuplas de la relación.",
    "b) Por la secuencia de tuplas que componen la relación en un momento dado.",
    "c) Por las características semánticas de sus elementos.",
    "d) Por el grado o cardinalidad de la relación."
], "c"),
("¿Cómo se representa formalmente una relación en el modelo relacional?", [
    "a) R{A}",
    "b) R(A)",
    "c) R[A]",
    "d) R/A"
], "b"),
("¿Cómo se implementa una relación en el modelo relacional?", [
    "a) En forma de grafo",
    "b) En forma de árbol",
    "c) En forma de lista enlazada",
    "d) Como un archivo lineal simple"
], "d"),
("¿Cómo se llama cada fila de una tabla en el modelo relacional?", [
    "a) Registro",
    "b) Entidad",
    "c) Tupla",
    "d) Nodo"
], "c"),
("¿Cómo se llama cada columna de una tabla en el modelo relacional?", [
    "a) Registro",
    "b) Campo",
    "c) Atributo",
    "d) Nodo"
], "c"),
("¿Qué representa el término 'cardinalidad' en el contexto del modelo relacional?", [
    "a) Número de campos de una tabla",
    "b) Número de filas en una tabla",
    "c) Número de atributos en una relación",
    "d) Número de dominios en una relación"
], "b"),
("¿Por qué la cardinalidad se considera variable en el contexto del modelo relacional?", [
    "a) Porque el número de campos puede cambiar",
    "b) Porque el número de atributos puede cambiar",
    "c) Porque el número de registros puede cambiar",
    "d) Porque el número de relaciones puede cambiar"
], "c"),
("¿Qué representa el grado en el contexto del modelo relacional?", [
    "a) Número de filas de la tabla",
    "b) Número de atributos de la tabla",
    "c) Número de registros de la tabla",
    "d) Número de campos de la tabla"
], "b"),
("¿Cómo se define el dominio de un atributo en el contexto del modelo relacional?", [
    "a) Como el número de filas de la tabla",
    "b) Como el número de atributos de la tabla",
    "c) Como el número de registros de la tabla",
    "d) Como el conjunto de valores que puede tomar ese atributo"
], "d"),
("En el contexto del modelo relacional, ¿cómo se clasifican los dominios de atributos?", [
    "a) Como registros y entidades",
    "b) Como generales y restringidos",
    "c) Como claves primarias y foráneas",
    "d) Como atributos y relaciones"
], "b"),
("En el contexto del modelo relacional, ¿cómo se describen los dominios generales de atributos?", [
    "a) Como combinaciones de valores con características comunes",
    "b) Como valores pertenecientes a un conjunto discreto",
    "c) Como claves primarias",
    "d) Como atributos restringidos"
], "a"),
("En el contexto del modelo relacional, ¿cómo se describiría el dominio del atributo 'Garantía', que refleja un número comprendido entre 3 y 18 que representa el número de meses mínimo y máximo que ofrece un concesionario?", [
    "a) Como atributo general",
    "b) Como atributo restringido",
    "c) Como atributo numeral",
    "d) Ninguna de las anteriores"
], "a"),
("En el contexto del modelo relacional, ¿cómo se describiría un atributo restringido?", [
    "a) Como combinaciones de valores con características comunes",
    "b) Como valores pertenecientes a un conjunto discreto",
    "c) Como claves primarias",
    "d) Como atributos que no pueden formar parte de la relación"
], "b"),
("En el contexto del modelo relacional, ¿cómo se describiría el dominio del atributo 'Sexo', que refleja solo como únicos valores 'masculino' y 'femenino'?", [
    "a) Como atributo general",
    "b) Como atributo restringido",
    "c) Como atributo numeral",
    "d) Ninguna de las anteriores"
], "b"),
("¿Cómo se define la 'Clave aspirante o candidata' en el contexto del modelo relacional?", [
    "a) Como un conjunto mínimo de atributos que identifican univocamente cada fila de una relación",
    "b) Como un conjunto mínimo de atributos que podrían identificar univocamente cada fila de una relación",
    "c) Como una restricción sobre los atributos para identificar univocamente cada fila de una relación",
    "d) Como un conjunto mínimo de atributos que podrían identificar univocamente cada columna de una relación"
], "a"),
("¿Cómo se define la 'Clave principal o primaria' en el contexto del modelo relacional?", [
    "a) Como un conjunto mínimo de atributos que identifican univocamente cada fila de una relación",
    "b) Como la combinación de valores en una relación",
    "c) Como una restricción sobre los atributos",
    "d) Como la clave candidata elegida como clave de la relación"
], "d"),
("¿Cuál es la función de una 'Clave externa o foránea o ajena' en el modelo relacional?", [
    "a) Identifica unívocamente cada fila de una relación",
    "b) Sirve como clave principal de una relación",
    "c) Relaciona una relación con otra mediante un campo de unión",
    "d) Establece la estructura de la relación"
], "c"),
("¿Cuántos tipos de tuplas o registros puede tener una tabla en una base de datos relacionada?", [
    "a) Solo uno",
    "b) Dos",
    "c) Cualquiera",
    "d) Varía según la tabla"
], "a"),
("¿Qué requisito cumple un campo o atributo en una tabla de base de datos relacionada?", [
    "a) Puede tener varios dominios",
    "b) Tiene un único dominio",
    "c) Puede tener un número variable de dominios",
    "d) No tiene dominio"
], "b"),
("¿Cómo están ordenados los registros dentro de una tabla en una base de datos relacionada?", [
    "a) Están ordenados alfabéticamente",
    "b) Están ordenados numéricamente",
    "c) No tienen un orden determinado",
    "d) Están ordenados según la fecha de inserción"
], "c"),
("¿Qué relación existe entre campos procedentes de dos o más tablas en una base de datos relacionada?", [
    "a) Complementarios",
    "b) Exclusivos",
    "c) Relacionados",
    "d) Independientes"
], "c"),
("¿Qué característica tiene cada registro en una tabla de una base de datos relacionada?", [
    "a) Un número variable de campos",
    "b) Un número fijo de campos",
    "c) Campos sin nombre",
    "d) Campos ordenados alfabéticamente"
], "b"),
("¿Cuántas tablas suele contener generalmente una base de datos relacionada?", [
    "a) Solo una tabla",
    "b) Varias tablas, una por cada tipo de registro",
    "c) Una tabla para todos los registros",
    "d) Dependiendo del número de registros"
], "b"),
("¿Qué requisito debe cumplir cada campo o atributo de una tabla en una base de datos relacionada?", [
    "a) Puede tener varios dominios",
    "b) No necesita tener un dominio",
    "c) Debe tener un único dominio",
    "d) Puede tener el mismo dominio que otros campos"
], "c"),
("¿Cómo se caracteriza la secuencia de los registros dentro de una tabla en una base de datos relacionada?", [
    "a) Están ordenados de forma ascendente",
    "b) Están ordenados de forma descendente",
    "c) No tienen una secuencia determinada",
    "d) Están ordenados alfabéticamente"
], "c"),
("¿Cómo se caracterizan los atributos dentro de un registro en una tabla de una base de datos relacionada?", [
    "a) Están ordenados alfabéticamente",
    "b) Están ordenados de forma ascendente",
    "c) Están ordenados de forma descendente",
    "d) No están ordenados"
], "d"),
("¿Qué afirmación es correcta sobre la presencia de tuplas y atributos duplicados en una tabla de una base de datos relacionada?", [
    "a) Pueden existir tuplas duplicadas",
    "b) Pueden existir atributos duplicados",
    "c) No pueden existir tuplas ni atributos duplicados",
    "d) Solo pueden existir tuplas duplicadas"
], "c"),
("¿Qué requisito asegura que cada celda en una tabla de una base de datos relacionada contiene un valor único que pertenece al dominio de la columna correspondiente?", [
    "a) No pueden existir tuplas ni atributos duplicados",
    "b) Cada intersección fila-columna puede contener valores duplicados",
    "c) Cada intersección fila-columna debe contener un valor único",
    "d) Las tablas no tienen este requisito"
], "c"),
("¿Qué sucede con cada tipo de entidad al convertirse al modelo relacional?", [
    "a) Se convierte en un nuevo tipo de entidad",
    "b) Se convierte en una relación o tabla",
    "c) Se convierte en un atributo",
    "d) Se convierte en una cardinalidad"
], "b"),
("¿Cómo se nombra la tabla resultante de la transformación de una entidad?", [
    "a) Con un nombre completamente nuevo",
    "b) Con el nombre de la relación",
    "c) Con un nombre aleatorio",
    "d) Con el nombre de la base de datos"
], "b"),
("¿Cómo se transforman los atributos de una entidad en el modelo relacional?", [
    "a) Se eliminan",
    "b) Se convierten en filas",
    "c) Se convierten en columnas de la relación",
    "d) Se combinan en una única columna"
], "c"),
("¿Qué se convierte en identificadores candidatos en el modelo relacional?", [
    "a) Atributos",
    "b) Tuplas",
    "c) Relaciones",
    "d) Claves primarias"
], "a"),
("¿Cómo se representa el identificador principal en el modelo relacional?", [
    "a) Con negrita",
    "b) En cursiva",
    "c) Subrayado",
    "d) Con comillas"
], "c"),
("¿Cómo se representa el identificador alternativo en el modelo relacional?", [
    "a) Con negrita",
    "b) En cursiva",
    "c) Con un guion bajo (subrayado)",
    "d) Con comillas"
], "a"),
("¿Cómo se representan los atributos opcionales en el modelo relacional?", [
    "a) Subrayados",
    "b) Con un asterisco (*)",
    "c) Con un signo de interrogación (?)",
    "d) Con una virgulilla (~)"
], "b"),
("¿Cómo se tratan los atributos compuestos en el modelo relacional?", [
    "a) Se descomponen en los atributos que lo componen",
    "b) Se representan con un símbolo especial",
    "c) Se eliminan",
    "d) Se fusionan en un solo atributo"
], "a"),
("¿Cómo se tratan los atributos derivados en el modelo relacional?", [
    "a) Se mantienen como atributos ordinarios",
    "b) Se eliminan",
    "c) Se representan con un símbolo especial",
    "d) Se descomponen"
], "a"),
("¿Qué ocurre con los atributos multivaluados de una entidad ER en el modelo relacional?", [
    "a) Se eliminan",
    "b) Se mantienen como atributos multivaluados",
    "c) Se creará una nueva relación",
    "d) Se descomponen"
], "c"),
("En la nueva relación que se crea para los atributos multivaluados de una entidad ER, ¿qué incluirá el identificador principal de la nueva relación?", [
    "a) Solo los atributos multivaluados",
    "b) Solo los atributos del identificador principal de la entidad",
    "c) Todos los atributos",
    "d) Ninguna de las anteriores"
], "c"),
("En el caso de entidades débiles, ¿qué se debe incluir como clave foránea en la nueva relación del modelo relacional?", [
    "a) Solo los atributos multivaluados",
    "b) Solo los atributos del identificador principal de la entidad",
    "c) Todos los atributos, incluyendo los multivaluados",
    "d) Ninguna de las anteriores"
], "b"),
("Si una entidad es débil por identificación, ¿cómo estará formada la clave principal en la relación del modelo relacional?", [
    "a) Solo por los atributos multivaluados",
    "b) Solo por los atributos del identificador principal de la entidad débil",
    "c) Por los atributos de clave foránea más los atributos que formen la clave parcial de la entidad débil",
    "d) Ninguna de las anteriores"
], "c"),
("En el modelo relacional, ¿cómo se indicará la clave foránea que hace referencia a la clave principal de otra tabla?", [
    "a) Con un asterisco (*)",
    "b) Con un número entero positivo que coincida con el número asociado a la tabla principal",
    "c) Con una flecha hacia abajo",
    "d) Con una flecha hacia la tabla principal"
], "d"),
("¿Cómo se transforma un tipo de interrelación N:M en el modelo relacional?", [
    "a) Se convierte en un atributo",
    "b) Se convierte en una nueva entidad",
    "c) Se convierte en una relación nueva",
    "d) Se elimina"
], "c"),
("¿Cómo se forma la clave primaria de la relación al transformar un tipo de interrelación N:M en el modelo relacional?", [
    "a) Se forma con los atributos de las entidades involucradas",
    "b) Se forma con los identificadores principales de las entidades involucradas",
    "c) No tiene clave primaria",
    "d) Se forma con una clave foránea"
], "b"),
("¿Cómo se trata la clave primaria de la relación al transformar un tipo de interrelación N:M en el modelo relacional?", [
    "a) Todas son incorrectas",
    "b) Se forma con un nuevo identificador",
    "c) Cada uno de ellos será a su vez una clave foránea",
    "d) No tiene clave primaria"
], "c"),
("¿Qué sucede adicionalmente al transformar un tipo de interrelación N:M en el modelo relacional?", [
    "a) Se forma con los atributos de las entidades involucradas",
    "b) Tendrá exclusivamente los identificadores de las entidades involucradas, que serán a su vez la clave pimaria en la nueva relación, y a su vez serán claves foráneas",
    "c) Tendrá exclusivamente los identificadores de las entidades involucradas, que serán a su vez la clave pimaria en la nueva relación, pero no serán claves foráneas",
    "d) Tendrá como atributos los propios de la interrelación, dando lugar a nuevas columnas"
], "d"),
("¿Qué sucede al transformar una interrelación 1:N en el modelo relacional?", [
    "a) Se forma una nueva relación con los atributos de las entidades involucradas",
    "b) Se forma una nueva relación con los identificadores principales de las entidades involucradas",
    "c) Se crea una nueva relación donde cada uno de ellos será a su vez una clave foránea",
    "d) No se crea una nueva relación"
], "d"),
("En una relación resultante de una interrelación 1:N en el modelo relacional, ¿cómo se propagan los atributos que conforman la clave del tipo de entidad con cardinalidad máxima 1?", [
    "a) No se propagan, se mantienen solo en la relación original",
    "b) Se propagan a la relación correspondiente al tipo de entidad con cardinalidad máxima N",
    "c) Se mantienen en la entidad con cardinalidad máxima 1",
    "d) Se duplican en ambas relaciones"
], "b"),
("En las interrelaciones 1:N, ¿qué ocurre con los atributos propios de la interrelación al transformarlas al modelo relacional?", [
    "a) No se propagan",
    "b) Se propagan a la entidad con cardinalidad máxima 1",
    "c) Se propagan a la entidad con cardinalidad máxima N",
    "d) Se propagan hacia una nueva relación"
], "c"),
("En las interrelaciones 1:1, ¿qué ocurre al transformarlas al modelo relacional?", [
    "a) Se crea una nueva relación",
    "b) No se crea una nueva relación",
    "c) Se propagan los atributos en ambos sentidos",
    "d) Ninguna es correcta"
], "b"),
("Cuando se transforman interrelaciones 1:1 al modelo relacional, ¿qué ocurre con los atributos que conforman la clave de un tipo de entidad?", [
    "a) Se crean nuevas relaciones",
    "b) No se crea una nueva relación",
    "c) Se propagan a la relación correspondiente al otro tipo de entidad",
    "d) No se propagan en ninguna relación"
], "c"),
("¿La propagación de la clave en las interrelaciones 1:1 puede realizarse en ambos sentidos?", [
    "a) Verdadero",
    "b) Falso"
], "a"),
("En las interrelaciones 1:1, ¿los atributos propios de la interrelación también se propagarán en el mismo sentido que en el que se propagó la clave?", [
    "a) Verdadero",
    "b) Falso"
], "a"),
("En las interrelaciones 1:1, ¿los atributos propios de la interrelación también se propagarán en el mismo sentido?", [
    "a) Verdadero",
    "b) Falso",
    "c) Depende del modelo de base de datos",
    "d) Solo en casos especiales"
], "c"),
("¿Cuál es una solución de transformación de tipos y subtipos (jerarquías) al modelo relacional?", [
    "a) Englobar todos los atributos en una sola relación",
    "b) Crear una relación para el supertipo y tantas relaciones como subtipos",
    "c) Considerar relaciones distintas para cada subtipo",
    "d) Todas las anteriores"
], "d"),
("¿En qué casos se adoptaría la solución de englobar todos los atributos de la entidad y sus subtipos en una sola relación?", [
    "a) Cuando los subtipos tienen muchos atributos diferentes",
    "b) Cuando los subtipos tienen pocos atributos diferentes y las interrelaciones son las mismas para todos o casi todos",
    "c) Cuando los subtipos tienen muchos atributos diferentes y las interrelaciones son las mismas para todos o casi todos",
    "d) Ninguna de las anteriores"
], "b"),
("Tenemos una jerarquía con el tipo 'profesor' y los subtipos 'doctor' y 'no doctor', con una diferencia mínima, pues ambos pueden impartir cursos y tienen los mismos atributos, ¿cuál sería la solución adecuada según el tipo de entidad y sus subtipos?", [
    "a) Crear una relación para el supertipo y tantas relaciones como subtipos haya, con sus atributos correspondientes",
    "b) Considerar relaciones distintas para cada subtipo, que contengan además de los atributos propios, los atributos comunes",
    "c) Englobar todos los atributos de la entidad y sus subtipos en una sola relación, con un atributo discriminante",
    "d) Ninguna de las anteriores"
], "c"),
("En una jerarquía, si hay muchos atributos distintos entre los subtipos y se quieren mantener de todas maneras los atributos comunes a todos ellos en una relación, ¿cuál sería la solución adecuada?", [
    "a) Crear una relación para el supertipo y tantas relaciones como subtipos haya, con sus atributos correspondientes",
    "b) Considerar relaciones distintas para cada subtipo, que contengan además de los atributos propios, los atributos comunes",
    "c) Englobar todos los atributos de la entidad y sus subtipos en una sola relación, con un atributo discriminante",
    "d) Ninguna de las anteriores"
], "a"),
("Si hay muchos atributos distintos entre los subtipos y los accesos realizados sobre los datos de los distintos subtipos siempre afectan a atributos comunes, ¿cuál sería la solución adecuada?", [
    "a) Crear una relación para el supertipo y tantas relaciones como subtipos haya, con sus atributos correspondientes",
    "b) Considerar relaciones distintas para cada subtipo, que contengan además de los atributos propios, los atributos comunes",
    "c) Englobar todos los atributos de la entidad y sus subtipos en una sola relación, con un atributo discriminante",
    "d) Ninguna de las anteriores"
], "b"),
("¿Cuál de las siguientes afirmaciones es correcta?", [
    "a) Las operaciones de inserción nunca afectan a la integridad.",
    "b) Solo las operaciones de modificación pueden afectar a la integridad.",
    "c) Solo las operaciones de borrado pueden afectar a la integridad.",
    "d) Tanto las operaciones de inserción, modificación y borrado pueden afectar a la integridad."
], "d"),
("¿Cuáles son las tres restricciones principales que forman parte del modelo relacional?", [
    "a) Integridad de entidad, integridad de relación e integridad de atributo.",
    "b) Integridad física y entegridad lógica.",
    "c) Integridad conceptual, integridad lógica e integridad física.",
    "d) Integridad de entidad, integridad de clave e integridad referencial."
], "d"),
("En la integridad de entidad en bases de datos, ¿qué afirmación es correcta?", [
    "a) La clave primaria de una relación puede tomar valores nulos o desconocidos.",
    "b) La clave primaria de una relación puede tomar cualquier valor.",
    "c) La clave primaria de una relación no puede tomar valores nulos ni desconocidos.",
    "d) La integridad de entidad no se aplica a las claves primarias."
], "c"),
("En el caso de que la clave primaria esté formada por varios atributos, ¿cómo se aplica la integridad de entidad a cada uno de ellos?", [
    "a) No se aplica la integridad de entidad a claves primarias con varios atributos.",
    "b) Solo se aplica a uno de los atributos de la clave primaria.",
    "c) La integridad de entidad se aplica solo al último atributo de la clave primaria.",
    "d) Se aplica la integridad de entidad a cada uno de los atributos de la clave primaria."
], "d"),
("¿Por qué las clave primaria no puede admitir valores nulos?", [
    "a) Porque algunos sistemas gestores de bases de datos no admiten valores nulos e impediría la independencia física de la base de datos.",
    "b) Porque las tuplas con valor nulo no se almacenan en la base de datos.",
    "c) Si que admite valores nulos, el valor nulo no afecta la identificación de las tuplas en la clave primaria.",
    "d) Porque el valor nulo en la clave primaria impide distinguir las tuplas."
], "d"),
("¿Cómo se puede garantizar que la restricción de que el valor de la clave primaria no sea nulo y forme parte de su dominio se cumpla en cada inserción y modificación en una base de datos?", [
    "a) No es necesario comprobar esta restricción en inserciones o modificaciones.",
    "b) Esta restricción solo se aplica en consultas SELECT.",
    "c) Se debe comprobar en cada inserción y modificación que el valor de la clave primaria no sea nulo y forme parte de su dominio.",
    "d) Esta restricción se aplica automáticamente y no requiere comprobación adicional."
], "c"),
("¿Cuál es la afirmación correcta respecto a la integridad de clave?", [
    "a) Las claves candidatas no deben tomar valores únicos para cada tupla.",
    "b) Las claves candidatas deben tomar valores duplicados para cada tupla.",
    "c) Las claves candidatas deben tomar valores únicos para cada tupla, ya sea la clave primaria o alguna clave alternativa.",
    "d) La integridad de clave solo se aplica a las claves primarias."
], "c"),
("En la integridad referencial de bases de datos, ¿cuál es la condición correcta para las claves foráneas de una relación con respecto a la clave primaria de la relación referenciada?", [
    "a) Las claves foráneas deben tomar valores diferentes de la clave primaria de la relación referenciada.",
    "b) Las claves foráneas deben tomar cualquier valor, incluso si no existe en la clave primaria de la relación referenciada.",
    "c) Las claves foráneas deben tomar valores existentes en la clave primaria de la relación referenciada o valores nulos.",
    "d) Las claves foráneas no tienen relación con la clave primaria de la relación referenciada."
], "c"),
("En el caso de que la clave foránea esté formada por varios atributos, ¿cómo se aplica la integridad referencial a ese grupo completo?", [
    "a) La integridad referencial no se aplica a claves foráneas con varios atributos.",
    "b) Se aplica a un atributo cualquiera de los atributos de la clave foránea.",
    "c) La integridad referencial se aplica solo al último atributo de la clave foránea.",
    "d) Se aplica la integridad referencial al grupo completo de atributos de la clave foránea."
], "d"),
("En una base de datos donde la relación R1 tiene una clave primaria formada por los atributos A1, A2, ... An, y la relación R2 tiene una clave foránea formada por los atributos B1, B2, ...Bn, que referencia a R1, ¿cuál es la condición correcta para los valores de los atributos B1, B2, ...Bn en cada tupla de R2?", [
    "a) Los valores de los atributos B1, B2, ...Bn deben ser siempre nulos.",
    "b) Los valores de los atributos B1, B2, ...Bn pueden ser cualquier valor, independientemente de R1.",
    "c) Los valores de los atributos B1, B2, ...Bn deben existir en una misma tupla de R1 o ser todos nulos.",
    "d) Los valores de los atributos B1, B2, ...Bn no tienen relación con R1."
], "c"),
("En el contexto de referenciar elementos de una relación, ¿cuál de las siguientes afirmaciones es correcta?", [
    "a) Si estamos haciendo referencia a un elemento de una relación, ese elemento debe existir en esa relación.",
    "b) Podemos hacer referencia a cualquier elemento, incluso si no existe en la relación.",
    "c) La existencia o no de un elemento en la relación no afecta al proceso de referencia.",
    "d) No es necesario considerar la existencia de elementos al hacer referencia en una relación."
    "e) b, c y d son correctas."
], "a"),
("Para garantizar la integridad referencial en una base de datos, ¿qué acciones son necesarias?", [
    "a) Solo es necesario comprobar en cada inserción y modificación que el valor de cada clave foránea es nulo.",
    "b) Solo es necesario comprobar en cada inserción y modificación que el valor de cada clave foránea existe en alguna de las tuplas de la relación referenciada.",
    "c) Se debe comprobar en cada inserción y modificación que el valor de cada clave foránea es nulo o existe en alguna de las tuplas de la relación referenciada, y en cada borrado, que el valor de la clave primaria de la tupla a borrar no existe como valor de la clave foránea en otra relación.",
    "d) Solo es necesario comprobar en cada borrado que el valor de la clave primaria de la tupla a borrar no existe como valor de la clave foránea en otra relación."
], "c"),
("En una base de datos donde en la relación IMPARTE aparece un profesor llamado Eduardo y no está presente en la relación PROFESOR, ¿cuál de las siguientes afirmaciones es correcta?", [
    "a) No se violaría ninguna regla de integridad, ya que las claves foráneas en la relación IMPARTE no están relacionadas con la relación PROFESOR.",
    "b) Se violaría la regla de integridad solo si Eduardo es un nuevo profesor que aún no ha sido registrado en la relación PROFESOR.",
    "c) Se violaría la regla de integridad, ya que en la relación IMPARTE los atributos PROFESOR y DISCIPLINA son claves foráneas y deben existir en la relación PROFESOR.",
    "d) No se violaría ninguna regla de integridad, ya que las claves foráneas en la relación IMPARTE permiten valores nulos."
], "c"),
("En una base de datos donde en la relación IMPARTE aparece una disciplina llamada 'Base de datos' y no está presente en la relación DISCIPLINA, ¿cuál de las siguientes afirmaciones es correcta?", [
    "a) No se violaría ninguna regla de integridad, ya que las claves foráneas en la relación IMPARTE no están relacionadas con la relación DISCIPLINA.",
    "b) Se violaría la regla de integridad referencial solo si 'Base de datos' es una nueva disciplina que aún no ha sido registrada en la relación DISCIPLINA.",
    "c) Se violaría la regla de integridad referencial, ya que en la relación IMPARTE los atributos PROFESOR y DISCIPLINA son claves foráneas y deben existir en las relaciones PROFESOR y DISCIPLINA, respectivamente.",
    "d) No se violaría ninguna regla de integridad, ya que las claves foráneas en la relación IMPARTE permiten valores nulos."
], "c"),
("Para mantener la integridad referencial al definir el esquema relacional, ¿qué aspecto debe especificarse con respecto a la operación a realizar al borrar o modificar un registro si este está siendo referenciado desde otro?", [
    "c) No es necesario especificar ninguna operación, ya que la base de datos se encargará automáticamente de mantener la integridad referencial.",
    "b) Solo es necesario especificar la operación a realizar al borrar un registro, no al modificarlo.",
    "a) Debe especificarse la operación a realizar tanto al borrar como al modificar un registro si este está siendo referenciado desde otro.",
    "d) La especificación de operaciones al borrar o modificar un registro referenciado no afecta la integridad referencial."
], "a"),
("En el contexto de la integridad referencial, ¿cómo se describe la operación de Borrado/Modificación en cascada (BC MC)?", [
    "a) La operación BC MC implica el borrado o modificación de un registro, pero no afecta a los registros que lo referencian.",
    "b) La operación BC MC no tiene relación con la integridad referencial.",
    "d) La operación BC MC implica que el borrado o modificación de un registro se traslada a todos los registros que lo referencian.",
    "c) La operación BC MC solo se aplica a la modificación de registros, no al borrado."
], "d"),
("En el contexto de la integridad referencial, ¿cómo se describe la operación de Borrado/Modificación restringido (BR MR)?", [
    "a) La operación BR MR implica el borrado o modificación de un registro y permite que otros registros lo referencien.",
    "b) La operación BR MR no tiene relación con la integridad referencial.",
    "c) La operación BR MR implica que el borrado o modificación de un registro no se permite si algún otro lo referencia.",
    "d) La operación BR MR solo se aplica al borrado de registros, no a la modificación."
], "c"),
("En el contexto de la integridad referencial, ¿cómo se describe la operación de Borrado/Modificación con posta a nulo (BN MN)?", [
    "a) La operación BN MN implica el borrado o modificación de un registro y permite que los valores de la clave ajena de los registros que lo referencian permanezcan sin cambios.",
    "c) La operación BN MN no tiene relación con la integridad referencial.",
    "b) La operación BN MN implica que, al borrar o modificar un registro, se deben establecer a nulo los valores de la clave ajena de los registros que lo referencian.",
    "d) La operación BN MN solo se aplica a la modificación de registros, no al borrado."
], "b"),
("En el contexto de la integridad referencial, ¿cómo se describe la operación de Borrado/Modificación con posta a un valor por defecto (BD MD)?", [
    "a) La operación BD MD implica el borrado o modificación de un registro y permite que los valores de la clave ajena de los registros que lo referencian permanezcan sin cambios.",
    "b) La operación BD MD no tiene relación con la integridad referencial.",
    "c) La operación BD MD implica que, al borrar o modificar un registro, se debe establecer un valor predefinido (valor por defecto) en la clave ajena de los registros que lo referencian.",
    "d) La operación BD MD solo se aplica a la modificación de registros, no al borrado."
], "c"),
("En el modelo relacional, al representar cada clave foránea junto a la flecha que la representa, ¿qué información es necesario indicar en relación a la integridad referencial?", [
    "a) Solo es necesario indicar la operación para la modificación (MC, MR, MN o MD), la operación para el borrado no es relevante.",
    "b) No es necesario indicar ninguna operación, ya que la integridad referencial se mantiene automáticamente.",
    "c) Es necesario indicar tanto la operación para la modificación (MC, MR, MN o MD) como la operación para el borrado (BC, BR, BN o BD).",
    "d) Solo es necesario indicar la operación para el borrado (BC, BR, BN o BD), la operación para la modificación no es relevante."
], "c"),
("En el contexto de la integridad de dominio de atributo, ¿cómo se define el comportamiento de los atributos en una tupla?", [
    "a) Cada atributo de una tupla puede tomar múltiples valores dentro de su dominio.",
    "b) La integridad de dominio de atributo no tiene relación con los valores de los atributos en una tupla.",
    "d) Cada atributo de una tupla solo puede tomar un valor dentro de su dominio, y si un atributo no tiene valor, se considera nulo.",
    "c) En una tupla, los atributos pueden tener valores nulos sin violar la integridad de dominio."
], "d"),
("En el contexto de restricciones que no forman parte del modelo relacional, ¿cuál de las siguientes opciones permite establecer condiciones en los valores de un atributo en función de otros valores del modelo?", [
    "a) CHECKS",
    "b) ASERTIONS",
    "c) TRIGGERS",
    "d) Todas las anteriores"
], "b")






]


######################################################################################

# Función para realizar el test individual (sin cambios)
def realizar_test_individual(nombre_usuario):
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
            puntaje += 3
        elif respuesta_usuario == "paso":
            print("-------------------------")
            print("Has pasado a la siguiente pregunta.\n")
            print("-------------------------\n")
        else:
            print("-------------------------")
            print(f"✖✖✖✖✖✖✖ Respuesta incorrecta. La opción correcta es: {respuesta}\n")
            print("-------------------------\n")
            puntaje -= 1

    print(f"Has completado el test, {nombre_usuario}. Puntuación final: {puntaje}/{len(preguntas) * 3}")

# Función para el modo competitivo 1vs1 (con cambios)
def modo_1vs1():
    nombre_jugador1 = input("Jugador 1, por favor introduce tu nombre: ")
    nombre_jugador2 = input("Jugador 2, por favor introduce tu nombre: ")

    puntaje_jugador1 = 0
    puntaje_jugador2 = 0

    for i, (pregunta, opciones, respuesta) in enumerate(preguntas, 1):
        print(f"\nPregunta {i}: {pregunta}")

        # Jugador 1
        print(f"\nTurno de {nombre_jugador1}:")
        random.shuffle(opciones)
        for opcion in opciones:
            print(opcion)
        respuesta_jugador1 = input("\nTu respuesta: ").strip().lower()

        if respuesta_jugador1 == respuesta:
            print("-------------------------")
            print(f"{nombre_jugador1}, ✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔ +3 ptos ¡respuesta correcta! ✔✔✔")
            print("-------------------------")
            puntaje_jugador1 += 3
        elif respuesta_jugador1 == "paso":
            print("-------------------------")
            print(f"{nombre_jugador1}, has pasado a la siguiente pregunta.\n")
        else:
            print("-------------------------")
            print(f"{nombre_jugador1}, ✖✖✖✖✖✖✖✖✖✖✖✖✖✖ -1 pto Respuesta incorrecta. Restas 1 punto; La opción correcta es: {respuesta}\n")
            print("-------------------------")
            puntaje_jugador1 -= 1

        # Jugador 2
        print(f"\nTurno de {nombre_jugador2}:")
        random.shuffle(opciones)
        for opcion in opciones:
            print(opcion)
        respuesta_jugador2 = input("\nTu respuesta: ").strip().lower()

        if respuesta_jugador2 == respuesta:
            print("-------------------------")
            print(f"{nombre_jugador1}, ✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔ +3 ptos ¡respuesta correcta! ✔✔✔")
            print("-------------------------")
            puntaje_jugador2 += 3
        elif respuesta_jugador2 == "paso":
            print("-------------------------")
            print(f"{nombre_jugador2}, has pasado a la siguiente pregunta.\n")
        else:
            print("-------------------------")
            print(f"{nombre_jugador1}, ✖✖✖✖✖✖✖✖✖✖✖✖✖✖ -1 pto Respuesta incorrecta. Restas 1 punto; La opción correcta es: {respuesta}\n")
            print("-------------------------")
            puntaje_jugador2 -= 1

        # Mostrar marcador después de cada pregunta
        print("==================================================")
        print(f"\nMarcador después de la pregunta {i}:\n{nombre_jugador1}: {puntaje_jugador1} puntos")
        print(f"{nombre_jugador2}: {puntaje_jugador2} puntos")
        print("==================================================")

    print(f"\nFin del juego:\n{nombre_jugador1}, tu puntuación final: {puntaje_jugador1}")
    print(f"{nombre_jugador2}, tu puntuación final: {puntaje_jugador2}")

# Solicitar el nombre del usuario (sin cambios)
nombre_usuario = input("Vamos a aprobar bases de datos. Por favor, introduce tu nombre: ")

# Solicitar el número de preguntas (sin cambios)
num_preguntas = int(input("¿Cuántas preguntas deseas en el test? "))
while num_preguntas > len(preguntas):
    print(f"Lo siento, solo hay {len(preguntas)} preguntas disponibles.")
    num_preguntas = int(input("Por favor, elige un número igual o menor: "))

# Mezclar las preguntas en orden aleatorio (sin cambios)
random.shuffle(preguntas)
preguntas = preguntas[:num_preguntas]

# Preguntar al usuario si desea modo individual o competitivo (sin cambios)
modo = input("¿Quieres jugar en modo individual (i) o competitivo 1vs1 (c)? ").lower()

if modo == "i":
    # Ejecutar el test individual (sin cambios)
    print("✵------------BASE DE DATOS UNIDAD 3 -PDF 1------------✵")
    print(f"Muy bien, {nombre_usuario}! Comencemos con tu test de {num_preguntas} preguntas.")
    realizar_test_individual(nombre_usuario)
elif modo == "c":
    # Ejecutar el modo competitivo 1vs1 (con cambios)
    modo_1vs1()
else:
    print("Modo no válido. Por favor, selecciona 'i' para modo individual o 'c' para competitivo 1vs1.")
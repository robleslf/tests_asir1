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
nombre_usuario = input("Vamos a aprobar bases de datos. Por favor, introduce tu nombre: ")

# Solicitar el número de preguntas
num_preguntas = int(input("¿Cuántas preguntas deseas en el test? "))
while num_preguntas > len(preguntas):
    print(f"Lo siento, solo hay {len(preguntas)} preguntas disponibles.")
    num_preguntas = int(input("Por favor, elige un número igual o menor: "))

# Mezclar las preguntas en orden aleatorio
random.shuffle(preguntas)
preguntas = preguntas[:num_preguntas]

# Ejecutar el test
print(f"Muy bien, {nombre_usuario}! Comencemos con tu test de {num_preguntas} preguntas.")
realizar_test()
import random

# Lista de preguntas y respuestas
preguntas = [
    ("¿Cuál es el objetivo del desarrollo de un esquema de base de datos relacional, según el texto?", [
    "a) Crear una representación inexacta de los datos.",
    "b) Generar datos sin restricciones.",
    "c) Crear una representación precisa y adecuada de los datos, sus relaciones y restricciones.",
    "d) Desarrollar un esquema sin representación de datos."
], "c"),
("¿Cómo se realizará la representación de la información en un esquema de base de datos relacional, según el texto?", [
    "a) Con un conjunto de esquemas sin relaciones.",
    "b) A través de esquemas de relación que permitirán almacenar la información del minimundo con redundancias.",
    "c) Sin utilizar esquemas de relación.",
    "d) Almacenando información sin considerar problemas de actualización o incoherencias."
], "b"),
("¿Qué llamamos Esquema relacional de la Base de Datos, según el texto?", [
    "a) El conjunto de todas las restricciones.",
    "b) El conjunto conceptual de todas las tablas.",
    "c) El conjunto de todas las relaciones.",
    "d) El conjunto de todas las consultas."
], "c"),
("¿Qué es la normalización, según el texto?", [
    "a) Una técnica para obtener un conjunto de restricciones en una organización.",
    "b) Un proceso de desorganización de datos.",
    "c) Una técnica que, a partir de los requisitos de datos de una organización, permite obtener un conjunto de relaciones con propiedades deseables y que representen lógicamente esos datos.",
    "d) Un método para representar datos ilógicos."
], "c"),
("¿Cómo se obtiene la representación conceptual de un sistema a partir de la descripción del sistema a modelar, según el texto?", [
    "a) A través de la normalización.",
    "b) Utilizando un modelo de bases de datos no relacional.",
    "c) Mediante un modelo ER extendido.",
    "d) Sin representación conceptual."
], "c"),
("¿Cómo se obtiene la representación lógica de un sistema a partir del esquema conceptual, según el texto?", [
    "a) Utilizando un modelo ER extendido.",
    "b) A través de la normalización.",
    "c) Mediante un modelo de bases de datos no relacional.",
    "d) A partir del modelo relacional."
], "d"),
("¿Qué problemas pueden existir en el modelo relacional obtenido, según el texto?", [
    "a) No puede haber problemas en el modelo relacional.",
    "b) Solo puede haber redundancias.",
    "c) Pueden existir redundancias, dependencias, entre otros.",
    "d) El modelo relacional siempre es óptimo."
], "c"),
("¿Cómo se podría definir la normalización de manera sencilla, según el texto?", [
    "a) Como el proceso de aumentar la redundancia en los datos.",
    "b) Como el proceso de desorganizar y desestructurar los datos.",
    "c) Como el proceso de organizar y estructurar los datos de forma que se maximice la redundancia.",
    "d) Como el proceso de organizar y estructurar los datos de forma que se minimice la redundancia."
], "d"),
("¿En qué se basa el proceso de normalización, según el texto?", [
    "a) En aumentar el riesgo de tener un diseño de base de datos defectuoso.",
    "b) En ignorar las reglas de normalización.",
    "c) En un conjunto de pautas, las reglas de normalización, que disminuyen el riesgo de tener un diseño de base de datos defectuoso.",
    "d) En no seguir ninguna regla o pauta."
], "c"),
("¿A qué se aplican las reglas de normalización, según el texto?", [
    "a) Al modelo ER extendido.",
    "b) Al modelo conceptual de bases de datos.",
    "c) A cualquier modelo de bases de datos.",
    "d) Al modelo relacional de la base de datos, normalmente obtenido a partir del modelo entidad-interrelación."
], "d"),
("¿Qué tipo de pautas se seguirán para la revisión del modelo, según el texto?", [
    "a) Solo pautas formales.",
    "b) Solo pautas informales.",
    "c) Pautas exclusivamente definidas por el diseñador.",
    "d) Pueden ser pautas formales e informales."
], "d"),
("¿Cuál es una pauta informal para la revisión del modelo, según el texto?", [
    "a) Utilizar esquemas de relación complicados.",
    "b) Diseñar esquemas de relación con significado difícil de entender.",
    "c) Difuminar el significado de los esquemas de relación.",
    "d) Diseñar esquemas de relación con significado fácil de entender y claras."
], "d"),
("¿Qué pautas informales se deben considerar para la revisión del modelo en términos de eficiencia de consulta y aprovechamiento de espacio en disco, según el texto?", [
    "a) Solo eficiencia de consulta.",
    "b) Solo aprovechamiento de espacio en disco.",
    "c) Eficiencia de consulta e independencia de datos.",
    "d) Eficiencia de consulta y aprovechamiento de espacio en disco."
], "d"),
("¿Cuál es una de las puatas informales de la normalización en relación con las tuplas, según el texto?", [
    "a) Aumentar la redundancia en los valores de las tuplas.",
    "b) Mantener valores redundantes en las tuplas.",
    "c) Reducir valores redundantes en las tuplas para evitar anomalías de actualización, facilitando el mantenimiento y la evolución del diseño.",
    "d) Ignorar los valores en las tuplas."
], "c"),
("¿Por qué es importante una buena selección de claves en el proceso de normalización, según el texto?", [
    "a) No tiene importancia en el proceso de normalización.",
    "b) Solo para la optimización de espacio en disco.",
    "c) Para facilitar la redundancia en las tuplas.",
    "d) Para mejorar la calidad del diseño y evitar problemas en la actualización de datos."
], "d"),
("¿Por qué se busca la reducción de valores nulos en las tuplas durante el proceso de normalización, según el texto?", [
    "a) Porque los valores nulos producen demasiada desinformación.",
    "b) Para facilitar las operaciones con valores nulos.",
    "c) Porque los valores nulos desperdician espacio de almacenamiento y dificultan las operaciones.",
    "d) Para incrementar la cantidad de valores nulos en las tuplas."
], "c"),
("¿En qué se basa el proceso de normalización al aplicar técnicas formales, según el texto?", [
    "a) En ignorar la clave primaria.",
    "b) En identificar relaciones basándose en sus atributos secundarios.",
    "c) En identificar relaciones basándose en la clave primaria (o candidatas en la FNBC) y en las dependencias funcionales entre sus atributos.",
    "d) En desconsiderar las dependencias funcionales."
], "c"),
("¿Por qué se puede normalizar el esquema relacional de la base de datos hasta una forma normal específica, según el texto?", [
    "a) Para incrementar las propiedades no deseadas.",
    "b) Para complicar el esquema relacional.",
    "c) Para evitar propiedades no deseadas.",
    "d) Porque la normalización no afecta las propiedades del esquema."
], "c"),
("¿Cómo se clasifican las formas normales, según el texto?", [
    "a) 1ª, 2ª, 3ª y 4ª Forma Normal.",
    "b) 1ª, 2ª, 3ª y BNFC.",
    "c) 1ª, 2ª, 3ª, BCNF, 4ª, 5ª y 6ª Forma Normal.",
    "d) 2ª, 3ª, 4ª, BCNF y 5ª Forma Normal."
], "c"),
("¿Cuál es el objetivo de la 1ª, 2ª, 3ª Forma Normal y BNFC, según el texto?", [
    "a) Incrementar la posibilidad de anomalías de actualización.",
    "b) Fortalecer la definición de la 3FN basadas en dependencias funcionales.",
    "c) Eliminar la posibilidad de anomalías de actualización.",
    "d) Crear dependencias funcionales en los atributos clave."
], "c"),
("¿Cómo se resumen las formas normales 1ª, 2ª, 3ª y BNFC, según el texto?", [
    "a) Requieren que todos los atributos clave sean dependientes de otros atributos no clave.",
    "b) Requieren que todos los atributos no clave sean dependientes de la clave completa y nada más que la clave.",
    "c) No establecen ninguna restricción sobre la dependencia de los atributos.",
    "d) Requieren que los atributos no clave sean independientes de la clave."
], "b"),
("¿En qué se basan la 4ª y 5ª Forma Normal, según el texto?", [
    "a) En dependencias funcionales.",
    "b) En dependencias multivaluadas y de reunión, respectivamente.",
    "c) En dependencias parciales y totales.",
    "d) En dependencias transitivas."
], "b"),
("¿En qué se basa la 6ª Forma Normal, según el texto?", [
    "a) En dependencias funcionales.",
    "b) En dependencias multivaluadas.",
    "c) En la existencia de más de dos claves candidatas en una tabla, lo que implica crear otras tablas con estos atributos clave.",
    "d) En la dependencia de atributos no clave."
], "c"),
("¿Cuál es el efecto de las últimas formas normales (4ª, 5ª y 6ª), según el texto?", [
    "a) Aumentan las anomalías de actualización excepcionales.",
    "b) No afectan las anomalías de actualización.",
    "c) Eliminan anomalías de actualización excepcionales.",
    "d) Introducen anomalías de actualización excepcionales."
], "c"),
("¿Cómo son las formas normales en términos de restricciones, según el texto?", [
    "a) Cada forma normal es independiente de las demás.",
    "b) Si se cumple la forma normal n-ésima, no necesariamente se cumple la (n-1)-ésima.",
    "c) Si se cumple la forma normal n-ésima, se cumple automáticamente la (n-1)-ésima.",
    "d) Las formas normales no imponen restricciones."
], "c"),
("¿Cuál es el consenso (más o menos) en cuanto a la normalización de tablas en bases de datos, según el texto?", [
    "a) Normalizar hasta la 4FN o 5FN es preferible para mejorar el rendimiento.",
    "b) Normalizar hasta la 3FN o superior es preferible, ya que bases en 4FN o 5FN tienen un rendimiento peor.",
    "c) Cuanto más normalizada una base de datos, mejor rendimiento.",
    "d) No hay consenso en la normalización de tablas en bases de datos."
], "b"),
("¿Qué forma normal se considera como obligatoria para cualquier diseñador, según el texto?", [
    "a) Primera Forma Normal (1FN).",
    "b) Segunda Forma Normal (2FN).",
    "c) Forma Normal de Boyce-Codd (FNBC).",
    "d) Cuarta Forma Normal (4FN)."
], "c"),
("¿Cuáles son los principales objetivos del proceso de normalización, según el texto?", [
    "a) Incrementar la redundancia de datos.",
    "b) Complicar el modelo de datos para los usuarios.",
    "c) Proporcionar independencia de la integridad de datos.",
    "d) Evitar la redundancia de datos, proteger la integridad, eliminar anomalías y facilitar el entendimiento del modelo de datos."
], "d"),
("¿Cuál de los siguientes es un objetivo principal de la normalización: Evitar la redundancia de datos?", [
    "a) Incrementar la redundancia de datos.",
    "b) Facilitar la duplicación de datos para mejorar el rendimiento.",
    "c) Reducir la normalización para simplificar el modelo de datos.",
    "d) Evitar la redundancia de datos y mejorar la eficiencia de las consultas."
], "d"),
("¿Cuál de los siguientes es un objetivo principal de la normalización: Proteger y dar un mejor soporte a la integridad de los datos?", [
    "a) Minimizar la protección de los datos para facilitar el acceso.",
    "b) Reducir el soporte a la integridad para aumentar la velocidad de las operaciones de la base de datos.",
    "c) Proporcionar independencia de datos sin considerar la integridad.",
    "d) Proteger y brindar un mejor soporte a la integridad de los datos."
], "d"),
("¿Cuál de los siguientes es un objetivo principal de la normalización: Eliminar las anomalías en los datos, tanto en las actualizaciones como en las inserciones y los borrados?", [
    "a) Fomentar las anomalías para mejorar la flexibilidad en la gestión de datos.",
    "b) Aceptar y mantener las anomalías para facilitar las operaciones de la base de datos.",
    "c) Eliminar las anomalías en las actualizaciones, pero permitirlas en las inserciones y borrados.",
    "d) Eliminar las anomalías en los datos, tanto en las actualizaciones como en las inserciones y los borrados."
], "d"),
("¿Cuál de los siguientes es un objetivo principal de la normalización: Reducir en la medida posible el rediseño de la base de datos cuando esta se amplía?", [
    "a) Promover un rediseño frecuente para mantener la flexibilidad.",
    "b) Aceptar un rediseño completo en cada ampliación para mejorar la adaptabilidad.",
    "c) Minimizar la adaptabilidad para evitar cambios en la estructura de la base de datos.",
    "d) Reducir en la medida posible el rediseño de la base de datos cuando esta se amplía."
], "d"),
("¿Cuál de los siguientes es un objetivo principal de la normalización: Hacer más entendible el modelo de datos a quienes lo van a utilizar, ya que se modeliza mejor la realidad y el dominio del problema?", [
    "a) Complicar el modelo de datos para mejorar la complejidad de la base de datos.",
    "b) Modelizar de manera abstracta para facilitar la interpretación por parte de los usuarios.",
    "c) Minimizar la representación de la realidad para simplificar el entendimiento.",
    "d) Hacer más entendible el modelo de datos a quienes lo van a utilizar, modelizando mejor la realidad y el dominio del problema."
], "d"),
("¿Cuál de los siguientes es un objetivo principal de la normalización: Proporcionar independencia de los lenguajes específicos para la consulta de datos?", [
    "a) Limitar la consulta de datos a un lenguaje específico para mejorar la consistencia.",
    "b) Favorecer la dependencia de lenguajes específicos para la consulta de datos.",
    "c) Reducir la independencia de los lenguajes para simplificar el acceso a la base de datos.",
    "d) Proporcionar independencia de los lenguajes específicos para la consulta de datos."
], "d"),
("¿Cuál de los siguientes NO es uno de los objetivos principales de la normalización?", [
    "a) Evitar la redundancia de datos.",
    "b) Mejorar el rendimiento de la base de datos.",
    "c) Proteger e dar un mejor soporte a la integridad de los datos.",
    "d) Eliminar las anomalías en los datos."
], "b"),
("¿Cuáles son algunas de las dificultades asociadas con bases de datos mal diseñadas?", [
    "a) Exceso de redundancia de datos, imposibilidad de almacenar cierta información y pérdida no deseada de información al modificar/borrar tuplas base.",
    "b) Ausencia de atributos multivaluados, relaciones sin atributos y sobreuso de jerarquías.",
    "c) Mayor flexibilidad en la manipulación de datos.",
    "d) Facilidad para almacenar toda la información necesaria."
], "a"),
("¿Cómo las bases de datos mal diseñadas pueden dar lugar a anomalías de actualización?", [
    "a) Provocando eficiencia en la manipulación de datos.",
    "b) Generando consistencia semántica y evitando errores.",
    "c) Creando redundancia de datos y riesgo de errores en las actualizaciones.",
    "d) Facilitando un diseño robusto y libre de problemas."
], "c"),
("¿Qué riesgo de inconsistencia puede surgir cuando hay datos redundantes y no se modifican todas las apariciones de esos datos?", [
    "a) Aumento de la eficiencia en la manipulación de datos.",
    "b) Consistencia semántica y prevención de errores.",
    "c) Inconsistencias en los datos si no se actualizan todas las apariciones.",
    "d) Diseño robusto y libre de problemas."
], "c"),
("¿Qué problema puede surgir al modificar tuplas base en una base de datos mal diseñada?", [
    "a) Mejora en la consistencia semántica y prevención de errores.",
    "b) Aumento de la eficiencia en la manipulación de datos.",
    "c) Pérdida de información no deseada.",
    "d) Diseño robusto y libre de problemas."
], "c"),
("¿Cuál es el enfoque recomendado para resolver problemas de almacenamiento redundante y evitar anomalías en una base de datos?", [
    "a) Minimizar la eficiencia en la manipulación de datos.",
    "b) Realizar un diseño E-R sin normalización.",
    "c) Seguir los pasos para obtener relaciones a partir del modelo E-R y normalizar las relaciones obtenidas.",
    "d) Aumentar el grado de vulnerabilidad de las tablas."
], "c"),
("¿Cómo se define una dependencia funcional en una relación?", [
    "c) Es una relación física entre los atributos.",
    "b) Es una restricción que impide la conexión entre atributos en una relación.",
    "a) Es una restricción entre atributos donde los valores de un conjunto determinan los valores de otro conjunto.",
    "d) Es una conexión directa entre dos atributos en una relación."
], "a"),
("En una dependencia funcional, ¿cuál es el primer conjunto que se denomina como determinante y cuál es el segundo como dependiente?", [
    "a) El determinante es el conjunto de atributos que depende del otro.",
    "b) El dependiente es el conjunto de atributos que determina el otro.",
    "c) El determinante es el conjunto de atributos que determina el otro.",
    "d) El dependiente es el conjunto de atributos que depende del otro."
], "c"),
("¿Cómo se describe la propiedad de una dependencia funcional en relación al contenido semántico de los datos?", [
    "a) La dependencia funcional es opcional y puede no cumplirse para algunas extensiones de la relación.",
    "b) La dependencia funcional es una propiedad externa que no afecta al contenido semántico de los datos.",
    "c) La dependencia funcional es inherente al contenido semántico de los datos y debe cumplirse para cada extensión de la relación.",
    "d) La dependencia funcional solo se aplica a ciertos tipos de datos específicos."
], "c"),
("¿Cómo se puede afirmar la existencia de una dependencia funcional en relación al contenido semántico de los datos?", [
    "c) La existencia de una dependencia funcional puede demostrarse mediante técnicas matemáticas avanzadas.",
    "b) La existencia de una dependencia funcional se demuestra a través de pruebas de rendimiento en la base de datos.",
    "a) La existencia de una dependencia funcional no puede ser demostrada, pero se puede afirmar mediante la observación de la realidad y el significado de los datos.",
    "d) La existencia de una dependencia funcional solo se establece a través de la documentación técnica de la base de datos."
], "a"),
("¿Cuál es la función principal de las dependencias funcionales en la descripción de un esquema de relación?", [
    "c) Las dependencias funcionales son solo una característica adicional y no afectan la descripción del esquema de relación.",
    "b) Las dependencias funcionales se utilizan para mejorar el rendimiento de la base de datos.",
    "a) Las dependencias funcionales permiten especificar restricciones sobre atributos para describir de manera más precisa el esquema de relación.",
    "d) Las dependencias funcionales son solo relevantes para la normalización y no afectan la descripción del esquema."
], "a"),


# seguir en pagina 6 con Definición formal de dependencia funcional (DF)







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
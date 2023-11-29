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
("¿Cuál es la definición formal de una dependencia funcional (DF) en un esquema de relación R(A)?", [
    "a) Una dependencia funcional se establece cuando todos los atributos de R son iguales entre dos tuplas t1 y t2.",
    "b) Una dependencia funcional existe entre los subconjuntos de atributos α y β si para todas las tuplas t1 y t2 en R, si los valores de α son iguales, entonces los valores de β también son iguales.",
    "c) La dependencia funcional se representa como α -> β si la relación R tiene exactamente N atributos.",
    "d) La dependencia funcional solo se cumple si α y β son conjuntos vacíos en el esquema de relación R(A)."
], "b"),
("En una dependencia funcional, ¿qué significa que para dos tuplas t1 y t2 en la extensión de una relación r(R), si tienen los mismos valores en los atributos de α, también tendrán los mismos valores en los atributos de β?", [
    "a) Si t1 y t2 tienen los mismos valores en los atributos de α, entonces deben tener diferentes valores en los atributos de β.",
    "b) Si t1 y t2 tienen diferentes valores en los atributos de α, entonces deben tener diferentes valores en los atributos de β.",
    "c) Si t1 y t2 tienen los mismos valores en los atributos de α, entonces deben tener diferentes valores en los atributos de β.",
    "d) La dependencia funcional no establece ninguna relación entre los valores de α y β en las tuplas t1 y t2."
], "c"),
("En el contexto de dependencias funcionales, ¿qué significa que β depende funcionalmente de α?", [
    "a) β y α son independientes entre sí.",
    "b) Cambios en α no afectan a β.",
    "c) α determina funcionalmente los valores de β.",
    "d) β determina funcionalmente los valores de α."
], "c"),
("En el contexto de dependencias funcionales, ¿qué significa que a un valor dado de α le corresponde un único valor de β?", [
    "a) Hay varios valores de β para un valor de α.",
    "b) β y α son independientes.",
    "c) β determina múltiples valores de α.",
    "d) Cada valor de α tiene un único valor correspondiente en β."
], "d"),
("¿Qué característica de las dependencias funcionales destaca el hecho de que se aplica sobre todos los valores posibles de la relación, no solo sobre los actuales?", [
    "a) Extensión",
    "b) Intensión",
    "c) Temporalidad",
    "d) Actualidad"
], "b"),
("En el contexto de las dependencias funcionales, ¿qué significa la afirmación 'dado α no se puede deducir el valor de β'?", [
    "a) α determina funcionalmente a β",
    "b) α no tiene relación con β",
    "c) α y β son independientes",
    "d) β determina funcionalmente a α"
], "c"),
("En el contexto de dependencias funcionales, ¿qué se puede concluir si se afirma que 'siendo diferentes en α pueden ser iguales en β'?", [
    "a) α y β son independientes",
    "b) α determina funcionalmente a β",
    "c) No hay relación entre α y β",
    "d) β determina funcionalmente a α"
], "a"),
("¿Cómo se define la clave de una relación R(A) según las dependencias funcionales?", [
    "a) La clave es un subconjunto de atributos Y tal que Y -> A1, A2, …, An.",
    "b) La clave es el conjunto mínimo de atributos que determina funcionalmente a todos los demás.",
    "c) La clave es el conjunto de todos los atributos A1, A2, …, An.",
    "d) La clave es el subconjunto máximo de atributos que determina funcionalmente a todos los demás."
], "b"),
("¿Cuál es un ejemplo de dependencia funcional?", [
    "a) El DNI depende funcionalmente del nombre de una persona.",
    "b) El nombre de una persona depende funcionalmente del DNI.",
    "c) Existe una dependencia funcional entre el nombre de una persona y su edad.",
    "d) La edad depende funcionalmente del nombre de una persona."
], "b"),
("¿Qué caracteriza al proceso de normalización de una relación?", [
    "a) Somete al esquema de relación a pruebas para mejorar el rendimiento.",
    "b) Somete al esquema de relación a pruebas para certificar si el esquema de relación pertenece a una cierta forma normal.",
    "c) Reduce la cantidad de datos almacenados en la relación.",
    "d) Aumenta la redundancia en el esquema de relación."
], "b"),
("¿Cuál es el resultado del proceso de normalización de datos?", [
    "a) Aumento de la redundancia en los esquemas de relación.",
    "b) Descomposición de esquemas de relación que no cumplen condiciones.",
    "c) Certificación de esquemas de relación sin cambios.",
    "d) Reducción de la independencia de datos en los esquemas."
], "b"),
("¿Qué garantiza el proceso de normalización en relación a las anomalías de actualización?", [
    "a) Aumento de anomalías de actualización.",
    "b) Descomposición de esquemas que previene anomalías de actualización.",
    "c) Certificación de esquemas sin cambios en las anomalías de actualización.",
    "d) Reducción de la consistencia de los datos en los esquemas."
], "b"),
("¿Cómo se expresa formalmente la descomposición en el proceso de normalización?", [
    "a) Se reorganiza directamente la relación R sin proyecciones ni reuniones.",
    "b) Se realiza una serie de proyecciones y reuniones para obtener nuevas relaciones R1, R2, ..., Rn.",
    "c) Se duplican los atributos de la relación R para evitar redundancias.",
    "d) Se eliminan aleatoriamente atributos de la relación R."
], "b"),
("¿Cuáles son las propiedades que debe verificar una buena descomposición en el proceso de normalización?", [
    "a) Pérdida y Modificación de dependencias.",
    "b) Reunión sin pérdida y Conservación de las dependencias.",
    "c) Pérdida y Conservación de las dependencias.",
    "d) Reunión sin pérdida y Modificación de dependencias."
], "b"),
("¿Qué significa la propiedad 'Reunión sin pérdida' en el proceso de normalización?", [
    "a) La extensión de las relaciones normalizadas debe ser más pequeña que la de la relación original.",
    "b) La extensión de las relaciones normalizadas debe permitir obtener todos los valores de todas las tuplas de la relación original.",
    "c) La extensión de las relaciones normalizadas debe contener solo algunos valores de la relación original.",
    "d) La extensión de las relaciones normalizadas no tiene relación con la relación original."
], "b"),
("¿Qué significa la propiedad 'Conservación de dependencias' en el proceso de normalización?", [
    "a) Las dependencias funcionales de la relación original deben eliminarse en las relaciones resultantes.",
    "b) Todas las dependencias funcionales de la relación original deben estar representadas en al menos una de las relaciones resultantes.",
    "c) Las dependencias funcionales no tienen importancia en el proceso de normalización.",
    "d) Solo algunas dependencias funcionales deben conservarse en las relaciones resultantes."
], "b"),
("¿Por qué es importante la propiedad 'Reunión sin pérdida' en el proceso de normalización?", [
    "a) Para eliminar información innecesaria en la relación original.",
    "b) Para garantizar que todas las relaciones resultantes tengan la misma cantidad de tuplas que la relación original.",
    "c) Para reducir la complejidad de las dependencias funcionales.",
    "d) No es importante, ya que algunas pérdidas de información son aceptables en el proceso de normalización."
], "b"),
("¿Qué condición debe cumplir un esquema para estar en la Primera Forma Normal (1FN)?", [
    "a) Todos los atributos deben tener dominios atómicos y multivaluados.",
    "b) Todos los atributos deben tener dominios atómicos y univaluados.",
    "c) Al menos un atributo debe tener dominio multivaluado.",
    "d) No hay condiciones específicas para la 1FN."
], "b"),
("¿Qué significa que un atributo tenga un dominio atómico en el contexto de la Primera Forma Normal (1FN)?", [
    "a) Puede tomar valores compuestos.",
    "b) Puede tomar valores multivaluados.",
    "c) Debe tomar valores únicos y simples.",
    "d) No hay restricciones para los valores del atributo."
], "c"),
("En el contexto de la Primera Forma Normal (1FN), ¿qué restricción se aplica a los atributos en cuanto a sus valores?", [
    "a) Pueden tener valores compuestos.",
    "b) Pueden tener valores multivaluados.",
    "c) Deben tener valores únicos y simples.",
    "d) No hay restricciones para los valores del atributo."
], "c"),
("¿Cuál de las siguientes afirmaciones es verdadera acerca de la Primera Forma Normal (1FN)?", [
    "a) Es una restricción opcional en el modelo relacional.",
    "b) Es una forma normal que permite valores compuestos en los atributos.",
    "c) Es una parte inherente del modelo relacional de datos.",
    "d) No tiene relación con los dominios de los atributos."
], "c"),
("¿Qué característica debe tener un elemento para que un atributo sea considerado atómico?", [
    "a) Ser divisible.",
    "b) Ser un número entero.",
    "c) Ser una unidad indivisible.",
    "d) Ser un valor compuesto."
], "c"),
("¿Cuál de los siguientes ejemplos representa un dominio no atómico en un esquema de relación?", [
    "a) Número entero.",
    "b) Nombre completo (compuesto por nombre y apellidos).",
    "c) Dirección de correo electrónico.",
    "d) Número de teléfono único."
], "b"),
("¿Qué puede depender de los usos que se hagan de los valores de un atributo en un esquema de relación?", [
    "a) El tipo de dato utilizado en el atributo.",
    "b) La longitud del valor almacenado en el atributo.",
    "c) Si el atributo se considera atómico o no.",
    "d) La unicidad de los valores en el atributo."
], "c"),
("¿Qué sucede cuando una relación no cumple con la primera forma normal y se descompone en otras relaciones?", [
    "a) Se pierde información de la relación original.",
    "b) Los atributos se duplican en las nuevas relaciones.",
    "c) Los atributos de la relación original se dividen entre las relaciones resultantes.",
    "d) Se conservan todas las dependencias funcionales de la relación original."
], "c"),
("¿Cuál es la idea principal al descomponer una relación que no cumple con la primera forma normal?", [
    "a) Eliminar todos los atributos de la relación original.",
    "b) Duplicar todos los atributos en la nueva relación.",
    "c) Eliminar el atributo que incumple la 1ª FN y colocarlo en una nueva relación junto con la clave primaria.",
    "d) Conservar solo los atributos atómicos en la relación original."
], "c"),
("En el proceso de normalización para cumplir con la 1ª FN, ¿cuál es la idea principal?", [
    "a) Eliminar la relación original.",
    "b) Duplicar todos los atributos en la nueva relación.",
    "c) Eliminar el atributo que incumple la 1ª FN y colocarlo en una relación diferente junto con la clave primaria de la relación original.",
    "d) Conservar todos los atributos en la relación original."
], "c"),
("En el proceso de normalización para cumplir con la 1ª FN, ¿cuál es un paso clave?", [
    "a) Eliminar la relación original.",
    "b) Duplicar todos los atributos en la nueva relación.",
    "c) Engadir os atributos non atómicos á relación existente.",
    "d) Crear unha nova relación cos atributos que incumpren ser atómico ou son táboas dentro de táboas."
], "d"),
("¿Cuáles son los pasos a seguir para normalizar a 1ª FN?", [
    "a) Crear unha nova relación sen engadir a clave primaria.",
    "b) Duplicar todos los atributos en la nueva relación.",
    "c) Buscar lo valores multivaluados, transformarlos en atributos compuestos, añadir una nueva clase formada por los atributos compuestos y si fuese necesario crear una nueva relación.",
    "d) Crear unha nova relación cos atributos que incumpren ser atómico ou son táboas dentro de táboas, Engadir a esta nova relación a clave primaria da relación que orixinalmente a contiña, Darlle un nome á nova relación (opcionalmente no nome incluirase a FN na que a táboa aparece), Determinar a clave primaria da nova relación, Repetir ata que non queden máis atributos non atómicos."
], "d"),
("Además de cumplir con la 1FN, ¿Cuándo una relación está en 2FN?", [
    "a) Si todos sus atributos son independientes de la clave primaria.",
    "b) Si todos sus atributos no clave dependen completamente de la clave primaria.",
    "c) Si todos los atributos son clave primaria.",
    "d) Cuando tiene solo atributos atómicos."
], "b"),
("¿Cuál de las siguientes afirmaciones es verdadera en relación con la 2FN?", [
    "a) Todos los atributos pueden depender de partes de una clave.",
    "b) Solo los atributos de una clave pueden depender de partes de una clave.",
    "c) Los atributos no clave deben ser independientes de la clave primaria.",
    "d) No hay restricciones en la dependencia funcional de los atributos."
], "b"),
("¿En qué tipo de relaciones se aplica la 2FN?", [
    "a) Solo en relaciones con claves primarias simples.",
    "b) Solo en relaciones sin claves primarias.",
    "c) Solo en relaciones con claves compuestas.",
    "d) En todo tipo de relaciones."
], "c"),
("¿Qué se hace con un esquema de relación que no está en 2FN?", [
    "a) Se mantiene sin cambios.",
    "b) Se descompone en varias relaciones que sí estén en 2FN.",
    "c) Se elimina.",
    "d) Se transforma en una relación diferente."
], "b"),
("¿En qué base se debe realizar la descomposición para cumplir con la 2FN?", [
    "a) Se debe realizar en base a cualquier dependencia funcional.",
    "b) Se debe realizar en base a la dependencia funcional completa.",
    "c) Se debe realizar en base a la dependencia funcional transitiva.",
    "d) Se debe realizar en base a la dependencia funcional incompleta."
], "d"),
("¿Cuál es una condición necesaria para que una relación esté en tercera forma normal (3FN)?", [
    "a) La relación no debe estar en 2FN.",
    "b) Todos los atributos no principales deben depender funcionalmente solo de la clave.",
    "c) Deben existir dependencias funcionales transitivas respecto de las claves.",
    "d) Los atributos no principales deben depender de otros atributos no clave."
], "b"),
("¿Qué significa que una relación cumple con la tercera forma normal (3FN)?", [
    "a) Debe tener dependencias funcionales transitivas respecto de las claves.",
    "b) Todos los atributos no principales deben depender funcionalmente solo de la clave.",
    "c) Deben existir dependencias funcionales transitivas entre los atributos no principales.",
    "d) No deben existir dependencias funcionales transitivas respecto de las claves."
], "d"),
("Resumindo, para toda dependencia funcional X -> Y, X é uma chave.", [
    "a) Verdadeiro",
    "b) Falso"
], "a"),
("La mayoría de las tablas en 3NF están libres de anomalías de actualización, inserción y eliminación.", [
    "a) Verdadero",
    "b) Falso"
], "a"),
("Ciertos tipos de tablas en 3NF, que en la práctica raramente se encuentran, son afectadas por tales anomalías; estas son tablas que no satisfacen la forma normal de Boyce-Codd (FNBC o BCNF) o, si satisfacen la FNBC, son insuficientes para satisfacer las formas normales más altas 4NF o 5NF, todas ellas formas a estudiar en los siguientes puntos.", [
    "a) Verdadero",
    "b) Falso"
], "a"),





















































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
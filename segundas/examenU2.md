# Examén Regularizacion Unidad 2





## Parte 1 (50%)

**Contesta si son Verdaderas o Falsas las siguientes afirmaciones según el protocolo MQTT**

1.  El cliente solo puede recibir mensajes.

2.  El servidor es un agente o broker centralizado que comunica  a los clientes. 

3.  Los clientes solo pueden suscribirse a un tópico a la vez.

4.  Los tópicos permanecen registrados cuando la bandera de retención es falsa y todos los clientes suscritos a esos tópicos se desconectan. 

5.  El esquema publicador - suscriptor permite dirigir mensajes sobre un tópico a otros clientes utilizando su id.
6.  El broker no puede publicar bajo alguna circunstancia mensajes de un tópico.



**Calidad de servicio**

Contesta las siguientes preguntas.  

Considerando los 3 niveles de servicio que manjea MQTT (QoS0, QoS1, QoS2)

7.  ¿Qué QoS's garantizan la entrega de mensaje al receptor?
8.  ¿Qué QoS's entregan un mensaje libre de duplicados?
9.  Menciona una caracerística clave que diferencía una sesión pasajera (transient) de una durable . 



**Banderas**

10.  ¿Para qué sirven los mensajes de último deseo (will messages).

11.  ¿Que función tiene  mandar un mensaje de un tópico con la bandera de retención en falso?

     11.  ¿Para que sirve la bandera de retención?

          

          12.  ¿Qué pasa cuando un cliente manda un mensaje con la bandera de retención en Verdadero?





## Parte 2 (50%)

**Práctica Paho-MQTT Callbacks y loops** 



-   Crear una implementación libre de la función callback `(on_publish(client, userdata, mid))`, y probar su funcionamiento. (1/3)
    -   Sugerencia: importar modulo `inspect` y utilizar `inspect.getmembers(client)`, para consultar los atributos de la clase.
    -   Seleccionar algunos atributos y mostrarlos en la funcion `on_publish`.
-   Crear dos clientes, un cliente maestro y uno esclavo. (1/3)
    -   El cliente esclavo solo recibe ordenes del cliente maestro a traves de un mensaje enviado en un topico especifico.
    -   El cliente maestro debe ser capaz de detener y cerrar la conexion del cliente esclavo con una instruccion especifica.

-   Detener el loop automáticamente si la conexión falla usando el callback def `on_disconnect(client, userdata,rc=0)` (1/3)



Recuerden utilizar help(mqtt) para consultar los callbacks. 























1.  Diseñar un concepto de prueba de alguna aplicación de IdC la cual tenga una conjunto de tópicos. Estos tópicos deben estar organizados en jerarquicamente en un arbol de jerarquías de al menos tres niveles para poder experimentar con los comodines (wildcards) **#** y **+**.
2.  Para que sirve el comodín #?
3.  Para que sirve el comodin +?




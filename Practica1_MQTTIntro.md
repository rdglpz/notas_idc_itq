# Práctica 1. Introducción a MQTT

En esta práctica revisaremos el funcionamiento general de MQTT visto en clase y aprenderemos a: 

* Definir una jerarquía de tópicos
* Suscribirnos a diferentes topicos
* Suscribir con diferentes QoS
* Publicar con diferentes QoS
* Utilizar `will message`
* Utilizar `retain flag`
* Utilizar diferentes clientes para pruebas y diagnóstico.
* Instalar un broker (MOSQUITTO)


Entregar un reporte de la práctica descrita de manera precisa en un documento. Utilizar capturas de pantalla para mostrar la realización exitosa de cada punto.


## Requerimientos

1. Una computadora (De preferencia Raspbian) con conexión a internet con un Broker Instalado (MOSQUITTO)  
	1.1 [Descargar Raspbian](https://www.raspberrypi.org/downloads/raspbian/)  (verificar con checksum https://www.dyclassroom.com/howto-mac/how-to-verify-checksum-on-a-mac-md5-sha1-sha256-etc)
	1.2 Instalar Broker MQTT.   
		Instalar Clientes de mosquitto en Linux. 
		Aplica para Linux mint y raspbian 
		
```
		$sudo apt-get update  
		$sudo apt-get install mosquitto  
		$sudo apt-get install mosquitto-client 
```

	

1.3 [Repositorio oficial MOSQUITTO](https://mosquitto.org/blog/2013/01/mosquitto-debian-repository/)  
1.4 Un cliente MQTT para smartphone (por ejemplo MQTTOOL)  
1.5 Un cliente Para computadora [MQTT.fx](http://www.jensd.de/apps/mqttfx/1.7.1/)


## Actividades:  
 
1. Diseñar un concepto de prueba de alguna aplicación teórica IdC la cual tenga una conjunto de tópicos. Estos tópicos deben estar organizados en jerarquicamente en un arbol de al menos tres niveles para poder experimentar con los comodites **#** y **+**.  

Por ejemplo:

> Un sistema de agrónica esta compuesto por un conjunto de sensores y actuadores localizados en diferentes secciones de una granja. La granja tiene 3 tipos de cultivos diferentes y cada cultivo esta organizado por 3 secciones. Cada seccion tiene un sensor para humedad, temperatura, y un aspersor que es un actuador. La jerarquía es descrita como sigue:

```
/granja/cultivo1/seccion1/humedad
/granja/cultivo1/seccion1/temperatura
/granja/cultivo1/seccion1/aspersor
```

La humedad es reportada por un higrómetro en kg de vapor de agua/$m^3$.
La temperatura es reportada por medio de un termómetro digital.  
El aspersor es un dispositivo mecánico que expulsa una flujo de agua presurizada.
 

Con `mosquitto_sub` y `mosquito_pub`:

2. Crear un cliente con un ID suscrito a uno de esos tópicos con QoS 0.

3. Crear un cliente con un ID y publique en el topico suscrito con Con QoS 0.

4. Crear primero un cliente que publica y después un cliente que suscribe con. 
  4. Qué sucede?  
  4. Como el cliente que suscribe podría conocer el mensaje que se publico anteriormente? 

5. Crear un cliente con `will message` asociado a un tópico y probarlo en dos escenarios:  
	5.1 Cuando el cliente se desconecta exitosamente  
	5.2 Cuando el cliente se desconecta inesperadamente

6. Experimentar con diferentes QoS. 

	`[cliente1]--QoSx--[Broker]--QoSy--[Cliente2] con QoSx != QoSy`

7. Incorporar wildcards **+** y **#** en algún cliente



Utilizar wildcars en los suscriptores y verificar que un cliente recibe mensajes de multiples suscripciones.

Diferencia intercambio de mensajes QoS 2 y QoS 0 con retain.



Quiz:

1. ¿Puede un cliente con un ID específico publicar y suscribirse al mismo tópico?  (Aquí se pueden apoyar de MQTT.fx)
2. ¿Puede un broker suscribirse a un cliente?


**Recomendaciones:**  
Utilizar Linux  `man` para conocer las opciones y la utilización de los diferentes comandos.  

Levantar Mosquitto Broker en MacOS o Linux (sustituir las respectivas rutas si no están agregadas al PATH):

**Nota:**

## Comandos Básicos

Ejecutar el Broker Mosquitto

```
/usr/local/sbin/mosquitto -c /usr/local/etc/mosquitto/mosquitto.conf
``` 
Suscribir 

```
mosquitto_sub -h 192.168.1.88 -t messenger
```

Publicar 

```
mosquitto_pub -V mqttv311 -t messenger -m hi
```


## Referencias 

[Tutorial Topicos y comodines en MQTT](https://www.luisllamas.es/que-son-y-como-usar-los-topics-en-mqtt-correctamente/)  
[Steves Internet Guide](http://www.steves-internet-guide.com/understanding-mqtt-qos-2/)  
[http://www.steves-internet-guide.com/into-mqtt-python-client/](http://www.steves-internet-guide.com/into-mqtt-python-client/)






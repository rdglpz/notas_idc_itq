# Instalación Anaconda Navigator y Paho-mqtt Python


1. Instalacion Anaconda 

```
https://docs.anaconda.com/anaconda/install/
```

2. Instalando en Linux 

```
https://docs.anaconda.com/anaconda/install/linux/
```

Instalar Eclipse Paho-mqtt en python con anaconda. (https://anaconda.org/sci-bots/paho-mqtt)

```
conda install -c sci-bots paho-mqtt

```
Nota: sci-bot no tiene descripción. https://pypi.org/project/scibot/

3. Equivalencia conda vs pip

```
https://docs.conda.io/projects/conda/en/latest/commands.html#conda-vs-pip-vs-virtualenv-commands
```

4. Crear Ambiente Conda

```
conda create --name $ENVIRONMENT_NAME python

```

5. Activate y deactivate

```
(p3paho) jabali-6:mqtt rodrigolopez$ conda deactivate
jabali-6:mqtt rodrigolopez$ conda activate p3paho
(p3paho) jabali-6:mqtt rodrigolopez$ 
```

6. Paho es instalado en un ambiente conda, en este caso el ambiente se llama p3paho:

```
/Users/[usuario]/anaconda2/envs/p3paho/lib/python3.8/site-packages

(p3paho) pc:~ rodrigolopez$ ls /Users/rodrigolopez/anaconda2/envs/p3paho/lib/python3.8/site-packages/paho/mqtt/
__init__.py	__pycache__	client.py	matcher.py	publish.py	subscribe.py

```




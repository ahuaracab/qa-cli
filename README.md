qa-cli: QA Command Line
=======================

¿Que incluye?
--------------
* source Code (directorio app)
* Dockerfile (directorio dev/Dockerfile)
* Makefile

Requerimientos
--------------
* Docker
* Cmake

Ayuda
-----
* make
* make help

Comandos
--------
```console
  build            Construir imagen de la aplicacion
  ssh              Conectar al container por el protocolo ssh
  venv-create      Crea el entorno virtual (virtualenv)
  venv-install-lib Instala las librerias en el entorno virtual (virtualenv)
```

Activar virtualenv
------------------
```console
~/qa-cli$ make ssh
[root@594ea994b77f]/app# source ../venv/bin/activate
(venv) [root@594ea994b77f]/app#
```

Ejecutar main.py
----------------
Primero debe activar virtualenv

```console
(venv) [root@594ea994b77f]/app# python main.py
```

Estructura del project
======================

Directorio de la Applicacion
-----------------------------
```console
app
├── lib
│   ├── __init__.py
│   ├── config.py
│   ├── exceptions.py
│   ├── log.py
│   ├── messages.py
│   └── validates.py
├── main.py
└── requirements.txt
```

Directorio Dockerfiles
----------------------
```console
docker
└── dev
    └── Dockerfile
```

Empezando
=========
Ejecutar los siguientes pasos:
* make build
* make venv-create
* make venv-install-lib

Agregar/Eliminar librerias
==========================
Esto se realiza en el archivo requirements.txt. Luego ejecutar el comando:

Ejemplo:

Para agregar la libreria request v2.19.1, debería copiar lo indicado a continuación en el archivo requirements.txt:

  * request==2.19.1

* make venv-install-lib

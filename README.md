
<!--
<p align="center" style="margin-bottom: 0;">
  <img src="/media/olimpiApp_a.svg" alt="Logo" width="50%" style="vertical-align: middle;">
</p>
-->

<h1 align="center">
    Aplicación web en Django para la gestión de incidencias en entornos técnicos.
</h1>

Permite registrar, asignar y seguir incidencias mediante un flujo de estados controlado, con historial auditable y acceso por roles (usuarios, técnicos y administradores), priorizando la trazabilidad y la claridad operativa.

## Configuración y ejecución (contemplada en Linux)
### Instalación de Python y Pip (Debian)
Con los siguientes comandos instalaremos Python, Pip y Env respectivamente:

```console
sudo apt update
sudo apt install python3
sudo apt install python3-pip
sudo apt install python3-env
```

### Creación del entorno virtual
Creamos el entorno virtual sobre el que trabajaremos y donde tendremos todas las dependencias que necesitemos para el proyecto.

```console
python3 -m venv .venv
```

### Activación del entorno virtual
Con el siguiente comando activaremos dicho entorno virtual creado. Sobre la ruta donde se haya creado:

```console
source .venv/bin/activate
```

---

## Clonación del repositorio
### Instalación de Git
Será necesario la instalación de Git para el posterior comando de clonación de repositorios.

```console
sudo apt update
sudo apt install git
```

Comprobamos que la instalación se ha realizado con éxito.

```console
git --version
```

<sup>Se recomienda encarecidamente configurar Git para futuros usos relacionados.

### Clonación en local
Con el siguiente comando tendremos una copia en local del repositorio disponible en Github con los últimos cambios.

```console
git clone https://github.com/Canexy/Incidex.git
```

Hecho esto, navegamos dentro de la carpeta creada donde ejecutaremos el resto de comandos para su configuración y uso.

```console
cd Incidex/
```

### Instalación de dependencias
Es ahora cuando, sobre el entorno virtual, instalaremos las dependencias necesarias para la aplicación.

```console
pip install -r requirements.txt
```

---

## Ejecución del servidor de la aplicación
### Acceso a la aplicación
Asegurándonos que el entorno virtual está activado y todas las dependencias están instaladas debidamente, ejecutamos el comando desde raíz del proyecto.

```console
python3 manage.py runserver
```

Si todo va bien, aparecerá un enlace. Copiando dicha dirección en un navegador, o haciendo 'Ctrl + Click' sobre el enlace que se muestra en consola, mostrará la página de Login.

Es posible hacer login como `admin`, con contraseña `hcW8PHjWTTMPuq2`. 
Desde `http://127.0.0.1:8080/admin/` con las mismas credenciales, podremos crear usuarios normales y técnicos para el uso de la aplicación.

Los siguientes usuarios están registrados y pueden usarse actualmente:

Usuarios normales:
`Álvaro` - `zCEzzDqhDYfR6r7`

Técnicos:
`Mario` - `PAZmuvF5wiHwk92`
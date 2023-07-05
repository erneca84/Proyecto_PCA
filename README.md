# Proyecto Python-PCAP

chatbot que permite al usuario manipular archivos y directorios en su sistema de archivos utilizando programación orientada a objetos. La aplicación tiene las siguientes funcionalidades:

## Instalación

En el disco local **C**, debe crear la carpeta **Ernesto** y dentro de esta, crear  la carpeta **Python**. Dentro de la carpeta Python, debe crear la carpeta **PRUEBA**

La ruta definida para trabajar es '**C:\Ernesto\Python**'

## Modo de Uso


### Crear Archivo
create file 'nombre_archivo'

### Listar Archivos. 
Lista archivos de la ruta de trabajo **C:\Ernesto\Python**
```python
list files
```

### Crear Directorio. 
El '**nombre_directorio**' a crear debe estar dentro de la carpeta **C:\Ernesto\Python**
```python
create directory 'nombre_directorio'
```

### Eliminar Directorio. 
El '**nombre_directorio**' a eliminar debe estar dentro de la carpeta **C:\Ernesto\Python**
```python
delete directory 'nombre_directorio'
```

### Renombrar Directorio. 
'**nombre_directorio**' es el directorio a renombrar y '**nuevo_nombre_directorio**' es el nuevo nombre de directorio que se va a asignar
```python
rename directory 'nombre_directorio' to 'nuevo_nombre_directorio'
```

### Renombrar Archivo. 

'**nombre_archivo**' es el archivo a renombrar y '**nuevo_nombre_archivo**' es el nuevo nombre de archivo que se va a asignar.

```python
rename 'nombre_archivo' to 'nuevo_nombre_archivo'
```
### Eliminar Archivo. 

'**nombre_archivo**' es el archivo a eliminar 

```python
delete file 'nombre_archivo'
```

### Buscar archivo o directorio. 

'**nombre_archivo**' es el archivo a buscar o **nombre_directorio** el directorio a buscar

```python
search 'nombre_archivo' or 'nombre_directorio'
```

### Mover archivo

'**nombre_archivo**' es el archivo a mover  y **nueva_ruta** la ruta donde se va a mover el archivo

```python
move file 'nombre_archivo' to 'nueva_ruta''
```

### Cambiar permisos de Archivo

'**nombre_archivo**' es el archivo a modificar permisos  y **777** ejemplo de permisos asignados

```python
change permissions 'nombre_archivo' to 777
```

### Graficar

'**numero_entidad**' es el nit de la entidad a graficar

```python
graphic entity 'numero_entidad'
```

## Ejecución

El archivo de incio de la aplicacion es **chatbot.py**


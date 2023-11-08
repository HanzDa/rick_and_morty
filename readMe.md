# FastAPI Conección a Rick and morty API para manejar datos externos

Esta API está desarrollada utilizando FastAPI para manejar datos provenientes de un servicio externo y almacenarlos en una base de datos MySQL.

## Requisitos

- Docker
- Conexión a internet para acceder al servicio externo


### Base de Datos MySQL (Opcional Si la conección es local)
1. Configura una base de datos MySQL y asegúrate de tener las credenciales y permisos necesarios.
2. Crea la base de datos `rick_and_morty`
3. Modifica las variables de entorno en el archivo `.env` para establecer la conexión a tu base de datos MySQL.


### Instalación
1. Clona este repositorio.
2. Accede al directorio clonado.
3. Construye la imagen de Docker:

```bash
docker-compose up --build
```

### Ejecutar tests
```bash
docker exec -it API pytest
or
docker exec -it <container_id> pytest
```

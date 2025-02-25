<p align="center">
  <img width="150px" src="https://i.ibb.co/bXvzjXm/LOGO-h1.png" alt="Logo del proyecto" />
</p>


# RED-SOCIAL

## Descripción

Este proyecto es una red social desarrollada con Django en el backend y Node.js para gestionar Tailwind CSS en el frontend. Su objetivo es servir como un espacio de comunicación y una plataforma para la práctica de programación.

---

## Instalación y Configuración

### 1. Clonar el repositorio
```bash
  git clone https://github.com/titooDiaz/RED-SOCIAL.git
  cd red-social
```

### 2. Crear y activar un entorno virtual
```bash
  python -m venv env  # Crear entorno virtual
  source env/bin/activate  # Activar en Linux/macOS
  env\Scripts\activate  # Activar en Windows
```

### 3. Instalar dependencias de Python
```bash
  pip install -r requirements.txt
```

### 4. Configurar la base de datos
Este proyecto utiliza PostgreSQL. Asegúrate de tener instalado PGAdmin y configurar la base de datos en el archivo `settings.py`.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_de_tu_bd',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Luego, ejecuta las migraciones:
```bash
  python manage.py migrate
```

### 5. Instalar dependencias de Node.js para Tailwind CSS
Asegúrate de tener Node.js instalado. Luego, ejecuta:
```bash
  npm install
```

Para compilar los estilos de Tailwind:
```bash
  npm run build
```

### 6. Ejecutar el servidor de desarrollo
```bash
  python manage.py runserver
```
La aplicación estará disponible en: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Tecnologías Usadas
- Django
- PostgreSQL
- Tailwind CSS
- Node.js

---

## Estado del Proyecto
El proyecto está en desarrollo y se seguirá actualizando con nuevas funcionalidades.

---

## Contribuir
Si deseas contribuir, siéntete libre de hacer un fork y enviar un pull request.

---

## Licencia
Este proyecto está bajo la licencia MIT.



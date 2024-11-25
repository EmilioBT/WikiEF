# WikiEF

WikiEF es una aplicación diseñada para facilitar la labor de los docentes de educación física, proporcionando herramientas para la planificación de clases, el acceso a recursos didácticos y el fomento de la formación continua.

## **Descripción del Proyecto**

El objetivo principal de WikiEF es optimizar la enseñanza de la educación física mediante la integración de la tecnología, ofreciendo:
- Recursos didácticos adaptados a diferentes niveles educativos.
- Herramientas para la planificación de actividades y la gestión de recursos.
- Espacios de colaboración y aprendizaje continuo para docentes.

## **Características Principales**

- **Gestión de usuarios**: Registro e inicio de sesión para docentes con roles definidos (administrador/docente).
- **Recursos didácticos**: Acceso, creación y gestión de contenidos educativos.
- **Gestión de actividades**: Organización de actividades diseñadas para diferentes niveles educativos.
- **Diseño responsivo**: Compatible con dispositivos móviles, tablets y computadoras.
- **Seguridad**: Autenticación segura y cifrado de contraseñas.

## **Tecnologías Utilizadas**

### **Backend**
- **Lenguaje**: Python.
- **Framework**: Django.
- **Base de datos**: PostgreSQL.

### **Frontend**
- **Librerías**: HTML, CSS, JavaScript.
- **Frameworks**: Bootstrap, jQuery.

### **Entorno**
- **Editor**: Visual Studio Code (VSCode).
- **Control de versiones**: Git.

## **Instalación y Configuración**

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local:

1. **Clona el repositorio**:
    ```bash
    git clone https://github.com/EmilioBT/WikiEF.git
    cd WikiEF
    ```

2. **Crea un entorno virtual**:
    ```bash
    python -m venv venv
    source venv/bin/activate # Para Linux/Mac
    venv\Scripts\activate    # Para Windows
    ```

3. **Instala las dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configura las variables de entorno**:
    - Crea un archivo `.env` con las siguientes variables:
      ```env
      DEBUG=True
      SECRET_KEY=tu_clave_secreta
      DATABASE_URL=postgres://usuario:contraseña@localhost:5432/nombre_base_datos
      ```

5. **Ejecuta las migraciones**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Inicia el servidor**:
    ```bash
    python manage.py runserver
    ```


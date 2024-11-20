        // Obtener todos los enlaces con la clase 'nav-link'
        const navLinks = document.querySelectorAll('.nav-link');

        // Agregar un evento de click a cada enlace
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                // Remover la clase 'active' de todos los enlaces
                navLinks.forEach(link => link.classList.remove('active'));
                
                // Añadir la clase 'active' al enlace que ha sido pulsado
                this.classList.add('active');
            });
        });
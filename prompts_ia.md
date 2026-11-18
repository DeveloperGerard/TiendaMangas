## Decora base.html y base.css
En base al archivo desing-system.md
decora la base.html y base.css
para poder tener una base de diseño de mi pagina


## Quiero que en base a las plantillas base.html y base.css
quiero que decores detalle_manga y mangas.html con su propio css todo dentro de app manga respetando y usando base.html


## Ajustes visuales realizados
- Se aplicó a `base.html` y `base.css` una identidad minimalista y responsiva, con tonos verdes, fondos claros y navegación sencilla.
- `mangas.html` y `detalle_manga.html` reutilizan `base.html`, Bootstrap y los estilos propios de `manga/static/manga/catalogo.css`.
- En el detalle, la portada con la inicial y la información del manga se distribuyen en columnas responsivas para evitar que se superpongan.

## Mejora visual del login con Bootstrap
- **Solicitud reformulada:** "Mejorar la presentación visual del inicio de sesión utilizando Bootstrap, manteniendo la estructura de Django y la plantilla base del proyecto."
- **Acciones realizadas:** se reemplazó el formulario plano por una tarjeta responsiva dividida en panel de identidad y panel de acceso; se aplicaron campos con etiquetas, iconografía CSS, estados de error, accesibilidad básica y enlaces de navegación; se añadió el estilo propio de la aplicación en `manga/static/manga/catalogo.css`.
- **Comportamiento preservado:** el login continúa usando `LoginView`, mantiene `csrf_token`, conserva el parámetro `next` y realiza la autenticación de Django sin cambios en las rutas o vistas.

## Simplificación del login después de revisión visual
- **Solicitud reformulada:** "Reemplazar el diseño decorativo anterior por una presentación Bootstrap convencional, limpia y sobria."
- **Acciones realizadas:** se sustituyó el diseño dividido y sus estilos personalizados por una tarjeta Bootstrap centrada con `card`, `shadow-sm`, `form-control`, `btn-success` y `container`.
- **Comportamiento preservado:** se mantuvieron los campos de usuario y contraseña, los mensajes de error, `csrf_token`, el parámetro `next` y el enlace de retorno al catálogo.
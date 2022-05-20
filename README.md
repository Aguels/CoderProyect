# EntregaIntermediaGrupo5
Proyecto de Agustín Ambrosi.

## Explicación:
La página creada es un blog sobre música de nombre "Musicy", con un apartado para cargar canciones y otro para cargar información de la banda, además del blog propiamente dicho. Actualmente se encuentra desarrollado el registro de la banda, en el cual uno puede cargar el nombre y el rol de cada miembro con texto (Pianista, Vocalista, Guitarrista, etc.) y luego también filtrar a los músicos según el rol; el blog, que reconoce automáticamente a su autor y tiene título, subtítulo y cuerpo; y el cancionero, que consta de varios campos monolínea de texto (nombre, tono, acordes), un campo link para ingresar el acceso a youtube de la canción y un campo de texto multilínea poara la letra.

Al iniciar uno es dirigido a /musicy, que es el "landing". Todos los botones son navegables (les invito a probar el botón de pánico), aunque no existe un indicador que señale en qué página está uno, ya que todo el menú de navegación se hizo con plantillas heredadas.

Las funcionalidades de abm se encuentran disponibles para todos los models (músico, blog y cancionero). Luego de cargar un músico, es posible buscarlo a través de "Músicos" al ingresar en la búsqueda el rol que se le ha asignado.

Se ha creado un login así como un registro, que son accesibles a través del botón "ingresar" de la barra de navegación, y se ha limitado el abm a todo usuario registrado (un usuario Unknown tiene bloqueado el acceso, pero no es necesario tener derechos especiales para realizar altas, bajas o modificaciones, únicamente estar logeado). El usuario puede ingresar a su perfil a modificar su nombre, apellido y correo, y desde ese lugar a través de botones adicionales puede ir al formulario para actualizar su contraseña, o cargar una imagen para su avatar.
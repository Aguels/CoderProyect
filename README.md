# EntregaIntermediaGrupo5
Proyecto de Agustín Ambrosi y Agustín Hinterwimmer

## Explicación:
La página creada es un blog sobre música de nombre "Musicy", con un apartado para cargar canciones y otro para cargar información de la banda, además del blog propiamente dicho. Actualmente se encuentra desarrollado únicamente el registro de la banda, en el cual uno puede cargar el nombre y el rol de cada miembro con texto (Pianista, Vocalista, Guitarrista, etc.) y luego también filtrar a los músicos según el rol.

Para iniciar se puede ir al "landing", que sería "/musicy/home/". A pesar de no tener todavía trabajado el front end, todos los botones son navegables, aunque no existe un indicador que señale en qué página está uno, ya que todo el menú de navegación se hizo con plantillas heredadas.

Las funcionalidades de carga y búsqueda se encuentran en los botones de "Cargar músico" ("musicy/form/") y "Músicos" ("musicy/navegador/") respectivamente. Luego de cargar un músico, es posible buscarlo a través de "Músicos" al ingresar en la búsqueda el rol que se le ha asignado. El estandar para asignar roles es que la primer letra es siempre mayúscula y siempre se nombra la función, no el instrumento (Por ejemplo, es "Guitarrista", no "guitarra").

Resta pulir el front end añadiendo los textos correspondientes e imagenes que se adecúen al tema. También crear el blog y el cancionero, el cual tendrá la especial caracteristica de colorear en rojo todas las lineas que inicien en "." (vendrían a ser los acordes de la canción).

También falta rectificar los nombres de clases, variables y paths para que sean coherentes, y trabajar más los formularios para identificar textos incorrectos, normalizar inputs y poder elegir el rol según una lista de opciones, y no tener que ingresar el rol tal cual fue escrito.

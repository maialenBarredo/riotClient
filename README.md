# RiotClient

En este proyecto hemos redefinido el **Riot Client** usando **Django**. Hemos creado una web con los juegos, sus noticias, los iconos y los usuarios.

Todavía no hemos definido la conexión con la API de Riot Games, por lo que **todos los datos son de prueba**.

Hemos definido una base de datos, el admin, las páginas de lista y los detalles.

---

## Descripción

Nos hemos basado en la estructura del ejemplo **proyectoFUTBOL**. Hemos definido:

- **6 Modelos:**
  - `Juego`
  - `Noticia`
  - `Icono`
  - `Servidor`
  - `Usuario`
  - `UsuarioJuego`
- **Admin:** como en el ejemplo, desde `/admin/` se puede editar, borrar y añadir objetos. En el admin, los juegos de cada usuario se ven dentro del mismo usuario.
- **Vistas:** hemos definido una `ListView` y una `DetailView` para:
  - juegos
  - noticias
  - usuarios
  - iconos
  - página de inicio
- **URLs:** hemos definido todas las URLs en `appClient/urls.py`
- **Templates:** en la carpeta `templates` hemos definido un `base.html` (header y footer) y una carpeta por cada uno de los modelos con su lista y su detalle.
- **CSS:** hemos definido el estilo de la página para que se parezca a la actual: con un estilo sencillo, fondo oscuro y con resaltes en rojo.
- **Datos de prueba:** como aún no estamos conectados a la API de Riot Games, hemos definido 4 juegos (LoL, Valorant, TFT y Legends of Runeterra) con noticias, iconos y servidores. Además de 3 usuarios.

### Notas

- Cada juego tiene sus servidores, y el servidor de cada usuario se guarda por juego en `UsuarioJuego`.
- El `tag_line` del usuario es la etiqueta del Riot ID, **no el servidor**.
- Los iconos están distribuidos por juego y hay un icono general (el de Riot Games).
- Las imágenes van con URL.

---

## Base de Datos

Mirar el esquema en `RiotClient/images/esquema_bd.jpeg`

| Modelo | Qué guarda | Con qué se relaciona |
|---|---|---|
| `Juego` | cada juego: nombre, género, descripción, foto e info | tiene muchas noticias, iconos y servidores |
| `Noticia` | una noticia de un juego (parche, actualización, merchandising o evento) | es de un `Juego` |
| `Icono` | una imagen de perfil | es de un `Juego`, o de ninguno si es el icono general |
| `Servidor` | un servidor de un juego (EUW, LATAM...) | es de un `Juego` |
| `Usuario` | la persona: `game_name` + `tag_line`, email, edad, país y dinero | tiene amigos (otros usuarios) y juegos |
| `UsuarioJuego` | "este usuario tiene este juego, en este servidor y con este icono" | une `Usuario`, `Juego`, `Servidor` e `Icono` |

> **Especificación:** cada usuario tiene dinero, el cual es el mismo para todos los juegos.

---

## Entrar al admin

Para entrar al admin (`/admin/`) usamos el usuario:

| Usuario | Contraseña |
|---|---|
| `admin` | `admin` |

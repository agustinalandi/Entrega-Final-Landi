# Entrega1Landi

Mi proyecto se llama Tienda, y su aplicacion Ropa.

Tiene un requirements.txt donde aclaro que librerias estoy usando y un .gitignore.

La aplicacion esta registrada en el archivo de configuracion de mi proyecto. Es decir, en el settings.py dentro de tienda.
Dentro de settings tambien configuro donde se deben buscar los templates. En la raiz del proyecto creo una carpeta que se llama templates, donde guardo todos
los archivos .html .

Dentro de mi aplicacion, en models.py, creo mis modelos donde estan creadas las clases Pedido, Prenda y Accesorios con sus respectivas caracteristicas. Ademas,
dentro de cada clase defino la "subclase" Meta, que es la que configura la palabra de la clase en plural y singular; para que el admin quede mas proljo.
Dentro de mi aplicacion tambien tengo el archivo admin.py que es donde importo y registro mis 3 clases para luego poder ser usadas en el admin de Django. Con el 
admin de Django puedo crear objetos para mis modelos.

Estos 3 modelos tienen vistas, que estan creadas en el views.py de la aplicacion ropa. Las funciones llamadas listar_pedidos y listar_accesorios muestran una lista de 
productos cargados en la web. Es lo que uno ve al apretar el apartado de Prendas o Accesorios en la Navbar.

Dentro de views.py tengo ademas las funciones de crear_pedido, crear_prenda y cargar_accesorio. Las 3 cargan, a partir de formularios creados en forms.py que luego se
muestran en pantalla, el pedido que la persona quiera en base a las caracteristicas de los modelos. Si alguna data cargada mediante formularios no es valida, tira error.
Ademas, esta creada la view de index (Inicio) y contacto. Tambien esta creada la funcion buscar_pedido, que es la que hace posible buscar un pedido mediante el
buscador: yo pongo una palabra y me busca cualquier prenda que contenga esa palabra. De lo contario, me dice que no existe el pedido que estoy buscando.

Todas estas views tienen su propia plantilla con terminacion .html dentro de la carpeta de templates.

Mi WEB Django tiene una Nabvar que incluye los sitios de Inicio, Contacto, Prendas, Accesorios, Crear Pedidos, Cargar Accesorio y Crear Prenda. 
Esta Navbar con sus titulos, al ser comun para todas, esta declarada en la plantilla "padre.html', ya que es un codigo que no cambia. Dentro del codigo de la Navbar
determino como ir de un sitio a otro. Esto lo hago mediante las propias urls de las plantillas. Las plantillas que son comunes para toda la WEB estan creadas en urls.py
de la carpeta de mi proyecto, es decir, tienda. Las url que son propias de mi aplicacion estan declaradas dentro del urls.py de ropa. Despues en el ulrs.py de tienda
llamo a todas las de ropa todas juntas. Las demas plantillas (buscador, cargar_accesorio, contacto, crear_pedido, crear_prenda, index, lista_accesorios y lista_pedidos)
heredan el codigo de la Navbar y tienen, ademas, su propio codigo. 




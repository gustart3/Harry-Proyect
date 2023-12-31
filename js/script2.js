function cambiarEstilo(casa) {
    const body = document.body;
    body.classList.remove('Gryffindor', 'Slytherin', 'Hufflepuff', 'Ravenclaw');
    body.classList.add(casa);
    
}



function generarCarta() {
    const title = document.querySelector('select[name="title"]').value;
    const name = document.querySelector('input[name="name"]').value;
    const surname = document.querySelector('input[name="surname"]').value;
    const address = document.querySelector('input[name="address"]').value;
    const address2 = document.querySelector('input[name="address2"]').value;

    if (!title || !name || !surname || !address || !address2) {
        alert("Por favor, completa todos los campos del formulario.");
        return; 
    }

    // Contenido de la carta

    const cartaMembrete = `Para: ${title} ${name} ${surname}.<br>` +
        `Dirección: ${address}, ${address2}`;

    const cartaTexto = `Estimado(a) ${title} ${name} ${surname},\n\n` +
        `Nos complace informarte que has sido aceptado(a) en el Colegio Hogwarts de Magia y Hechicería.\n\n` +
        `Tu aventura en el mundo mágico está a punto de comenzar. \n\n` +
        `¡Te esperamos en la plataforma 9¾ el 1 de septiembre! <br>` +
        `Sinceramente,\n\n`;

    const cartaFirma =
        `Minerva McGonagall<br>` +
        `Directora del Colegio Hogwarts de Magia y Hechicería`;


    // Mostrar la carta de Hogwarts (mostrar #carta-imagen)
   const cartaImagenElement = document.getElementById('cartaImagen');
   cartaImagenElement.classList.add('cartaImagen');

   const cartaMembreteElement = document.getElementById('carta-membrete');
   cartaMembreteElement.classList.add('cartaMembreteEstilo');
    
    const cartaTextoElement = document.getElementById('carta-texto');
    cartaTextoElement.classList.add('cartaTextoEstilo');

    const cartaFirmaElement = document.getElementById('carta-firma');
    cartaFirmaElement.classList.add('cartaFirmaEstilo');
   
    cartaTextoElement.innerHTML = cartaTexto;
    cartaMembreteElement.innerHTML = cartaMembrete;
    cartaFirmaElement.innerHTML = cartaFirma;

   const ocultarTexto = document.getElementById("texto1");
   ocultarTexto.style.display = "none";

   const mostrarTexto = document.getElementById("texto2");
   mostrarTexto.style.display = "flex";

    // Restablecer los valores de los campos del formulario
    document.querySelector('select[name="title"]').value = 'Sr.';
    document.querySelector('input[name="name"]').value = '';
    document.querySelector('input[name="surname"]').value = '';
    document.querySelector('input[name="address"]').value = '';
    document.querySelector('input[name="address2"]').value = '';
}

//enviar con enter
document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("carta-form");
    const inputFields = form.querySelectorAll("input");

    inputFields.forEach((input) => {
        input.addEventListener("keydown", function (event) {
            if (event.key === "Enter") {
                event.preventDefault(); // Evita que se envíe el formulario automáticamente
                generarCarta(); // Llama a la función para enviar el formulario
            }
        });
    });

})


document.addEventListener("DOMContentLoaded", function () {
        const url = "https://harry-potter-api.onrender.com/db";
            fetch(url)
                .then((response) => {
                    if (!response.ok) {
                        throw new Error('Error en la solicitud a la API');
                    }
                    return response.json();
                })
                .then((data) => {
                    // Aquí puedes trabajar con los datos de la respuesta
                    console.log(data);
                })
                .catch((error) => {
                    console.error('Error:', error);
                });

            const searchInput = document.getElementById("search-input");
            const searchButton = document.getElementById("search-button");
            const fichaPersonaje = document.getElementById("ficha-personaje");
            

    // Define una variable para almacenar la lista de personajes
        let personajes = [];
            function traerDatos() {
                const url = "https://harry-potter-api.onrender.com/db";
                fetch(url)
                    .then(datos => datos.json())
                    .then(data => {
                        // Almacena la lista de personajes
                        personajes = data.personajes;
                        // Llama a la función para mostrar un personaje aleatorio
                        mostrarPersonajeAleatorio();
                    })
                    .catch(error => {
                        console.error("Error al obtener datos de la API:", error);
                    });
            }


            const bookList = document.getElementById("libro1");

    function crearElementosLibro(libro) {
        const tituloPrincipal = document.getElementById("tituloPrincipal1");
        const fecha = document.getElementById("fecha1");
        const descripcion = document.getElementById("descripcion1");
        const tituloOriginal = document.getElementById("tituloOriginal1");

        tituloPrincipal.textContent = libro.libro;
        fecha.textContent = `<strong>Fecha de Lanzamiento:</strong> ${libro.fecha_de_lanzamiento}`;
        descripcion.textContent = `<strong>Descripción:</strong> ${libro.descripcion}`;
        tituloOriginal.textContent = `<strong>Título Original:</strong> ${libro.titulo_original}`;
    }

    function obtenerDatosLibros() {
        const url = "https://harry-potter-api.onrender.com/db";
        fetch(url)
            .then(response => response.json())
            .then(data => {
                const libros = data.libros;
                if (libros.length >= 0) {
                    libros.forEach((libro, index) => {
                        // Llama a la función para crear elementos de libro con el libro actual
                        crearElementosLibro(libro, index + 1);
                    });
                }
            })
            .catch(error => {
                console.error("Error al obtener datos de los libros:", error);
            });
    }
    function crearElementosLibro(libro, index) {
        const tituloPrincipal = document.getElementById(`tituloPrincipal${index}`);
        const fecha = document.getElementById(`fecha${index}`);
        const descripcion = document.getElementById(`descripcion${index}`);
        const tituloOriginal = document.getElementById(`tituloOriginal${index}`);
    
        tituloPrincipal.textContent = libro.libro;
        fecha.textContent = `Fecha de Lanzamiento: ${libro.fecha_de_lanzamiento}`;
        descripcion.textContent = `Descripción: ${libro.descripcion}`;
        tituloOriginal.textContent = `Título Original: ${libro.titulo_original}`;
    }
    // Llama a la función para obtener y mostrar los datos de los libros
    obtenerDatosLibros();


})
    //lista
    const charactersList = document.getElementById("characters-list");
        function traerDatos() {
            const url = "https://harry-potter-api.onrender.com/db";
            fetch(url)
                .then(datos => datos.json())
                .then(data => {
                    // Almacena la lista de personajes
                    const personajes = data.personajes;
                    // Llama a la función para mostrar la lista de personajes
                    mostrarListaDePersonajes(personajes);
                })
                .catch(error => {
                    console.error("Error al obtener datos de la API:", error);
                });
        }

            function mostrarListaDePersonajes(personajes) {
                // Limpia el contenido existente en la lista
                charactersList.innerHTML = "";

                // Recorre la lista de personajes y crea un elemento <li> para cada uno
                personajes.forEach(personaje => {
                    const listItem = document.createElement("li");
                    listItem.textContent = personaje.personaje;
                    listItem.classList.add("personaje-item"); // Agrega una clase CSS para estilizar los elementos de la lista
                    listItem.addEventListener("click", () => mostrarDetallesDelPersonaje(personaje));
                    charactersList.appendChild(listItem);

                });
            }
//acummula fichas



    //fondo del contenedor


    function cambiarFondoPorCasa(casa) {

        const columnaFicha = document.querySelector('#contenido');
        // Elimina todas las clases de casa existentes
        columnaFicha.classList.remove('Gryffindor', 'Slytherin', 'Hufflepuff', 'Ravenclaw');
        // Agrega la clase correspondiente a la casa
        columnaFicha.classList.add(casa);
        
    }

    function mostrarDetallesDelPersonaje(personaje) {
        document.getElementById("foto-personaje").src = personaje.imagen; 
        document.getElementById("nombre-personaje").textContent = personaje.personaje;
        document.getElementById("apodo-personaje").textContent = `Apodo: ${personaje.apodo}`;
        document.getElementById("estudiante-personaje").textContent = `Estudiante de Hogwarts: ${personaje.estudianteDeHogwarts ? "Sí" : "No"}`;
        document.getElementById("casa-personaje").textContent = `Casa de Hogwarts: ${personaje.casaDeHogwarts}`;
        document.getElementById("actor").textContent = `Interpretado por: ${personaje.interpretado_por}`;
        console.log('Valor de "casa" al cambiar el fondo:', personaje.casaDeHogwarts);
        cambiarFondoPorCasa(personaje.casaDeHogwarts);

        const columnaFicha = document.querySelector('.contenido');
        if (columnaFicha) {
            // Cambiar el fondo solo si el elemento existe
            columnaFicha.className = 'column';
            columnaFicha.classList.add(personaje.casaDeHogwarts);
    
        }
    }


  

    document.addEventListener("DOMContentLoaded", function () {
        // Agregar un manejador de eventos para los elementos de menú
        const links = document.querySelectorAll(".menu a"); // Modifica el selector para que coincida con tus elementos de menú
        const headerHeight = document.getElementById("elemento0").offsetHeight; // Altura del header
    
        links.forEach(link => {
            link.addEventListener("click", (event) => {
                event.preventDefault();
                const targetId = link.getAttribute("href").substring(1); // Obtener el ID de la sección
                const targetSection = document.getElementById(targetId);
                if (targetSection) {
                    const targetOffset = targetSection.getBoundingClientRect().top + window.scrollY - headerHeight;
                    window.scrollTo({
                        top: targetOffset,
                        behavior: "smooth" // Desplazamiento suave
                    });
                }
            });
        });
    });
    


//galeria de imagenes
// Seleccionamos todos los elementos que contengan la clase .image
const image = document.querySelectorAll('.image');

// creamos un ciclo for of para cada una de nuestras imágenes del array
for (let [i, imageSelected] of image.entries()) {
  // Luego le decimos al image seleccionado que ejecute la función focus que a su vez ejecutará el resetFocus el cual eliminará la clase active de cualquiera de las imágenes del array, luego al image seleccionado le agregará la clase active
  imageSelected.addEventListener('click', function focus(){
    resetFocus();
    imageSelected.classList.toggle('active');
  });
}
function resetFocus() {
  image.forEach(i => i.classList.remove('active'));
}


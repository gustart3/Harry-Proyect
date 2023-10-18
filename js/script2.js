function cambiarEstilo(casa) {
    // Obtén el elemento body
    const body = document.body;
    // Quita todas las clases de casa existentes
    body.classList.remove('Gryffindor', 'Slytherin', 'Hufflepuff', 'Ravenclaw');

    // Agrega la clase correspondiente a la casa seleccionada
    body.classList.add(casa);
    
}



function generarCarta() {
    // Obtén los valores del formulario
    const title = document.querySelector('select[name="title"]').value;
    const name = document.querySelector('input[name="name"]').value;
    const surname = document.querySelector('input[name="surname"]').value;
    const address = document.querySelector('input[name="address"]').value;
    const address2 = document.querySelector('input[name="address2"]').value;

    if (!title || !name || !surname || !address || !address2) {
        alert("Por favor, completa todos los campos del formulario.");
        return; // No envíes el formulario si no están llenos todos los campos
    }

    // Componer el contenido de la carta
    const cartaMembrete = `Estimado(a) ${title} ${name} ${surname}.<br>` +
        `Dirección: ${address}, ${address2}`;

    const cartaTexto = `Estimado(a) ${title} ${name} ${surname},\n\n` +
        `Nos complace informarte que has sido aceptado(a) en el Colegio Hogwarts de Magia y Hechicería.\n\n` +
        `Tu aventura en el mundo mágico está a punto de comenzar. \n\n` +
        `¡Te esperamos en la plataforma 9¾ el 1 de septiembre! <br>` +
        `Sinceramente,\n\n`;

    const cartaFirma =
        `Minerva McGonagall<br>` +
        `Directora del Colegio Hogwarts de Magia y Hechicería`;

    // Mostrar la carta en la misma ventana
    
    const cartaTextoElement = document.getElementById('carta-texto');
    cartaTextoElement.style.position = 'absolute';
    cartaTextoElement.style.top = '35%';
    cartaTextoElement.style.left = '25%';
    cartaTextoElement.style.fontFamily = 'Vujahday Script, cursive';
    cartaTextoElement.style.fontSize = '1.5rem';
    cartaTextoElement.style.color = 'black';
    cartaTextoElement.style.paddingRight = '33%';
    cartaTextoElement.style.paddingLeft = '5%';

    const cartaMembreteElement = document.getElementById('carta-membrete');
    const cartaFirmaElement = document.getElementById('carta-firma');


    cartaTextoElement.innerHTML = cartaTexto;
    cartaMembreteElement.innerHTML = cartaMembrete;
    cartaFirmaElement.innerHTML = cartaFirma;

    // Mostrar la carta de Hogwarts (mostrar #carta-imagen)
   const cartaImagenElement = document.getElementById('carta-imagen');
    //cartaImagenElement.style.width = '100%';
    //cartaImagenElement.style.display = 'block';
   //cartaImagenElement.style.position = 'absolute';
    //cartaImagenElement.style.objectFit = 'cover';
    //cartaImagenElement.style.zIndex = '-1';

    
    

    const firmaElement = document.getElementById('carta-firma')
       firmaElement.style.position = 'absolute';
    firmaElement.style.bottom = '20%';
    firmaElement.style.left = '16%';
    firmaElement.style.overflow = 'hidden';
    firmaElement.style.width = '5%';
    firmaElement.style.height = '10%';
    firmaElement.style.fontSize = '20px';
    firmaElement.style.fontFamily = 'Vujahday Script, cursive';
    firmaElement.style.fontSize = '1.5rem';
    firmaElement.style.paddingRight = '20%';
    firmaElement.style.paddingLeft = '5%';
    


    const membreteElement = document.getElementById('carta-membrete')
    membreteElement.style.position = 'absolute';
    membreteElement.style.top = '20%';
    membreteElement.style.left = '33%';
    membreteElement.style.fontFamily = 'Vujahday Script, cursive';
    membreteElement.style.marginBottom = '50px';
    membreteElement.style.fontSize = '1.2rem';
    membreteElement.style.minWidth = "30%"

    const cartaContainer = document.getElementById("carta-container");
    cartaContainer.style.display = "block";
    cartaContainer.style.position = "relative";
    cartaContainer.style.height = "100%";
    cartaContainer.style.width = '100%';
    cartaContainer.style.gridColumn = "2/ span 2";
  

    const ocultarTexto = document.getElementById("texto1");
    ocultarTexto.style.display = "none";

    const mostrarTexto = document.getElementById("texto2");
    mostrarTexto.style.display = "flex";
    
/*
    const hogwartsContainer = document.getElementById("carta-hogwarts");
    hogwartsContainer.style.display = "block";
    hogwartsContainer.style.position = "right";
    hogwartsContainer.style.height = "100vh";
    hogwartsContainer.style.gridRow ="1";
    hogwartsContainer.style.gridColumn ="3";
*/

    // Restablecer los valores de los campos del formulario
    document.querySelector('select[name="title"]').value = 'Sr.';
    document.querySelector('input[name="name"]').value = '';
    document.querySelector('input[name="surname"]').value = '';
    document.querySelector('input[name="address"]').value = '';
    document.querySelector('input[name="address2"]').value = '';
}

//funcion enter
document.addEventListener("DOMContentLoaded", function () {
    // Tu código existente para cargar la página

    // Agrega un manejador de eventos "keydown" a los campos de entrada
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


  

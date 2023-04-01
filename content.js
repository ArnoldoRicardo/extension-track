console.log("Hola");

const get_events = () => {
  const events = document.querySelectorAll('[aria-label^="event"]');
  events.forEach((event) => {
    console.log(event);
    const eventText = event.getAttribute("aria-label");
    console.log(eventText);
  });
};

const get_data = () => {
  fetch("https://jsonplaceholder.typicode.com/todos/1")
    .then((response) => response.json())
    .then((json) => console.log(json));
};

setTimeout(get_events, 5000);

//setInterval(get_data, 6000);

document.addEventListener("DOMContentLoaded", function () {
  // Obtén el contenido del body de la página
  const bodyContent = document.body.textContent;
  console.log(bodyContent);
});

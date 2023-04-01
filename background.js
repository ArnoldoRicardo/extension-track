// Escucha los mensajes enviados por el script de contenido
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  // Envía el contenido del body a una página web o a otro script
  console.log(request.body);
  console.log('hola')
});

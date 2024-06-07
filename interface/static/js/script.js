// Fonction pour envoyer un message
function sendMessage() {
  const messageInput = document.getElementById("message-input");
  const messageText = messageInput.value;

  if (messageText.trim()) {
    const messageContainer = document.getElementById("messages-container");

    // Créez un élément HTML pour le message de l'utilisateur
    const userMessage = document.createElement("div");
    userMessage.classList.add("message", "user");
    userMessage.textContent = messageText;

    // Ajoutez le message à la fenêtre de discussion
    messageContainer.appendChild(userMessage);

    // Envoyez le message au bot (via AJAX ou WebSocket, par exemple)
    // ...

    // Videz le champ de saisie
    messageInput.value = "";
  }
}

// Écoutez l'événement clic sur le bouton d'envoi
const sendButton = document.getElementById("send-button");
sendButton.addEventListener("click", sendMessage);

// (Optionnel) Écoutez l'appui sur la touche Entrée pour envoyer un message
document.addEventListener("keypress", function (event) {
  if (event.key === "Enter") {
    sendMessage();
  }
});

document.getElementById("send-button").addEventListener("click", function () {
  var userInput = document.getElementById("user-input").value;
  fetch("/message", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: "message=" + encodeURIComponent(userInput),
  })
    .then((response) => response.json())
    .then((data) => {
      var chatBox = document.getElementById("chat-box");
      chatBox.innerHTML += '<div class="user-message">' + userInput + "</div>";
      chatBox.innerHTML +=
        '<div class="bot-response">' + data.response + "</div>";
      document.getElementById("user-input").value = "";
    });
});

document.getElementById("clear-button").addEventListener("click", function () {
  document.getElementById("chat-box").innerHTML = "";
  document.getElementById("user-input").value = "";
});

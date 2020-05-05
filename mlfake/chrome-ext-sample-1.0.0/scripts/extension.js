document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("status").textContent = "Extension loaded";
  var button = document.getElementById("changelinks");
  button.addEventListener("click", function () {
    $("#status").html("Clicked change links button");
    let text = [];
    text[0] = $("#text0").val();
    text[1] = $("#text1").val();
    text[2] = $("#text2").val();
    text[3] = $("#text3").val();
    text[4] = $("#text4").val();
    text[5] = $("#text5").val();
    text[6] = $("#text6").val();
    window.onload = function () {
      document.getElementById("submitbutton").click();
    };

    // if (!text) {
    //   $("#status").html("Invalid text provided");
    //   return;
    // }
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
      chrome.tabs.sendMessage(tabs[0].id, { data: text }, function (response) {
        $("#status").html("changed data in page");
        console.log("success");
      });
    });
  });
});

document.addEventListener("DOMContentLoaded", function () {
//  document.getElementById("status").textContent = "Extension loaded";
  var button = document.getElementById("btn-post");
  button.addEventListener("click", function () {
        var req = new XMLHttpRequest();
        var result = document.getElementById('result');
        req.onreadystatechange = function()
        {
          if(this.readyState == 4 && this.status == 200) {
            result.innerHTML = this.responseText;
            alert(this.responseText)
          } else {
            result.innerHTML = "error";
          }
        }
        req.open('POST', 'http://127.0.0.1:5000/', true);
        req.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
        req.send("statuses="+document.getElementById('text0').value+"&followers="+document.getElementById('text1').value
        +"&friends="+document.getElementById('text2').value+"&favourites="+document.getElementById('text3').value
        +"&listed="+document.getElementById('text4').value+"&sex="+document.getElementById('text5').value
        +"&lang="+document.getElementById('text6').value);
//    $("#status").html("Clicked change links button");
//    let text = [];
//    text[0] = $("#text0").val();
//    text[1] = $("#text1").val();
//    text[2] = $("#text2").val();
//    text[3] = $("#text3").val();
//    text[4] = $("#text4").val();
//    text[5] = $("#text5").val();
//    text[6] = $("#text6").val();
//    window.onload = function () {
//      document.getElementById("submitbutton").click();
//    };
//
//    // if (!text) {
//    //   $("#status").html("Invalid text provided");
//    //   return;
//    // }
////    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
////      chrome.tabs.sendMessage(tabs[0].id, { data: text }, function (response) {
////        $("#status").html("changed data in page");
////        console.log("success");
////      });
////    });
//        chrome.tabs.query({
//        active: true,
//        lastFocusedWindow: true
//        }, function(tabs) {
//        var tab=tabs[0];
//            console.log(tab.url);
//        var xhr = new XMLHttpRequest();
//
//            xhr.addEventListener("readystatechange", function () {
//            if (xhr.readyState == 4) {
//                console.log(xhr.responseText);
//                alert(xhr.responseText)
//          }
//        });
//         formData = {
//        "data[tumblelog]": "drunknight",
//        "data[source]": "FOLLOW_SOURCE_REBLOG"
//    };
//            xhr.open("POST", "http://localhost:5000/",true);
//            xhr.send(JSON.stringify(formData));
//        });
  });
});

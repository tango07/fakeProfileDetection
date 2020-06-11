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
            alert("The Profile is "+this.responseText)
          } else {
            result.innerHTML = "Predicting.....";
          }
        }
        if(document.getElementById('text0').validity.valid &&document.getElementById('text1').validity.valid &&
        document.getElementById('text2').validity.valid &&document.getElementById('text3').validity.valid &&
        document.getElementById('text4').validity.valid &&document.getElementById('text5').validity.valid &&
        document.getElementById('text6').validity.valid){

        req.open('POST', 'http://127.0.0.1:5000/', true);
        req.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
        req.send("statuses="+document.getElementById('text0').value+"&followers="+document.getElementById('text1').value
        +"&friends="+document.getElementById('text2').value+"&favourites="+document.getElementById('text3').value
        +"&listed="+document.getElementById('text4').value+"&sex="+document.getElementById('text5').value
        +"&lang="+document.getElementById('text6').value);
        }
        else{
        alert("OOP's you have not entered data Correctly!")
        }
  });
});

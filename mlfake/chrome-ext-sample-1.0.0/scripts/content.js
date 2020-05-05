chrome.runtime.onMessage.addListener(function (response, sender, sendResponse) {
  console.log("something happening from the extension");
  var data = response.data || {};

  var linksList = document.querySelectorAll("input");
  [].forEach.call(linksList, function (header) {
    if (header.name === "statuses_count") header.value = response.data[0];
    if (header.name === "followers_count") header.value = response.data[1];
    if (header.name === "friends_count") header.value = response.data[2];
    if (header.name === "favourites_count") header.value = response.data[3];
    if (header.name === "listed_count") header.value = response.data[4];
    if (header.name === "sex_code") header.value = response.data[5];
    if (header.name === "lang_code") header.value = response.data[6];
  });
  var result = document.getElementById("result").innerHTML;
  sendResponse({ data: data, success: true });
});

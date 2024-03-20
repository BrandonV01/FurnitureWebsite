// When the user clicks on <div>, open the popup
function openPopup1(item_id) {
  var popup = document.getElementById("popup");
  popup.style.visibility = 'visible';
  
  document.popupForm.action = "manage-products/" + item_id + "/delete";
}

function openPopup2(tag_id) {
  var popup = document.getElementById("popup");
  popup.style.visibility = 'visible';
  
  document.popupForm.action = "manage-tags/" + tag_id + "/delete";
}

function openPopup3(tag_id) {
  var popup = document.getElementById("popup");
  popup.style.visibility = 'visible';
  
  document.popupForm.action = "manage-users/" + tag_id + "/delete";
}

function openPopup4(subtag_id) {
  var popup = document.getElementById("popup");
  popup.style.visibility = 'visible';
  
  document.popupForm.action = "manage-subtags/" + subtag_id + "/delete";
}

function closePopup() {
  var popup = document.getElementById("popup");
  popup.style.visibility = 'hidden';

  document.popupForm.action = "/";
}
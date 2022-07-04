// When the user scrolls the page, execute myFunction
window.onscroll = function() {myFunction()};

function myFunction() {
  var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
  console.log('Win Scroll '+winScroll);
  var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  console.log('Height '+height);
  var scrolled = (winScroll / height) * 100;
  console.log('Scrolled '+scrolled);
  document.getElementById("myBar").style.width = scrolled + "%";
  
}

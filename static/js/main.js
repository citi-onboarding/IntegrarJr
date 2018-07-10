// NAVBAR
function navResponsive() {
  var e = document.getElementById("idNavbar");
  if (e.className === "navbar navbar_colored") {
    e.className += " responsive";
  } else {
    e.className = "navbar navbar_colored";
  }
}

function iconEffect(x) {
  x.classList.toggle("change");
}

$(document).click(function(event) { 
  if (!$(event.target).closest('.navbar').length) {
    var e = document.getElementById("idNavbar");
    if (e.className === "navbar navbar_colored responsive") {
      e.className = "navbar navbar_colored";
      var x = document.getElementById("navbar-x-container");
      iconEffect(x);
    }
  }
});

$('a[href*="#"]')
  // Remove links that don't actually link to anything
  .not('[href="#"]')
  .not('[href="#0"]')
  .click(function(event) {
    // On-page links
    if (
      location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') 
      && 
      location.hostname == this.hostname
    ) {
      // Figure out element to scroll to
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      // Does a scroll target exist?
      if (target.length) {
        // Only prevent default if animation is actually gonna happen
        event.preventDefault();
        $('html, body').animate({
          scrollTop: target.offset().top
        }, 1000, function() {
          // Callback after animation
          // Must change focus!
          var $target = $(target);
          $target.focus();
          if ($target.is(":focus")) { // Checking if the target was focused
            return false;
          } else {
            $target.attr('tabindex','-1'); // Adding tabindex for elements not focusable
            $target.focus(); // Set focus again
          };
        });
      }
    }
  });

// CARROSSEL
$(document).ready(function(){
  $('.carrossel-container').slick({
    prevArrow: '<div class="seta-esquerda"></div>',
    nextArrow: '<div class="seta-direita"></div>',
    dots: true,
    /*
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 4000,
    */
  });
});

// FORM
$(document).ready(function(){
  var form = document.getElementById("contatoform");
  $('#contatoform').prepend($('<div id="divaux2"></div>'));
  $('#contatoform').prepend($('<div id="divaux1"></div>'));
  $('#divaux1').append(form.children[2]);
  $('#divaux1').append(form.children[2]);
  $('#divaux1').append(form.children[3]);
  $('#divaux1').append(form.children[2]);
  $('#divaux1').append(form.children[4]);
  $('#divaux2').append(form.children[2]);
  $('#divaux2').append(form.children[2]);
  $('#divaux2').append(form.children[2]);
});
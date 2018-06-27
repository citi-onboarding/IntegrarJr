$(document).ready(function(){
    var form = document.getElementById("contatoform");
    $('#contatoform').prepend($('<div id="divaux2"></div>'));
    $('#contatoform').prepend($('<div id="divaux1"></div>'));
    $('#divaux1').append(form.children[2]);
    $('#divaux1').append(form.children[2]);
    $('#divaux1').append(form.children[2]);
    $('#divaux1').append(form.children[2]);
    $('#divaux2').append(form.children[2]);
    $('#divaux2').append(form.children[3]);
    $('#divaux2').append(form.children[2]);
});
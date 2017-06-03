var impresion = function (){
  window.print();
  var pathname = window.location.pathname;
  window.location.replace(pathname + "?mensaje=yes");
};

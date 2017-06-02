$( document ).ready(function() {
  if(  $('#id_articulo').attr("type")!=="hidden"){
      var values = [];
      var names = [];
      var trying = [];
      var valuestrying = [];
      var counter = -1;

      $('#id_articulo').before('<div id="appender" class="input-group"><span class="input-group-addon glyphicon glyphicon-search" id="basic-addon1"></span><input class="form-control" name="text">');
      $('#id_articulo option').each(function() {
          values.push( $(this).attr('value').toLowerCase() );
          names.push( $(this).text().toLowerCase() );
      });

      $('input[name=text]').on('input',function() {
        valuestrying = [];
        counter = -1;
        var busca = $('input[name=text]').val().toLowerCase();
        $('#id_articulo').empty();
        trying = jQuery.grep(names, function( a ) {
          counter++;
          var comparacion = a.toLowerCase();
          if(comparacion.includes(busca.toLowerCase())){
            valuestrying.push(values[counter])
            return a;
          }
        });
        counter = 0;
        $.each(trying, function(val, text) {
                $('#id_articulo').append( $('<option></option>').val(valuestrying[counter]).html(text) )
                counter++;
          });
      });
    }
});

$( document ).ready(function() {
  if(  $('#id_trabajador').attr("type")!=="hidden"){
      var values = [];
      var names = [];
      var trying = [];
      var valuestrying = [];
      var counter = -1;

      $('#id_trabajador').before('<div id="appender" class="input-group"><span class="input-group-addon glyphicon glyphicon-search" id="basic-addon1"></span><input class="form-control" name="text">');
      $('#id_trabajador option').each(function() {
          values.push( $(this).attr('value').toLowerCase() );
          names.push( $(this).text().toLowerCase() );
      });

      $('input[name=text]').on('input',function() {
        valuestrying = [];
        counter = -1;
        var busca = $('input[name=text]').val().toLowerCase();
        $('#id_trabajador').empty();
        trying = jQuery.grep(names, function( a ) {
          counter++;
          var comparacion = a.toLowerCase();
          if(comparacion.includes(busca.toLowerCase())){          valuestrying.push(values[counter])
            return a;
          }
        });
        counter = 0;
        $.each(trying, function(val, text) {
                $('#id_trabajador').append( $('<option></option>').val(valuestrying[counter]).html(text) )
                counter++;
          });
      });
    }
});
$( document ).ready(function() {
  if(  $('#id_recibe').attr("type")!=="hidden"){
      var values = [];
      var names = [];
      var trying = [];
      var valuestrying = [];
      var counter = -1;

      $('#id_recibe').before('<div id="appender" class="input-group"><span class="input-group-addon glyphicon glyphicon-search" id="basic-addon1"></span><input class="form-control" name="text">');
      $('#id_recibe option').each(function() {
          values.push( $(this).attr('value').toLowerCase() );
          names.push( $(this).text().toLowerCase() );
      });

      $('input[name=text]').on('input',function() {
        valuestrying = [];
        counter = -1;
        var busca = $('input[name=text]').val().toLowerCase();
        $('#id_recibe').empty();
        trying = jQuery.grep(names, function( a ) {
          counter++;
          var comparacion = a.toLowerCase();
          if(comparacion.includes(busca.toLowerCase())){
            valuestrying.push(values[counter])
            return a;
          }
        });
        counter = 0;
        $.each(trying, function(val, text) {
                $('#id_recibe').append( $('<option></option>').val(valuestrying[counter]).html(text) )
                counter++;
          });
      });
    }
});

$( document ).ready(function() {

  if(  $('#id_cliente').attr("type")!=="hidden"){
  var values = [];
  var names = [];
  var trying = [];
  var valuestrying = [];
  var counter = -1;

  $('#id_cliente').before('<div id="appender" class="input-group"><span class="input-group-addon glyphicon glyphicon-search" id="basic-addon1"></span><input class="form-control" name="text">');
  $('#id_cliente option').each(function() {
      values.push( $(this).attr('value').toLowerCase() );
      names.push( $(this).text().toLowerCase() );
  });


  $('input[name=text]').on('input',function() {
    valuestrying = [];
    counter = -1;
    var busca = $('input[name=text]').val().toLowerCase();
    $('#id_cliente').empty();
    trying = jQuery.grep(names, function( a ) {
      counter++;
      var comparacion = a.toLowerCase();
      if(comparacion.includes(busca.toLowerCase())){
        valuestrying.push(values[counter])
        return a;
      }
    });
    counter = 0;
    $.each(trying, function(val, text) {
            $('#id_cliente').append( $('<option></option>').val(valuestrying[counter]).html(text) )
            counter++;
      });
  });
}
});

$( document ).ready(function() {

  if(  $('#id_encargado').attr("type")!=="hidden"){
  var values = [];
  var names = [];
  var trying = [];
  var valuestrying = [];
  var counter = -1;

  $('#id_encargado').before('<div id="append" class="input-group"><span class="input-group-addon glyphicon glyphicon-search" id="basic-addon1"></span><input class="form-control" name="texto">');
  $('#id_encargado option').each(function() {
      values.push( $(this).attr('value').toLowerCase() );
      names.push( $(this).text().toLowerCase() );
  });


  $('input[name=texto]').on('input',function() {
    valuestrying = [];
    counter = -1;
    var busca = $('input[name=texto]').val();
    $('#id_encargado').empty();
    trying = jQuery.grep(names, function( a ) {
      counter++;
      var comparacion = a.toLowerCase();
      if(comparacion.includes(busca.toLowerCase())){
        valuestrying.push(values[counter])
        return a;
      }
    });
    counter = 0;
    $.each(trying, function(val, text) {
            $('#id_encargado').append( $('<option></option>').val(valuestrying[counter]).html(text) )
            counter++;
      });
  });
}
});

$( document ).ready(function() {

  if(  $('#id_municipio').attr("type")!=="hidden"){
  var values = [];
  var names = [];
  var trying = [];
  var valuestrying = [];
  var counter = -1;

  $('#id_municipio').before('<div id="append" class="input-group"><span class="input-group-addon glyphicon glyphicon-search" id="basic-addon1"></span><input class="form-control" name="texto">');
  $('#id_municipio option').each(function() {
      values.push( $(this).attr('value').toLowerCase() );
      names.push( $(this).text().toLowerCase() );
  });

  $('input[name=texto]').on('input',function() {
    valuestrying = [];
    counter = -1;
    var busca = $('input[name=texto]').val();
    $('#id_municipio').empty();
    trying = jQuery.grep(names, function( a ) {
      counter++;
      var comparacion = a.toLowerCase();
      if(comparacion.includes(busca.toLowerCase())){
        valuestrying.push(values[counter])
        return a;
      }
    });
    counter = 0;
    $.each(trying, function(val, text) {
            $('#id_municipio').append( $('<option></option>').val(valuestrying[counter]).html(text) )
            counter++;
      });
  });
}
});

$( document ).ready(function() {

  if(  $('#id_personal').attr("type")!=="hidden"){
  var values = [];
  var names = [];
  var trying = [];
  var valuestrying = [];
  var counter = -1;

  $('#id_personal').before('<div id="append" class="input-group"><span class="input-group-addon glyphicon glyphicon-search" id="basic-addon1"></span><input class="form-control" name="texto">');
  $('#id_personal option').each(function() {
      values.push( $(this).attr('value').toLowerCase() );
      names.push( $(this).text().toLowerCase() );
  });


  $('input[name=texto]').on('input',function() {
    valuestrying = [];
    counter = -1;
    var busca = $('input[name=texto]').val();
    $('#id_personal').empty();
    trying = jQuery.grep(names, function( a ) {
      counter++;
      var comparacion = a.toLowerCase();
      if(comparacion.includes(busca.toLowerCase())){
        valuestrying.push(values[counter])
        return a;
      }
    });
    counter = 0;
    $.each(trying, function(val, text) {
            $('#id_personal').append( $('<option></option>').val(valuestrying[counter]).html(text) )
            counter++;
      });
  });
}
});
$( document ).ready(function() {

  if(  $('#id_proveedor').attr("type")!=="hidden"){
  var values = [];
  var names = [];
  var trying = [];
  var valuestrying = [];
  var counter = -1;

  $('#id_proveedor').before('<div id="append" class="input-group"><span class="input-group-addon glyphicon glyphicon-search" id="basic-addon1"></span><input class="form-control" name="texto">');
  $('#id_proveedor option').each(function() {
      values.push( $(this).attr('value').toLowerCase() );
      names.push( $(this).text().toLowerCase() );
  });



  $('input[name=texto]').on('input',function() {
    valuestrying = [];
    counter = -1;
    var busca = $('input[name=texto]').val();
    $('#id_proveedor').empty();
    trying = jQuery.grep(names, function( a ) {
      counter++;
      var comparacion = a.toLowerCase();
      if(comparacion.includes(busca.toLowerCase())){
        valuestrying.push(values[counter])
        return a;
      }
    });
    counter = 0;
    $.each(trying, function(val, text) {
            $('#id_proveedor').append( $('<option></option>').val(valuestrying[counter]).html(text) )
            counter++;
      });
  });
}
});

$( document ).ready(function() {

  if(  $('#id_proyecto').attr("type")!=="hidden"){
  var values = [];
  var names = [];
  var trying = [];
  var valuestrying = [];
  var counter = -1;

  $('#id_proyecto').before('<div id="append" class="input-group"><span class="input-group-addon glyphicon glyphicon-search" id="basic-addon1"></span><input class="form-control" name="texto">');
  $('#id_proyecto option').each(function() {
      values.push( $(this).attr('value').toLowerCase() );
      names.push( $(this).text().toLowerCase() );
  });

  $('input[name=texto]').on('input',function() {
    valuestrying = [];
    counter = -1;
    var busca = $('input[name=texto]').val();
    $('#id_proyecto').empty();
    trying = jQuery.grep(names, function( a ) {
      counter++;
      var comparacion = a.toLowerCase();
      if(comparacion.includes(busca.toLowerCase())){
        valuestrying.push(values[counter])
        return a;
      }
    });
    counter = 0;
    $.each(trying, function(val, text) {
            $('#id_proyecto').append( $('<option></option>').val(valuestrying[counter]).html(text) )
            counter++;
      });
  });
}
});

$( document ).ready(function() {

if(  $('#id_receta').attr("type")!=="hidden"){
  var values = [];
  var names = [];
  var trying = [];
  var valuestrying = [];
  var counter = -1;

  $('#id_receta').before('<div id="appender" class="input-group"><span class="input-group-addon glyphicon glyphicon-search" id="basic-addon1"></span><input class="form-control" name="text">');
  $('#id_receta option').each(function() {
      values.push( $(this).attr('value').toLowerCase() );
      names.push( $(this).text().toLowerCase() );
  });


  $('input[name=text]').on('input',function() {
    valuestrying = [];
    counter = -1;
    var busca = $('input[name=text]').val().toLowerCase();
    $('#id_receta').empty();
    trying = jQuery.grep(names, function( a ) {
      counter++;
      var comparacion = a.toLowerCase();
      if(comparacion.includes(busca.toLowerCase())){
        valuestrying.push(values[counter])
        return a;
      }
    });
    counter = 0;
    $.each(trying, function(val, text) {
            $('#id_receta').append( $('<option></option>').val(valuestrying[counter]).html(text) )
            counter++;
      });
  });
}
});


$( document ).ready(function() {

if(  $('#id_sede').attr("type")!=="hidden"){
  var values = [];
  var names = [];
  var trying = [];
  var valuestrying = [];
  var counter = -1;

  $('#id_sede').before('<div id="appender" class="input-group"><span class="input-group-addon glyphicon glyphicon-search" id="basic-addon1"></span><input class="form-control" name="text">');
  $('#id_sede option').each(function() {
      values.push( $(this).attr('value').toLowerCase() );
      names.push( $(this).text().toLowerCase() );
  });


  $('input[name=text]').on('input',function() {
    valuestrying = [];
    counter = -1;
    var busca = $('input[name=text]').val().toLowerCase();
    $('#id_sede').empty();
    trying = jQuery.grep(names, function( a ) {
      counter++;
      var comparacion = a.toLowerCase();
      if(comparacion.includes(busca.toLowerCase())){
        valuestrying.push(values[counter])
        return a;
      }
    });
    counter = 0;
    $.each(trying, function(val, text) {
            $('#id_sede').append( $('<option></option>').val(valuestrying[counter]).html(text) )
            counter++;
      });
  });
}
});

$( document ).ready(function() {
  if(  $('#id_codigo_obra').attr("type")!=="hidden"){
    if($('#id_codigo_obra').hasClass("select form-control")){
      var values = [];
      var names = [];
      var trying = [];
      var valuestrying = [];
      var counter = -1;

      $('#id_codigo_obra').before('<div id="appender" class="input-group"><span class="input-group-addon glyphicon glyphicon-search" id="basic-addon1"></span><input class="form-control" name="text">');
      $('#id_codigo_obra option').each(function() {
          values.push( $(this).attr('value').toLowerCase() );
          names.push( $(this).text().toLowerCase() );
      });

      $('input[name=text]').on('input',function() {
        valuestrying = [];
        counter = -1;
        var busca = $('input[name=text]').val().toLowerCase();
        $('#id_codigo_obra').empty();
        trying = jQuery.grep(names, function( a ) {
          counter++;
          var comparacion = a.toLowerCase();
          if(comparacion.includes(busca.toLowerCase())){
            valuestrying.push(values[counter])
            return a;
          }
        });
        counter = 0;
        $.each(trying, function(val, text) {
                $('#id_codigo_obra').append( $('<option></option>').val(valuestrying[counter]).html(text) )
                counter++;
          });
      });
    }
  }
});

$(document).on('click', '#elboton', function(){
  var busca = $('#busca').val();
  var pathname = window.location.pathname;
  if (pathname[pathname.length - 1] === "/"){
    window.location.replace(pathname + busca);
  }
  else{
    pathnombre = pathname.split("/");
    realpathname = "";
    for(i=1; i<pathnombre.length; i++){
      if (pathnombre[i-1]!==""){
        realpathname += pathnombre[i-1];
        if (i!==pathname.length -1){
          realpathname += "/";
        };
      };
    };
    window.location.replace("/"+realpathname + busca);
  };
});

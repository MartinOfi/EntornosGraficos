<?php 
if (isset($_POST['enviar'])) {
  require("config/config.php");
  $ciudad = $_POST['ciudad'];
  $pais = $_POST['pais'];
  $habitantes = $_POST['habitantes'];
  $superficie = $_POST['superficie'];
  $metro = $_POST['metro'];
  $insertar = $conexion->query("INSERT INTO ciudades(ciudad,pais,habitantes,superficie,tieneMetro) VALUES ('$ciudad','$pais','$habitantes','$superficie','$metro')");

  if ($insertar) {
    echo "Se ah enviado correctamente";
  } else {
    echo "Ocurrio un error";
  }
}
header("Location: tabla.php")
?>
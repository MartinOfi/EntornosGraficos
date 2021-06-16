<?php

$CONserver = "localhost";
$CONuser="root";
$CONpass="";
$CONdb="capitales";

$conexion= new mysqli($CONserver,$CONuser,$CONpass,$CONdb);

if ($conexion-> connect_errno) {
  die("La conexion ha fallado");
}

?>

<?php 
  include("./config/config.php");

  if(isset($_GET['id'])){
    $id=$_GET['id'];
    $query="DELETE FROM ciudades WHERE id=$id";
    $results=mysqli_query($conexion,$query);
    if (!$results) {
      die("Query Failed");
    }
    $_SESSION['message']='City Removed Successfully';
    header("Location: tabla.php");
  }
?>
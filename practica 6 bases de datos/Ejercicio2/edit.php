<?php
include("./config/config.php");
if (isset($_GET['id'])) {
  $id = $_GET['id'];
  $query = "SELECT * FROM ciudades WHERE id=$id";
  $result = mysqli_query($conexion, $query);
  if (mysqli_num_rows($result) == 1) {
    $row = mysqli_fetch_array($result);
    $ciudad = $row['ciudad'];
    $pais = $row['pais'];
    $habitantes = $row['habitantes'];
    $superficie = $row['superficie'];
    $metro = $row['tieneMetro'];
  }
}
if (isset($_POST['actualizar'])) {
  $id=$_GET['id'];
  $ciudad = $_POST['ciudad'];
  $pais = $_POST['pais'];
  $habitantes = $_POST['habitantes'];
  $superficie = $_POST['superficie'];
  $metro = $_POST['metro'];
  
  $query="UPDATE ciudades set ciudad='$ciudad', pais='$pais',habitantes='$habitantes', superficie='$superficie',tieneMetro='$metro' WHERE id=$id";
  mysqli_query($conexion,$query);
  header("Location: tabla.php");
}

?>
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="./tabla.css">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.3/css/all.css" integrity="sha384-SZXxX4whJ79/gErwcOYf+zWLeJdY/qpuqC4cAa9rOGUstPomtqpuNWT9wdPEn2fk" crossorigin="anonymous">
  <title>Document</title>
</head>

<body>
  <div class="container p-4">
    <div class="col md-4">
      <div class="card-body">
        <h1 class="text-center">Formulario de modificacion</h1>
        <h3 class="text-center">Ingrese los nuevos datos</h3>
        <form action="edit.php?id=<?php echo $_GET['id'] ?>" method="POST">
          <label for="InpCiudad">Ciudad</label>
          <input type="text" name="ciudad" id="InptCiudad" class="form-control" value="<?php echo $ciudad?>">
          <br>
          <label for="InpPais">Pais</label>
          <input type="text" name="pais" id="InpPais" class="form-control" value="<?php echo $pais ?>">
          <br>
          <label for="InpHabitantes">Habitantes</label>
          <input type="number" name="habitantes" id="InpHabitantes" class="form-control" value="<?php echo $habitantes ?>">
          <br>
          <label for="InpSuperficie">Superficie</label>
          <input type="number" name="superficie" id="InpSuperficie" class="form-control" value="<?php echo $superficie ?>">
          <br>
          <label for="InpMetro">Cantidad de Metros</label>
          <input type="number" name="metro" id="InpMetro" class="form-control" value="<?php echo $metro ?>">
          <br>
          <input type="submit" name="actualizar" class="btn btn-primary" value="actualizar">
        </form>
      </div>
    </div>
  </div>
</body>

</html>
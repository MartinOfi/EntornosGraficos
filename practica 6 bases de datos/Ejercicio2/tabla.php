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
  <div class="container pt-5">
    <div class="row mr-2">
      <div class="col-3 ">
        <form action="save.php" method="POST">
          <label for="InpCiudad">Ciudad</label>
          <input type="text" name="ciudad" id="InptCiudad" class="form-control">
          <br>
          <label for="InpPais">Pais</label>
          <input type="text" name="pais" id="InpPais" class="form-control">
          <br>
          <label for="InpHabitantes">Habitantes</label>
          <input type="number" name="habitantes" id="InpHabitantes" class="form-control">
          <br>
          <label for="InpSuperficie">Superficie</label>
          <input type="number" name="superficie" id="InpSuperficie" class="form-control">
          <br>
          <label for="InpMetro">Cantidad de Metros</label>
          <input type="number" name="metro" id="InpMetro" class="form-control">
          <br>
          <input type="submit" name="enviar" class="btn btn-primary">
        </form>
      </div>
 
      <div class="col-9">
        <div class="row">
          <div class="col 1">
            <p>ID</p>
          </div>
          <div class="col 2">
            <p>CIUDAD</p>
          </div>
          <div class="col 2">
            <p>PAIS</p>
          </div>
          <div class="col 2">
            <p>HABITANTES</p>
          </div>
          <div class="col 2">
            <p>SUPERFICIE</p>
          </div>
          <div class="col 1">
            <p>METROS</p>
          </div>
          <div class="col 2">Option</div>
        </div>
        <?php
        require("config/config.php");
        $sql = "SELECT * from ciudades";
        $result = mysqli_query($conexion, $sql);
        while ($row = mysqli_fetch_array($result)) {
        ?>

          <div class="row">
            <div class="col 1"><?php echo $row['id'] ?></div>
            <div class="col 2"><?php echo $row['ciudad']  ?></div>
            <div class="col 2"><?php echo $row['pais']  ?></div>
            <div class="col 2"><?php echo $row['habitantes']  ?></div>
            <div class="col 2"><?php echo $row['superficie']  ?></div>
            <div class="col 1"><?php echo $row['tieneMetro']  ?></div>
            <div class="col 2"><a href="edit.php?id=<?php echo $row['id'] ?>" class="btn btn-secondary"><i class="fas fa-edit fa-xs"></i></a><a href="delete.php?id=<?php echo $row['id'] ?>" class="btn btn-danger"><i class="far fa-trash-alt fa-xs"></i></a></div>

          </div>
   
        <?php
        }
        ?>
      </div>
    </div>
  </div>

</body>

</html>
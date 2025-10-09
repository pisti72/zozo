<?php
    $vezeteknev = $_POST["fname"];
    $keresztnev = $_POST["lname"];
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="mystyle.css" rel="stylesheet">
</head>
<body>
    <h1> Üdvözöllek <?php echo($vezeteknev ." ". $keresztnev); ?> ! </h1>
    <a href= "index.php" > vissza </a>
</body>
</html>
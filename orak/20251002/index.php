<!DOCTYPE html>
<html lang="hu">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
  

   <title>Zozo weboldala</title>
   <link rel="stylesheet" href="mystyle.css">
</head>
<body>
<h1> Hello world </h1>
<p> Zozo weboldala </p>
<form action="/output.php" method="post">
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname" value="John"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname" value="Doe"><br><br>
  <input type="submit" value="Submit">
</form> 
<?php
   $szamok = array("Laci","Pista","Akármi","Valami");
   foreach($szamok as $szam){
?>
   <p>Hello világ --> <?php echo($szam); ?>. </p>
<?php
   }
?>


<a href="teszt.php">teszt</a>

</body>
</html>




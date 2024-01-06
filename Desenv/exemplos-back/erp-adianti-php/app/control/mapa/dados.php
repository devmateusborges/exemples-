<?php
 

 
$dsn = "pgsql:host=abdb.ceaiono4y2vq.sa-east-1.rds.amazonaws.com;port=5432;dbname=abdadosdev;user=postgres;password=abpg123#";
 
try{
 // create a PostgreSQL database connection
 $conn = new PDO($dsn);
 
 // display a message if connected to the PostgreSQL successfully
 if($conn){

    $sql = 'SELECT * FROM bor_mov ';
    foreach ($conn->query($sql) as $row) {
        print $row['numero_serie'] . "\t";
    }

 //echo "Connected to the <strong>$db</strong> database successfully!";
 }
}catch (PDOException $e){
 // report error message
 echo $e->getMessage();
}
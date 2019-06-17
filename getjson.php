<?php

    error_reporting(E_ALL); 
    ini_set('display_errors',1); 

    include('dbcon.php');
        

    $stmt = $con->prepare('select * from ranking');
    $stmt->execute();

    if ($stmt->rowCount() > 0)
    {
        $data = array(); 

        while($row=$stmt->fetch(PDO::FETCH_ASSOC))
        {
            extract($row);
    
            array_push($data, 
                array(
                'name'=>$concert_name,
                'place'=>$concert_place,
				'start_date'=>$concert_start_date,
				'end_date'=>$concert_end_date
            ));
        }

        header('Content-Type: application/json; charset=utf8');
        $json = json_encode(array("ranking"=>$data), JSON_PRETTY_PRINT+JSON_UNESCAPED_UNICODE);
        echo $json;
    }
?>

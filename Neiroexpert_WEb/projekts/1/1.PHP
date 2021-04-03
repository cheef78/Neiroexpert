<?php
    $fp = fopen ( "force_line.csv" , "r" );
    while (( $data = fgetcsv ( $fp , 1000 , "," )) !== FALSE ) {
        $i = 0;
        echo "<tr>";
        foreach($data as $row) {
           echo "<td>" . $row . "</td>";
           $i++ ;
        }
        echo "/<tr>";
    }
    fclose ( $fp );
?>
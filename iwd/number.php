<?php
$number = $_POST['number'];
$range_1 = $_POST['range1'];
$range_2 = $_POST['range2'];

function RandomNumber($range_1,$range_2){
    echo "range between $range_1 and $range_2:  ";
    echo rand($range_1,$range_2);
    echo "<br>";
}

function Conversion($number){
    echo "decimal - binary $number:  ";
    echo decbin($number);
    echo "<br>";
    echo "decimal - Hexa $number:  ";
    echo dechex($number);
    echo "<br>";
    echo "decimal - oct $number:  ";
    echo decoct($number);
    echo "<br>";

}

    function Angle($number){
    echo "sin $number:  ";
    echo sin($number);
    echo "<br>";
    echo "cos $number:  ";
    echo cos($number);
    echo "<br>";
    echo "tan $number:  ";
    echo tan($number);
    echo "<br>";
}

RandomNumber($range_1,$range_2);
Conversion($number);
Angle($number);
?>
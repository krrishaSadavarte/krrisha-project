<?php
$choice = $_GET['radio1'];
$a = $_GET['a'];
$b = $_GET['b'];
switch($choice)
{
    case "add":
        $result =$a+$b;
        echo "sum=$result";
        break;
    case "sub":
        $result =$a-$b;
        echo "sub=$result";
        break;
    case "multi":
        $result =$a*$b;
        echo "multiply=$result";
        break;
    case "div":
        $result =$a/$b;
        echo "divide=$result";
        break;
    default:
        echo "invalid choice";
}

?>
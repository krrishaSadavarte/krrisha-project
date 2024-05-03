<?php
$str = $_POST['name'];
$replace = $_POST['rep'];
echo "givin string : $str";
echo "<br>";
function CheckForLowerCase($string){
     if(strtolower($string)){
        echo "Lower Case : true" ; 
        echo "<br>";
     }
     else{
        echo "Lower Case : False";
        echo "<br>";

     }
}
 
function ReverseString($string){
    echo"Reverse: " ;
     echo strrev($string);
     echo "<br>";

}

function RemoveWhiteSpace($string){
    echo "White space  : ";
    echo trim($string);
    echo "<br>";

}

function ReplaceWord($string,$word){
    echo "Replace : ";
    print(str_replace($string,$word,$string));
    echo "<br>";

}
CheckForLowerCase($str);
ReverseString($str);
RemoveWhiteSpace($str);
ReplaceWord($str,$replace);
?>
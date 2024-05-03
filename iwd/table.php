<?php
$num= $_GET['num'];
echo "Multiplication of $num";
echo "<br>";
for ($i=1;$i<=10;$i++)
{   $result = $num*$i;
    echo "$num X $i = $result";
    echo "<br>";
}

?>
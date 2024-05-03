<?php
$number = $_GET['num'];
$fnum = 0;
$snum = 1;
echo "Fibonacci series of $number";
echo "<br>";
echo "$fnum + $snum +";
for($i = 0;$i<=$number;$i++)
{
    $next = $fnum + $snum;
    echo "$next+" ;
    $fnum = $snum;
    $snum = $next;

}

?>
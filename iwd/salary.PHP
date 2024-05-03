<?php
$Basic_salary = $_GET['salary'];
$EMP_NAME = $_GET['name'];
$DA = 50/100*$Basic_salary;
$HRA = 10/100*$Basic_salary;
$MEDICAL = 4/100*$Basic_salary;
$INSURANCE = 7/100*$Basic_salary;
$PF = 5/100*$Basic_salary;
$NET_SALARY = $Basic_salary+$DA+$HRA+$MEDICAL - $INSURANCE+$PF;

echo "NAME : $EMP_NAME ";
echo "<br>";
echo "BASIC SALARY : $Basic_salary";
echo "<br>";
echo "NET SALARY : $NET_SALARY";


?>
<?php
$fname=$_GET['fname'];
$lname=$_GET['lname'];
$age=$_GET['age'];
$number=$_GET['number'];
$email=$_GET['email'];

if(Empty($fname) ||Empty($lname) || Empty($age) ||Empty($number)|| Empty($email)){
    echo "enter your data";
    exit;
}
else{
    echo "First Name : $fname";
    echo "<br>";
    echo "last name : $lname";
    echo "<br>";
    echo "Age : $age";
    echo "<br>";
    echo "Conatct Number : $number";
    echo "<br>";
    echo "Email : $email";
}
?>
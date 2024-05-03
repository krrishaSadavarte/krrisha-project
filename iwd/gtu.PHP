<?php
$math = $_GET['maths'];
$science = $_GET['science'];
$social_science = $_GET['ss'];
$english = $_GET['english'];
$flag = 1;
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>   
<div class="cl1">
  <table cellpadding="10px" border="solid black 1px">
   <tr>
    <td>NAME : SADAVARTE KRRISHA</td>
    <td>EN_ROLL : 226150307195</td>>
   </tr>
  </table>
</div>
<div class="cl2">
    <table cellpadding="15px" border="solid black 1px">
        <tr>
            <th>Sr.No</th>
            <th>SUBJECT</th>
            <th>CODE</th>
            <th>GRADE</th>
        </tr>
        <tr>
            <td>1</td>
            <td>MATHS</td>
            <td>220179</td>
            <td> <?php if ($math >= 85){
                echo "AA";
            }
            elseif($math >=75 && $math<=84){
                echo "AB";
            }
            elseif($math >=65 && $math<=74){
                echo "BB";
            }
            elseif($math >=55 && $math<=64){
                echo "BC";
            }
            elseif($math >=45 && $math<=54){
                echo "CC";
            }
            elseif($math >=40 && $math<=44){
                echo "CD";
            }
            elseif($math >=35 && $math<=39){
                echo "DD";
            }
            elseif($math <=39){
                echo "FF";
                $flag = 0;
            
            }
            else{
                echo "Invalid Choice";
            } ?></td>
            
        </tr>

        <tr>
            <td>2</td>
            <td>ENGLISH</td>
            <td>220159</td>
            <td> <?php if ($english >= 85){
                echo "AA";
            }
            elseif($english >=75 && $english<=84){
                echo "AB";
            }
            elseif($english >=65 && $english<=74){
                echo "BB";
            }
            elseif($english >=55 && $english<=64){
                echo "BC";
            }
            elseif($english >=45 && $english<=54){
                echo "CC";
            }
            elseif($english >=40 && $english<=44){
                echo "CD";
            }
            elseif($english >=35 && $english<=39){
                echo "DD";
            }
            elseif($english <=39){
                echo "FF";
                $flag = 0;
            
            }
            else{
                echo "Invalid Choice";
            } ?></td>
            
        </tr>

        <tr>
            <td>3</td>
            <td>SCIENCE</td>
            <td>220180</td>
            <td> <?php if ($science >= 85){
                echo "AA";
            }
            elseif($science >=75 && $science<=84){
                echo "AB";
            }
            elseif($science >=65 && $science<=74){
                echo "BB";
            }
            elseif($science >=55 && $science<=64){
                echo "BC";
            }
            elseif($science >=45 && $science<=54){
                echo "CC";
            }
            elseif($science >=40 && $science<=44){
                echo "CD";
            }
            elseif($science >=35 && $science<=39){
                echo "DD";
            }
            elseif($science <=39){
                $flag = 0;
            
                echo "FF";
            }
            else{
                echo "Invalid Choice";
            }?></td>
            
        </tr>
        <tr>
            <td>4</td>
            <td>SOCIAL SCIENCE</td>
            <td>220181</td>
            <td> <?php if ($social_science >= 85){
                echo "AA";
            }
            elseif($social_science >=75 && $social_science<=84){
                echo "AB";
            }
            elseif($social_science>=65 && $social_science<=74){
                echo "BB";
            }
            elseif($social_science >=55 && $social_science<=64){
                echo "BC";
            }
            elseif($social_science >=45 && $social_science<=54){
                echo "CC";
            }
            elseif($social_science >=40 && $social_science<=44){
                echo "CD";
            }
            elseif($social_science >=35 && $social_science<=39){
                echo "DD";
            }
            elseif($social_science <=39){
                $flag = 0;
                echo "FF";
            }
            else{
                echo "Invalid Choice";
            }?></td>
            
        </tr>
      
    </table>
</div>
<div class="cl3">
    <table cellpadding="10px" border="solid black 1px">
        <tr>
        <th>
            <?php
        $flag = 1;

        if ($flag != 0){
            echo "<br> congratulations! you have cleared this exam successfully!!!!";
        }
        else{
            echo "<br>sorry! you have not cleared this exam!!!!!!!";
        }
        
        ?>
        </th>
        </tr>
       </table>


</div>
</body>
</html>
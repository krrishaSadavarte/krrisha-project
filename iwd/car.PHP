<?php
$Car_Name = $_GET['car'];
if($Car_Name=='Safari'||$Car_Name=='Nexon'||$Car_Name=='Tiago'||$Car_Name=='Tigor'){
    echo "$Car_Name belongs to TATA Company";
}
elseif ($Car_Name=='XUV700'||$Car_Name=='XUV300'||$Car_Name=='Bolero') {
    echo "$Car_Name belongs to MAHINDRA Company";
}
elseif($Car_Name=='i20'||$Car_Name=='Verna'||$Car_Name=='Venue'||$Car_Name=='Creta'){
    echo "$Car_Name belongs to HYUNDAI Company";
}
elseif($Car_Name=='Alto'||$Car_Name=='Swift'||$Car_Name=='Baleno'||$Car_Name=='Brezza'){
    echo "$Car_Name belongs to SUZUKI Company";
}
else{
    echo "Invalid Choice";
}
?>
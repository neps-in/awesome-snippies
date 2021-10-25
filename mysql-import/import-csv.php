<?php
/**
 * FileName: Import CSV file into mysql database
 * @var string
 */

$csv_file = 'india_pincodes.csv';

$database = 'pfs_py';

$field_names = [
    "office_name","pincode","office_type",
    "delivery_status","division_name",
    "region_name","circle_name","taluk",
    "district_name","state_name","telephone",
    "related_suboffice","related_headoffice","longitude","latitude"
];

function read_csv_file_to_array( $csv_file ){
   
   $rows = []; $i = 0;
   if (($handle = fopen($csv_file, "r")) !== FALSE) {
        while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
            $num = count($data);
            // echo "--------------------- I := " . $i . PHP_EOL ;
           
            $single_row['office_name'] = $data[0];
            $single_row['pincode'] = $data[1];
            $single_row['office_type'] = $data[2];
            $single_row['delivery_status'] = $data[3];
            $single_row['division_name'] = $data[4];
            
            $single_row['region_name'] = $data[5];
            $single_row['circle_name'] = $data[6];
            $single_row['taluk'] = $data[7];
            $single_row['district_name'] = $data[8];
            $single_row['state_name'] = $data[9];

            $single_row['telephone'] = $data[10];
            $single_row['related_suboffice'] = $data[11];
            $single_row['related_headoffice'] = $data[12];
            $single_row['longitude'] = $data[13];
            $single_row['latitude'] = $data[14];

            $rows[$i] = $single_row;

            //print_r( $rows[$i] );
            $i++;

        }
        fclose($handle);
    } 

    return $rows;
}



$mysqli = new mysqli("localhost", "root", "mysql", $database); 
  
if ($mysqli === false) { 
    die("ERROR: Could not connect. ".$mysqli->connect_error); 
}
   
$row_count = 0;
$fields = '';
echo PHP_EOL. 'Reading CSV file : ' . $csv_file ;
$rows = read_csv_file_to_array( $csv_file );

foreach( $rows as $row ){

   echo PHP_EOL . ' ------------------------------------------- ' . PHP_EOL;
   echo PHP_EOL . ' Row := ' . $row_count . PHP_EOL;
  
   $fields = '';

   $count = 0;
   foreach($row as $col => $val) {
      if ($count != 0) $fields .= ', ';
      $col = mysqli_real_escape_string($mysqli, $col);
      $val = mysqli_real_escape_string($mysqli, $val);
      $fields .= "`$col` = '$val'";
      $count++;
   }
   $query = "INSERT INTO `dummy_pincodes` SET $fields;";
   
   echo 'Query : ' . PHP_EOL;   
   print_r( $query );
   
   if ($mysqli->query($query) === true) { 
        echo PHP_EOL . PHP_EOL . "Records inserted successfully." . PHP_EOL;
   } else { 
        echo PHP_EOL . "ERROR: Could not able to execute $query. "
               .$mysqli->error; 
   }
   echo PHP_EOL . ' ------------------------------------------- ' . PHP_EOL;

   $row_count++;

}

//Close connection 
$mysqli->close(); 
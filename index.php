<?php
    ini_set('display_errors', 1);
    ini_set('display_startup_errors', 1);
    error_reporting(E_ALL);

    include_once 'DbWorker.php';

    $db = new DbWorker();
    // $db->initDb();
    // $test = ["ac" => 1, "rf" => 2];
    // $db->insert($test);
    //$test = ["ac"];
    $test = "ac";
    print_r($db->select($test));
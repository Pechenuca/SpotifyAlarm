<?php
    ini_set('display_errors', 1);
    ini_set('display_startup_errors', 1);
    error_reporting(E_ALL);

    include_once 'DbWorker.php';
    include_once 'ApiWorker.php';

    $apiworker = new ApiWorker();
    $db = new DbWorker();
    $db->initDb();


    $test = ["ac", "rf"];
    $token = $db->select($test)["ac"];
    $api = $apiworker->getAcces($token);
    $pl = $apiworker->showPlaylists($api);
    print_r($pl);
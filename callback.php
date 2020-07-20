<?php

ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

include_once 'ApiWorker.php';

$apiworker = new ApiWorker(
    '4c1a95527dc54225a451755541e9206d',
    'cb042e53ec654ded8685375027afd105',
    'http://localhost:8888/callback.php'
);

$session = $apiworker->sessionCreater();
$tokens = $apiworker->getTokens($session);

// header('Location: index.php');
// die();


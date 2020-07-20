<?php

require 'vendor/autoload.php';

$session = new SpotifyWebAPI\Session(
    '4c1a95527dc54225a451755541e9206d',
    'cb042e53ec654ded8685375027afd105',
    'http://localhost:8888/callback.php'
);

$api = new SpotifyWebAPI\SpotifyWebAPI();

if (isset($_GET['code'])) {
    $session->requestAccessToken($_GET['code']);
    $api->setAccessToken($session->getAccessToken());

    //print_r($api->me());
} else {
    $options = [
        'scope' => [
            'user-read-email',
        ],
    ];

    header('Location: ' . $session->getAuthorizeUrl($options));
    die();
}
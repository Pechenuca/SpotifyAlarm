<?php

require 'vendor/autoload.php';

$session = new SpotifyWebAPI\Session(
    '4c1a95527dc54225a451755541e9206d',
    'cb042e53ec654ded8685375027afd105',
    'http://localhost:8888/callback.php'
);

$options = [
    'scope' => [
        'playlist-read-private',
        'user-read-private',
    ],
];

header('Location: ' . $session->getAuthorizeUrl($options));
die();
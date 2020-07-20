<?php

    require 'vendor/autoload.php';

    class ApiWorker{

        private $client_id;
        private $client_secret;
        private $redirect_uri;

        function __construct($client_id="", $client_secret="", $redirect_uri=""){
            $this->client_id = $client_id;
            $this->client_secret = $client_secret;
            $this->redirect_uri = $redirect_uri;
        }

        function sessionCreater(){
            $session = new SpotifyWebAPI\Session(
                $this->client_id,
                $this->client_secret,
                $this->redirect_uri
            );
            return $session;
        }

        function getTokens($session){
            $session->requestAccessToken($_GET['code']);
            $accessToken = $session->getAccessToken();
            $refreshToken = $session->getRefreshToken();

            $tokens = [
                "ac" => $accessToken,
                "rf" => $refreshToken
            ];

            return $tokens;
        }

        function thowCallback($session, $options){
            header('Location: ' . $session->getAuthorizeUrl($options));
            die();
        }

        function getAcces($accessToken){
            $api = new SpotifyWebAPI\SpotifyWebAPI();
            $api->setAccessToken($accessToken);
            return $api;
        }

        function showPlaylists($api, $limit=25){
            
            $userId = $api->me()->id;

            $playlists = $api->getUserPlaylists($userId, [
                'limit' => $limit
            ]);
            
            return $playlists;
            
        }

    }
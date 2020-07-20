<!DOCKTYPE HTML>
<html>
<head>
    <title> Spotify Alarm</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="assets/main.css">
    <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500&display=swap" rel="stylesheet">
</head>
<body>
    <div id = "header">
        <header> 
            <img id= "image" src="assets/Menhera.jpg">

        </header>
        <nav></nav>
        <div id = "heading"></div>
        <aside></aside>
        <section></section>
    </div>

<!-- <form>
    <button>
        Поставить будильник
    </button>

    <button>
        Удалить будильник
    </button>
</form> -->

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
    try{
        $pl = $apiworker->showPlaylists($api);
    } catch (Exception $e){
        $db->dropDeBase();
        $db->initDb();
        header('Location: auth.php');
        die();
    }

    if (filter_var($db->select("al")["al"], FILTER_VALIDATE_BOOLEAN) == false){
        echo 'Будильник не стоит 0))))0000)000), выбери плейлист суко!';
  
        echo '<div id="playlistsBlock">';
        foreach ($pl->items as $playlist) {
            echo '
                    <div class="imgHolder">
                        <img src="' . $playlist->images[0]->url  . '"> <br>
                        <a href="' . addAlarm . '">' . $playlist->name . '</a>
                    </div>
                ';
        }
        echo '</div>';

    }
    
    echo '<pre>';
    print_r($pl);
    echo '</pre>';
?>

</body>
</html>
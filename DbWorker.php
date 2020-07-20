<?php

    class DbWorker extends SQLite3 {
        
        function __construct(){
            $this->open('database.db');
        }

        function initDb(){
            $this->exec('CREATE TABLE IF NOT EXISTS spotify (ac STRING, rf STRING, al BOOL)');
        }

        function dropDeBase(){
            $this->exec("DROP TABLE IF EXISTS spotify");
        }

        function insert($values){
            $ac = $values["ac"];
            $rf = $values["rf"];
            $al = $values["al"];
            $this->exec("INSERT INTO spotify (ac, rf, al) VALUES ('$ac', '$rf', '$al')");
        }

        function select($options){

            if (is_array($options) == true){
                if (count($options) >= 1){
                    $optionsString = implode(", ", $options);
                }
            } else {
                $optionsString = $options;
            }
            
            return $this->query('SELECT '. $optionsString .' FROM spotify')->fetchArray();
        }

        
    }
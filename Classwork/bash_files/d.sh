#!/bin/bash 
                function quit {
                   exit
                }  
                function e {
                    echo $1 
                }  
                e $1
                e $2
                quit
                echo foo 
#!/bin/sh

touch botTestData.txt
nodejs ../Node1/bot.js>botTestData.txt
line=$(head -n 2 botTestData.txt.txt)
expectResult="^[A-Za-z]{3} [A-Za-z]{3} [0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} [+][0-9]{4} [0-9]{4} ---\$\%\^\--- .*"

if ["$line"="$expectResult"];then
    echo testpassed
else
    echo testfailed
    echo $line
fi


 #!/bin/bash
let "a = $1 % 2"
if [ $a == 0 ]
    then
        echo $1 is even!
    else
        echo $1 is odd!
fi

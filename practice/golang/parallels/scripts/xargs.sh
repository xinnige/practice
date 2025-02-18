
xargs -I {} -P 20 echo {} < <(printf '%s\n' {1..10})

seq 10 | xargs -I X bash -c "echo X \$RANDOM"


xargs -I {} -P 10 curl -u admin:123456 http://127.0.0.1/index.html  < <(printf '%s\n' {1..20})
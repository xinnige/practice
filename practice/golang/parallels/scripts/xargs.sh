xargs -I {} -P 20 echo {} < <(printf '%s\n' {1..10})

seq 10 | xargs -I X bash -c "echo X \$RANDOM"
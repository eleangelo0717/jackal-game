{
  echo 'my data source'
  while true ; do
    echo "${i}000 $RANDOM"
    sleep 1
  done
} | nc localhost 8765
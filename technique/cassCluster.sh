#!/bin/bash
docker pull abh1nav/opscenter:latest
docker pull abh1nav/cassandra:latest
echo "Starting OpsCenter"
docker run -d --name opscenter abh1nav/opscenter:latest
sleep 10
OPS_IP=$(docker inspect -f '{{ .NetworkSettings.IPAddress }}' opscenter)
echo "Starting node cass1"
docker run -d --name cass1 -e OPS_IP=$OPS_IP abh1nav/cassandra:latest
sleep 30
SEED_IP=$(docker inspect -f '{{ .NetworkSettings.IPAddress }}' cass1)
for name in cass{2..3}; do
  echo "Starting node $name"
  docker run -d --name $name -e SEED=$SEED_IP -e OPS_IP=$OPS_IP abh1nav/cassandra:latest
  sleep 30
done
echo "Registering cluster with OpsCenter"
curl \
  http://$OPS_IP:8888/cluster-configs \
  -X POST \
  -d \
  "{
      \"cassandra\": {
        \"seed_hosts\": \"$SEED_IP\"
      },
      \"cassandra_metrics\": {},
      \"jmx\": {
        \"port\": \"7199\"
      }
  }" > /dev/null
echo "Go to http://$OPS_IP:8888/"
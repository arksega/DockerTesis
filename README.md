# DockerTesis
This is a series of scripts and config files to test docker/kubernetes using ampache as example service

# Minikube demo
```
# Init minikube
minikube start

# Start wordpress deployments
cd wordpress
kubectl apply -f db-deployment.yaml
# Check db is running
kubectl get po --watch
kubectl apply -f wordpress-deployment.yaml
# Check worpress is running
kubectl get po --watch
# Get external address
minikube service wordpress --url

# Install prometheus operator
helm init
helm install --name monitor stable/prometheus-operator
kubectl get po --watch
# Expose services
kubectl expose po prometheus-monitor-prometheus-operato-prometheus-0 --type=LoadBalancer --name=prometheus
kubectl expose deployment monitor-grafana --name grafana --type=LoadBalancer

# Loging admin:prom-operator
minikube service grafana --url

# Prometheus
minikube service prometheus --url
```

## Exposed metrics
```
# HELP apache_accesses_total Current total apache accesses (*)
# TYPE apache_accesses_total counter
apache_accesses_total 848
# HELP apache_cpuload The current percentage CPU used by each worker and in total by all workers combined (*)
# TYPE apache_cpuload gauge
apache_cpuload 0.20183
# HELP apache_exporter_build_info A metric with a constant '1' value labeled by version, revision, branch, and goversion from which apache_exporter was built.
# TYPE apache_exporter_build_info gauge
apache_exporter_build_info{branch="",goversion="go1.8.7",revision="",version=""} 1
# HELP apache_scoreboard Apache scoreboard statuses
# TYPE apache_scoreboard gauge
apache_scoreboard{state="closing"} 0
apache_scoreboard{state="dns"} 0
apache_scoreboard{state="graceful_stop"} 0
apache_scoreboard{state="idle"} 9
apache_scoreboard{state="idle_cleanup"} 0
apache_scoreboard{state="keepalive"} 0
apache_scoreboard{state="logging"} 0
apache_scoreboard{state="open_slot"} 140
apache_scoreboard{state="read"} 0
apache_scoreboard{state="reply"} 1
apache_scoreboard{state="startup"} 0
# HELP apache_sent_kilobytes_total Current total kbytes sent (*)
# TYPE apache_sent_kilobytes_total counter
apache_sent_kilobytes_total 9817
# HELP apache_up Could the apache server be reached
# TYPE apache_up gauge
apache_up 1
# HELP apache_uptime_seconds_total Current uptime in seconds (*)
# TYPE apache_uptime_seconds_total counter
apache_uptime_seconds_total 4043
# HELP apache_workers Apache worker statuses
# TYPE apache_workers gauge
apache_workers{state="busy"} 1
apache_workers{state="idle"} 9
```

# Bare metal demo
```
cd baremetal
mkdir ampache
cd ampache
wget https://github.com/ampache/ampache/releases/download/3.9.0/ampache-3.9.0_all.zip
unzip ampache
cd ..
docker-compose -p ampache up
```

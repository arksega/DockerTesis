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

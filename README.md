# apppy
A hello world Flask web app for testing docker/Kubernetes with.

## docker stuff

From the project directory,

``` bash
docker build -t py-server .
```

will build the image.

``` bash
docker run -p5000:5000 -d py-server
```

runs the server. You should see **Hello, world.** at [http://localhost:5000](http://localhost:5000)

To publish to a docker repo, after a `docker login ...` to your repo ([dockerhub](https://hub.docker.com/) or similar), first you tag your image:

``` bash
docker tag py-server <your repo username>/py-server
```

then

``` bash
docker push <your repo username>/py-server
```

## Kubernetes Stuff
To get the server running on Kubernetes:

``` bash
kubectl run apppy --image=<your repo username>/py-server
```

This runs the server, pulling it from your docker repo. You can see your new pod running with

``` bash
kubectl get pods
```

You won't be able to see your web app running just yet, until you expose it:

``` bash
kubectl expose deployments apppy --port=80 --type=LoadBalancer
```

You can see the exposed service with

``` bash
kubectl get services
```

To get Kubernetes' horizontal scaling going you use something like

``` bash
kubectl autoscale deployment/apppy --min=10 --max=15 --cpu-percent=80
```

To keep a copy of what you've built

``` bash
kubectl get deployments --field-selector metadata.name=apppy -o yaml > apppy-deployment.yaml
```

Next time you need to make one just like it:

``` bash
kubectl create --save-config -f apppy-deployment.yaml
```

Some other commands that may be enlightening:

``` bash
kubectl get replicasets
kubectl get deployments
```

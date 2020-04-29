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

This runs the server, pulling it from your docker repo.

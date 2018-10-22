SOURCE_DIR = ./

all: env

.PHONY : env app push clean

env:
	docker build -t hyhlinux/flask_env  .  -f Dockerfile.env

app:
	docker build -t hyhlinux/flask_app  .  -f Dockerfile

push:
	docker push hyhlinux/flask_env
	docker push hyhlinux/flask_app

clean:
	docker build -t hyhlinux/flask_env  .  -f Dockerfile.env --no-cache
	docker build -t hyhlinux/flask_app  .  -f Dockerfile --no-cache

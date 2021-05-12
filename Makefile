ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))


build:
	docker build -t covid_model .


# run:
# 	docker run \
# 		-d \
# 		-p 8501:8501 \
# 		--mount type=bind,source="$(ROOT_DIR)",target=/app \
# 		--name covid_model \
# 		covid_model


run-dev:
	docker run \
		--rm \
		-it \
		-p 8501:8501 \
		-p 8888:8888 \
		--mount type=bind,source="$(ROOT_DIR)",target=/app \
		--name covid_model \
		covid_model


clean:
	docker rm covid_model


deep-clean: clean
	docker image rm covid_model

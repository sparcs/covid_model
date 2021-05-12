# WIP: COVID-19 Resource Estimation Modelling using SIR and SIRS
---

## Requirements

- Docker


## Setup

### Commands

- `make` builds the docker image
- `make run-dev` runs the docker container in development mode
- `make clean` deletes the docker container
- `make deep-clean` deletes the container and the image

### Development Install

- run `make` and then `make run-dev` to get the docker container running on \
    your local env
- prefix the `make` commands with `sudo` if required on linux
- run the following commands once logged into the container's bash shell
  - `pip install -e .` # [required step] to install covid_model package
  - `jupyter notebook --ip 0.0.0.0 --allow-root` # [optional step] to start \
      notebook server
  - `streamlit run app.py` # [optional step] to run the streamlit app


## Usage

- Run app using the Install instructions mentioned above and access it at \
    http://localhost:8501
- Run notebook server if required and access it at http://localhost:8888

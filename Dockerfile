FROM continuumio/miniconda3

SHELL ["/bin/bash", "--login", "-c"]
EXPOSE 8501
EXPOSE 8888

RUN apt-get update && \
    apt -y upgrade && \
    apt-get install -y gcc pkg-config

RUN conda update -y conda && \
    conda init bash

WORKDIR /app

COPY environment.yml .
RUN conda env create -f environment.yml && \
    echo "source activate covid_model" >> ~/.bashrc

ENV PATH /opt/conda/envs/covid_model/bin:$PATH

CMD ["bash"]  # For development

# CMD ["streamlit", "run", "app.py"]

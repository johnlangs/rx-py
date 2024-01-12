FROM mambaorg/micromamba:alpine

WORKDIR /app

COPY --chown=$MAMBA_USER:$MAMBA_USER . ./
RUN micromamba install --yes --file ./env.yaml && \
    micromamba clean --all --yes
ARG MAMBA_DOCKERFILE_ACTIVATE=1

WORKDIR /app/src
EXPOSE 5000
CMD flask --app server run --host=0.0.0.0

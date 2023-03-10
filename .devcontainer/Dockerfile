FROM mcr.microsoft.com/vscode/devcontainers/universal:2

RUN python -m pip install --upgrade pip \
    && python -m pip install \
    black \
    flake8 \
    flit \
    pylint \
    pytest \
    pytest-cov

COPY .pre-commit-config.yaml .
RUN python -m pip install pre-commit \
    && git init . \
    && pre-commit install-hooks

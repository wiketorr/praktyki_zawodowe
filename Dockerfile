FROM python:3.14.0 AS develop
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/


ENV UV_CACHE_DIR=/var/cache/uv
ENV UV_LINK_MODE=copy
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/workdir
ENV UV_PROJECT_ENVIRONMENT=/usr/local


WORKDIR /workdir

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --dev

COPY . .
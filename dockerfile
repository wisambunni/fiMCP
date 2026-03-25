FROM python:3.12

# install uv
RUN curl -LsSf http://astral.sh/uv/install.sh | sh

ENV PATH="/root/.local/bin/:$PATH"

WORKDIR /app
COPY pyproject.toml uv.lock ./
COPY README.md ./
RUN uv sync --frozen --no-dev
COPY . .
# EXPOSE 3000
CMD ["uv", "run", "python", "src/main.py"]
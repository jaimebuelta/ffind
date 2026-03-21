FROM python:3.13-slim
WORKDIR /app
COPY src/ src/
COPY tests/ tests/
COPY pyproject.toml build.py README.md ./
RUN pip install --no-cache-dir cram .
ENV FFIND_SORT=1
CMD cram tests/ && python3 tests/benchmark.py

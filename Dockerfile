ARG PYTHON_VERSION=3.12
ARG POETRY_VERSION=1.8.3
FROM python:$PYTHON_VERSION

ENV \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=$POETRY_VERSION \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Install curl and other dependencies
RUN apt-get update \
    && apt-get install -y curl build-essential

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && export PATH="$POETRY_HOME/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy only the dependency files first
COPY pyproject.toml poetry.lock /app/

# Install dependencies
RUN poetry install --no-root

# Copy the rest of the project files
COPY . /app/

# Expose the port
EXPOSE 8000

# Run the application
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]

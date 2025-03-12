# Use an official Python runtime as a parent image.
FROM python:3.9-slim

# Set the working directory in the container.
WORKDIR /app

# Copy the dependency files.
COPY pyproject.toml poetry.lock* /app/

# Install Poetry.
RUN pip install poetry

# Install dependencies. We disable virtual environments to install directly.
RUN poetry config virtualenvs.create false && poetry install --no-root

# Copy the rest of the application code.
COPY . /app

# Expose the port the app runs on.
EXPOSE 8000

# Run the FastAPI app with Uvicorn.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

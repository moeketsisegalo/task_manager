FROM pypy:latest
WORKDIR /app
# COPY . /app

# Copy the project files into the container
COPY . .
CMD python task_manager.py

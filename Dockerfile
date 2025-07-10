# Use the custom base image
FROM lukerobertson19/base-os:latest

# OCI labels for the image
LABEL org.opencontainers.image.title="AI Assistant plugin: Palo Alto Firewalls"
LABEL org.opencontainers.image.description="Palo Alto plugin to manage stand-alone firewalls"
LABEL org.opencontainers.image.base.name="lukerobertson19/base-os:latest"
LABEL org.opencontainers.image.source="https://github.com/LukeRoberson/Palo-Alto-Plugin"
LABEL org.opencontainers.image.version="1.0.0"

# Custom Labels for the image
LABEL net.networkdirection.healthz="http://localhost:5100/api/health"
LABEL net.networkdirection.plugin.name="PaloAlto"

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Start the application using uWSGI
CMD ["uwsgi", "--ini", "uwsgi.ini"]

# Set the version of the image in metadata
ARG VERSION
LABEL org.opencontainers.image.version="${VERSION}"

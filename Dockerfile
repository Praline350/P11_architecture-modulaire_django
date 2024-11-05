# pull official base image
FROM python:3.10-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBUG=0

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# collect static files
RUN python manage.py collectstatic --noinput

# add and run as non-root user
RUN adduser -D myuser
USER myuser
# TODO : ne pas changer d'user

# Copy entrypoint.sh
COPY ./entrypoint.sh /app/entrypoint.sh

# Change permissions for the entrypoint script as root
USER root
RUN chmod +x /app/entrypoint.sh

# Switch back to non-root user
USER myuser

# Set entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]

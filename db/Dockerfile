# db/Dockerfile
FROM postgres:14

# Set environment variables
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=admin
ENV POSTGRES_DB=devops

# Copy initialization SQL script
COPY init.sql /docker-entrypoint-initdb.d/

# Expose default port
EXPOSE 5432

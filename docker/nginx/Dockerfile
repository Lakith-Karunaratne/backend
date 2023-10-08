# Use an official NGINX runtime as a parent image
FROM nginx:latest

# Copy the NGINX configuration file to the container
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80 to the outside world
EXPOSE 80

# Run NGINX in the foreground when the container starts
CMD ["nginx", "-g", "daemon off;"]

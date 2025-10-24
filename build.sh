#!/bin/bash

# Build Docker image
docker build -t finance-assistant-swarm .

echo "Docker image 'finance-assistant-swarm' built successfully!"
echo "To run the container:"
echo "docker run -it --rm finance-assistant-swarm"

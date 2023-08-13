# Use an official Python runtime as a parent image
FROM python:3.7-slim

# Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flask
RUN pip install flask_restful
RUN apt-get update && apt-get install -y libpq-dev
RUN pip install psycopg2-binary

# Set the working directory in the container
WORKDIR /app

# Add the current directory contents into the container
ADD . /app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]
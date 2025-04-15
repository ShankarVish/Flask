# Installing OS(slim) and Python version(can be checked using "python --version")
FROM python:3.12-slim

# Create working directory
WORKDIR /flask-docker 

# Upgrade pip
RUN python -m pip install --upgrade pip

# Install Python dependencies
# first name which is to be copied and then name in new folder of docker
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy source files, including app.py, artefacts, etc.
COPY . .

# Environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_PORT=5000
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000


# Run the Flask app
CMD ["flask", "run"]


# COMMAND TO CREATE DOCKER IMAGE ->" docker build -t flask_loan_app . "
# COMMAND TO RUN THE DOCKER IMAGE -> " docker run -p 8000:5000 flask_loan_app " 
# PREVIOUSLY THE FLASK WAS RUNNING ON PORT 5000 (DEFAULT) BUT NOW WE HAVE MAPPED IT USING COMMAND "-p 5000:8000" SO THAT NOW IT RUNS ON PIRT 8000 ON slim machine

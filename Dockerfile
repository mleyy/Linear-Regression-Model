FROM python:3.12

# Set the working directory
WORKDIR /src/app

# Set a default value for the PORT environment variable
ENV PORT=9090

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .
COPY src/ .

# Expose the port that your app runs on (e.g., 9090)
EXPOSE $PORT

# Use Gunicorn to run the application
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app

# Your CLEANED Dockerfile should start here:
FROM python:3.11-bullseye

# Set environment variable for non-interactive commands
ENV DEBIAN_FRONTEND noninteractive

# 1. Install necessary system dependencies for Tkinter
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    tk \
    libx11-6 && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the Python code 
COPY chatbot_gui.py /app/

# Install the necessary Python libraries (google-genai)
RUN pip install google-genai

# Command to run the application (Note: Running a GUI is tricky in headless environments)
ENTRYPOINT ["python", "chatbot_gui.py"]

# This Dockerfile builds a Python environment with Streamlit and your project files.

FROM python:3.9-slim

WORKDIR /app

# Copy requirements.txt (if you have one) and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy your project files
COPY . .

# Expose Streamlit port (default 8501)
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py"]
# Replace 'main.py' with your app's filename

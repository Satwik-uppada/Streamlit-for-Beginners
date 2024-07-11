# This Dockerfile builds a Python environment with Streamlit and your project files.

FROM python:3.9-slim

WORKDIR /webapp

# Copy requirements.txt (if you have one) and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy your project files
COPY . .

EXPOSE 8801

# Run the Streamlit app
CMD ["streamlit", "run", "stream.py"]

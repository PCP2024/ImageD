FROM python:3.12

# Set working directory
WORKDIR /app

# Install the application dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the whole code
COPY . .

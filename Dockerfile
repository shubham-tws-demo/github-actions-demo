FROM python:3.11-alpine

# ----- WORKING DIRECTORY -----
WORKDIR /app

# ----- COPY DEPENDENCIES FIRST -----
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# ----- COPY APPLICATION CODE -----
COPY app.py ./
COPY templates/ templates/

# ----- EXPOSE PORT -----
EXPOSE 5000

# ----- START THE APP -----
CMD ["python", "app.py"]

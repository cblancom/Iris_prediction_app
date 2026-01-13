FROM python:3.13-slim

WORKDIR /home/proyect

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY app .

# CMD ["fastapi", "run", "backend/app/main.py"]
CMD ["fastapi", "run", "main.py"]

FROM python:3.13-slim

WORKDIR /home/proyect

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8501
# CMD ["fastapi", "run", "backend/app/main.py"]
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]

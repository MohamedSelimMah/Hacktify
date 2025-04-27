FROM python:3.11-slim
#set working directory
WORKDIR /app
#copy files
COPY . .
#install dependencies
RUN pip install -r requirements.txt
#exxpose Port
EXPOSE 5000
#run the app
CMD["python","app.py"]
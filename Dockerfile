FROM python:3.10-buster

WORKDIR /service/

RUN pip install --upgrade pip
COPY requirements.txt /service/
RUN pip install -r requirements.txt

EXPOSE 5000

COPY ./service /service/
#COPY environment_variables.py ./
#COPY ./.config /.config

CMD ["uvicorn", "service.main:app", "--host", "0.0.0.0", "--port", "5000"]
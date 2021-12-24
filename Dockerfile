FROM python:3.9.0

WORKDIR /home/
# 데이터들이 바겼을때 의미없는 말을 추가해야할때가 있다고 말함 (강사가)
RUN echo "ssdf1141415152111411af"

RUN git clone https://github.com/dirn0568/shop.git

WORKDIR /home/shop/

RUN pip install -r requirements.txt

# gunicorn을 왜 이후에 다시 추가한지 잘모르겠음 이전에 캐쉬화 되어있어서 추가했다고 강사가 말함 일단 requirements에는 구니콘이 추가되어 있음

RUN pip install gunicorn

# mysqlclient를 설치해줘야 마리아db랑 정상적으로 연결이됨
RUN pip install mysqlclient

EXPOSE 8000

# noinput은 원래 collectstaticd을 할때 우리에게 묻는 창이 나오는데 그거를 스킵해주기 위해서 넣었음

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=pickme.settings && python manage.py migrate --settings=pickme.settings && gunicorn pickme.wsgi --env DJANGO_SETTINGS_MODULE=pickme.settings --bind 0.0.0.0:8000"]

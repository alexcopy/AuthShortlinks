FROM python:3
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir pipenv
RUN pipenv install --system --ignore-pipfile --deploy --clear
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=redcopy
CMD ["python3", "manage.py", "runserver", "0.0.0.0"]
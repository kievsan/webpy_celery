
FROM python:3.10
COPY . /app
WORKDIR /app
#RUN apt update && apt install -y build-essential gcc clang clang-tools cmake python3-dev cppcheck valgrind afl \
#     gcc-multilib && \
#     pip install --no-cache-dir -r /flask_celery/requirements.txt
RUN apt update && pip install --no-cache-dir -r requirements.txt
ENTRYPOINT bash run.sh

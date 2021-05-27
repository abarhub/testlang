FROM rust:1.52-buster
COPY ./langrust/src /usr/src/myapp
COPY ./run.py /usr/src/myapp
#COPY C:/projet/testlang/run.py /usr/src/myapp
WORKDIR /usr/src/myapp
#RUN gcc -o myapp main.c
RUN apt-get update && apt-get install -y time python3
#CMD time gcc -o myapp main.c  && time ./myapp
#CMD date && time gcc -o myapp main.c  && time ./myapp && date
#ENV BUILD_CMD="time, gcc, -o, myapp, main.c, -Wall"
#ENV RUN_CMD="time, ./myapp"
ENV RUST_BACKTRACE=1
CMD /bin/sh -c date && python3 run.py $OPTCMD && date
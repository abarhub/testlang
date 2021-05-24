FROM gcc:11.1
COPY ./src /usr/src/myapp
COPY ./run.py /usr/src/myapp
WORKDIR /usr/src/myapp
#RUN gcc -o myapp main.c
RUN apt-get update && apt-get install -y time python3.9
#CMD time gcc -o myapp main.c  && time ./myapp
#CMD date && time gcc -o myapp main.c  && time ./myapp && date
CMD date && python3 run.py $OPTCMD && date
FROM debian:bullseye-20210927
COPY ./langasm/src /usr/src/myapp
COPY ./run.py /usr/src/myapp
#COPY C:/projet/testlang/run.py /usr/src/myapp
WORKDIR /usr/src/myapp
#RUN gcc -o myapp main.c
RUN apt-get update && apt-get install -y time python3
RUN apt-get update && apt-get install -y nasm gcc
#RUN nasm -f elf64 -o main.o main.asm
#RUN ld -o main main.o

#CMD time gcc -o myapp main.c  && time ./myapp
#CMD date && time gcc -o myapp main.c  && time ./myapp && date
#ENV BUILD_CMD="time, gcc, -o, myapp, main.c, -Wall"
#ENV RUN_CMD="time, ./myapp"
CMD /bin/sh -c date && python3 run.py $OPTCMD && date
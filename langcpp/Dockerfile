FROM gcc:11.1
COPY langcpp/src /usr/src/myapp
COPY ./run.py /usr/src/myapp
WORKDIR /usr/src/myapp
#RUN gcc -o myapp main.c
RUN apt-get update && apt-get install -y time python3
#CMD time gcc -o myapp main.c  && time ./myapp
#RUN apt-get update && apt-get install -y build-essential
#CMD date && time g++ -o myapp main.cpp  && time ./myapp && date
#ENV BUILD_CMD="time, g++, -o, myapp, main.cpp, -Wall"
#ENV RUN_CMD="time, ./myapp"
CMD date && python3 run.py $OPTCMD && date
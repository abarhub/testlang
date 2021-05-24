FROM gcc:11.1
COPY ./src /usr/src/myapp
WORKDIR /usr/src/myapp
#RUN gcc -o myapp main.c
RUN apt-get update && apt-get install -y time
#CMD time gcc -o myapp main.c  && time ./myapp
#RUN apt-get update && apt-get install -y build-essential
CMD date && time g++ -o myapp main.cpp  && time ./myapp && date
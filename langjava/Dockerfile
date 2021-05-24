FROM openjdk:11.0-slim-buster
COPY ./src /usr/src/myapp
COPY ./run.py /usr/src/myapp
WORKDIR /usr/src/myapp
#RUN gcc -o myapp main.c
RUN apt-get update && apt-get install -y time python3
#CMD time gcc -o myapp main.c  && time ./myapp
#RUN apt-get update && apt-get install -y build-essential
#CMD date && g++ -o myapp main.cpp  && ./myapp && echo && date
#RUN javac Main.java
#CMD date +"%T.%N" && time javac Main.java && time java Main && echo && date +"%T.%N"
CMD date +"%T.%N" && python3 run.py && date +"%T.%N"
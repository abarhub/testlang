Build du programme en java avec openJDK

Pour builder, il faut faire ça :
docker build -t sort-test-java-app .

Pour executer, il faut faire :
docker run -it --rm --name sort-test-java-app-run sort-test-java-app

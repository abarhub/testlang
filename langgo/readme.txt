Build du programme en go

Pour builder, il faut faire ça :
docker build -t sort-test-go-app .

Pour executer, il faut faire :
docker run -it --rm --name sort-test-go-app-run sort-test-go-app

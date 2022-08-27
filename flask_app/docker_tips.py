#run metabase on docker
docker run -d -p 3000:3000 --name metabase metabase/metabase
#copy db into docker
docker cp spotify.db metabase:spotify.db
#look inside docker
docker exec -it metabase bash
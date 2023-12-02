This is the database for secret-santa.

# PostgreSQL

To start we need to perform the following commands:
```
docker pull postgres
```

And then we start container:
```
docker run --name postgres-santa -p 5434:5432 -e POSTGRES_PASSWORD=password -e POSTGRES_USER=postgres -e POSTGRES_DB=santa -v ./postgres-schema/init.sql:/docker-entrypoint-initdb.d/init.sql -d postgres
```

Now we can access this database on the localhost:5434.
const santaDB = db.getSiblingDB('santa');

santaDB.createCollection("users");
santaDB.createCollection("groups");
santaDB.createCollection("members");

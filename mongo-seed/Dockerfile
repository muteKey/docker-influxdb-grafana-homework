FROM mongo

COPY init.json /init.json
CMD mongoimport --host mongodb --db test --collection TestCollection --type json --file /init.json --jsonArray --authenticationDatabase admin --username root --password password
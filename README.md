# futurestick
read futures tick from sina api

# Run sample command

~~~
python futuresticks get_quote
~~~

# install

~~~
python setup.py install
fticks
~~~

# Mongo DB

You can install mongo with docker 
1. `docker pull mongo`
1. Run mongo with port mapped `docker run --name mongo -p 27017:27017 -d mongo`
1. (Optional) Install mongo with brew to get mongo shell in your mac, `brew install mongo`, please remember to stop mongo service.

There are some simple mongo shell commands in `MONGO.md`.

for quick start

~~~
mongo # start mongo shell, you can install mongo with brew `brew install mongo`
show dbs
show collections
db.first_product.find().count()
db.first_product.count()
db.first_product.dataSize()
~~~

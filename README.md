## latch-security-challenge
Challenge for a security position in Latch.

📣 ##About the guidelines:
Create a new microservice that can be deployed using docker containers. This microservice should be delivered with all the information needed just to run without further effort. 
 - We need to develop a microservice to handle allowed and used names ([dataset](https://data.buenosaires.gob.ar/dataset/nombres))
    “Nombres-permitidos”
      - Create an endpoint to retrieve the data associated with a given name
      - Create an endpoint to retrieve all the names that start with a given letter and/or a pattern contained in the name.
      - Create an endpoint to show the count of names per gender
    “Dataset_nombres”
      - Create an endpoint to retrieve the top 10 used names, no matter the gender.
 - Create an endpoint to check if a combined name is approved by splitting in parts. E.g: Dionel Maximiliano. Is Dionel an approved name, is Maximiliano approved as well? Please return a data structure to know which is approved and which is not in case of failure/success. 

##🎯 Output:
 - Deliver all the basic files to run the microservice using Docker. 
 - Deliver a one liner to create the image and run the microservice, using docker/docker compose. 
 - Upload the information in your preferred cloud storage, and send the link back :)


##🌱 Get Started!

- Install [Docker](https://www.docker.com/get-started/)
- Download [Postman](https://www.postman.com/) and import the latch-security-challenge-postman-collection located in the root of the project
- Clone github repository with the following command
```
git clone https://github.com/MicaFesta/latch-security-challenge.git
```
- Move through the terminal to the folder where we clone the project, and execute the following commands:
```
docker build -t my-latch-v1 .
```
```
docker run --name my-latch-v1 -p 3030:3030 my-latch-v1
```
- Run the postman endpoints imported from the collection
- Enjoy 🙂


If you do not want to use Postman, the endpoints are the following:
```
GET - /ping
GET - /get-data-name?name=micaela
GET - /get-names-by-condition?letter=a&pattern=ron
GET - /get-count-names-per-gender
GET - /get-top-10-names
GET - /is-an-approved-name?name=julian dionelio carlos juancho
```


# latch-security-challenge
Challenge for a security position in Latch.

About the guidelines:
Create a new microservice that can be deployed using docker containers. This microservice should be delivered with all the information needed just to run without further effort. 
 - We need to develop a microservice to handle allowed and used names ([dataset](https://data.buenosaires.gob.ar/dataset/nombres))
    “Nombres-permitidos”
      - Create an endpoint to retrieve the data associated with a given name
      - Create an endpoint to retrieve all the names that start with a given letter and/or a pattern contained in the name.
      - Create an endpoint to show the count of names per gender
    “Dataset_nombres”
      - Create an endpoint to retrieve the top 10 used names, no matter the gender.
 - Create an endpoint to check if a combined name is approved by splitting in parts. E.g: Dionel Maximiliano. Is Dionel an approved name, is Maximiliano approved as well? Please return a data structure to know which is approved and which is not in case of failure/success. 

Output:
 - Deliver all the basic files to run the microservice using Docker. 
 - Deliver a one liner to create the image and run the microservice, using docker/docker compose. 
 - Upload the information in your preferred cloud storage, and send the link back :)



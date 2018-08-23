FROM node:8.2.1-alpine
RUN mkdir /frontend-code
WORKDIR /frontend-code
COPY frontend/package.json /frontend-code
RUN npm install
ADD frontend/ /frontend-code/

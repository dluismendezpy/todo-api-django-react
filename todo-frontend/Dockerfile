# syntax=docker/dockerfile:1

FROM node:16.14.0-alpine
WORKDIR /react

COPY . .
RUN npm install
RUN npm run build

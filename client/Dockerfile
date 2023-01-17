FROM node:lts-alpine AS build

COPY package.json package.json

RUN npm install

COPY . .

RUN npm run build

FROM nginx:alpine

COPY --from=build dist /usr/share/nginx/html
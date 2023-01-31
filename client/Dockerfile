FROM node:lts-alpine AS build

ARG VITE_API_PROT https
ARG VITE_API_HOST sep-api-dev.marcelstruck.de
ARG VITE_API_PATH /api/v1

COPY package.json package.json

RUN npm install

COPY . .

RUN npm run build

FROM nginx:alpine

COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=build dist /usr/share/nginx/html

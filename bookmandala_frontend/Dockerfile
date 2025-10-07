# Build stage
FROM node:18-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .

# Explicitly copy safe env (non-secrets) so Vite sees it on build
COPY .env .env

RUN npm run build

# Nginx stage (serving built React app)
FROM nginx:stable-alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

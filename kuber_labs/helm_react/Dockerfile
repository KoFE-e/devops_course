FROM nginx:alpine
COPY ./reactApp/build /usr/share/nginx/html
COPY ./reactApp/nginx/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
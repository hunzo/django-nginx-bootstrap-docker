FROM nginx 

RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/conf.d/
COPY ./conf.d/common_location.conf /etc/nginx/conf.d/common_location.conf


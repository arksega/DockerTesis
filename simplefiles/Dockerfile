FROM openresty/openresty:alpine-fat
RUN mkdir -p /usr/share/nginx/html \
    && rm /etc/nginx/conf.d/* \
    && apk add openssl \
    && /usr/local/openresty/luajit/bin/luarocks install nginx-lua-prometheus
ENV LUA_PATH=$LUA_PATH';/usr/local/openresty/luajit/share/lua/5.1/nginx/?.lua'
COPY lukhash.ghosts /usr/share/nginx/html
COPY files.conf metrics.conf /etc/nginx/conf.d/
COPY nginx.conf /usr/local/openresty/nginx/conf/nginx.conf

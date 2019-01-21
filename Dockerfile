FROM alpine:3.8

RUN apk add --update --no-cache py3-yaml py-pillow py3-lxml libstdc++ musl-dev && \
    apk add --update --no-cache \
    --repository http://dl-cdn.alpinelinux.org/alpine/edge/main \
    --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
      geos geos-dev && \
    apk add --update --no-cache --virtual buildstuff \
     build-base python3-dev py3-pip && \
    pip3 install pyproj Shapely && \
    apk del buildstuff geos-dev


ADD mapproxy/ /opt/mapproxy/mapproxy/
ADD docker/entrypoint.py /opt/mapproxy/

VOLUME /opt/mapproxy/config/cache_data

CMD ["/opt/mapproxy/entrypoint.py"]

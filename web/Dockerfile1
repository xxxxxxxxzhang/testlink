FROM bitnami/testlink:1.9.20-debian-10-r12

COPY ./web/img/tl-logo-transparent-12.5.png /opt/bitnami/testlink/gui/themes/default/images/tl-logo-transparent-12.5.png
COPY ./web/img/tl-logo-transparent-25.png /opt/bitnami/testlink/gui/themes/default/images/tl-logo-transparent-25.png
HEALTHCHECK --interval=5m --timeout=3s \
  CMD curl -f http://web || exit 1

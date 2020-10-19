FROM bitnami/testlink:1.9.20-debian-10-r12
RUN DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get install -y openssh-server \
    && apt-get clean \
    && rm -rf \
      /tmp/* \
      /usr/share/doc/* \
      /var/cache/* \
      /var/lib/apt/lists/* \
      /var/tmp/* \
    && mkdir -p /var/run/sshd \
    && echo 'root:AJzUzGER3fc7' | chpasswd \
    && sed -i 's/#*PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config \
    && sed -i 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' /etc/pam.d/sshd 

COPY ./web/img/tl-logo-transparent-12.5.png /opt/bitnami/testlink/gui/themes/default/images/tl-logo-transparent-12.5.png
COPY ./web/img/tl-logo-transparent-25.png /opt/bitnami/testlink/gui/themes/default/images/tl-logo-transparent-25.png
HEALTHCHECK --interval=5m --timeout=3s \
  CMD curl -f http://web || exit 1
EXPOSE 22
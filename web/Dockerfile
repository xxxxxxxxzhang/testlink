FROM zxinxin/testlink:base
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
    && echo 'root:${SSH_PASSWORD}' | chpasswd \
    && sed -i 's/#*PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config \
    && sed -i 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' /etc/pam.d/sshd 
RUN /usr/sbin/sshd 
EXPOSE 22
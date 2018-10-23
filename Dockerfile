FROM centos:7
MAINTAINER Kim min cheol <mcauto@naver.com>
WORKDIR /code
ADD . /code
RUN yum install -y http://centos7.iuscommunity.org/ius-release.rpm 
RUN yum install -y python36u python36u-libs python36u-devel python36u-pip wget gcc
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3.6 get-pip.py
RUN pip3 install pipenv
RUN echo "export LC_ALL=en_US.utf-8" >> ~/.bashrc
RUN echo "export LANG=en_US.utf-8" >> ~/.bashrc
RUN source ~/.bashrc && cd /code && pipenv install https://github.com/squeaky-pl/japronto/archive/master.zip

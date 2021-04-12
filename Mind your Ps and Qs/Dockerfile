FROM ubuntu

RUN apt update
RUN apt install -y wget build-essential libgmp3-dev zlib1g-dev libecm-dev
RUN wget "http://downloads.sourceforge.net/project/msieve/msieve/Msieve%20v1.52/msieve152.tar.gz?r=&ts=1452107977&use_mirror=jaist" -O msieve152.tar.gz
RUN tar xvf msieve152.tar.gz
WORKDIR msieve-1.52/
RUN make all ECM=1
CMD ./msieve
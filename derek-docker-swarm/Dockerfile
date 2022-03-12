FROM ubuntu:20.04
RUN apt-get update
RUN apt-get -y upgrade
RUN apt install -y --fix-missing openjdk-8-jre-headless
RUN apt install -y scala
RUN apt install -y wget
RUN apt install -y screen
RUN wget https://archive.apache.org/dist/spark/spark-3.2.0/spark-3.2.0-bin-hadoop3.2.tgz
RUN tar xvf spark-3.2.0-bin-hadoop3.2.tgz
RUN mv spark-3.2.0-bin-hadoop3.2/ /usr/local/spark 
ENV PATH="${PATH}:$SPARK_HOME/bin"
ENV SPARK_HOME="/usr/local/spark"
ENV SPARK_NO_DAEMONIZE="true"
RUN sleep 15
CMD screen -d -m $SPARK_HOME/sbin/start-master.sh ; $SPARK_HOME/sbin/start-worker.sh -p 4242 spark://sparkmaster:7077
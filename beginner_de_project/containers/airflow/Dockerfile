FROM apache/airflow:2.9.2
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

USER root

COPY quarto.sh /
COPY setup_conn.py /opt/airflow/
RUN chmod +x /quarto.sh && \
    bash /quarto.sh && \
    rm /quarto.sh && \
    chown -R airflow:root /opt/quarto

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    default-jdk

RUN curl https://archive.apache.org/dist/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz -o spark-3.5.1-bin-hadoop3.tgz && \
    chmod 755 spark-3.5.1-bin-hadoop3.tgz && \
    mkdir -p /opt/spark && \
    tar xvzf spark-3.5.1-bin-hadoop3.tgz --directory /opt/spark --strip-components=1

ENV JAVA_HOME='/usr/lib/jvm/java-17-openjdk-amd64'
ENV PATH=$PATH:$JAVA_HOME/bin
ENV SPARK_HOME='/opt/spark'
ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin

USER airflow


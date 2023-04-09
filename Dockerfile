FROM python:3.11

COPY . .
# ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
#RUN pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    #pip3 config set install.trusted-host mirrors.aliyun.com

RUN pip3 install pygame

EXPOSE 8888
CMD ["python3", "server.py"]

# docker build -t ribin-py-2dgame .
# docker run -p 8888:8888 ribin-py-2dgame

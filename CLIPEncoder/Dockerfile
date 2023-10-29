FROM jinaai/jina:3-py38-perf

COPY . /executor_root/

WORKDIR /executor_root

RUN pip install -r requirements.txt

ENTRYPOINT ["jina", "executor", "--uses", "config.yml"]

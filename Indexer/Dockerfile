FROM jinaai/jina:3-py38-perf

COPY . /executor_root/

WORKDIR /executor_root

ENTRYPOINT ["jina", "executor", "--uses", "config.yml"]

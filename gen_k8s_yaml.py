from jina import Deployment, Flow

#dir_name = './k8s_deployment'
ns_name = 'default'

## single excutor
#d = Deployment(port=8080, name='encoder', uses='docker://gabbro:30500/jina/clip-encoder')
#
#d.to_kubernetes_yaml(dir_name, k8s_namespace=ns_name)

## a flow
#f = (
#    Flow(port=8080)
#    .add(
#        name='encoder', 
#        uses='docker://gabbro:30500/jina/clip-encoder',
##        replicas=2,
#     )
#    .add(
#        name='indexer',
#        uses='docker://gabbro:30500/jina/indexer',
##        shards=2,
#    )
#)

### flow with traces and metrics
f = (
    Flow(
        tracing=True,
        traces_exporter_host='http://localhost',
        traces_exporter_port=4317,
        metrics=True,
        metrics_exporter_host='http://localhost',
        metrics_exporter_port=4317,
        port=8080,
    )
    .add(
        name='encoder', 
        uses='docker://gabbro:30500/jina/clip-encoder',
#        replicas=2,
     )
    .add(
        name='indexer',
        uses='docker://gabbro:30500/jina/indexer',
#        shards=2,
    )
)


dir_name = './k8s_flow_otlp'
f.to_kubernetes_yaml(dir_name, k8s_namespace=ns_name)

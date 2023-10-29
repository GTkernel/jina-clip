#CLIP application with Jina AI

The configuration/deployment files and codes are based on the [official documentations](https://docs.jina.ai/cloud-nativeness/kubernetes/) of Jina. 
[Here](https://clip-as-service.jina.ai) has more idea of CLIP.
Please refer to them for up-to-date setup and information.

The goal of this project is to generate AI process and traffic in microservice deployment.

## Introduction

This repo have three sets of files:
- Containerized components of CLIP: `./Indexer` and `./CLIPEncoder`
- K8s config files generator: `gen_k8s_yaml.py`
- User-side functions: `client.py` and `flow_client.py`

The deploying processes are:
1. Build docker images
2. Generate K8s config files
3. Run microservice in K8s
4. Fire client requests for benchmarking

## How to start

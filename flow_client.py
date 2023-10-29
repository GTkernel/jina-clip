from typing import List, Optional
import portforward
from docarray import DocList, BaseDoc
from docarray.typing import NdArray
import sys
from jina.clients import Client


ns_name = 'default'
gateway_pod_name = sys.argv[1]

print(gateway_pod_name)

class MyDoc(BaseDoc):
    text: str
    embedding: Optional[NdArray] = None


class MyDocWithMatches(MyDoc):
    matches: DocList[MyDoc] = []
    scores: List[float] = []


with portforward.forward(ns_name, gateway_pod_name, 8080, 8080):
    client = Client(host='localhost', port=8080)
    client.show_progress = True
    docs = client.post(
        '/index',
        inputs=DocList[MyDoc]([MyDoc(text=f'This is document indexed number {i}') for i in range(100)]),
        return_type=DocList[MyDoc],
        request_size=10
    )

    print(f'------------ Test 1 ---------------')
    print(f'Indexed documents: {len(docs)}')
    docs = client.post(
        '/search',
        inputs=DocList[MyDoc]([MyDoc(text=f'This is document query number {i}') for i in range(10)]),
        return_type=DocList[MyDocWithMatches],
        request_size=10
    )

    for doc in docs:
        print(f'Query {doc.text} has {len(doc.matches)} matches')


    print(f'------------ Test 2 ---------------')
    docs = DocList[MyDoc]([MyDoc(text=f'This is document indexed number {i}') for i in range(100)])
    queried_docs = client.post("/search", inputs=docs, return_type=DocList[MyDocWithMatches])

    matches = queried_docs[0].matches
    print(f"Matched documents: {len(matches)}")

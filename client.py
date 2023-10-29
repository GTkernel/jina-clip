from typing import Optional
import portforward
from docarray import DocList, BaseDoc
from docarray.typing import NdArray

from jina.clients import Client


class MyDoc(BaseDoc):
    text: str
    embedding: Optional[NdArray] = None


with portforward.forward('default', 'encoder-8464fb5487-mncwg', 8080, 8080):
    client = Client(host='localhost', port=8080)
    client.show_progress = True
    docs = client.post(
        '/encode',
        inputs=DocList[MyDoc]([MyDoc(text=f'This is document indexed number {i}') for i in range(100)]),
        return_type=DocList[MyDoc],
        request_size=10
    )

    for doc in docs:
        print(f'{doc.text}: {doc.embedding}')

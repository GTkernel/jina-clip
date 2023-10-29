import torch
from typing import Optional
from transformers import CLIPModel, CLIPTokenizer
from docarray import DocList, BaseDoc
from docarray.typing import NdArray
from jina import Executor, requests


class MyDoc(BaseDoc):
    text: str
    embedding: Optional[NdArray] = None


class Encoder(Executor):
    def __init__(
            self, pretrained_model_name_or_path: str = 'openai/clip-vit-base-patch32', device: str = 'cpu', *args,**kwargs ):
        super().__init__(*args, **kwargs)
        self.device = device
        self.tokenizer = CLIPTokenizer.from_pretrained(pretrained_model_name_or_path)
        self.model = CLIPModel.from_pretrained(pretrained_model_name_or_path)
        self.model.eval().to(device)

    def _tokenize_texts(self, texts):
        x = self.tokenizer(
            texts,
            max_length=77,
            padding='longest',
            truncation=True,
            return_tensors='pt',
        )
        return {k: v.to(self.device) for k, v in x.items()}

    @requests
    def encode(self, docs: DocList[MyDoc], **kwargs) -> DocList[MyDoc]:
        with torch.inference_mode():
            input_tokens = self._tokenize_texts(docs.text)
            docs.embedding = self.model.get_text_features(**input_tokens).cpu().numpy()
        return docs

# Resources

Below are useful resources, further reading, and links referenced throughout this course.

## Course Libraries and Documentation

- [Hugging Face Transformers](https://huggingface.co/docs/transformers/)
- [Hugging Face Hub InferenceClient](https://huggingface.co/docs/huggingface_hub/en/package_reference/inference_client)
- [Hugging Face Inference Providers pricing](https://huggingface.co/docs/inference-providers/pricing)
- [Hugging Face user access tokens](https://huggingface.co/docs/hub/en/security-tokens)
- [tiktoken](https://github.com/openai/tiktoken)
- [Sentence Transformers](https://www.sbert.net/)
- [scikit-learn cosine similarity](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html)
- [Plotly Python](https://plotly.com/python/)

## Further Exploration

### Tokenization

- [OpenAI Tokenizer Tool](https://platform.openai.com/tokenizer) - interactive web tool
- [tiktoken GitHub](https://github.com/openai/tiktoken) - source code and documentation
- [Hugging Face Tokenizers](https://huggingface.co/docs/tokenizers/) - learn about other tokenizers

### Embeddings

- [Sentence Transformers](https://www.sbert.net/) - library used in the embeddings notebook
- [Hugging Face Model Hub](https://huggingface.co/models?pipeline_tag=sentence-similarity) - browse embedding models
- [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings) - embeddings via API

## Hugging Face Models Referenced

| Model | Course use | Licence listed by provider |
| --- | --- | --- |
| <a href="https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2" style="color: #005ea8;">mistralai/Mistral-7B-Instruct-v0.2</a> | Hosted text-generation examples | Apache-2.0 |
| [openai-community/gpt2](https://huggingface.co/openai-community/gpt2) | GPT-2 tokenizer comparison | MIT |
| <a href="https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2" style="color: #005ea8;">sentence-transformers/all-MiniLM-L6-v2</a> | Embedding examples | Apache-2.0 |
| [google-bert/bert-base-uncased](https://huggingface.co/google-bert/bert-base-uncased) | Tokenizer comparison | Apache-2.0 |
| <a href="https://huggingface.co/google-t5/t5-small" style="color: #005ea8;">google-t5/t5-small</a> | Tokenizer comparison | Apache-2.0 |
| [deepseek-ai/DeepSeek-R1-Distill-Llama-8B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-8B) | Tokenizer comparison | MIT listed by provider; model card notes this is a distillation from a Llama-derived base model |
| <a href="https://huggingface.co/distilbert/distilgpt2" style="color: #005ea8;">distilbert/distilgpt2</a> | Local text-generation fallback | Apache-2.0 |

## Python Package Licences

| Package | Course use | Licence |
| --- | --- | --- |
| <a href="https://github.com/openai/tiktoken" style="color: #005ea8;">tiktoken</a> | OpenAI-compatible token counting | MIT |
| [transformers](https://github.com/huggingface/transformers) | Hugging Face tokenizers and local model loading | Apache-2.0 |
| <a href="https://github.com/UKPLab/sentence-transformers" style="color: #005ea8;">sentence-transformers</a> | Embedding model wrapper | Apache-2.0 |
| [huggingface_hub](https://github.com/huggingface/huggingface_hub) | Hosted inference client | Apache-2.0 |
| <a href="https://github.com/theskumar/python-dotenv" style="color: #005ea8;">python-dotenv</a> | Loading local `.env` files | BSD-3-Clause |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | Cosine similarity utilities | BSD-3-Clause |
| <a href="https://github.com/plotly/plotly.py" style="color: #005ea8;">plotly</a> | Interactive plots | MIT |

## Data and Hosted Inference

The practical prompting notebook can send prompt text to Hugging Face Inference Providers when hosted inference is enabled. Do not submit personal data, confidential research data, student or patient data, unpublished intellectual property, or data covered by ethics or data-sharing restrictions to hosted inference services unless you have explicit approval.

Hugging Face pricing, available providers, token scopes, and model availability can change. Check the current Hugging Face documentation before running live inference examples repeatedly or in teaching sessions.

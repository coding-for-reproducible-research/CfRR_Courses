# Introduction to Large Language Models

## Overview

Welcome to Introduction to Large Language Models, a course designed to enhance your understanding of modern Large Language Models (LLMs) and how they work. This course takes a hands-on approach, combining conceptual slides with interactive Jupyter notebooks to guide you from the fundamentals of machine learning and neural networks through to the architecture underlying today's state-of-the-art models. You will finish the session equipped with practical skills for working with LLMs effectively, including how to interpret tokenization, understand semantic embeddings, and craft effective prompts.

## Course Objectives

By the end of this course, participants will be able to:

- Describe what an LLM does at a high level and explain the concept of next-token prediction
- Trace the key developments in machine learning and neural networks that led to modern LLMs
- Explain the core components of a transformer-based LLM: tokenization, embeddings, and attention
- Understand important practical concepts such as statelessness, context windows, and model parameters
- Explore how text is tokenized and why token counts matter for cost and context limits
- Visualize and interpret text embeddings as representations of semantic meaning
- Apply prompt engineering techniques — including few-shot learning and chain-of-thought reasoning — to improve model outputs
- Control LLM output behaviour by tuning temperature and sampling parameters

## Pre-requisite knowledge

Participants should have completed Introduction to Machine Learning, or have equivalent prior experience, before attending this course.

Participants should also have access to a Python environment for the interactive notebook activities.

## Resources

- Instructions on configuring a Python environment with Jupyter Notebooks can be found in the [Introduction to Python setup guide](https://coding-for-reproducible-research.github.io/CfRR_Courses/programme_information/intro_to_python.html).
- Alternatively, the interactive sessions can be in a Google Colab session [here](https://colab.research.google.com/). If this is preferred, participants should ensure they can log into a Colab session, upload and run the example notebook.

````{admonition} Running the interactive LLM notebooks
:class: note

The website build does not execute the interactive LLM notebooks, and the standard CfRR build environment does not need to install the LLM-specific model and API packages.

If you are running these notebooks locally with Poetry, install the optional LLM dependency group first:

```bash
poetry install --with llm
```

If you are running the notebooks in a separate Jupyter or Colab environment, install the notebook-specific packages there instead:

```python
%pip install tiktoken transformers sentence-transformers huggingface-hub python-dotenv
```

The practical prompting notebook can send prompts to Hugging Face Inference Providers when hosted inference is enabled. Set a Hugging Face token as `HF_TOKEN` only in your local environment, and do not submit personal, confidential, unpublished, sensitive, or institutionally restricted data to hosted inference services unless you have explicit approval.
````

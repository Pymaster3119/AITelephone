import os
os.system("pip install diffusers")
os.system("CMAKE_ARGS=\"-DLLAMA_METAL=on\" pip install llama-cpp-python")
from diffusers import DiffusionPipeline
from llama_cpp import Llama

#Initialize the image generation model
pipeline = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipeline.to("mps")
pipeline.enable_attention_slicing()

#Initialize the GPT-like model
llm = Llama(
  model_path=os.path.realpath("open_gpt4_8x7b_v0.2.Q2_K.gguf"),  # Download the model file first
  n_ctx=32768,  # The max sequence length to use - note that longer sequence lengths require much more resources
  n_threads=8,            # The number of CPU threads to use, tailor to your system and the resulting performance
  n_gpu_layers=35         # The number of layers to offload to GPU, if you have GPU acceleration available
)
output = llm(
  "Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n### Instruction:\n{prompt}\n\n### Response:", # Prompt
  max_tokens=512,  # Generate up to 512 tokens
  stop=["</s>"],   # Example stop token - not necessarily correct for this specific model! Please check before using.
  echo=True        # Whether to echo the prompt
)
print(output)

image = pipeline("An image of a squirrel in Picasso style").images[0]
print(type(image))

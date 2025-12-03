import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

aoc ="REMOVED_SECRETBAAwWhRLWLFHwXRSDPoyxhLgiuOUXDbybo" 

model_name = "joeddav/distilbert-base-uncased-go-emotions-student"

Toknizer = AutoTokenizer.from_pretrained(model_name,token = aoc)
model = AutoModelForCausalLM.from_pretrained(model_name,token = aoc)
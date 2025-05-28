import torch
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
print(torch.cuda.is_available())
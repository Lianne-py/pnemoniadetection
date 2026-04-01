#This is a simple script to use torch to detect pneumonia 
from IPython.core.interactiveshell import InteractiveShell
#using seaborn for data handling
import seaborn as sns

#pytorch libraries
import torchvision
from torchvision import transforms,datasets, models
import torch
from torch import optim, cuda
from torch.utils.data import DataLoader, sampler
import torch.nn as nn

import warning 
warnings.filterwarning('ignore', category=FutureWarning)


#data science librarie and functionalities
import numpy as npp
import pandas as pd
import os

#Image manipulations
from PIL import Image

from torchsummary import summary

#timeit ensures that databases queries dont hold connections indefinitely
from timeit import default_timer as timer

#displaying figures
import matplotlib.pyplot as plt
%matplotlib inline
plt.rcParams['font-size'] = 14

InteractiveShell.ast_node_interactivity = 'all'

import os
print(os.listdir("../input"))

import os
import contentful
#from django.db import models

# Create your models here.

client = contentful.Client(
    os.environ.get('CTF_SPACE_ID', 'stx37o49ip9v'),
    os.environ.get('CTF_DELIVERY_KEY', 'yKdAXSipckMzkNjQryWnv4vqVCug9pDR7dH04Egj9Bw')
)

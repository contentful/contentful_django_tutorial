import os
import contentful
#from django.db import models

# Create your models here.

client = contentful.Client(
    os.environ.get('CTF_SPACE_ID', '1t8fkm227wii'),
    os.environ.get('CTF_DELIVERY_KEY', 'db4920ea9db282ed36c6728dcd153575c6aafc35958dccbbf3fb02801b8e8f21')
)

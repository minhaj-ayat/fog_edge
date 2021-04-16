from django.forms import model_to_dict
import sys
print(sys.path)
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FogEdge.settings')
import django
django.setup()
from Proxy.models import Mapper


def get_string():
    user_record = Mapper.objects.using('proxydb').get(imsi="111")
    av = model_to_dict(user_record)
    st = ""
    for key, value in av.items():
        if key != "id":
            st += str(value) + " "
    print(st)
    return st

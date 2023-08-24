def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

import datetime 
from jinja2 import Template

template = Template("""
# Generation started on {{ now()  }}
--- this the rest of my template ---
# Completed generation.
""")
template.globals['now'] = datetime.datetime.now

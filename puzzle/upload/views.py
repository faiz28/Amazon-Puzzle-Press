
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def upload_file(request):
    current_datetime = datetime.datetime.now()  
    html = "<html><body><b>Current Date and Time Value:</b> %s</body></html>" % current_datetime
    # pdf_file = models.FieldFile(html)
    return HttpResponse(html)


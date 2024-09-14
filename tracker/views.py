from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.templatetags.static import static
import os
from tracker.models import EmailTracking


# Create your views here.
def track_email_open(request):
    email = request.GET.get('email')
    token = request.GET.get('token')

    # Create a new record or update the existing one
    EmailTracking.objects.update_or_create(email=email, token=token, defaults={'opened': True})

    # Get the path to the image file using Django's static files handling
    image_path = static('ima.png')
    absolute_image_path = os.path.join(os.path.dirname(__file__), '..', 'static', 'ima.png')

    # Return a 1x1 transparent pixel
    response = HttpResponse(content_type="image/png")
    try:
        with open(absolute_image_path, "rb") as image_file:
            response.write(image_file.read())
    except FileNotFoundError:
        return HttpResponse("Image not found", status=404)

    return response

def get_tracking_data(request):
    email = request.GET.get('email')

    # Query email tracking information
    tracking_records = EmailTracking.objects.filter(email=email).values('email', 'opened', 'timestamp')

    return JsonResponse(list(tracking_records), safe=False)
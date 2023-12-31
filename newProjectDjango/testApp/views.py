from django.shortcuts import render
from django.http import HttpResponseRedirect
import matplotlib.pyplot as plt
import datetime
import numpy as np
from django.urls import reverse
from urllib.parse import urlencode
from django.http import HttpResponse
e = datetime.datetime.now()
time_now=e.strftime("%a, %b %d, %Y")
def index(request):
    return render(
        request,
        "testApp/index.html",
        {
            'q1':time_now,
            'q':"Enter Frequency" 
        }
        )
def outputsine(request):
    frequency = float(request.GET.get('Frequency', 0))
    # Generate sine wave with given frequency
    x = np.linspace(0, 2*np.pi, 1000)
    y = np.sin(2*np.pi*frequency*x)
    # Create plot
    plt.plot(x, y)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Sine Wave ({} Hz)'.format(frequency))
    # Save plot to a buffer
    from io import BytesIO
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    # Return the image as an HttpResponse
    return HttpResponse(buffer.getvalue(), content_type='image/png')

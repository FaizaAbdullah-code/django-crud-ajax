from django.shortcuts import render, redirect
# from appname.forms import DataForm
from .serializers import PointSerializer
from .models import Point

from django.contrib import messages
from django.shortcuts import get_object_or_404
from faker import Faker
from random import randint, choice

# def form_detail(request):
#     # if request.method == 'POST':
#     #     form = DataForm(request.POST)
#     #     if form.is_valid():
#     #         form.save()
#     # form = DataForm()
#     return render(request,'contact.html')

def postPoint(request):
    try:
        point_name = request.POST["description"]
        x = Point.objects.create(
        vehicle_name=point_name)
        return redirect(f"/points")
        

    except Exception as e:
        messages.error(request, str(e))
        employee_list = Point.objects.all().values()
        return render(request,'contact.html', {'employee_list': employee_list})
        # return render(request,'contact.html')

def update_points(request):
    # user = getUser(request.user)

    point_id = request.POST["edit_point_id"]
    point_name = request.POST["edit_point_name"]

    selected_point = get_object_or_404(Point, pk=point_id)
    selected_point.vehicle_name = point_name
    selected_point.save()
    return redirect(f"/points")
        # messages.success(request, "Point has been updated successfully!")

    # except Exception as e:
    #     messages.error(request, str(e))
    #     return render(request,'contact.html')

        

    # if user:
    #     return redirect(f"/{user.organization.abbr}/{user.status.name}/points")
    # else:
    #     return redirect("index")

def delete_point(request):
    point_id = request.POST["point_id_delete"]

    # try:
    selected_point = get_object_or_404(Point, pk=point_id)
    selected_point.delete()
    messages.success(request, "Point has been deleted successfully!")
    # return render(request,'contact.html')
    return redirect(f"/points")

    # except Exception as e:
    #     messages.error(request, str(e))
    #     return render(request,'contact.html')

    # if user:
    #     return redirect(f"/{user.organization.abbr}/{user.status.name}/points")
    # else:
    #     return redirect("index")

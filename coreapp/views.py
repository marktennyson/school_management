from .models import Student
import typing as t
import json 
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

if t.TYPE_CHECKING:
    from django.http import HttpRequest

invalid_id = dict(
    status=0, 
    message="Invalid Id"
)

id_required = dict(
    status=0, 
    message="Id required"
)

@csrf_exempt
def student_view(request:"HttpRequest"):
    if request.method == 'GET':
        if request.GET.get('id', None) is not None:
            try:
                student:"Student" = Student.objects.get(pk=request.GET.get('id'))
            except Student.DoesNotExist:
                return JsonResponse(invalid_id)

            return JsonResponse(student.to_dict())
        else:
            students = Student.objects.all()
            students_data:t.List[t.Dict[str, t.Any]] = [student.to_dict() for student in students]
            return JsonResponse(students_data, safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        student:"Student" = Student.objects.create(**data)
        student.save()
        return JsonResponse(student.to_dict())

    elif request.method == 'PUT':
        if request.GET.get('id', None) is not None:
            print ("id:", request.GET.get('id', None))
            student = Student.objects.filter(id=int(request.GET.get('id')))
            if student is None:
                return JsonResponse(invalid_id)

            data = json.loads(request.body.decode('utf-8'))
            student.update(**data)
            return JsonResponse(student[0].to_dict())
        else:
            return JsonResponse(id_required)

    elif request.method == 'DELETE':
        if request.GET.get('id', None) is not None:
            try:
                student = Student.objects.get(id=request.GET.get('id'))
            except Student.DoesNotExist:
                return JsonResponse(invalid_id)

            student.delete()
            return HttpResponse(status=204)
        
        else:
            return JsonResponse(id_required)
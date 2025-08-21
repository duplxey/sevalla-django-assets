from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from uploads.models import Upload


def index_view(request):
    uploads = Upload.objects.all()

    return render(request, "uploads/index.html", {"uploads": uploads})


@csrf_exempt
@require_POST
def upload_view(request):
    slug = request.POST.get("slug")
    file = request.FILES.get("file")

    if not slug or not file:
        return JsonResponse({"success": False, "error": "Slug and file are required."}, status=400)

    try:
        # Run the validators and upload the file
        upload = Upload(slug=slug, file=file)
        upload.full_clean()
        upload.save()

        return JsonResponse({"success": True, "id": upload.id})
    except ValidationError as e:
        return JsonResponse({"success": False, "error": e.message_dict}, status=400)
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=500)

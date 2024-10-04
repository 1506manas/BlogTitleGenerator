from django.shortcuts import render
from django.http import JsonResponse
from .model import generate_blog_titles
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def generate_titles_view(request):
    if request.method == "POST":
        content = request.POST.get("content")
        if not content:
            return JsonResponse({"error": "Content is required."}, status=400)
        try:
            suggested_titles = generate_blog_titles(content)
            return JsonResponse({"suggested_titles": suggested_titles})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request method. Please use POST."}, status=400)

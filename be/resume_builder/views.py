from django.http import JsonResponse, FileResponse
from pathlib import Path

from resume_builder.utils.main import main


def generate_resume(request):
    try:
        main()

        resume_path = Path("resume.pdf")
        if resume_path.exists():
            return FileResponse(open(resume_path, "rb"), content_type="application/pdf")
        else:
            return JsonResponse({"error": "Failed to generate resume"}, status=500)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

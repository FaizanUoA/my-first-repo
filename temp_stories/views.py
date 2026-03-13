from django.shortcuts import render


def story_page(request):
    raw_temperature = request.GET.get("temp", "").strip()

    context = {
        "temp": raw_temperature,
        "error": None,
        "story": None,
    }
    return render(request, "temp_stories/index.html", context)
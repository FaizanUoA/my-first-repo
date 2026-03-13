from django.shortcuts import render


def story_page(request):
    raw_temperature = request.GET.get("temp", "").strip()
    if raw_temperature:
        story = f"It is {raw_temperature}C today my friends!"

    context = {
        "temp": raw_temperature,
        "error": None,
        "story": story,
    }
    return render(request, "temp_stories/index.html", context)
from django.shortcuts import render


def story_page(request):
    raw_temperature = request.GET.get("temp", "").strip()

    error = None
    story = None
    temp = raw_temperature
    if raw_temperature:
        try:
            temp_value = float(raw_temperature)
            if not temp_value.is_integer():
                error = "Please enter a whole number."
            else:
                story = f"It is {int(temp_value)}C today my friends!"
        except ValueError:
            error = "Please enter a valid number."

    context = {
        "temp": temp,
        "error": error,
        "story": story,
    }
    return render(request, "temp_stories/index.html", context)
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Note
from datetime import datetime

def create_note(request):
    if request.method == "POST":
        date = request.POST.get("datepicker")
        title = request.POST.get("title")
        notes = request.POST.get("notes")

        # Validate and format the date
        try:
            formatted_date = datetime.strptime(date, "%Y-%m-%d").date() if date else None
        except ValueError:
            messages.error(request, "Invalid date format. Please use YYYY-MM-DD.")
            return redirect("create-data")

        if not title or not notes:
            messages.error(request, "Title and Notes fields cannot be empty.")
            return redirect("create-data")

        Note.objects.create(date=formatted_date, title=title, notes=notes)
        messages.success(request, "Note added successfully!")
        return redirect("create-data")

    return render(request, "index.html")

def show_notes(request):
    all_notes = Note.objects.all()
    return render(request, "show_notes.html", {"notes": all_notes})

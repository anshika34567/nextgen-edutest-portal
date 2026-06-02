def download_result(request, score):
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="result.pdf"'

    p = canvas.Canvas(response)

    p.setFont("Helvetica", 16)
    p.drawString(200, 750, "EduTest Portal")

    p.setFont("Helvetica", 12)
    p.drawString(200, 700, f"Your Score: {score}")

    p.drawString(200, 670, "Congratulations for completing the exam!")

    p.save()

    return response
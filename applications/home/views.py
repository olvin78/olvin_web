from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from applications.portfolio.models import Project
from applications.technologies.models import Technology


def index_view(request):
    projects = Project.objects.all()
    technologies = Technology.objects.all()
    return render(request, 'home/index.html', {
        'projects': projects,
        'technologies': technologies,
    })


@csrf_exempt
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message')

        full_message = f"""
Nombre: {name}
Email: {email}
Teléfono: {phone}
Mensaje:
{message}
"""
        try:
            send_mail(
                subject=f'📩 Nuevo mensaje de {name} web olvin',
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            return render(request, 'home/index.html', {
                'success': True,
                'projects': Project.objects.all(),
                'technologies': Technology.objects.all(),
            })
        except Exception as e:
            return render(request, 'home/index.html', {
                'error': f'❌ Hubo un error al enviar tu mensaje: {e}',
                'projects': Project.objects.all(),
                'technologies': Technology.objects.all(),
            })

    return render(request, 'home/index.html', {
        'projects': Project.objects.all(),
        'technologies': Technology.objects.all(),
    })

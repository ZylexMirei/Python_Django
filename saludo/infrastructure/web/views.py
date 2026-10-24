import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from saludo.application.ports.saludar_use_case import SaludarUseCase
from saludo.application.services.saludar_service import SaludarService
from saludo.domain.persona import Persona


@csrf_exempt
@require_POST
def saludar_view(request):
    try:
        datos = json.loads(request.body)
    except (ValueError, UnicodeDecodeError):
        return JsonResponse({"error": "JSON inválido"}, status=400)

    if not isinstance(datos, dict):
        return JsonResponse({"error": "Debes enviar un objeto JSON"}, status=400)

    nombre = datos.get("nombre")
    if not isinstance(nombre, str):
        return JsonResponse({"error": "Debes enviar un nombre válido"}, status=400)

    nombre = nombre.strip()
    if not nombre:
        return JsonResponse({"error": "Debes enviar un nombre válido"}, status=400)

    persona = Persona(nombre=nombre)
    servicio: SaludarUseCase = SaludarService()
    mensaje = servicio.ejecutar(persona)

    return JsonResponse({"mensaje": mensaje})

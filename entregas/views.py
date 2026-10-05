from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

from entregas.reglas import elegir_medio


def hola(request):
    return HttpResponse("Hola. Plataforma de entregas (aún sin pedidos).")


def cotizar(request):
    try:
        km = float(request.GET.get("km", 0))
        kg = float(request.GET.get("kg", 0))
    except (ValueError, TypeError):
        return JsonResponse({"error": "Valores inválidos para km o kg"}, status=400)

    medio = elegir_medio(km, kg)
    if isinstance(medio, JsonResponse):
        return medio
    return JsonResponse({"mensaje": f"Cotización de entrega (aún sin pedidos). Medio de transporte: {medio}."})
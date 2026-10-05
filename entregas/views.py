from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

from entregas.reglas import elegir_medio


def hola(request):
    return HttpResponse("Hola. Plataforma de entregas (aún sin pedidos).")

def estado(request):
    return JsonResponse({
        "status": "ok", 
        "Servicio": "Plataforma de entregas", 
        "versión": "1.0",
        "Propietario": "Ricardo Hernández",
        "mensaje": "Plataforma de entregas (aún sin pedidos)."})

def cotizar(request):
    try:
        km = float(request.GET.get("km", 0))
        kg = float(request.GET.get("kg", 0))
    except (ValueError, TypeError):
        return JsonResponse({"error": "Valores inválidos para km o kg"}, status=400)

    medio = elegir_medio(km, kg)
    return JsonResponse({"mensaje": f"Cotización de entrega (aún sin pedidos). Medio de transporte: {medio}."})
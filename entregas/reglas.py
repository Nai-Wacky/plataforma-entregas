"Definición de reglas para la plataforma de entregas"

from django.http import JsonResponse


def elegir_medio(km, kg):

    if km <= 5 and kg <= 2:
        return JsonResponse({"km": km, "kg": kg, "medio": "Bicicleta", "Motivo": "Distancia y peso menores a 5 km y 2 kg"})
    elif km <= 20 and kg <= 5:
        return JsonResponse({"km": km, "kg": kg, "medio": "Moto", "Motivo": "Distancia y peso moderados"})
    else:
        return JsonResponse({"km": km, "kg": kg, "medio": "Camión", "Motivo": "Distancia o peso elevados"})


    
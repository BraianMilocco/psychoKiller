from django.http import JsonResponse


def locura(request):
    hi = {"Balada para un Loco": "Ya se que estoy piantao, piantao, piantao...  No ves que va la luna rodando por Callao; que un corso de astronautas y niños, con un vals,  me baila alrededor... Baila! Veni! Vola!"}

    return JsonResponse(hi)

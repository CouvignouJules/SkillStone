from django.contrib import admin
from .models import Cardtype, CardtypeAdmin, Effect, EffectAdmin, Card, CardAdmin, Player, PlayerAdmin, Deck, DeckAdmin

# Register your models here.

admin.site.register(Cardtype, CardtypeAdmin)
admin.site.register(Effect, EffectAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Deck, DeckAdmin)

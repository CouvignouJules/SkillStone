from django.contrib import admin
from .models import CardType, CardTypeAdmin, Effect, EffectAdmin, Card, CardAdmin, Player, PlayerAdmin, Deck, DeckAdmin

# Register your models here.

admin.site.register(CardType, CardTypeAdmin)
admin.site.register(Effect, EffectAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Deck, DeckAdmin)

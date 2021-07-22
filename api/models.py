from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.conf import settings

class Deal(models.Model):
    title = models.CharField(
        max_length=100,
        default="Deal"
    )

    investments = (
        ("BTCUSDC", "BTCUSDC"),
        ("ETHUSDC", "ETHUSDC"),
        ("BTCETH", "BTCETH"),
        ("LINK", "CHAINLINK"),
        ("BTC", "BITCOIN"),
        ("ETH", "ETHEREUM"),
        ("AAVE", "AAVE"),
        ("ADA", "CARDANO"),
        ("DOT", "POLKADOT"),
        ("LTC", "LITECOIN"),
        ("USDT", "TETHER"),
        ("BNB", "BINANCE COIN"),
        ("FIL", "FILECOIN"),
        ("DOGE", "DOGECOIN"),
        ("TRX", "TRON"),
        ("USDC", "USD COIN")
    )

    opIn = "BUY"
    opOut = "SEL"
    operations_choices = (
        ('Buy', opIn),
        ('Sell', opOut),
    )

    entryP = "PRC"
    entryA = "AUT"
    entry_price_choices = (
        ("Price", entryP),
        ("Auto", entryA),
    )

    strategyF = "STF"
    strategyT = "STT"
    strategy_choices = (
        ("None", strategyF),
        ("Strategy", strategyT),
    )

    visibilityT = "VST"
    visibilityF = "VSF"
    visibility_choices = (
        ("Public", visibilityT),
        ("Private", visibilityF),
    )

    investment = models.CharField(
        max_length=10,
        choices=investments,
        default="BTC",
    )
    indicators = models.IntegerField(default=1)
    description = models.TextField()
    operation = models.CharField(
        max_length= 10,
        choices=operations_choices,
        default=opIn,
    )
    entry_price = models.CharField(
        max_length=10,
        choices=entry_price_choices,
        default=entryA,
    )
    stop_gain = models.FloatField()
    stop_loss = models.FloatField()
    strategy = models.CharField(
        max_length=10,
        choices=strategy_choices,
        default=strategyF,
    )
    visibility = models.CharField(
        max_length=10,
        choices=visibility_choices,
        default=visibilityT,
    )
    contribuitors = models.IntegerField(default=1)
    amount = models.FloatField()
    creation = models.DateTimeField(auto_now_add=True)
    execution = models.DateTimeField(default=now, blank=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class UserDetails():
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.FloatField()
    earnings = models.FloatField()

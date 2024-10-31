import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def plastik_el_isi(ctx):
    fikirler = [
        "Plastik şişelerden kalemlik yapabilirsin.",
        "Plastik kapakları kullanarak mozaik tablo yapabilirsin.",
        "Eski plastik kutulardan küçük saksılar yapabilirsin.",
        "Plastik kaşıkları boyayıp dekoratif çerçeve tasarlayabilirsin."
    ]
    await ctx.send(f"Evde yapabileceğin plastik el işleri:\n- " + "\n- ".join(fikirler))

@bot.command()
async def atık_sınıfla(ctx, *, item: str):
    geri_donusum = {
        "plastik şişe": "Geri dönüştürülebilir",
        "kağıt": "Geri dönüştürülebilir",
        "cam şişe": "Geri dönüştürülebilir",
        "metal kutu": "Geri dönüştürülebilir",
        "pil": "Tehlikeli atık olarak ayrılmalı",
        "ampul": "Özel atık merkezine götürülmeli"
    }
    cevap = geri_donusum.get(item.lower(), "Bu eşya hakkında bilgi yok.")
    await ctx.send(f"{item.capitalize()} -> {cevap}")

@bot.command()
async def ayrışma_süresi(ctx, *, item: str):
    ayrışma_süreleri = {
        "plastik şişe": "450 yıl",
        "kağıt": "2-6 hafta",
        "cam şişe": "1 milyon yıl",
        "metal kutu": "50 yıl",
        "pil": "100 yıl"
    }
    süre = ayrışma_süreleri.get(item.lower(), "Bu eşya hakkında bilgi yok.")
    await ctx.send(f"{item.capitalize()} doğada {süre} sürede ayrışır.")

bot.run("token")

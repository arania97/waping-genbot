import discord,json,os,random
from discord.ext import commands

with open("setting.json") as file:
    info = json.load(file)
    token = info["token"]
    delete = info["autodel"]
    prefix = info["prefix"]

bot = commands.Bot(command_prefix=prefix)
channel = '00000000000000000'

def embed(embedtype, embedtitle, description):
    if (embedtype == "error"):
        return discord.Embed(color=0x5865f2, title=embedtitle, description=description)
    if (embedtype == "success"):
        return discord.Embed(color=0x5865f2, title=embedtitle, description=description)
    if (embedtype == "warning"):
        return discord.Embed(color=0x5865f2, title=embedtitle, description=description)

@bot.event
async def on_ready():
    print("[+] μνμ΅ πππ μ μ μμ μλ£ νμμ΅λλ€.")
    game = discord.Game('πππ κ΄λ¦¬')
    await bot.change_presence(status=discord.Status.dnd, activity=game)

@bot.command()
async def μ¬κ³ (message):
    if not message.channel.id == int(channel):
        return
    stockmenu = discord.Embed(title="π μ νλͺ©λ‘",description="",color=0x5865f2)
    for filename in os.listdir("μ¬κ³ "):
        with open("μ¬κ³ \\"+filename) as f: 
            ammount = len(f.read().splitlines()) 
            name = (filename[0].upper() + filename[1:].lower()).replace(".cfg","")
            stockmenu.description += f"μ ν : `{name}` \nμ¬κ³  : `{ammount}κ°`\n-------------------\n"
    await message.send(embed=stockmenu)

@bot.command()
async def μ°(message,name=None):
    if not message.channel.id == int(channel):
        return
        await message.channel.send(embed=embed("error", "β μμ± μ€ν¨" , "κ³μ μ μλ ₯ν΄μ£ΌμΈμ."))
    else:
        name = name.lower()+".cfg"
        if name not in os.listdir("μ¬κ³ "):
            await message.channel.send(embed=embed("error", "β μμ± μ€ν¨" , "ν΄λΉ κ³μ μ μμ΅λλ€."))
        else:
            with open("μ¬κ³ \\"+name) as file:
                lines = file.read().splitlines() 
            if len(lines) == 0: 
                await message.channel.send(embed=embed("error", "β μμ± μ€ν¨" , "ν΄λΉ κ³μ μ μ¬κ³ κ° λΆμ‘±ν©λλ€."))
            else:
                with open("μ¬κ³ \\"+name) as file:
                    account = random.choice(lines)
                try: 
                    await message.author.send(embed=embed("success", "π μμ± μ±κ³΅" , "```" + str(account) + "```\n\nν΄λΉ λ©μμ§λ 30μ΄ λ€μ μ κ±°λ©λλ€."),delete_after=delete)
                except: 
                    await message.channel.send(embed=embed("error", "β μμ± μ€ν¨" , "DM μ μ‘μ νμ©ν΄μ£ΌμΈμ."))
                else: 
                    await message.channel.send(embed=embed("success", "π μμ± μ±κ³΅" , "DMμ νμΈν΄μ£ΌμΈμ."))
                    with open("μ¬κ³ \\"+name,"w") as file:
                        file.write("")
                    with open("μ¬κ³ \\"+name,"a") as file:
                        for line in lines:
                            if line != account: 
                                file.write(line+"\n") 

bot.run(token)
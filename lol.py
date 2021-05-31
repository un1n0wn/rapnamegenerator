import random
import sys
lol = ["MC ","Cold ","Gangsta ","Killah","dollar","Ya ","Menace","Street ","Boom","DJ ","Pusha ","Gauge","Kid ","XXX","DJ ","Master ","Drugz","DJ ","Hott ","Blade","DJ ","Smoke ","Boom","Master ","Hustle","Pusha ","Quik","Mobb ","Blade","Eazy ","Gauge","MC ","Sharp ","Blow","Cold ","Boy","Notorious ","Blaster","MC ","Mac ","Blade","Mobb ","MC","DJ ","Mobb ","Mack","Pimp ","Blow","DJ ","Gang ","Pistols","Chief ","Pistols","Cold ","Shot","Junior ","Needlz","The ","Notorious ","Havoc ","Boy","Ace ","Problem","The ","Notorious ","Cool ","Venom","MC ","Kid ","Gunz","Mobb ","Dogg","MC ","Knight ","Needlz","The ","Notorious ","Mobb ","Blow","Ghetto ","Needlz","DJ ","Gang ","Boy","DJ ","Pusha ","G","Lil' ","Pistols","The ","Notorious ","Street ","Bang","MC ","Mobb ","Bang","DJ ","Schoolboy ","Boy","The ","Notorious ","Spice ","Pistols"]
try:
    olo = sys.argv[1]
except:
    print("Use the tool as E.G - python3 lol.py NAME <-- The NAME can be your name or nickname")
    quit()
l = random.randint(0,10)
if l > 4:
    name = random.choice(lol), random.choice(lol), olo
else:
    name = random.choice(lol), olo
string2=" ".join(map(str,name))
print (string2)



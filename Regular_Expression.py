import re

pattern = r"[A-Z]oogle"
text = '''The company has since rapidly grown to offer a multitude of products and services beyond Google Search, many of which hold dominant market positions. Doogle These products address a wide range of use cases, including email (Gmail), navigation (Waze & Maps), cloud computing (Cloud), web browsing (Chrome), video sharing (YouTube), productivity (Workspace), operating systems (Android), cloud storage (Drive), language translation (Translate), photo storage (Photos), video calling (Meet), smart home (Nest), smartphones (Pixel), wearable technology (Pixel Watch & Fitbit), music streaming (YouTube Music), video on demand (YouTube TV)'''

matches = re.finditer(pattern, text)
# print(match)
for match in matches:
    # print(match)
    print(match.span())
    # print(type(match.span()))
    print(text[match.span()[0]:match.span()[1]])
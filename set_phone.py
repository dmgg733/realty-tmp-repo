import os, re, sys

raw = os.environ.get("PHONE", "").strip()
d = re.sub(r"\D", "", raw)
if len(d) == 10:
    d = "7" + d
elif len(d) == 11 and d[0] == "8":
    d = "7" + d[1:]
if not re.fullmatch(r"7\d{10}", d):
    sys.exit(f"Неверный номер: {raw!r}. Пример: +79991234567")
phone = "+" + d

with open("feed.xml", encoding="utf-8", newline="") as f:
    text = f.read()
new, n = re.subn(r"(<phone>)[^<]*(</phone>)", lambda m: m.group(1) + phone + m.group(2), text)
if n == 0:
    sys.exit("В feed.xml не найдено ни одного <phone>")
with open("feed.xml", "w", encoding="utf-8", newline="") as f:
    f.write(new)
print(f"OK: {phone}, заменено {n}")

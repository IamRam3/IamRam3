from datetime import datetime

today = datetime.utcnow()
start = datetime(today.year, 1, 1)
end = datetime(today.year + 1, 1, 1)
progress = (today - start).total_seconds() / (end - start).total_seconds()
percent = round(progress * 100, 2)

bar_length = 30
filled_length = int(bar_length * progress)
bar = "█" * filled_length + "▁" * (bar_length - filled_length)

output = f"⏳ Year progress {{ {bar} }} {percent} % I still have time to learn more Techs this year"
print(output)

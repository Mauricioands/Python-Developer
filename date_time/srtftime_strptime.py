from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2025-03-28 08:57"
mascara_ptbr = "%d/%m/%Y %H:%M"

print(data_hora_atual.strftime(mascara_ptbr))


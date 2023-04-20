import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

faturamento = 10000
gasto = 200

faturamento_texto = f'{faturamento:,.2f}'.replace(',','_').replace('.',',').replace('_','.')
print(faturamento_texto)

lucro = 200 if faturamento > 1000 else 50
faturamento2 = locale.currency(faturamento)

print(lucro)
print(faturamento2)

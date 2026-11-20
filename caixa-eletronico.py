sair = False
saldo_atual = 0
numero_operacao = 0

while numero_operacao < 4:
 print("====== CAIXA ELETRÔNICO ======")
 print("1 - Consultar saldo")
 print("2 - Depositar")
 print("3 - Sacar")
 print("4 - Sair")

 numero_operacao = int(input())

 if numero_operacao == 1:
  print("Seu saldo atual é de: ", saldo_atual)

 elif numero_operacao == 2:
  print("Que valor deseja depositar?")
  valor_deposito = int(input())
  saldo_atual += valor_deposito

 elif numero_operacao == 3:
  print("Que valor deseja sacar?")
  valor_saque = int(input())
  saldo_atual -= valor_saque

 else:
  print("Encerrando...")
  



 

     




 



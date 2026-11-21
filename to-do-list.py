tarefas = []
number = 0

while number < 4:
 
 print("===== TO-DO LIST =====")
 print("1 - Adicionar tarefa")
 print("2 - Listar tarefas")
 print("3 - Remover tarefa")
 print("4 - Sair")

 print("Oque deseja fazer?")
 number = int(input())

 if number == 1:
  print("Qual sua tarefa?")
  tarefa = input()
  tarefas.append(tarefa)

 elif number == 2:
  for i in tarefas:
   print(i)





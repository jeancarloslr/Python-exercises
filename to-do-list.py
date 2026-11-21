import os

tarefas = []
number = 0

def clean_terminal():
  os.system("cls")

def mostrar_tarefas():
 for tarefa in tarefas:
  print(tarefa)

while number < 4:
 
 print("===== TO-DO LIST =====")
 print("1 - Adicionar tarefa")
 print("2 - Listar tarefas")
 print("3 - Remover tarefa")
 print("4 - Sair")

 print("Oque deseja fazer?")
 number = int(input())
 clean_terminal()

 if number == 1:
  print("Qual sua tarefa?")
  tarefa = input()
  tarefas.append(tarefa)
  clean_terminal()

 elif number == 2:
  mostrar_tarefas()

 elif number == 3:
  if len(tarefas) == 0:
   print("Não há tarefas.")

  else:
   
   print("Qual tarefa deseja remover")
   i = 1

   for tarefa in tarefas:
     print(i, tarefa)
     i = i + 1
    
   remover_tarefa = int(input())
   remover_tarefa = remover_tarefa - 1
                     
   tarefas.pop(remover_tarefa)

 elif number >= 4:
  print("Encerrando...")
  break

  
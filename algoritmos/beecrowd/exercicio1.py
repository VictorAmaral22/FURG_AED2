# -*- coding: utf-8 -*-
import sys

def main():
  #Quando rodar localmente descomente as linhas abaixo para ler e escrevar em arquivos locais
#   fin = open("arquivo_entrada_local.txt", "r")
#   fout = open("arquivo_saida_local.txt", "w")
  
  #Quando submeter descomente as linhas abaixo para ler e escrevar da entrada e saída padrão
  fin = sys.stdin
  fout = sys.stdout

  linha = fin.readline()

  fout.write(linha)

  fin.close()

  fout.close()

# main function call
main()
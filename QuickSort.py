#!/usr/bin/python
#coding: utf-8

# Filename  : QuickSort.py
# Autor     : Joshua Ayala
# Website   : https://github.com/JoshuaAyala/QuickSort-Python
# pep8: 100%

def QuickSort(lista):
	if(len(lista) > 1):
		pivot = lista[0]
		listaIz = []
		listaDe = []
		listaPi = []
		for i in range(0, len(lista)):
			if(lista[i] < pivot):
				listaIz.append(lista[i])
			elif(lista[i] == pivot):
				listaPi.append(lista[i])
			else:
				listaDe.append(lista[i])
		return QuickSort(listaIz) + listaPi + QuickSort(listaDe)
	else:
		return lista


c = int(input("¿Cuántos datos deseas ingresar?\n >: "))
lista = []
for i in range(0, c):
	lista.append(int(input("Introduce un dato >: ")))
print("\n	+- Lista dada: ", lista, "\n	+- Lista ordenada: ", QuickSort(lista))

# Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável, nós não
# colocamos o tipo de dado dela. Este tipo é inferior ao atribuírmos o valor à mesma

numero = 42 # Exemplo de variável global
print(numero)
print(type(numero))

numero = 'Geek' # Reatribuição
print(numero)
print(type(numero))

nao_existo = 'Oi'
print(nao_existo)

numero = 42

if numero > 10:
  novo = numero + 10 # variavel novo esta declarada localmente dentro do bloco do if. Portanto, é local
  print(novo)

print(novo)

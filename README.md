## Digital Innovation One

## Bootcamp: Cognizant Data Engineer

## Módulo: Desafios Matemáticos em Python

Nesse desafio de codificação você irá praticar através do desenvolvimento de algoritmos os conceitos de pensamento computacional apresentados nas aulas e exercícios anteriores.

## 1 / 3 - Rodízio de cavalos e carruagens

** Intermediário

** Princípios Básicos

------

#### Desafio

O rodízio de veículos de Bravoos é uma restrição à circulação de veículos na cidade. Com o propósito de melhorar as condições ambientais reduzindo a carga de poluentes na atmosfera,incluindo na região de Westeros, se consolidou como um instrumento para reduzir congestionamentos nas principais vias da cidade, nos horários de maior movimento. Nas ruas delimitadoras não é permitido o tráfego de cavalos e carruagens que estejam dentro da restrição. Há uma escala que determina em quais dias da semana quais veículos não podem circular. Essa escala é regida pelo último dígito da placa do animal, sendo:

- Segunda-feira, digito final da placa 1 e 2
- Terça-feira, digito final da placa 3 e 4
- Quarta-feira, digito final da placa 5 e 6
- Quinta-feira, digito final da placa 7 e 8
- Sexta-feira, digito final da placa 9 e 0

Os motoristas que são flagrados violando a restrição de circulação são autuados com multa de 4 galinhas e condenados a passar 1 semana na Muralha.

#### Entrada

A primeira linha de entrada representa a quantidade de testes **N** (0 <= **N** < 1000) que deverão ser considerados. As demais entradas são cadeia de caracteres com tamanho máximo **S** (1 <= **S** <= 100) que representam cada placa que deverá ser analisada, de tal forma que, cada placa fique em uma única linha de entrada. O formato esperado para uma placa veicular válida em Bravoos é "**AAA-9999**", tal que A é um caracter válido em [A-Z], e 9 um dígito numérico válido em [0-9].

#### Saída

O conjunto de valores válidos como saída são: SEGUNDA, TERCA, QUARTA, QUINTA e SEXTA, de acordo com a tabela de restrições predefinida, e FALHA caso a placa não apresente o padrão definido.

 

| Exemplos de Entrada                                          | Exemplos de Saída                           |
| ------------------------------------------------------------ | ------------------------------------------- |
| 3<br />ABC-1234<br />XYZ-1010<br />AAA3333                   | TERCA <br />FRIDAY <br />FALHA              |
| 4 <br />abc-1234 <br />a-1010 <br />ABCD-1234 <br />AIQ-2001 | FALHA <br />FALHA <br />FALHA <br />SEGUNDA |

## 2 / 3 - Preenchimento de Vetor III

** Intermediário		** Princípios Básicos

------

#### Desafio

Leia um valor **X**. Coloque este valor na primeira posição de um vetor **N**[100]. Em cada posição subsequente de N (1 até 99), coloque a metade do valor armazenado na posição anterior, conforme o exemplo abaixo. Imprima o vetor **N**.

#### Entrada

A entrada contem um valor de dupla precisão com 4 casas decimais.

#### Saída

Para cada posição do vetor **N**, escreva "N[*i*] = Y", onde *i* é a posição do vetor e **Y** é o valor armazenado naquela posição. Cada valor do vetor deve ser apresentado com 4 casas decimais.

| Exemplo de Entrada | Exemplo de Saída                                             |
| ------------------ | ------------------------------------------------------------ |
| 200.0000           | N[0] = 200.0000 <br />N[1] = 100.0000 <br />N[2] = 50.0000 <br />N[3] = 25.0000 <br />N[4] = 12.5000 ... |

## 3 / 3 - A Mudança

** Intermediário		** Princípios Básicos

------

#### Desafio

![img](https://www.urionlinejudge.com.br/gallery/images/problems/UOJ_2686.png)

Hermione está criando um novo Vira Tempo especialmente para programadores. É impressionante as vantagens que ele oferece e o conforto pra codar que ele tem. O artefato ainda está em desenvolvimento e ele prometeu consertar os bugs e colocar uns apetrechos melhores e, em troca, pediu um sistema simples para o modo Standy Bay. O problema é que o artefato por si só sempre tem o ângulo de inclinação do Sol/Lua(de 0 a 360). Valendo um Vira Tempo, caso deseja aceitar: dada em grau da inclinação do Sol/Lua, informe em qual período do dia ele se encontra.

#### Entrada

A entrada contém um número inteiro **M** (0 ≤ **M** ≤ 360) representando o grau do Sol/Lua. Como a posição muda constantemente seu programa receberá diversos casos a cada segundo(EOF).

#### Saída

Imprima uma saudação referente ao período do dia que ele se encontra: "Boa Tarde!!", "Boa Noite!!", "Bom Dia!!" e "De Madrugada!!".

| Exemplo de Entrada | Exemplo de Saída                                      |
| ------------------ | ----------------------------------------------------- |
| 0 45 360 90 180    | Bom Dia!! Bom Dia!! Bom Dia!! Boa Tarde!! Boa Noite!! |

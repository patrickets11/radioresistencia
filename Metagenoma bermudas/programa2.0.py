import time
palavras=[]
x=[]
i=0
k=[]
w=[]
g=[]
e=['>']
novoparametro=0
fasta='.fasta'
print('Todos os arquivos devem estar no mesmo diretório. Basta digitar o nome do arquivo que o formato ".fasta" será incluído automaticamente.\n')
#comando1=input('Digite o nome do arquivo de parâmetro: ')
comando1= 'UvrC_Lista_Identificação_Ber'
#comando2=input('Digite o nome do arquivo de busca: ')
comando02= input('numero')
comando2= 'parte' + comando02
#comando3=input('Digite o nome do arquivo a ser criado: ')
comando3= 'UvrC'+ comando02
paragrafo_fim=[]
ref_arquivo1 = open(comando2+fasta,"r")
linha = ref_arquivo1.read()
arquivofim = open(comando3+fasta,'a')
antes=time.time()
with open(comando1+fasta) as f:
	for line in f:
		x.append(line.split())
		k.append(x[i][1])
		i+=1
	del x

palavras.append(linha.split('>'))
del palavras[0][0]
ref_arquivo1.close()
while novoparametro < len(palavras[0]):
        g=palavras[0][novoparametro]
        w=g.split()
        if w[0] in k:
                arquivofim.write(e[0]+g)
        #print(novoparametro)
        novoparametro+=1
depois=time.time()
print('O## processamento terminou, ele demorou: ', depois-antes, 'segundos para rodar')
input("Pressione <enter> encerrar")
arquivofim.close()

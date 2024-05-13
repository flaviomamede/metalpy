from metalpy.perfis import PerfilI
from metalpy.material import Aco

#Definindo o aço do tipo MR250 com as propriedades em kN/cm²
MR250 = Aco(20000, 0.3, 25, 30, 0.6)

#Dados do perfil CVS 450 X 16 em cm

# Altura total
d = 45
# Largura da mesa superior e inferior
bfs=bfi= 30
# Espessura da alma
tw = 1.25
# Espessura da alma superior e inferior
tfs=tfi= 1.6
# Criando o perfil CVS 450 X 116 com métodos de determinação da
# capacidade resistente da norma NBR8800:2008
CVS450X116 = PerfilI(d, bfs, bfi, tw, tfs, tfi, mat=MR250, norma='NBR8800')

#Obtendo as respostas com Metalpy

#Propriedades do perfil
A = CVS450X116.A #área do perfil
Wx = CVS450X116.Wx #módulo elástico em relação ao eixo X
rx = CVS450X116.rx #raio de giração em relação ao eixo X
Zx = CVS450X116.Zx #módulo plástico em relação ao eixo X
Iy = CVS450X116.Iy #momento de inércia em relação ao eixo Y
Wy = CVS450X116.Wy #módulo elástico em relação ao eixo Y
ry = CVS450X116.ry #módulo plástico em relação ao eixo Y
J = CVS450X116.J #inércia a torção
Cw = CVS450X116.Cw #constante de empenamento
esb_mesa = CVS450X116.esb_mesa #esbeltez da mesa
esb_alma = CVS450X116.esb_alma #esbeltez da alma

# Verificação à flexo-compressão

#Solicitações
Nsd = -1.4 * 800
Msdx = 1.4 * 50 * 1.039 * 100 # Considerando os efeitos de 2ª ordem
Msdy = 0

# Obtendo os valores da resistência do perfil

#Resistência a compressão
Nrd, dados_Ncrd = CVS450X116.Ncrd(klx=600, kly=0.1, klz=0.1, data=True)
ier = dados_Ncrd.ier #Indice de esbeltez reduzido

#Momento resistente em relação ao eixo X
Mrd, dados_Mrd = CVS450X116.Mrdx(Lb=0, Cb=1, data=True)

#Verificação a flexo-compressão
verif= CVS450X116.verif_NM(Nsd,Msdx,Msdy,Lbx=0,Cb=1,klx=600,kly=1,klz=1)

CVS450X116_map = vars(CVS450X116)

print("Key\tValue")
print("--------------")
for key, value in CVS450X116_map.items():
    print(f"{key};{value}")

print(f"NM;{verif}")
class Solution:

    def palabrasUtecsinas(self, palabra):

        if ('u' in palabra) and ('t' in palabra) and ('e' in palabra) and ('c' in palabra):
          return True
        else:
          return False        

    def aprobe(self,T1,T2,E1,E2,TC,P1,P2):

      NFT = (0.15*T1)+(0.15*T2)+(0.35*E1)+(0.35*E2)
      NFL = (0.3*TC)+(0.25*P1)+(0.45*P2)
      NF = (NFT+NFL)/2
      if NFT>=10.5 and NFL>=10.5 and NF>=10.5:
        return True
      elif NFT<=10.5 or NFL<=10.5 and NF>=10.5:
        return False

    def IMvsCap (self,mensaje):

        capitan = 0
        ironman = 0
        for i in mensaje:
          if i== 'I' or i== 'i':
            ironman += 1
          elif i== 'C' or i== 'c':
            capitan +=1          
        if ironman>capitan:
          return"Iron Man"
        elif ironman<capitan:
          return"Capitan America"
        else:
          return "Empate"

    def rectanguloEspecial(self,longitud,altura,letra_base,letra_especial):

        if (longitud>0) and (altura>0) and (longitud!=altura):
          VD=abs(longitud - altura)
          matriz=[]
          for i in range(altura):
            for j in range(longitud):
              if (i+j)%VD==1:
                matriz.append(letra_base)
              else:
                matriz.append(letra_especial)
            if i < altura-1:
              matriz.append("\n")
          return("".join(matriz))


# === CASOS EJEMPLO ===
print(Solution().palabrasUtecsinas("cuenta")) # output en consola: True
print(Solution().aprobe(13,15,16,11,17,10,13)) # output en consola: True
print(Solution().IMvsCap("ICICICIICI")) # output en consola: "Iron Man"
print(Solution().rectanguloEspecial(6,4,"O","L"))
"""
output en consola:      LOLOLO
                        OLOLOL
                        LOLOLO
                        OLOLOL
"""


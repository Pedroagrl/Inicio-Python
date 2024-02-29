import random
import time

print('\033[93m-=-\033[0m' * 20)
numero = print('\033[34mVou pensar em um numero entre 0 e 5. Tente adivinhar... \033[0m')
print('\033[93m-=-\033[0m' * 20)
pergunta = int(input('Em que número pensei? '))
print('\033[95mPROCESSANDO...\033[0m')
time.sleep (2)
escolhido = random.choice([0, 1, 2, 3, 4, 5])
if pergunta == escolhido:
    print('\033[92mParabéns, você acertou!\033[0m]')
else:
    print(f'\033[91mVocê errou!, o número era {escolhido}\033[0m')
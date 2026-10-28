# Projeto: caixa compacta (substituir o som atual)

## Som atual (referência do vídeo)
- Caixa em pé de MDF verde, com alça e módulo Bluetooth/USB no topo.
- 2 × JBL Multisystem coaxial de 5" lado a lado em cima.
- Bomber Outdoor de 10" embaixo, com duto em fenda na base da frente.
- O dono gosta do som, mas acha a caixa grande. O Outdoor de 10" não será reaproveitado.
- Amplificador de 800 W.

## Proposta
![Caixa compacta 3D](projeto-compacto-3d.png)

- **Medida externa:** 320 × 450 × 300 mm (L × A × P), cerca de 43 L. Em MDF de 15 mm.
- **Câmara de cima:** dividida em 2 câmaras **fechadas** de cerca de 5,5 L, uma para cada JBL de 5" (interno 137 × 150 × 270 mm cada).
- **Câmara de baixo:** Bomber Bicho Papão 8", interno 290 × 252 × 270 mm, ou seja, 19,7 L bruto e cerca de 15,8 L líquidos.
  - Sintonia em cerca de 37 Hz e F3 de cerca de 34 Hz ao ar livre (veja `projeto-bomber-bp8.md`).
  - Duto de PVC 75 mm, com cerca de 48 cm em "L/U", saindo pela traseira embaixo.
- **Alto-falantes na frente:**
  - JBL com centro a 75 mm do eixo central da caixa, na altura do meio da câmara de cima.
  - Sub com centro a 141 mm acima do fundo externo.
- **Topo:** alça e módulo, como na caixa atual.

## Ajustes de amplificador / DSP
- **Sub:**
  - Filtro passa-baixas em cerca de 80–100 Hz.
  - **Subsônico em cerca de 28 Hz.**
  - Ganho limitado: acima de cerca de 170–200 W em grave contínuo o cone passa do Xmax, e o sub aguenta no máximo 600 W RMS.
- **JBL:** filtro passa-altas em cerca de 100–120 Hz, porque numa câmara pequena eles não devem receber grave.

## A confirmar
- Furo e profundidade dos JBL Multisystem 5" (medir; um 5" típico tem furo de cerca de 11–12 cm e frame de cerca de 13,5 cm).
- Medidas da caixa atual, para comparar.
- Quantos canais tem o amplificador de 800 W.

## Revisão: compartimento técnico (tomada + bateria)

![Esquema de ligação](projeto-compacto-ligacao.png)

- **Medida externa:** 320 × 480 × 340 mm (L × A × P).
- **Câmara do sub (embaixo):** interno 290 × 220 × 310 mm, cerca de 15,8 L líquidos. Duto de 75 mm com cerca de 48 cm saindo pela traseira.
- **JBL:** os dois juntos numa câmara **fechada** na frente de cima (interno 290 × 215 × 110 mm, cerca de 6 L).
- **Compartimento técnico:** atrás da câmara dos JBL (interno 290 × 215 × 185 mm, cerca de 11,5 L), vedado em relação às câmaras de som.
  - Tampa traseira removível, com grelha de ventilação e, se precisar, uma ventoinha de 12 V.
  - Cabem a bateria LiFePO4 12 V 20 Ah (em pé), a fonte chaveada 60 A (deitada), o amplificador (preso na parede) e o processador.
  - Os barramentos + e − e o fusível com chave geral ficam na lateral.
- **Alimentação:**
  - A fonte chaveada 12 V 60 A fica ajustada em 14,2–14,4 V e precisa ter **limite de corrente** ou função carregador.
  - Ela fica em paralelo com a bateria pelo barramento. Com tomada, a fonte alimenta o som e carrega a bateria. Sem tomada, a bateria segura tudo.
  - Um diodo ou relé isola a fonte quando está desligada.
- **Fusíveis:**
  - bateria: 100 A, perto do polo;
  - amplificador: conforme o manual;
  - processador: 5 A;
  - módulo: 3 A.
- **Cabos principais:** 16–25 mm².

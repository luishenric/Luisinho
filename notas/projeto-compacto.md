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

## Bateria montada com solda ponto (análise)
- **ICR18650 2200 mAh (anúncio barato): NÃO usar.**
  - É química de baixa descarga, cerca de 1–2C (≈ 2–4 A por célula).
  - Para picos de 40–80 A do amplificador de 800 W seriam precisas de 10 a 20 células em paralelo.
  - As células são de procedência duvidosa (código borrado).
- **Li-ion em 3S** (11,1 V nominal, 12,6 V cheio) **não combina com a fonte em 14,2–14,4 V**: sobrecarrega e há risco de incêndio. Só serviria com a fonte travada em 12,6 V.
- **Recomendado: LiFePO4 32700 (3,2 V, ~6 Ah) em 4S3P.**
  - 12,8 V nominal e 14,6 V cheio, o que é compatível com som automotivo e com a fonte em 14,2–14,4 V.
  - 12 células, ≈ 18 Ah e ≈ 230 Wh.
  - Tamanho de ≈ 13 × 10 × 7,5 cm e peso de ≈ 1,8 kg.
  - A descarga típica é de 3C (≈ 18 A por célula, ≈ 54 A no pack); conferir no datasheet.
  - BMS **4S LiFePO4** com balanceamento, de ≥ 100 A.
  - Fita de níquel puro grossa (0,2 mm, em várias camadas) ou chapa de cobre/níquel; existem 32700 com terminal de parafuso, que não precisam de solda.
- **Alternativa Li-ion:** 18650 de alta descarga (Samsung 25R, LG HG2, Molicel P28A) em 3S, com fonte limitada a 12,6 V.

## Pack Li-ion 3S7P / 3S8P (fonte regulada em ~12,4 V)
- 3S7P = 21 células; 3S8P = 24 células (por exemplo, 3 kits de 10 de 2000 mAh, com sobra para descartar ruins).
- Corrente por célula num pico de 40–60 A: ≈ 5–8 A (7P) ou 5–7,5 A (8P). Na média de ≈ 10 A: ≈ 1,3 A por célula.
- Capacidade nominal: 14 Ah (7P) ou 16 Ah (8P), ≈ 155–180 Wh. Em células genéricas a real costuma ser menor.
- Tamanho do 3S8P deitado: ≈ 15 × 6 × 7 cm, ≈ 1,1 kg.
- Obrigatório: testar capacidade e resistência interna de cada célula, montar grupos paralelos equilibrados, BMS 3S ≥ 100 A com balanceamento, e ligações série dimensionadas para 60–80 A.

# Caixa acústica para alto-falante: litragem, dutos e frequência

Referência para projetar caixas (foco em subwoofer / som automotivo).
Revisado com pesquisa em 2026-10-28. Fontes no fim do arquivo.

> **Nível de confiança:** fórmulas marcadas com ✅ são teoria padrão (Thiele-Small / Helmholtz) e batem em várias fontes. Itens marcados com ⚠️ são regras práticas de fórum / car audio: servem de ponto de partida, não são lei. Sempre confirmar num simulador (WinISD).

## 1. Parâmetros Thiele-Small (vêm no manual do alto-falante)

| Parâmetro | O que é |
|---|---|
| **Fs** | Frequência de ressonância do alto-falante (Hz) |
| **Qts** | Fator de amortecimento total |
| **Qes** | Parte elétrica do Qts |
| **Vas** | Volume de ar equivalente à suspensão (**usar em litros** nas fórmulas) |
| **Xmax** | Excursão máxima linear do cone |
| **Sd** | Área efetiva do cone |

### ⚠️ EBP (Efficiency Bandwidth Product) = Fs ÷ Qes
- **≤ 50** → caixa selada
- **50 a 100** → selada ou dutada (depende do objetivo)
- **> 100** → dutada
- Algumas fontes usam **90** em vez de 100 como limite. É guia rápido, não regra absoluta.

### Qts como pista
- Qts ≈ **0,4 ou menos** → bom para caixa dutada.
- Qts ≈ **0,383** → caixa dutada ideal é o alinhamento B4 (Butterworth de 4ª ordem).
- Qts alto (≈ 0,5+) → tende a ir melhor em selada.

## 2. Litragem

- Litros = largura × altura × profundidade **internas** (cm) ÷ 1000
- Descontar a espessura do MDF (geralmente 15–18 mm) de cada lado.
- **Volume líquido** = volume interno − volume ocupado pelo alto-falante − volume do duto − reforços internos.
- Duto grande ocupa bastante volume: recalcular a caixa depois de dimensionar o duto.

## 3. Caixa selada ✅

- **Vb = Vas ÷ ((Qtc / Qts)² − 1)** (Vas em litros)
- Forma equivalente: **Qtc = Qts × √(1 + Vas/Vb)**
- Frequência de ressonância do sistema: **Fc = Fs × Qtc ÷ Qts**
- **Qtc**:
  - 0,707 → resposta Butterworth (grave seco, linear; padrão)
  - 0,8 a 1,0 → mais "punch", menos extensão
- Caixa menor → Qtc maior → grave mais duro e curto.

## 4. Caixa dutada (bass reflex)

O duto funciona como ressonador de Helmholtz: o ar dentro dele é uma massa sobre a "mola" do ar da caixa. Na frequência de sintonia (**Fb**), o duto é quem toca e o cone quase não se move.

### Fórmulas de partida
**Alinhamento B4 (Butterworth), ideal para Qts ≈ 0,383:**
- **Vb = Vas × (Qts ÷ 0,383)³**
- **Fb = Fs × 0,383 ÷ Qts**

**⚠️ Aproximação empírica (aparece em mais de uma fonte de fórum):**
- **Vb ≈ 20 × Vas × Qts^3,3**
- **Fb ≈ 0,42 × Fs × Qts^-0,96**

> Correção: a versão anterior destas notas usava `Vb ≈ 15 × Vas × Qts^2,87`, `Fb ≈ 0,42 × Fs × Qts^-0,9` e `F3 ≈ 0,26 × Fs × Qts^-1,4`. Na pesquisa só achei a de Vb citada num único post de fórum, e não achei fonte para a de F3. Foram trocadas pelas versões acima. O F3 real deve ser lido no simulador.

### Comprimento do duto redondo ✅
D em cm, Vb em litros, Fb em Hz, N = número de dutos:

**L (cm) = (23562 × D² × N) ÷ (Fb² × Vb) − k × D**

Correção de ponta (k):
- **0,732** → uma ponta com flange (rente à parede) e outra livre (o caso mais comum)
- **0,850** → as duas pontas com flange
- **0,614** → as duas pontas livres

Versão em milímetros (Richard Small): L (mm) = 2350 × D² ÷ (Vb × Fb²) − 0,732 × D, com D em mm.

### Como cada coisa mexe na sintonia
- Duto mais **longo** → frequência mais **baixa**
- Duto mais **largo** → precisa ser mais comprido para manter a mesma Fb
- Caixa **maior** (mesmo duto) → frequência mais **baixa**

### Velocidade do ar no duto
- **Abaixo de 17 m/s** → seguro, sem ruído (alvo conservador).
- **17 a 26 m/s** → zona intermediária; pode fazer ruído em volume alto.
- **≈ 25 a 35 m/s** → faixa onde a maioria das fontes coloca o "chuffing" (assobio/sopro) ou limite absoluto.
- Velocidade alta demais → **aumentar a área do duto** (e compensar o volume que ele ocupa).
- A velocidade mostrada em simulador é o pior caso.

### ⚠️ Área do duto (regra prática de car audio)
| Tipo de duto | pol² por pé³ | cm² por litro (aprox.) |
|---|---|---|
| Fenda (slot) de MDF | 12 a 16 | **2,7 a 3,6** |
| Redondo (aero / PVC) | 7 a 11 | **1,6 a 2,5** |

- Duto redondo aceita menos área porque o ar flui melhor nele (ainda mais com as pontas arredondadas).
- Essa regra é polêmica: a área certa depende do **deslocamento do cone (Sd × Xmax)** e da potência, não só do volume da caixa. Para sub de alta excursão/potência, a regra pode dar duto pequeno demais. Conferir a velocidade no WinISD.

## 5. Exemplo resolvido

Sub de 12" com Fs = 30 Hz, Qts = 0,4, Vas = 60 L:

- **Selada (Qtc 0,707)**: Vb = 60 ÷ ((0,707/0,4)² − 1) ≈ **28 L**, Fc ≈ **53 Hz**
- **Dutada (B4)**: Vb = 60 × (0,4/0,383)³ ≈ **68 L**, Fb = 30 × 0,383/0,4 ≈ **29 Hz**
- **Dutada (aproximação 20 × Vas × Qts^3,3)**: Vb ≈ **58 L**, Fb ≈ **30 Hz**
  - As duas dão resultado parecido; o simulador decide o valor final.
- **Duto** (caixa de 58 L, Fb 30 Hz):
  - Área pela regra prática do duto redondo: 58 × 1,6 a 2,5 ≈ **93 a 145 cm²** → um tubo de **11 a 13,5 cm** de diâmetro.
  - Com D = 10 cm (78,5 cm², pouco para muita potência): L = 23562 × 100 ÷ (30² × 58) − 7,3 ≈ **38 cm**
  - Com D = 12 cm: L = 23562 × 144 ÷ (30² × 58) − 8,8 ≈ **56 cm** → longo; por isso em sub se usa muito duto em fenda dobrado (em "L").

## 6. ⚠️ Escolha da sintonia (som automotivo)

Não existe frequência "oficial"; são faixas comuns citadas em fóruns:

| Fb | Uso comum |
|---|---|
| ~30–35 Hz | Dia a dia / qualidade (SQ), grave mais profundo |
| ~34 Hz | Meio-termo entre SQ e pressão |
| ~40 Hz+ | Foco em pressão (SPL) no dia a dia |

- Para **SPL de competição**: medir a frequência de ressonância do carro (cabin gain) e sintonizar perto dela (até ~5 Hz).
- Sempre conferir se o fabricante do sub recomenda uma caixa.

### Filtro subsônico
Abaixo da Fb o cone fica sem controle. Usar filtro subsônico (passa-altas) um pouco abaixo da Fb. Regras encontradas:
- **Fb × 0,75** (≈ meia oitava abaixo) → a mais comum. Ex.: Fb 40 Hz → filtro em 30 Hz.
- **Fb × 0,8** → Ex.: Fb 35 Hz → 28 Hz.
- **2 a 5 Hz abaixo da Fb** → usado por alguns instaladores.
- O filtro é uma curva, não um corte seco: ajustar no ouvido e observar se o cone "bate".

## 7. Ferramentas

- **WinISD** (gratuito): simula resposta, velocidade do ar no duto e excursão do cone.
- As fórmulas acima são ponto de partida; sempre confirmar no simulador.

## Fontes

- Fórmula do duto e correção de ponta: [diyAudio – port sizes and effects](https://www.diyaudio.com/community/threads/port-sizes-and-effects.5590/post-54996), [diyAudio – port tuning](https://www.diyaudio.com/community/threads/port-tuning.387253/post-7049141), [Omni Calculator – port length](https://wba.omnicalculator.com/other/port-length), [Boomspeaker – bass port tuning calculator](https://boomspeaker.com/calculators/bass-port-tuning-calculator/)
- Caixa selada (Vb, Qtc, Fc): [Audio Intensity – sealed box design](https://audiointensity.com/blogs/how-to-build/sealed-subwoofer-box-design), [Audio Judgement – sealed box example](https://audiojudgement.com/how-to-build-a-sealed-subwoofer-box/), [diyAudio – verify my reverse engineering](https://www.diyaudio.com/community/threads/verify-my-reverse-engineering.407629/), [Boomspeaker – Thiele-Small alignment calculator](https://boomspeaker.com/calculators/thiele-small-box-alignment-calculator/)
- Alinhamentos dutados (B4, 20 × Vas × Qts^3,3): [diyAudio – Vas vs enclosure volume](https://www.diyaudio.com/community/threads/relation-between-vas-and-enclosure-volume.26085/post-303313), [diyAudio – bass reflex alignments](https://www.diyaudio.com/community/threads/bass-reflex-alignments.424903/), [Scan-Speak Technote 07 – box alignments](https://www.scan-speak.dk/datasheet/tech/Scan-Speak_Technote07_Box-alignments.pdf), [diyAudio – vb vas vented box](https://www.diyaudio.com/community/threads/vb-vas-vented-box.415444/)
- EBP: [DIY Audio & Video – sealed vs ported](https://diyaudioandvideo.com/Calculator/SealedVsPortedSpeakerBox/Help/), [Audio Judgement – sealed vs bass reflex](https://audiojudgement.com/sealed-vs-bass-reflex/), [Audio Intensity – EBP](https://audiointensity.com/pages/ebp)
- Velocidade do ar no duto: [Speaker Box Lite – port area guide](https://speakerboxlite.com/es/articles/port-area-calculation-guide-speaker-box-lite-workflow), [diyAudio – flared ports turbulence](https://www.diyaudio.com/forums/subwoofers/64528-flared-ports-turbulence.html), [Patente – port velocity limiter](https://patents.justia.com/patent/20200083853), [Audioholics – port chuffing](https://forums.audioholics.com/forums/goto/post?id=1692148)
- Área do duto por volume: [Audio Intensity – port area calculator](https://audiointensity.com/pages/subwoofer-port-area-calculator-for-high-excursion-car-subwoofers), [Boomspeaker – subwoofer port calculator](https://boomspeaker.com/?p=9768), [CarAudio.com – port area](https://www.caraudio.com/threads/port-area.334345/), [CarAudio.com – too little or too much port area](https://www.caraudio.com/threads/what-happens-if-you-have-too-little-or-too-much-port-area.592498/)
- Sintonia: [CarAudio.com – why higher tuning for SPL](https://www.caraudio.com/threads/why-higher-tuning-for-spl-and-lower-for-sq.178636/), [CarAudio.com – what should I tune to](https://www.caraudio.com/threads/what-should-i-tune-to.424107/), [CarAudio.com – SPL box tuning](https://www.caraudio.com/threads/plans-for-an-spl-box-optimum-tuning-frequency-trying-to-pass-150db.563387/page-2)
- Filtro subsônico: [AudioControl – setting up a subsonic filter](https://www.audiocontrol.com/knowledge-base/the-procedure-for-setting-up-a-subsonic-filter/), [Boomspeaker – subsonic filter setting](https://boomspeaker.com/subsonic-filter-setting/), [CarAudio.com – subsonic filtering](https://www.caraudio.com/threads/subsonic-filtering.572562/)

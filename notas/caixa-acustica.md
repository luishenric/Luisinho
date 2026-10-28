# Caixa acústica para alto-falante: litragem, dutos e frequência

Referência para projetar caixas (foco em subwoofer / som automotivo).

## 1. Parâmetros Thiele-Small (vêm no manual do alto-falante)

| Parâmetro | O que é |
|---|---|
| **Fs** | Frequência de ressonância do alto-falante (Hz) |
| **Qts** | Fator de amortecimento total |
| **Qes** | Parte elétrica do Qts |
| **Vas** | Volume de ar equivalente à suspensão (litros) |
| **Xmax** | Excursão máxima linear do cone |
| **Sd** | Área efetiva do cone |

### EBP (Efficiency Bandwidth Product) = Fs ÷ Qes
- **< 50** → caixa selada
- **50 a 100** → selada ou dutada
- **> 100** → dutada

## 2. Litragem

- Litros = largura × altura × profundidade **internas** (cm) ÷ 1000
- Descontar a espessura do MDF (geralmente 15–18 mm) de cada lado.
- **Volume líquido** = volume interno − volume ocupado pelo alto-falante − volume do duto − reforços internos.

## 3. Caixa selada

- **Vb = Vas ÷ ((Qtc / Qts)² − 1)**
- **Qtc**:
  - 0,707 → resposta Butterworth (grave seco, linear; padrão)
  - 0,8 a 1,0 → mais "punch", menos extensão
- Frequência de corte: **Fc = Fs × Qtc ÷ Qts**
- Caixa menor → Qtc maior → grave mais duro e curto.

## 4. Caixa dutada (bass reflex)

O duto funciona como ressonador de Helmholtz: o ar dentro dele é uma massa sobre a "mola" do ar da caixa. Na frequência de sintonia (**Fb**), o duto é quem toca e o cone quase não se move.

### Fórmulas de partida (alinhamento de Small / QB3 aproximado)
- **Vb ≈ 15 × Vas × Qts^2,87**
- **Fb ≈ 0,42 × Fs × Qts^-0,9**
- **F3 ≈ 0,26 × Fs × Qts^-1,4** (ponto de −3 dB)

### Comprimento do duto redondo
D em cm, Vb em litros, Fb em Hz, N = número de dutos:

**L (cm) = (23562 × D² × N) ÷ (Fb² × Vb) − 0,73 × D**

(0,73 × D é a correção de ponta: uma ponta com flange e outra livre.)

### Como cada coisa mexe na sintonia
- Duto mais **longo** → frequência mais **baixa**
- Duto mais **largo** → precisa ser mais comprido para manter a mesma Fb
- Caixa **maior** (mesmo duto) → frequência mais **baixa**

### Área do duto
- Duto estreito demais faz o ar "assobiar" (chuffing / ruído de porta).
- Manter a velocidade do ar **abaixo de ~17 m/s** (cerca de 5% da velocidade do som).
- Regra prática de som automotivo: **12–16 pol² por pé³** ≈ **3 a 4 cm² de duto por litro**.
- Duto em fenda (slot) de MDF: usar a mesma área equivalente; uma parede da caixa pode servir de lateral do duto.

## 5. Exemplo resolvido

Sub de 12" com Fs = 30 Hz, Qts = 0,4, Vas = 60 L:

- **Selada (Qtc 0,707)**: Vb = 60 ÷ ((0,707/0,4)² − 1) ≈ **28 L**, Fc ≈ **53 Hz**
- **Dutada**: Vb ≈ **65 L**, Fb ≈ **29 Hz**, F3 ≈ **28 Hz**
  - Duto redondo de 10 cm: L = 23562 × 100 ÷ (29² × 65) − 7,3 ≈ **36 cm**

## 6. Escolha da sintonia (som automotivo)

| Fb | Resultado |
|---|---|
| 28–33 Hz | Grave profundo (eletrônica, rap) |
| 35–40 Hz | Equilibrado, uso diário |
| 40–50 Hz+ | Mais pressão (SPL), perde o grave mais profundo |

**Atenção:** abaixo da Fb o cone fica sem controle (descarrega). Usar **filtro subsônico** cerca de 5 Hz abaixo da Fb para não danificar o alto-falante.

## 7. Ferramentas

- **WinISD** (gratuito): simula resposta, velocidade do ar no duto e excursão do cone.
- As fórmulas acima são ponto de partida; sempre confirmar no simulador.

# Projeto: caixa compacta com Bomber Bicho Papão 8" 600 W (cód. 1.23.121)

Objetivo: caixa compacta, de boa qualidade, com grave o mais perto possível de **35 Hz** (F3). O projeto é para replicar e vender.

## Parâmetros (manual Bomber, rev. 02, 04/02/2026)
| Fs | Qts | Qes | Vas | Sd | Mms | Xmax | Xlim | Volume ocupado |
|---|---|---|---|---|---|---|---|---|
| 46 Hz | 0,47 | 0,49 | 8,33 L | 183 cm² | 66,28 g | 11 mm | 19 mm | 1,44 L |

- O EBP é Fs ÷ Qes ≈ 94. Está na fronteira, e a caixa dutada funciona bem.
- Re não foi encontrado e foi estimado em 3,4 Ω. Com isso, Bl ≈ 11,5 e Qms ≈ 11,5 (o Vas recalculado bate: 8,6 L).

## Simulação (`ferramentas/sim_caixa.py`, ao ar livre, sem ganho de cabine)

**Selada:** não chega a 35 Hz. O F3 fica em cerca de 70 Hz com qualquer volume, e em 35 Hz o som já está cerca de 10 dB abaixo.

**Dutada (volume líquido):**
| Volume | Fb | F3 | F6 | Pico |
|---|---|---|---|---|
| 10 L | 38 Hz | 42 Hz | 34 Hz | plano |
| 12 L | 38 Hz | 38 Hz | 33 Hz | plano |
| **15 L** | **36–38 Hz** | **≈ 35 Hz** | 31 Hz | plano |
| 18 L | 35 Hz | 32 Hz | 29 Hz | plano |
| 20 L | 35 Hz | 32 Hz | 29 Hz | plano |
| 25 L+ | — | — | — | começa a formar pico (+1,6 a +5 dB) |

## Proposta inicial para testar
- **15 L líquidos, Fb ≈ 37 Hz.**
- **Duto redondo de 7,5 cm, com cerca de 55 cm de comprimento** (com uma ponta rente à parede). Ocupa cerca de 2,4 L.
- **Volume bruto interno ≈ 19 L** (15 + duto + alto-falante + reforços). Exemplo: 27 × 27 × 27 cm por dentro, ou cerca de 30 × 30 × 30 cm por fora em MDF de 15 mm.
- Dá para usar o duto dobrado ou em fenda com área de cerca de 45 a 55 cm². O comprimento muda, então recalcular.

## Limites encontrados
- **Excursão:** perto de 45 a 60 Hz, o cone chega ao Xmax (11 mm) com cerca de **150 a 200 W em tom contínuo**. Com 600 W contínuos ele passaria do Xlim. Com música dá para usar mais, mas o produto precisa de **filtro subsônico em cerca de 28 Hz** e de limitador.
- **Velocidade no duto de 7,5 cm:** 16 m/s a 100 W e 23 m/s a 200 W. Fica na zona intermediária quando o cone está no limite, então arredondar as pontas do duto.
- **Duto de 10 cm:** daria cerca de 100 cm de comprimento e ocuparia 8 L, o que é inviável numa caixa compacta.

## Alternativas para compactar
- **Radiador passivo** no lugar do duto. É o que caixas portáteis comerciais usam, porque não tem duto longo nem ruído de ar.
- **DSP / equalização** (Linkwitz transform) numa caixa selada pequena. Exige mais potência e excursão.
- **No carro**, o ganho de cabine reforça o grave abaixo de cerca de 50 a 60 Hz. Uma caixa de 10 a 12 L pode soar como 35 Hz lá dentro.

## Próximos passos
1. Confirmar Re e a tabela de caixa do manual oficial da Bomber (PDF 3.27.443-1.23.121).
2. Conferir no WinISD.
3. Construir o protótipo e medir a sintonia real (impedância ou microfone).

import Front_Calculadora

def calcula_VP( vfi, tc):
    result = (vfi + tc ) * -1
    print(result)
    return result

v_valor_financiado = calcula_VP(Front_Calculadora.var_vlr_financiamento , Front_Calculadora.var_tc)

def calc_vlr_parcela( taxa , parcela , vp ):
    pmt = vp / (((1 + taxa)**parcela - 1) / ((1 + taxa)**parcela * taxa))
    print (pmt)
    return pmt
v_valor_parcela = calc_vlr_parcela( Front_Calculadora.var_tx_juros, )

def calc_receita_juros(vp, valor_parcela, qtd_parcelas):
    receita_juros = (vp + (valor_parcela*qtd_parcelas))
    print (receita_juros)
    return receita_juros




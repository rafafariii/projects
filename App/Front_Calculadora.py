


def lambda_handler():
    var_vlr_financiamento=2500
    var_tc=50
    var_qtd_parcelas=10
    var_tx_juros=5.79
    var_comis_agt_financi=2
    var_comis_agt_recebiment=2
    var_comis_loja_financi=0
    var_comis_loja_recebiment=0
    ###Variáveis fixas
    var_desp_Cred=8.00
    var_ef_cred=47.00 #47%
    var_Desp_Mesa=9.32
    var_Desp_Carne=0.71
    var_Desp_CP_CR=2.20
    var_Desp_Desc=5.31
    var_Desp_Gestao=7.10
    var_CDI=0
    var_ISS=5/100	#5%
    var_PIS_Cofins=4.65/100 #4,65%


    v_valor_financiado = calcula_VP(var_vlr_financiamento, var_tc)
    v_valor_parcela = calc_vlr_parcela(var_tx_juros, var_qtd_parcelas, v_valor_financiado)
    v_receita_juros = calc_receita_juros(v_valor_financiado, v_valor_parcela, var_qtd_parcelas)
    v_valor_comissao_financiamento = calc_vlr_com_financiamento(var_vlr_financiamento,var_comis_agt_financi, var_comis_loja_financi)
    v_valor_comissao_recebimento = calc_vlr_com_recebimento(v_valor_parcela, var_qtd_parcelas, var_comis_agt_recebiment, var_comis_loja_recebiment)
    v_valor_ISS = var_ISS * var_tc
    var_carteira_bruta0 = var_vlr_financiamento + var_tc
    var_renda0 = var_carteira_bruta0 * (var_tx_juros / 100)

    return None

def calcula_VP(vfi, tc):
    result = (vfi + tc) * -1
    return result

def calc_vlr_parcela(taxa, parcela, vp):
    tx = taxa / 100
    pmt = (vp / (((1 + tx) ** parcela - 1) / ((1 + tx) ** parcela * tx))) * -1
    return pmt


def calc_receita_juros(vp, valor_parcela, qtd_parcelas):
    receita_juros = (vp + (valor_parcela*qtd_parcelas))
    return receita_juros


def calc_vlr_com_financiamento(vlrfinanciamento, comiss_agt_financ, comiss_lj_financ):
    com_agt_fin = comiss_agt_financ/100
    com_lj_fin = comiss_lj_financ/100
    return (com_agt_fin+com_lj_fin)*vlrfinanciamento


def calc_vlr_com_recebimento(vlrparcela, qtd_parcelas, comiss_agt_receb, comiss_lj_receb):
    com_agt_receb = comiss_agt_receb/100
    comiss_lj_receb = comiss_lj_receb/100
    return ((com_agt_receb+comiss_lj_receb)*qtd_parcelas)*vlrparcela










#VARIÁVEIS DISPONÍVEIS
#v_valor_financiado
#v_valor_parcela
#v_receita_juros
#v_valor_comissao_financiamento
#v_valor_comissao_recebimento
#v_valor_ISS

#print("=============================")
#print("=========RESULTADO===========")
#print("RECEITA ADIMPLENTE",v_receita_juros+var_tc )
#print("JUROS ADIMPLENTE",v_receita_juros)
#print("COMISSAO FINANC",v_valor_comissao_financiamento)
#print("COMISSAO RECEB",v_valor_comissao_recebimento)

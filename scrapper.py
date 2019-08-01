import requests
import pandas as pd
import os
from bs4 import BeautifulSoup
from datetime import date, timedelta

# ontem
# pd_ontem = pd.to_datetime((datetime.now() - timedelta(2)).strftime('%Y-%m-%d'))
# print(pd_ontem)
ontem = (date.today() - timedelta(days=1)).strftime('%d/%m/%Y')
print(ontem)

# list of stocks
stocks = ['AALR3', 'GSHP3', 'ABCB3', 'ABCB4', 'BPAT33', 'ABEV3', 'ACES3', 'ACES4', 'ADHM3', 'AEDU11', 'AEDU3', 'AESL3', 'AESL4', 'AFLT3', 'AFLU3', 'AFLU5', 'AGIN3', 'AGRO3', 'ALBA3', 'ALLL11', 'ALLL3', 'ALLL4', 'ALPA3', 'ALPA4', 'ALSC3', 'ALUP11', 'ALUP3', 'BBSE3', 'ALUP4', 'AMAR3', 'AMBV3', 'AMBV4', 'AMPI3', 'DIRR3', 'ANIM3', 'ARCE3', 'ARLA3', 'ARLA4', 'ARPS3', 'ARPS4', 'ARTE3', 'ARTE4', 'ARZZ3', 'ATOM3', 'AUTM3', 'AVIL3', 'AZEV3', 'AZEV4', 'B3SA3', 'BALM3', 'CCPR3', 'BALM4', 'BAUH4', 'BAZA3', 'BBAS3', 'BBDC3', 'BBDC4', 'BCAL6', 'BEEF3', 'BEES3', 'BEES4', 'BELG3', 'RPAD5', 'BELG4', 'BEMA3', 'BESP3', 'BESP4', 'MSPA4', 'BFIT3', 'BFIT4', 'BGIP3', 'KLBN4', 'BGIP4', 'BIDI4', 'BKBR3', 'BMEB3', 'BMEB4', 'BMIN3', 'BMIN4', 'MSPA3', 'BMKS3', 'BMTO3', 'KLBN11', 'BMTO4', 'BNBR3', 'BNBR4', 'BPAC11', 'BPAC3', 'BPAC5', 'BPAN4', 'BPAR3', 'BPIA3', 'BPNM3', 'BRAP3', 'BRAP4', 'BRDT3', 'BRGE11', 'BRGE12', 'BRGE3', 'BRGE5', 'BRGE6', 'BRGE7', 'CSAB4', 'BRGE8', 'BRIV3', 'BRIV4', 'BRKM3', 'KLBN3', 'BRKM5', 'BRKM6', 'BRML3', 'BRSR3', 'BRSR4', 'BRSR5', 'BRSR6', 'BSCT3', 'BSCT5', 'BSCT6', 'BSLI3', 'BSLI4', 'BUET3', 'BUET4', 'CAMB3', 'CAMB4', 'CAML3', 'CARD3', 'CBEE3', 'CBMA3', 'CBMA4', 'CCRO3', 'CCTU4', 'CALI4', 'CEBR3', 'CSAB3', 'CEBR5', 'CEBR6', 'CEDO3', 'CEDO4', 'CEEB3', 'CEEB5', 'CEED3', 'CEED4', 'CEGR3', 'CELM3', 'CELP5', 'CELP7', 'CEPE3', 'CEPE5', 'CEPE6', 'CESP3', 'CESP4', 'CESP5', 'CESP6', 'CFLU4', 'CGAS3', 'CGAS5', 'CGRA3', 'CGRA4', 'CIEL3', 'CIQU3', 'IRBR3', 'CIQU4', 'CLSC3', 'CLSC4', 'CLSC5', 'CLSC6', 'CMET4', 'CMIG3', 'CMIG4', 'CNFB4', 'COCE3', 'COCE5', 'COCE6', 'CORR3', 'CORR4', 'CPFE3', 'CPFG3', 'CPFG4', 'CPLE3', 'CPLE5', 'CPLE6', 'CPRE3', 'CPSL3', 'CREM3', 'CREM4', 'CRFB3', 'CRIV3', 'CRIV4', 'CRPG3', 'CRPG5', 'CRPG6', 'CRTP3', 'CRTP5', 'CRUZ3', 'CSAN3', 'CSMG3', 'CSNA3', 'CSPC3', 'CSPC4', 'CSRN3', 'CSRN5', 'CSRN6', 'CSTB3', 'CSTB4', 'CTIP3', 'CTKA3', 'CTKA4', 'CTNM3', 'CTNM4', 'CTPC3', 'CTPC4', 'CTSA3', 'CTSA4', 'CTSA8', 'CTWR3', 'CVCB3', 'CYRE3', 'CYRE4', 'CZLT33', 'CZRS3', 'CZRS4', 'DAGB33', 'DASA3', 'DAYC3', 'DAYC4', 'DHBI3', 'DHBI4', 'DMMO3', 'DOCA3', 'DOCA4', 'DOHL3', 'DOHL4', 'SUZB3', 'DPPI3', 'DPPI4', 'DSUL3', 'DTCY3', 'DTEX3', 'DUQE3', 'DUQE4', 'DURA3', 'DURA4', 'DXTG4', 'SHOW3', 'EALT3', 'EALT4', 'EBCO3', 'EBCO4', 'EBEN4', 'EUCA4', 'ECIS3', 'ECIS4', 'ECOR3', 'HBTS5', 'ECPR3', 'ECPR4', 'EEEL3', 'EEEL4', 'EGIE3', 'EKTR3', 'EKTR4', 'ELCA3', 'ELCA4', 'ELEK3', 'ELEK4', 'ELET3', 'ELET5', 'ELET6', 'ELEV3', 'ELUM3', 'ELUM4', 'EMAE4', 'ENAT3', 'ENBR3', 'ENER3', 'ENER5', 'EUCA3', 'ENER6', 'ENEV3', 'ENGI11', 'ENGI3', 'ENGI4', 'ENMT3', 'ENMT4', 'EQTL3', 'ESCE3', 'ESTC11', 'EMBR3', 'ESTC3', 'STBP3', 'ESTC4', 'ESTR3', 'ESTR4', 'ETER3', 'ETER4', 'ABYA3', 'EZTC3', 'FBMC3', 'FBMC4', 'FCAP3', 'FCAP4', 'AELP3', 'FESA3', 'FESA4', 'FFTL3', 'FFTL4', 'AGEI3', 'AGEN33', 'FGUI3', 'AHEB3', 'AHEB5', 'AHEB6', 'FGUI4', 'FHER3', 'FIBR3', 'FIGE3', 'FIGE4', 'FJTA3', 'FJTA4', 'AMIL3', 'FLCL3', 'APTI4', 'FLCL5', 'ARCZ3', 'ARCZ6', 'FLCL6', 'FLRY3', 'FRAS3', 'FRAS4', 'FRIO3', 'FRTA3', 'ARTR3', 'ASSM3', 'ASSM4', 'ASTA4', 'FTRX3', 'FTRX4', 'GAFP3', 'GAFP4', 'GALO3', 'AZUL4', 'BAHI11', 'BAHI3', 'BAHI4', 'BAHI5', 'BBRK3', 'BBTG11', 'BBTG12', 'BBTG13', 'GALO4', 'BDLL3', 'BDLL4', 'BECE3', 'BECE4', 'GBIO33', 'GEPA3', 'GEPA4', 'GETI3', 'BERG3', 'GETI4', 'GGBR3', 'GGBR4', 'GNDI3', 'BHGR3', 'BICB3', 'BICB4', 'BIOM3', 'BIOM4', 'BISA3', 'BMEF3', 'GOAU3', 'GOAU4', 'GOLL4', 'BNCA3', 'BOBR3', 'BOBR4', 'BOVH3', 'BPHA3', 'GPCP3', 'GRND3', 'BRFS3', 'GRNL4', 'BRIN3', 'GUAR3', 'GUAR4', 'GVTT3', 'HAPV3', 'BRPR3', 'HGTX3', 'BRTP3', 'BRTP4', 'HGTX4', 'HOOT4', 'HYPE3', 'BSEV3', 'BSGR3', 'BTOW3', 'BTTL3', 'BTTL4', 'IDNT3', 'IGBR3', 'CAFE3', 'CAFE4', 'CALI3', 'IGBR5', 'IGBR6', 'CASN3', 'IGTA3', 'IGUA3', 'IGUA5', 'CCHI3', 'CCHI4', 'CCIM3', 'IGUA6', 'CCXC3', 'ILLS4', 'ILMD3', 'ILMD4', 'IMCH3', 'INEP3', 'INEP4', 'ITSA3', 'ITSA4', 'ITUB3', 'ITUB4', 'CGOS3', 'CGOS4', 'JBDU3', 'JBDU4', 'CLAN3', 'CLAN4', 'JBSS3', 'JFAB4', 'JHSF3', 'CMMA4', 'JOPA3', 'CNTO3', 'JOPA4', 'JPSA3', 'JSLG3', 'KEPL3', 'KROT11', 'CPFP4', 'CPNY3', 'KROT3', 'KROT4', 'CRBM3', 'CRBM7', 'CRDE3', 'KSSA3', 'LAME3', 'LAME4', 'LATS3', 'LCAM3', 'LCSA3', 'LCSA4', 'LETO3', 'LETO5', 'LEVE3', 'LEVE4', 'LIGH3', 'LIGT3', 'LINX3', 'LIPR3', 'LLIS3', 'LOGG3', 'LOGN3', 'LREN3', 'LREN4', 'LUXM3', 'LUXM4', 'MAGS3', 'MAPT3', 'MAPT4', 'MARI3', 'DFVA3', 'DFVA4', 'MDIA3', 'MEAL3', 'DJON4', 'MEND5', 'MEND6', 'MERC3', 'MERC4', 'MGEL3', 'MGEL4', 'MGLU3', 'DUFB11', 'MILK33', 'MLFT4', 'MLPA12', 'MLPA3', 'MLPA4', 'MMAQ3', 'MMAQ4', 'MMXM3', 'EBTP3', 'EBTP4', 'MNPR3', 'MNPR4', 'MNSA3', 'MNSA4', 'MOAR3', 'MOVI3', 'ELPL3', 'ELPL4', 'ELPL5', 'ELPL6', 'MPLU3', 'MRFG3', 'MRSL3', 'MRSL4', 'MRVE3', 'MSAN3', 'MSAN4', 'MTBR3', 'MTBR4', 'MTIG3', 'MTIG4', 'MTSA4', 'MULT3', 'EVEN3', 'MWET3', 'MWET4', 'FBRA4', 'MYPK3', 'MYPK4', 'NAFG3', 'NAFG4', 'NATU3', 'NEOE3', 'NEOE3', 'NETC3', 'NETC4', 'NORD3', 'NUTR3', 'ODPV3', 'OFSA3', 'OMGE3', 'OSAO4', 'OSXB3', 'PALF11', 'PALF3', 'PALF5', 'PARD3', 'PATI3', 'GAZO3', 'GAZO4', 'PATI4', 'PCAR3', 'PCAR4', 'GFSA3', 'GLOB4', 'PCAR5', 'GPIV33', 'PDGR3', 'PEAB3', 'HAGA3', 'HAGA4', 'HBOR3', 'HETA3', 'HETA4', 'PEAB4', 'PETR3', 'ICPI3', 'PETR4', 'IDVL11', 'IDVL3', 'IDVL4', 'IENG3', 'IENG5', 'PLAS3', 'PLIM4', 'PLTO5', 'PLTO6', 'PMET3', 'PMET5', 'PMET6', 'PNVL3', 'PNVL4', 'IMBI3', 'IMBI4', 'POMO3', 'POMO4', 'POPR4', 'INHA3', 'ITEC3', 'IVTT3', 'PQUN3', 'PQUN4', 'PRBC3', 'JFEN3', 'PRBC4', 'PRIO3', 'PRTX3', 'LATM11', 'PSSA3', 'PTBL3', 'PTBL4', 'LECO3', 'LECO4', 'PTNT3', 'PTNT4', 'PTPA3', 'LFFE3', 'LFFE4', 'LGLO4', 'PTPA4', 'LIQO3', 'LIXC3', 'LIXC4', 'PTQS4', 'LPSB3', 'QUAL3', 'LUPA3', 'RADL3', 'MAGG3', 'RAIA3', 'RAIL3', 'RANI3', 'RANI4', 'MEDI3', 'RAPT3', 'RAPT4', 'RCSL4', 'RDCD3', 'RDTR3', 'REDE3', 'MILS3', 'REDE4', 'REEM4', 'RENT3', 'REPA3', 'REPA4', 'RGEG3', 'MNDL3', 'MNDL4', 'RHDS3', 'RHDS4', 'RLOG3', 'RNEW11', 'RNEW3', 'RNEW4', 'RNPT3', 'RNPT4', 'ROMI3', 'ROMI4', 'RPSA4', 'RSID3', 'RSIP3', 'RSIP4', 'SALM3', 'SALM4', 'SANB11', 'SANB3', 'OGXP3', 'OIBR3', 'OIBR4', 'SANB4', 'SAPR11', 'SAPR3', 'SAPR4', 'SBSP3', 'SCAR3', 'SCAR4', 'SEBB11', 'PEFX3', 'PEFX5', 'PFRM3', 'PINE3', 'PINE4', 'PITI4', 'SEBB3', 'PLDN4', 'SEBB4', 'SEER3', 'SFSA3', 'PMAM3', 'PMAM4', 'SFSA4', 'SGPS3', 'SHUL4', 'PNOR5', 'PNOR6', 'SLCE3', 'PORP4', 'POSI3', 'SMLE3', 'SMLS3', 'SMTO3', 'SNSY5', 'PRGA4', 'SOND3', 'PRML3', 'SOND5', 'PRVI3', 'SOND6', 'PTIP3', 'PTIP4', 'SQIA3', 'SSBR3', 'STRP4', 'SUBA3', 'SULA11', 'SULA3', 'RCTB31', 'RCTB33', 'RCTB41', 'RCTB42', 'SULA4', 'RDNI3', 'SULT3', 'SULT4', 'TAEE11', 'TAEE3', 'TAEE4', 'TARP11', 'TBLE5', 'TBLE6', 'RIPI3', 'RIPI4', 'RJCP3', 'TCOC3', 'TCOC4', 'TCSL4', 'TECN3', 'TEFC11', 'TEKA3', 'TEKA4', 'RPAD3', 'RPAD6', 'RPMG3', 'RPMG4', 'TEMP3', 'TEND3', 'TENE5', 'TENE7', 'RSUL4', 'TGMA3', 'TIET11', 'SASG3', 'TIET3', 'SCLO3', 'SCLO4', 'SDIA3', 'SDIA4', 'TIET4', 'TIMP3', 'TKNO4', 'SEDU3', 'SEMP3', 'TMAR3', 'TMAR5', 'SGEN3', 'SGEN4', 'TMAR6', 'SJOS3', 'SJOS4', 'SLCP3', 'SLED3', 'SLED4', 'TMCP3', 'TMCP4', 'SPRI3', 'SPRI5', 'SPRI6', 'STBP11', 'TMGC11', 'TMGC12', 'TMGC13', 'TMGC3', 'SUZA4', 'SUZB5', 'SUZB6', 'SZPQ4', 'TAMM3', 'TAMM4', 'TANC4', 'TMGC7', 'TNCP3', 'TNCP4', 'TCNO3', 'TCNO4', 'TNEP3', 'TNEP4', 'TCSA3', 'TNLP3', 'TDBH3', 'TDBH4', 'TNLP4', 'TOTS3', 'TOYB3', 'TOYB4', 'TELB3', 'TELB4', 'TPRC3', 'TPRC6', 'TRFO3', 'TERI3', 'TESA3', 'TRFO4', 'TLCP3', 'TLCP4', 'TRIS3', 'TROR3', 'TROR4', 'TRPL3', 'TRPL4', 'TRPN3', 'TSEP3', 'TSEP4', 'TSPP3', 'TSPP4', 'TUPY3', 'TUPY4', 'TVIT3', 'UBBR11', 'UBBR3', 'UBBR4', 'UCAS3', 'UCOP4', 'TPIS3', 'UGPA3', 'UGPA4', 'UNIP3', 'UNIP5', 'UNIP6', 'UOLL4', 'USIM3', 'USIM5', 'USIM6', 'VAGV3', 'VAGV4', 'VALE3', 'TXRX3', 'TXRX4', 'VALE5', 'VCPA4', 'VIGR3', 'VINE3', 'VINE5', 'VIVO3', 'VIVO4', 'VIVT3', 'VIVT4', 'VLID3', 'VNET3', 'VGOR3', 'VGOR4', 'VPTA3', 'VPTA4', 'VTLM3', 'VULC3', 'VULC4', 'VIVR3', 'WEGE3', 'VPSC3', 'VPSC4', 'WEGE4', 'WHRL3', 'WHRL4', 'WISA3', 'WISA4', 'VVAR11', 'VVAR3', 'VVAR4', 'VVAX3', 'VVAX4', 'WIZS3', 'WLMM3', 'WLMM4', 'WSON33', 'WMBY3']
# stocks = ['PETR4', 'VALE3', 'BIDI4', 'ABEV3', 'MGLU3', 'AALR3', 'GSHP3', 'ABCB3', 'ABCB4', 'BPAT33', 'ABEV3', 'ACES3', 'ACES4', 'ADHM3', 'AEDU11', 'AEDU3', 'AESL3', 'AESL4', 'AFLT3', 'AFLU3', 'AFLU5', 'AGIN3', 'AGRO3', 'ALBA3', 'ALLL11', 'ALLL3', 'ALLL4', 'ALPA3', 'ALPA4', 'ALSC3', 'ALUP11', 'ALUP3', 'BBSE3', 'ALUP4', 'AMAR3', 'AMBV3', 'AMBV4', 'AMPI3', 'DIRR3', 'ANIM3']
# stocks = ['BRIN3', 'PETR4', 'VALE3', 'BIDI4', 'ABEV3', 'MGLU3']
headers = ['Papel', 'Ult_Vl_Cotação', 'Tipo', 'Dt_ult_cot', 'Nome_Empresa', 'Min_52_ sem', 'Setor', 'Max_52_sem', 'Subsetor',  'Vol_med_neg', 'Vlr_de_mercado', 'dt_ult_balan', 'Vlr_firma', 'Nro_Acoes', 'Osc_dia', 'preco_lucro', 'Lucro_Acao', 'Osc_Mes', 'Preco_vlr_patr', 'Vlr_patr_acao', 'Osc_30_dias', 'Prec_acao_EBIT', 'Marg_Bruta', 'Osc_12_meses', 'Price_sales_ratio', 'Marg_EBIT', 'Osc_2019', 'Prec_por_ativo', 'Marg_Liquida', 'Osc_2018', 'Prec_cap_giro',
           'EBIT_Ativo', 'Osc_2017', 'Prec_Ativ_Circ_Liq', 'ROIC', 'Osc_2016', 'Div_Yield', 'ROE', 'Osc_2015', 'Vlr_firma_EBIT', 'Liquidez_Corr', 'Osc_2014', 'Rec_liq_ativ_tot', 'Div_bruta_div_patr', 'Branco1', 'Cres_Rec_liq_5anos', 'branco2', 'Ativo', 'Div_Bruta', 'Disponibilidades', 'Div_liquida', 'Ativo_Circulante', 'Patrim. Líq', 'Receita_liquida_12meses', 'Receita_liquida_03meses', 'ebit_12meses', 'ebit_03meses', 'Lucro_liquido_12meses', 'Lucro_liquido_03meses']
dropar = ['Dt_ult_cot', 'Vol_med_neg', 'dt_ult_balan', 'Vlr_firma', 'Nro_Acoes', 'Vlr_de_mercado', 'preco_lucro', 'Vlr_patr_acao', 'Prec_acao_EBIT', 'Lucro_Acao', 'Marg_Bruta', 'Price_sales_ratio', 'Marg_EBIT', 'Prec_por_ativo', 'Marg_Liquida', 'Prec_cap_giro', 'EBIT_Ativo', 'Prec_Ativ_Circ_Liq',
          'Vlr_firma_EBIT', 'Liquidez_Corr', 'Rec_liq_ativ_tot', 'Branco1', 'branco2', 'Ativo', 'Div_Bruta', 'Disponibilidades', 'Div_liquida', 'Ativo_Circulante', 'Patrim. Líq', 'Receita_liquida_12meses', 'Receita_liquida_03meses', 'ebit_12meses', 'ebit_03meses', 'Lucro_liquido_12meses', 'Lucro_liquido_03meses']

reord = ['Papel', 'ROE', 'Div_Yield', 'Preco_vlr_patr', 'Div_bruta_div_patr', 'Cres_Rec_liq_5anos', 'Ult_Vl_Cotação', 'Min_52_ sem', 'Max_52_sem', 'Osc_dia', 'Osc_Mes', 'Osc_30_dias',
         'Osc_12_meses', 'Osc_2019', 'Osc_2018', 'Osc_2017', 'Osc_2016', 'Osc_2015', 'Osc_2014', 'ROIC', 'Tipo', 'Nome_Empresa', 'Setor', 'Subsetor', 'ult_cot']


stck_data = []


def get_fundamentus():

    planilha = pd.DataFrame(data=None, columns=headers)

    for idx, stock in enumerate(stocks, start=1):
        '''
        http://www.fundamentus.com.br/detalhes.php?papel=
        '''
        url = 'http://www.fundamentus.com.br/detalhes.php?papel=' + stock
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        stck_data.clear()
        for tb in soup.find_all('table'):
            table = tb
            table_rows = table.find_all('tr')

            for tr in table_rows:
                td = tr.find_all('td', 'data')
                for item in td:
                    # print(item.text)
                    a = item.text.strip('\n')
                    b = a.strip('%')
                    stck_data.append(b.strip())

        if len(stck_data) > 0:
            print(f'{idx} - {stock}')
            planilha.loc[len(planilha)] = stck_data

    if len(planilha.index) > 0:
        planilha.to_csv('dados.csv', index=False, sep=';')
        return planilha
    else:
        return None


def get_csv():
    if os.path.isfile('dados.csv'):
        # carregar e gerar um pd.df
        planilha = pd.read_csv('dados.csv', sep=';')
        return planilha
    else:
        return None


# escolher carregar os dados do csv ou buscar novos dados.
planilha = get_fundamentus()
# planilha = get_csv()

if planilha is not None:
    # print(planilha)
    # planilha.to_excel('teste2.xlsx', index=False)

    # filtra apenas as linhas que tem data de cotacao
    # planilha = planilha.loc[planilha['Dt_ult_cot'].dt.date == ontem]
    planilha = planilha.loc[planilha['Dt_ult_cot'] == ontem]

    # # converter a coluna ultima cotacao para date
    planilha['Dt_ult_cot'] = pd.to_datetime(
        planilha['Dt_ult_cot'], dayfirst=True, errors='coerce', format='%d/%m/%Y')

    # apenas a porcao data
    planilha['ult_cot'] = planilha['Dt_ult_cot'].dt.strftime('%d/%m/%Y')

    planilha.drop(columns=dropar, axis=1, inplace=True)
    planilha = planilha[reord]
    planilha.to_excel('stocks.xlsx', index=False)

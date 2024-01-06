--select * from TFICHA
--select * from TFICHA_CONTAS
--select * from TFICHA_END_COBRA
--select * from TFICHA_END_ENTREGA

--select * from VRELGSB_FIS_DANFE -- View de dados DANFE
--select * from VRELGSB_FIS_DANFE_ITEM -- View de dados DANFE, 
--select * from VRELGSB_FIS_NF_TRIB -- View de dados Tributarios, 

--select * from tnf_compra
--select * from tnf_compra_itens
--select * from tnf_compra_trib

--select * from tnf_venda
--select * from tnf_venda_itens
--select * from tnf_venda_trib

--select * from tnatur
--select * from ttipo_imposto
--select * from tcb_toc_desc




select 'b1c3543f-d051-4111-ae96-9a5c53058104' /*ven do ini*/ as unit_id, 
t1.zuuid as id,
t1.fantasia as nome,  
t1.razao as razao_social,   
decode(t1.desativado,'N','S','S') as ativo, 
tirar_acentos(t1.cgc) as doc_cnpj,  
tirar_acentos(t1.cpf) as doc_cpf, 
tirar_acentos(t1.ins_est) as doc_ie,  
t1.ins_mun as doc_im,
'10'||trim(to_char(t1.cod_nr,'000000')) as sigla_pes
from tficha t1

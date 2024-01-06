--select * from fnind_valores('f3996813-838e-49af-9649-8dc44e24bc75','30f96759-2081-4bb3-acfd-121c8f7215e0','','','','N','ANO','2014-01-01','2014-12-31','0','%')
Drop FUNCTION IF EXISTS fnind_valores;
CREATE OR REPLACE FUNCTION fnind_valores(
pparunitid varchar, 
ppargerempresaid varchar default null,
pparindgrupoid varchar default null,
pparindsubgrupoid varchar default null,
pparindid varchar default null,
pparindvrhist varchar default 'N', 
ppargerpertipo varchar default null, 
pparinddtini varchar default null,
pparinddtfin varchar default null,
pparindfaixameta varchar default '0',
pparindaprovexib varchar default 'S'
)
RETURNS TABLE(
 unit_id varchar,
 ind_id	varchar,	
 ind_sigla_ind	varchar,	
 ind_nome	varchar,	
 ind_casas_dec	int4,
 ind_campo_ordenacao	varchar,	
 ind_metodo_ordenacao	int4,
 ind_totalizador_atributo	int4,	
 ind_tipo_acumulo	int4	,
 ind_ind_id_ponderacao	varchar	,
 ind_grafico_tipo_atributo	int4	,
 ind_grafico_valor_vazio_zero	varchar	,
 ind_grafico_tipo_ind	int4	,
 ind_ger_umedida_id	varchar	,
 ind_tipo_meta	int4	,
 ind_faixa_meta_vr_01	float8	,
 ind_faixa_meta_vr_02	float8	,
 ind_faixa_meta_vr_03	float8	,
 ind_faixa_meta_vr_04	float8	,
 ind_faixa_meta_vr_05	float8	,
 ind_faixa_meta_cor_01	varchar,
 ind_faixa_meta_cor_02	varchar,
 ind_faixa_meta_cor_03	varchar,
 ind_faixa_meta_cor_04	varchar,
 ind_faixa_meta_cor_05	varchar,
 ind_observacao	varchar, 
 ger_empresa_id	varchar,
 ger_empresa_nome	varchar,
 ger_empresa_sigla 	varchar,
 ger_per_id	varchar,
 atributo	varchar,
 valor_real	numeric,
 valor_meta	numeric,
 aprovado_exibicao	varchar,
 ordem	int4,
 ger_per_tipo varchar
 ) AS $BODY$
DECLARE


--pparindvrhist: S/N Traz valor apenas ou historio do indicador, para isso o pparindid é necessário (Escolha Binaria)
--ppargerpertipo: DIA,SEMANA,QUINZENA,MES,BIMESTRE,SEMESTRE,ANO para tabelas ind_vr_dia .. ano (Multiplo escolha)
--pparindfaixameta: Retorna apenas linhas que estão nessa faixas 0-Todos, 1..5 o desvio (Multiplo escolha)
--pparindaprovexib: %/S/N apenas valores que traz aprovados para exibição

vSql varchar;
vPar1 varchar :='';
r record;
begin
	
	--Exemplo
	if ppargerpertipo != '' THEN
		vPar1 = vPar1||'Tipo Período ['||ppargerpertipo||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'Tipo Período [] '||chr(13)||chr(10);
	end if;
	
    --Exemplo
    if ppargerempresaid != '' then
	   vPar1 := vPar1||'Empresa ['||fnreport_sigla(pParUnitId,'ger_empresa','sigla_empresa','id',''''||ppargerempresaid||'''')||'] '||chr(13)||chr(10);
    else
	   vPar1 := vPar1||'Empresa []'||chr(13)||chr(10);
    end if;


	vSql = 'select 
	 v2.unit_id ,
	 v1.id,
	 v1.sigla_ind,
	 v1.nome,
	 v1.casas_dec,
	 v1.campo_ordenacao,
	 v1.metodo_ordenacao,
	 v1.totalizador_atributo,
	 v1.tipo_acumulo,
	 v1.ind_id_ponderacao,
	 v1.grafico_tipo_atributo,
	 v1.grafico_valor_vazio_zero,
	 v1.grafico_tipo_ind,
	 v1.ger_umedida_id,
	 v1.tipo_meta,
	 v1.faixa_meta_vr_01,
	 v1.faixa_meta_vr_02,
	 v1.faixa_meta_vr_03,
	 v1.faixa_meta_vr_04,
	 v1.faixa_meta_vr_05,
	 v1.faixa_meta_cor_01,
	 v1.faixa_meta_cor_02,
	 v1.faixa_meta_cor_03,
	 v1.faixa_meta_cor_04,
	 v1.faixa_meta_cor_05,
	 v1.observacao, 
	 v2.ger_empresa_id,
	 v3.nome as ger_empresa_nome,
	 v3.sigla_empresa as ger_empresa_sigla ,
	 v2.ger_per_id,
	 v2.atributo,
	 v2.valor_real,
	 v2.valor_meta,
	 v2.aprovado_exibicao,
	 v2.ordem
	 from ind v1
	   join ind_vr_'||ppargerpertipo|| ' v2 on (v1.id = v2.ind_id )
	   join ger_empresa v3 on(v3.id = v2.ger_empresa_id)
	   join ger_per v4 on(v4.id = v2.ger_per_id)
	where v2.unit_id =''' ||pParUnitId||'''
	 and v4.'||ppargerpertipo||'_tipo = ''S''
	 and v4.ano_numero = ''2014''
	 and CAST(v4.data_dia_inicial AS DATE)' || ' >= ''' || pparinddtini|| ''' and  CAST(v4.data_dia_inicial AS DATE)' || ' <= ''' || pparinddtfin || '''';
	 
	
		
		if ppargerempresaid != '' then
			vSql = vSql || ' and v2.ger_empresa_id in ('||'''' ||ppargerempresaid||''')';
		end if;
	
		
	
	FOR r IN EXECUTE vSql loop
		unit_id := r.unit_id;
		ind_id	:= r.id;	
		ind_sigla_ind	:= r.sigla_ind;	
		ind_nome	:= r.nome;	
		ind_casas_dec	:= r.casas_dec;
		ind_campo_ordenacao	:= r.campo_ordenacao;	
		ind_metodo_ordenacao	:= r.metodo_ordenacao;
		ind_totalizador_atributo	:= r.totalizador_atributo;	
		ind_tipo_acumulo	:= r.tipo_acumulo	;
		ind_ind_id_ponderacao	:= r.ind_id_ponderacao	;
		ind_grafico_tipo_atributo	:= r.grafico_tipo_atributo	;
		ind_grafico_valor_vazio_zero	:= r.grafico_valor_vazio_zero	;
		ind_grafico_tipo_ind	:= r.grafico_tipo_ind	;
		ind_ger_umedida_id	:= r.ger_umedida_id	;
		ind_tipo_meta	:= r.tipo_meta	;
		ind_faixa_meta_vr_01	:= r.faixa_meta_vr_01;
		ind_faixa_meta_vr_02	:= r.faixa_meta_vr_02;
		ind_faixa_meta_vr_03	:= r.faixa_meta_vr_03;
		ind_faixa_meta_vr_04	:= r.faixa_meta_vr_04;
		ind_faixa_meta_vr_05	:= r.faixa_meta_vr_05;
		ind_faixa_meta_cor_01	:= r.faixa_meta_cor_01;
		ind_faixa_meta_cor_02	:= r.faixa_meta_cor_02;
		ind_faixa_meta_cor_03	:= r.faixa_meta_cor_03;
		ind_faixa_meta_cor_04	:= r.faixa_meta_cor_04;
		ind_faixa_meta_cor_05	:= r.faixa_meta_cor_05;
		ind_observacao	:= r.observacao; 
		ger_empresa_id	:= r.ger_empresa_id;
		ger_empresa_nome	:= r.ger_empresa_nome;
		ger_empresa_sigla 	:= r.ger_empresa_sigla;
		ger_per_id	:= r.ger_per_id;
		atributo	:= r.atributo;
		valor_real	:= r.valor_real;
		valor_meta	:= r.valor_meta;
		aprovado_exibicao	:= r.aprovado_exibicao;
		ger_per_tipo := ppargerpertipo;

	RETURN NEXT;
	
	END loop;



end;
$BODY$
LANGUAGE plpgsql VOLATILE;
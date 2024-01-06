-- DROP VIEW IF EXISTS vwger_pessoa;
CREATE OR REPLACE VIEW vwger_pessoa AS
SELECT gp.id as id_pessoa,
			 gp.nome as nome_pessoa,
			 gp.ativo as ativo_pessoa,
			 fnstd('SN', 'default',gp.ativo) as ativo_pessoa_desc,
			 gp.razao_social as razao_social_pessoa,
			 gp.doc_cnpj as doc_cnpj_pessoa,
			 gp.doc_cpf as doc_cpf_pessoa,
			 (case when gp.doc_cnpj is null then gp.doc_cpf ELSE gp.doc_cnpj end) as doc_cnpj_cpf_pessoa,
			 gp.sigla_pes as sigla_pes,
			 gpe.id as id_endereco,
			 gpe.end_logradouro as endereco,
			 gpe.end_logradouro_nr as endereco_numero,
			 gpe.end_cep as cep_endereco,
			 gc.id as id_cidade,
			 gc.nome as nome_cidade,
			 gUf.sigla_uf as uf_cidade
FROM ger_pessoa gp
Left Join ger_pessoa_endereco gpe
on gp.id = gpe.ger_pessoa_id
Left Join ger_cidade gc
on gpe.end_ger_cidade_id = gc.id
Inner join ger_uf gUf
on  gc.ger_uf_id = gUf.id
ORDER BY gp.id;
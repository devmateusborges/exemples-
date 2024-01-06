from alembic import op

revision = "202206151339032"
down_revision = "202206151339031"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
ALTER TABLE ger_itemserv_lote ADD ger_itemserv_id varchar(36) NULL;
ALTER TABLE ger_itemserv_lote ADD CONSTRAINT fk_ger_itemserv_lote_ger_itemserv_id FOREIGN KEY (ger_itemserv_id) REFERENCES ger_itemserv(id) ON DELETE CASCADE;

Drop FUNCTION IF EXISTS fnsystem_psql_result;
Drop FUNCTION IF EXISTS fnsys_program_acesso;
CREATE OR REPLACE FUNCTION fnsys_program_acesso(
pvSysId varchar,
pvUserLogin varchar, 
pvSysProgramAdmin varchar, 
pvSysProgramMenu varchar
)
RETURNS TABLE(
sys_program_id varchar,
sys_program_name varchar,
sys_program_controller varchar,
sys_program_type_program varchar,
sys_program_icon varchar,
sys_module_id varchar,
sys_module_name varchar,
sys_module_icon varchar,
sys_module_sigla_module varchar,
sys_module_sigla_module_desc varchar,
sys_module_color varchar
) AS $BODY$
DECLARE
vSql varchar;
r record;
begin
	
			vSql = 'select distinct
								t1.id as sys_program_id,
								t1.name as sys_program_name,
								t1.controller as sys_program_controller,
								t1.type_program as sys_program_type_program,
								t1.icon as sys_program_icon,
								t1.sys_module_id,
								t2.name as sys_module_name,
								t2.icon as sys_module_icon,
								t2.sigla_module as sys_module_sigla_module,
								t2.sigla_module||''-''||t2.name as sys_module_sigla_module_desc,
								t2.color as sys_module_color
								from sys_program t1, 
										 sys_module  T2
								where t1.sys_module_id = t2.id
									and t1.menu = '''||pvSysProgramMenu||'''
									and t1.admin = '''||pvSysProgramAdmin||'''
									and t2.active = ''S''
									and t2.sys_id = '''||pvSysId||'''
									and (exists (select 1 
																from sys_group_program s1,
																		 sys_user_group s2,
																		 sys_user s3,
																		 sys_group s4
																where s1.sys_group_id = s2.sys_group_id
																	and s2.sys_user_id = s3.id
																	and s2.sys_group_id = s4.id
																	and s1.sys_program_id = t1.id
																	and s3.active= ''S''
																	and s4.active = ''S''
																	and s3.login = '''||pvUserLogin||'''	) 
											or exists 	(select 1 
																		 from sys_user_program x1,
																					sys_user x2
																	 where x1.sys_program_id = t1.id
																		 and x1.sys_user_id = x2.id
																		 and x2.active = ''S''
																		 and x2.login = '''||pvUserLogin||'''))
								order by t2.sigla_module, t1.type_program, t1.name';
   
	FOR r IN EXECUTE vSql loop
		sys_program_id               := r.sys_program_id;
		sys_program_name             := r.sys_program_name;
		sys_program_controller       := r.sys_program_controller;
		sys_program_type_program     := r.sys_program_type_program;
		sys_program_icon             := r.sys_program_icon;
		sys_module_id                := r.sys_module_id;
		sys_module_name              := r.sys_module_name;
		sys_module_icon              := r.sys_module_icon;
		sys_module_sigla_module      := r.sys_module_sigla_module;
		sys_module_sigla_module_desc := r.sys_module_sigla_module_desc;
		sys_module_color             := r.sys_module_color;
	RETURN NEXT;
	
	END loop;



end;
$BODY$
LANGUAGE plpgsql VOLATILE;

Drop FUNCTION IF EXISTS fnutil_result_Json;

Drop FUNCTION IF EXISTS fnutil_result_json_to_table;
CREATE OR REPLACE FUNCTION fnutil_result_json_to_table(pJson json)
  RETURNS table(code varchar, data varchar, name varchar, msg varchar) AS $BODY$
BEGIN
  RETURN QUERY
		SELECT * from json_to_record($1) as x(code varchar, data varchar, name varchar, msg varchar);
END;
$BODY$
  LANGUAGE plpgsql VOLATILE;

Drop FUNCTION IF EXISTS fnutil_result_json_create;
CREATE OR REPLACE FUNCTION fnutil_result_json_create(pncode numeric, pvdata json, pvname varchar, pvmsg varchar)
  RETURNS varchar AS $BODY$
declare
		vResult json;
begin
		select json_build_object(
						 'code',pncode,
						 'data', pvdata,
						 'name',pvname,
						 'msg', pvmsg) INTO vResult;
						 return vResult;
end;
$BODY$
  language plpgsql volatile;
  
  
Drop FUNCTION IF EXISTS fnsys_program_acesso;
CREATE OR REPLACE FUNCTION fnsys_program_acesso(
pvSysId varchar,
pvUserLogin varchar, 
pvSysProgramAdmin varchar, 
pvSysProgramMenu varchar,
pvSysProgramFavorite varchar
)
RETURNS TABLE(
sys_program_id varchar,
sys_program_name varchar,
sys_program_controller varchar,
sys_program_type_program varchar,
sys_program_icon varchar,
sys_module_id varchar,
sys_module_name varchar,
sys_module_icon varchar,
sys_module_sigla_module varchar,
sys_module_sigla_module_desc varchar,
sys_module_color varchar
) AS $BODY$
DECLARE
vSql varchar;
r record;
begin
	
			vSql = 'select distinct
								t1.id as sys_program_id,
								t1.name as sys_program_name,
								t1.controller as sys_program_controller,
								t1.type_program as sys_program_type_program,
								t1.icon as sys_program_icon,
								t1.sys_module_id,
								t2.name as sys_module_name,
								t2.icon as sys_module_icon,
								t2.sigla_module as sys_module_sigla_module,
								t2.sigla_module||''-''||t2.name as sys_module_sigla_module_desc,
								t2.color as sys_module_color
								from sys_program t1, 
										 sys_module  T2
								where t1.sys_module_id = t2.id
									and t1.menu = '''||pvSysProgramMenu||'''
									and t1.admin = '''||pvSysProgramAdmin||'''
									and t2.active = ''S''
									and t2.sys_id = '''||pvSysId||'''
									and (exists (select 1 
																from sys_group_program s1,
																		 sys_user_group s2,
																		 sys_user s3,
																		 sys_group s4
																where s1.sys_group_id = s2.sys_group_id
																	and s2.sys_user_id = s3.id
																	and s2.sys_group_id = s4.id
																	and s1.sys_program_id = t1.id
																	and s3.active= ''S''
																	and s4.active = ''S''
																	and s3.login = '''||pvUserLogin||'''	) 
											or exists 	(select 1 
																		 from sys_user_program x1,
																					sys_user x2
																	 where x1.sys_program_id = t1.id
																		 and x1.sys_user_id = x2.id
																		 and x2.active = ''S''
																		 and x2.login = '''||pvUserLogin||'''))';
																		 
								if pvSysProgramFavorite = 'S' then
                   vSql = vSql || 'and exists (select 1 
																		             from sys_program_favorite x1,
																					            sys_user x2
																								 where x1.sys_program_id = t1.id
																									 and x1.sys_user_id = x2.id
																									 and x2.active = ''S''
																									 and x2.login = '''||pvUserLogin||''')';
               end if;																		 
																		 
								vSql = vSql || 'order by t2.sigla_module, t1.type_program, t1.name';
   
	FOR r IN EXECUTE vSql loop
		sys_program_id               := r.sys_program_id;
		sys_program_name             := r.sys_program_name;
		sys_program_controller       := r.sys_program_controller;
		sys_program_type_program     := r.sys_program_type_program;
		sys_program_icon             := r.sys_program_icon;
		sys_module_id                := r.sys_module_id;
		sys_module_name              := r.sys_module_name;
		sys_module_icon              := r.sys_module_icon;
		sys_module_sigla_module      := r.sys_module_sigla_module;
		sys_module_sigla_module_desc := r.sys_module_sigla_module_desc;
		sys_module_color             := r.sys_module_color;
	RETURN NEXT;
	
	END loop;



end;
$BODY$
LANGUAGE plpgsql VOLATILE;


 
alter table sys_user_preference rename column	defaultd	to isdefault;
						



COMMENT ON TABLE ger_per_tipo IS 'Geral-Periodo Tipo';
COMMENT ON COLUMN ger_per_tipo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ger_per_tipo.id IS 'ID do Tipo Periodo';
COMMENT ON COLUMN ger_per_tipo.nome IS 'Nome';
COMMENT ON COLUMN ger_per_tipo.ativo IS 'Ativo: S-Sim, N-Não';
COMMENT ON COLUMN ger_per_tipo.sigla_per_tipo IS 'Sigla Tipo Periodo';
COMMENT ON COLUMN ger_per_tipo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_per_tipo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ger_per_tipo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_per_tipo.log_date_upd IS 'Log - Data de Alteração';					

alter table ger_per add ger_per_tipo_id varchar(36);
alter table ger_per add  CONSTRAINT fk_ger_per_ger_per_tipo_id FOREIGN KEY (ger_per_tipo_id) REFERENCES ger_per_tipo (id);

COMMENT ON COLUMN ger_per.ger_per_tipo_id IS 'ID do Tipo Periodo ';


create TABLE ind_vr_meta (
		unit_id varchar(36) NOT NULL,
		id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
		ger_per_id varchar(50) NOT NULL,
		ind_id varchar(36) NOT NULL,
		atributo varchar(100) NOT NULL,
		valor_meta numeric(18,6) NOT NULL DEFAULT 0,
		aprovado_exibicao varchar(1) NOT NULL,
		ger_empresa_id varchar(36) NOT NULL,
		log_user_ins varchar(100) NULL,
		log_date_ins timestamp(0) NULL DEFAULT now(),
		log_user_upd varchar(100) NULL,
		log_date_upd timestamp(0) NULL,
		ordem int4 NULL DEFAULT 0,
		CONSTRAINT pk_ind_vr_meta PRIMARY KEY (id),
		CONSTRAINT fk_ind_vr_meta_ger_empresa_id FOREIGN KEY (ger_empresa_id) REFERENCES ger_empresa(id),
		CONSTRAINT fk_ind_vr_meta_ger_per_id FOREIGN KEY (ger_per_id) REFERENCES ger_per(id),
		CONSTRAINT fk_ind_vr_meta_unit_id FOREIGN KEY (unit_id) REFERENCES sys_unit(id)
);

COMMENT ON TABLE ind_vr_meta IS 'Indicador-Valor Meta';
COMMENT ON COLUMN ind_vr_meta.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ind_vr_meta.id IS 'ID do Valor Meta';
COMMENT ON COLUMN ind_vr_meta.ordem IS 'Ordem';
COMMENT ON COLUMN ind_vr_meta.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN ind_vr_meta.ger_per_id IS 'ID do Período';
COMMENT ON COLUMN ind_vr_meta.ind_id IS 'ID do Indicador';
COMMENT ON COLUMN ind_vr_meta.atributo IS 'Atributo';
COMMENT ON COLUMN ind_vr_meta.valor_meta IS 'Valor da Meta';
COMMENT ON COLUMN ind_vr_meta.aprovado_exibicao IS 'Aprovado para Exibição';
COMMENT ON COLUMN ind_vr_meta.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ind_vr_meta.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ind_vr_meta.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ind_vr_meta.log_date_upd IS 'Log - Data de Alteração';		

alter table ind_vr_meta add import_id varchar(50) NULL;
alter table ind_vr_meta add import_arquivo varchar(100) NULL;
alter table ind_vr_ano add import_id varchar(50) NULL;
alter table ind_vr_ano add import_arquivo varchar(100) NULL;
alter table ind_vr_bimestre add import_id varchar(50) NULL;
alter table ind_vr_bimestre add import_arquivo varchar(100) NULL;
alter table ind_vr_dia add import_id varchar(50) NULL;
alter table ind_vr_dia add import_arquivo varchar(100) NULL;
alter table ind_vr_mes add import_id varchar(50) NULL;
alter table ind_vr_mes add import_arquivo varchar(100) NULL;
alter table ind_vr_quadrimestre add import_id varchar(50) NULL;
alter table ind_vr_quadrimestre add import_arquivo varchar(100) NULL;
alter table ind_vr_quinzena add import_id varchar(50) NULL;
alter table ind_vr_quinzena add import_arquivo varchar(100) NULL;
alter table ind_vr_semana add import_id varchar(50) NULL;
alter table ind_vr_semana add import_arquivo varchar(100) NULL;
alter table ind_vr_semestre add import_id varchar(50) NULL;
alter table ind_vr_semestre add import_arquivo varchar(100) NULL;
alter table ind_vr_trimestre add import_id varchar(50) NULL;
alter table ind_vr_trimestre add import_arquivo varchar(100) NULL;

COMMENT ON COLUMN ind_vr_meta.import_id is 'ID de importacao';
COMMENT ON COLUMN ind_vr_meta.import_arquivo is 'Nome arquivo de importacao';
COMMENT ON COLUMN ind_vr_ano.import_id is 'ID de importacao';
COMMENT ON COLUMN ind_vr_ano.import_arquivo is 'Nome arquivo de importacao';
COMMENT ON COLUMN ind_vr_bimestre.import_id is 'ID de importacao';
COMMENT ON COLUMN ind_vr_bimestre.import_arquivo is 'Nome arquivo de importacao';
COMMENT ON COLUMN ind_vr_dia.import_id is 'ID de importacao';
COMMENT ON COLUMN ind_vr_dia.import_arquivo is 'Nome arquivo de importacao';
COMMENT ON COLUMN ind_vr_mes.import_id is 'ID de importacao';
COMMENT ON COLUMN ind_vr_mes.import_arquivo is 'Nome arquivo de importacao';
COMMENT ON COLUMN ind_vr_quadrimestre.import_id is 'ID de importacao';
COMMENT ON COLUMN ind_vr_quadrimestre.import_arquivo is 'Nome arquivo de importacao';
COMMENT ON COLUMN ind_vr_quinzena.import_id is 'ID de importacao';
COMMENT ON COLUMN ind_vr_quinzena.import_arquivo is 'Nome arquivo de importacao';
COMMENT ON COLUMN ind_vr_semana.import_id is 'ID de importacao';
COMMENT ON COLUMN ind_vr_semana.import_arquivo is 'Nome arquivo de importacao';
COMMENT ON COLUMN ind_vr_semestre.import_id is 'ID de importacao';
COMMENT ON COLUMN ind_vr_semestre.import_arquivo is 'Nome arquivo de importacao';
COMMENT ON COLUMN ind_vr_trimestre.import_id is 'ID de importacao';
COMMENT ON COLUMN ind_vr_trimestre.import_arquivo is 'Nome arquivo de importacao';
  
Drop FUNCTION IF EXISTS fnutil_ExtraiValorArrayJson;  


Drop FUNCTION IF EXISTS fnger_per_gerar;
CREATE OR REPLACE FUNCTION fnger_per_gerar(
pvUnitId varchar,
pvGerEmpresaId varchar,
pvGerPerTipo varchar, 
pvAno varchar, 
pvSysId varchar
)
RETURNS varchar AS $BODY$
 declare
		vposicerro varchar(1000);
		vparam varchar(500);


		vAchou float := 0;
		vAtualizados float := 0;
		vInseridos float := 0;

		VdDataIni date;
		VdDataFin date;

		VdSemanaIni date;
		VdSemanaFin date;
		VdQuinzenaIni date;
		VdQuinzenaFin date;
		VdMesIni date;
		VdMesFin date;
		VdBimestreIni date;
		VdBimestreFin date;
		VdTrimestreIni date;
		VdTrimestreFin date;
		VdQuadrimestreIni date;
		VdQuadrimestreFin date;
		VdSemestreIni date;
		VdSemestreFin date;
		VdAnoIni date;
		VdAnoFin date;

		VdSemanaIniAnt date := To_date('30/01/'||pvAno,'DD/MM/YYYY');

		vnDiaNumero float;
		vnSemanaNumero float := 0;
		vnQuinzenaNumero float := 0;
		vnMesNumero float;
		vnBimestreNumero float := 0;
		vnTrimestreNumero float := 0;
		vnQuadrimestreNumero float := 0;
		vnSemestreNumero float := 0;
		vnAnoNumero float := 0;


		vvDiaNome varchar(50);
		vvSemanaNome varchar(50);
		vvQuinzenaNome varchar(50);
		vvMesNome varchar(50);
		vvBimestreNome varchar(50);
		vvTrimestreNome varchar(50);
		vvQuadrimestreNome varchar(50);
		vvSemestreNome varchar(50);
		vvAnoNome varchar(50);


		vvDiaTipo varchar(1) := 'N';
		vvSemanaTipo varchar(1) := 'N';
		vvQuinzenaTipo varchar(1) := 'N';
		vvMesTipo varchar(1) := 'N';
		vvBimestreTipo varchar(1) := 'N';
		vvTrimestreTipo varchar(1) := 'N';
		vvQuadrimestreTipo varchar(1) := 'N';
		vvSemestreTipo varchar(1) := 'N';
		vvAnoTipo varchar(1) := 'N';

		delCalend ger_per%rowtype;
		vResult json;
		vResultData json;
 begin
		vParam := 'Tipo Periodo['||pvGerPerTipo||'] Ano['||pvAno||'] ID Usuario['||pvSysId||']';

		VdDataIni := to_date('01/01/'||pvAno,'DD/MM/YYYY');
		VdDataFin := to_date('31/12/'||pvAno,'DD/MM/YYYY');

		vposicerro:='Apagando calendario para geracao do novo';
		for delCalend in (
			 select *
			 from ger_per t
			 where t.unit_id = pvUnitId
			 and t.ger_per_tipo_id = pvGerPerTipo
			 and t.data_dia_inicial between vdDataIni and vdDataFin
			 and not exists (select 1 from ind_vr_dia t1          where t1.ger_per_id  = t.id and t1.unit_id  = t.unit_id)
			 and not exists (select 1 from ind_vr_semana t2       where t2.ger_per_id  = t.id and t2.unit_id  = t.unit_id)
			 and not exists (select 1 from ind_vr_quinzena t3     where t3.ger_per_id  = t.id and t3.unit_id  = t.unit_id)
			 and not exists (select 1 from ind_vr_mes t4          where t4.ger_per_id  = t.id and t4.unit_id  = t.unit_id)
			 and not exists (select 1 from ind_vr_bimestre t5     where t5.ger_per_id  = t.id and t5.unit_id  = t.unit_id)
			 and not exists (select 1 from ind_vr_trimestre t6    where t6.ger_per_id  = t.id and t6.unit_id  = t.unit_id)
			 and not exists (select 1 from ind_vr_quadrimestre t7 where t7.ger_per_id  = t.id and t7.unit_id  = t.unit_id)
			 and not exists (select 1 from ind_vr_semestre t8     where t8.ger_per_id  = t.id and t8.unit_id  = t.unit_id)
			 and not exists (select 1 from ind_vr_ano t9          where t9.ger_per_id  = t.id and t9.unit_id  = t.unit_id)
			 and not exists (select 1 from ind_vr_meta t10        where t10.ger_per_id = t.id and t10.unit_id = t.unit_id)
		)
		loop
		begin
			 delete
					from ger_per t
			 where t.id  = delCalend.id
					and t.unit_id     = delCalend.unit_id;

			 exception
			 when others then
					null;
			 end;
		end loop;



		while vdDataIni <= vdDataFin
		loop
			 vposicerro:='Numero do Dia';
			 vnDiaNumero := EXTRACT(DAY FROM vdDataIni);
			 vvDiaNome :=  trim(to_char(vdDataIni,'DD/MM/YYYY'));
			 vvDiaTipo := 'S';

			 vposicerro:='Recuperando periodo: Semana';
			 VdSemanaIni := fnutil_ini_fim_semana(pvGerPerTipo, vdDataIni, 0);
			 VdSemanaFin := fnutil_ini_fim_semana(pvGerPerTipo, vdDataIni, 1);
			 -- Numero da semana
			 if VdSemanaIniAnt <> VdSemanaIni then
				 VnSemanaNumero := VnSemanaNumero + 1;
			 end if;
			 VdSemanaIniAnt := VdSemanaIni;
			 vvSemanaNome := trim(to_char(vdDataIni,'YYYY'))||'/'||trim(to_char(vdDataIni,'MM'))||'-'||'SM'||trim(to_char(VnSemanaNumero,'00'));
			 if VdSemanaFin = vdDataIni then
			 vvSemanaTipo := 'S';
			 else
			 vvSemanaTipo := 'N';
			 end if;



			 vposicerro:='Recuperando periodo: Quinzena';
			 if EXTRACT(DAY FROM vdDataIni) <= 15 then
				 VdQuinzenaIni := to_date('01/' || to_char(vdDataIni,'MM/YYYY'),'DD/MM/YYYY');
				 VdQuinzenaFin := to_date('15/' || to_char(vdDataIni,'MM/YYYY'),'DD/MM/YYYY');
				 vvQuinzenaNome := trim(to_char(vdDataIni,'YYYY'))||'/'||trim(to_char(vdDataIni,'MM'))||'-1QZ';
			 else
				 VdQuinzenaIni := to_date('16/' || to_char(vdDataIni,'MM/YYYY'),'DD/MM/YYYY');
				 VdQuinzenaFin := to_date(to_char(fnutil_last_day(vdDataIni),'DD') ||'/'|| to_char(vdDataIni,'MM/YYYY'),'DD/MM/YYYY');
				 vvQuinzenaNome := trim(to_char(vdDataIni,'YYYY'))||'/'||trim(to_char(vdDataIni,'MM'))||'-2QZ';
			 end if;
			 if VdQuinzenaIni = vdDataIni then
			 vvQuinzenaTipo := 'S';
			 vnQuinzenaNumero := vnQuinzenaNumero + 1;
			 else
			 vvQuinzenaTipo := 'N';
			 end if;

			 vposicerro:='Recuperando periodo: Mes';
			 VdMesIni := to_date('01/' || to_char(vdDataIni,'MM/YYYY'),'DD/MM/YYYY');
			 VdMesFin := to_date(to_char(fnutil_last_day(vdDataIni),'DD') ||'/'|| to_char(vdDataIni,'MM/YYYY'),'DD/MM/YYYY');
			 vvMesNome := trim(to_char(vdDataIni,'YYYY'))||'/'||trim(to_char(vdDataIni,'MM'));
			 vnMesNumero := EXTRACT(MONTH FROM vdDataIni);
			 if VdMesIni = vdDataIni then
			 vvMesTipo := 'S';
			 else
			 vvMesTipo := 'N';
			 end if;

			vposicerro:='Recuperando periodo: Bimestre';
			if EXTRACT(MONTH FROM vdDataIni) >= 1 and EXTRACT(MONTH FROM vdDataIni) <= 2 then
				 VdBimestreIni := to_date('01/01/' || pvAno, 'DD/MM/YYYY');
				 VdBimestreFin := fnutil_last_day(to_date('01/02/' || pvAno, 'DD/MM/YYYY'));
				 vvBimestreNome := trim(to_char(vdDataIni,'YYYY'))||'/'||trim(to_char(vdDataIni,'MM'))||'-1BI';
			elsif EXTRACT(MONTH FROM vdDataIni) >= 3 and EXTRACT(MONTH FROM vdDataIni) <= 4 then
				 VdBimestreIni := to_date('01/03/' || pvAno, 'DD/MM/YYYY');
				 VdBimestreFin := fnutil_last_day(to_date('01/04/' || pvAno, 'DD/MM/YYYY'));
				 vvBimestreNome := trim(to_char(vdDataIni,'YYYY'))||'/'||trim(to_char(vdDataIni,'MM'))||'-2BI';
			elsif EXTRACT(MONTH FROM vdDataIni) >= 5 and EXTRACT(MONTH FROM vdDataIni) <= 6 then
				 VdBimestreIni := to_date('01/05/' || pvAno, 'DD/MM/YYYY');
				 VdBimestreFin := fnutil_last_day(to_date('01/06/' || pvAno, 'DD/MM/YYYY'));
				 vvBimestreNome := trim(to_char(vdDataIni,'YYYY'))||'/'||trim(to_char(vdDataIni,'MM'))||'-3BI';
			elsif EXTRACT(MONTH FROM vdDataIni) >= 7 and EXTRACT(MONTH FROM vdDataIni) <= 8 then
				 VdBimestreIni := to_date('01/07/' || pvAno, 'DD/MM/YYYY');
				 VdBimestreFin := fnutil_last_day(to_date('01/08/' || pvAno, 'DD/MM/YYYY'));
				 vvBimestreNome := trim(to_char(vdDataIni,'YYYY'))||'/'||trim(to_char(vdDataIni,'MM'))||'-4BI';
			elsif EXTRACT(MONTH FROM vdDataIni) >= 9 and EXTRACT(MONTH FROM vdDataIni) <= 10 then
				 VdBimestreIni := to_date('01/09/' || pvAno, 'DD/MM/YYYY');
				 VdBimestreFin := fnutil_last_day(to_date('01/10/' || pvAno, 'DD/MM/YYYY'));
				 vvBimestreNome := trim(to_char(vdDataIni,'YYYY'))||'/'||trim(to_char(vdDataIni,'MM'))||'-5BI';
			elsif EXTRACT(MONTH FROM vdDataIni) >= 11 and EXTRACT(MONTH FROM vdDataIni) <= 12 then
				 VdBimestreIni := to_date('01/11/' || pvAno, 'DD/MM/YYYY');
				 VdBimestreFin := fnutil_last_day(to_date('01/12/' || pvAno, 'DD/MM/YYYY'));
				 vvBimestreNome := trim(to_char(vdDataIni,'YYYY'))||'/'||trim(to_char(vdDataIni,'MM'))||'-6BI';
			end if;
			 if VdBimestreIni = vdDataIni then
			 vvBimestreTipo := 'S';
			 vnBimestreNumero := vnBimestreNumero + 1;
			 else
			 vvBimestreTipo := 'N';
			 end if;

			vposicerro:='Recuperando periodo: Trimestre';
			if EXTRACT(MONTH FROM vdDataIni) >= 1 and EXTRACT(MONTH FROM vdDataIni) <= 3 then
				 VdTrimestreIni := to_date('01/01/' || pvAno, 'DD/MM/YYYY');
				 VdTrimestreFin := fnutil_last_day(to_date('01/03/' || pvAno, 'DD/MM/YYYY'));
				 vvTrimestreNome := trim(to_char(vdDataIni,'YYYY'))||'/'||trim(to_char(vdDataIni,'MM'))||'-1TR';
			elsif EXTRACT(MONTH FROM vdDataIni) >= 4 and EXTRACT(MONTH FROM vdDataIni) <= 6 then
				 VdTrimestreIni := to_date('01/04/' || pvAno, 'DD/MM/YYYY');
				 VdTrimestreFin := fnutil_last_day(to_date('01/06/' || pvAno, 'DD/MM/YYYY'));
				 vvTrimestreNome := trim(to_char(vdDataIni,'YYYY'))||'/'||trim(to_char(vdDataIni,'MM'))||'-2TR';
			elsif EXTRACT(MONTH FROM vdDataIni) >= 7 and EXTRACT(MONTH FROM vdDataIni) <= 9 then
				 VdTrimestreIni := to_date('01/07/' || pvAno, 'DD/MM/YYYY');
				 VdTrimestreFin := fnutil_last_day(to_date('01/09/' || pvAno, 'DD/MM/YYYY'));
				 vvTrimestreNome := trim(to_char(vdDataIni,'YYYY'))||'/'||trim(to_char(vdDataIni,'MM'))||'-3TR';
			elsif EXTRACT(MONTH FROM vdDataIni) >= 10 and EXTRACT(MONTH FROM vdDataIni) <= 12 then
				 VdTrimestreIni := to_date('01/10/' || pvAno, 'DD/MM/YYYY');
				 VdTrimestreFin := fnutil_last_day(to_date('01/12/' || pvAno, 'DD/MM/YYYY'));
				 vvTrimestreNome := trim(to_char(vdDataIni,'YYYY'))||'/'||trim(to_char(vdDataIni,'MM'))||'-4TR';
			end if;
			 if VdTrimestreIni = vdDataIni then
			 vvTrimestreTipo := 'S';
			 vnTrimestreNumero := vnTrimestreNumero + 1;
			 else
			 vvTrimestreTipo := 'N';
			 end if;

			vposicerro:='Recuperando periodo: Quadrimestre';
			if EXTRACT(MONTH FROM vdDataIni) >= 1 and EXTRACT(MONTH FROM vdDataIni) <= 4 then
				 VdQuadrimestreIni := to_date('01/01/' || pvAno, 'DD/MM/YYYY');
				 VdQuadrimestreFin := fnutil_last_day(to_date('01/04/' || pvAno, 'DD/MM/YYYY'));
				 vvQuadrimestreNome := trim(to_char(vdDataIni,'YYYY'))||'/'||trim(to_char(vdDataIni,'MM'))||'-1QD';
			elsif EXTRACT(MONTH FROM vdDataIni) >= 5 and EXTRACT(MONTH FROM vdDataIni) <= 8 then
				 VdQuadrimestreIni := to_date('01/05/' || pvAno, 'DD/MM/YYYY');
				 VdQuadrimestreFin := fnutil_last_day(to_date('01/08/' || pvAno, 'DD/MM/YYYY'));
				 vvQuadrimestreNome := trim(to_char(vdDataIni,'YYYY'))||'/'||trim(to_char(vdDataIni,'MM'))||'-2QD';
			elsif EXTRACT(MONTH FROM vdDataIni) >= 9 and EXTRACT(MONTH FROM vdDataIni) <= 12 then
				 VdQuadrimestreIni := to_date('01/09/' || pvAno, 'DD/MM/YYYY');
				 VdQuadrimestreFin := fnutil_last_day(to_date('01/12/' || pvAno, 'DD/MM/YYYY'));
				 vvQuadrimestreNome := trim(to_char(vdDataIni,'YYYY'))||'/'||trim(to_char(vdDataIni,'MM'))||'-3QD';
			end if;
			 if VdQuadrimestreIni = vdDataIni then
			 vvQuadrimestreTipo := 'S';
			 vnQuadrimestreNumero := vnQuadrimestreNumero + 1;
			 else
			 vvQuadrimestreTipo := 'N';
			 end if;

			vposicerro:='Recuperando periodo: Semestre';
			if EXTRACT(MONTH FROM vdDataIni) >= 1 and EXTRACT(MONTH FROM vdDataIni) <= 6 then
				 VdSemestreIni := to_date('01/01/' || pvAno, 'DD/MM/YYYY');
				 VdSemestreFin := to_date('30/06/' || pvAno, 'DD/MM/YYYY');
				 vvSemestreNome := trim(to_char(vdDataIni,'YYYY'))||'/'||trim(to_char(vdDataIni,'MM'))||'-1ST';
			elsif EXTRACT(MONTH FROM vdDataIni) >= 7 and EXTRACT(MONTH FROM vdDataIni) <= 12 then
				 VdSemestreIni := to_date('01/07/' || pvAno, 'DD/MM/YYYY');
				 VdSemestreFin := to_date('31/12/' || pvAno, 'DD/MM/YYYY');
				 vvSemestreNome := trim(to_char(vdDataIni,'YYYY'))||'/'||trim(to_char(vdDataIni,'MM'))||'-2ST';
			end if;
			 if VdSemestreIni = vdDataIni then
			 vvSemestreTipo := 'S';
			 vnSemestreNumero := vnSemestreNumero + 1;
			 else
			 vvSemestreTipo := 'N';
			 end if;

			 vposicerro:='Recuperando periodo: Ano';
			 VdAnoIni := to_date('01/01/' || pvAno, 'DD/MM/YYYY');
			 VdAnoFin := to_date('31/12/' || pvAno, 'DD/MM/YYYY');
			 vvAnoNome := trim(to_char(vdDataIni,'YYYY'));
			 vnAnoNumero := EXTRACT(YEAR FROM vdDataIni);
			 if VdAnoIni = vdDataIni then
					vvAnoTipo := 'S';
			 else
					vvAnoTipo := 'N';
			 end if;

			 vposicerro:='Achou ger_per';
			 select count(1)
				 into vAchou
				 from ger_per c
				where c.data_dia_inicial  = vdDataIni
					and c.unit_id     = pvUnitId
					and c.ger_per_tipo_id     = pvGerPerTipo;

			 if vAchou = 0 then

				 vposicerro:='Inserindo na tabela ger_per - Tipo Periodo['||pvGerPerTipo||'] Data['||to_char(vdDataIni,'YYYYMMDD')||']';

				 insert into ger_per
					 (id,                           unit_id,                   ger_per_tipo_id,
						data_dia_inicial,             data_dia_final,            dia_nome,          dia_numero,
						data_semana_inicial,          data_semana_final,         semana_nome,       semana_numero,
						data_quinzena_inicial,        data_quinzena_final,       quinzena_nome,     quinzena_numero,
						data_mes_inicial,             data_mes_final,            mes_nome,          mes_numero,
						data_bimestre_inicial,        data_bimestre_final,       bimestre_nome,     bimestre_numero,
						data_trimestre_inicial,       data_trimestre_final,      trimestre_nome,    trimestre_numero,
						data_quadrimestre_inicial,    data_quadrimestre_final,   quadrimestre_nome, quadrimestre_numero,
						data_semestre_inicial,        data_semestre_final,       semestre_nome,     semestre_numero,
						data_ano_inicial,             data_ano_final,            ano_nome,          ano_numero,
						dia_tipo,  		                semana_tipo,               quinzena_tipo,     mes_tipo, 
						bimestre_tipo,                trimestre_tipo,    				 quadrimestre_tipo, semestre_tipo, 
						ano_tipo,                     log_date_ins,              log_date_upd)
				 values
					 (uuid_generate_v4(),   pvUnitId,           pvGerPerTipo, 
						vdDataIni,            vdDataIni,          vvdianome,             vndianumero,
						vdsemanaini,          vdsemanafin,        vvsemananome,          vnsemananumero,
						vdquinzenaini,        vdquinzenafin,      vvquinzenanome,        vnquinzenanumero,
						vdmesini,             vdmesfin,           vvmesnome,             vnmesnumero,
						vdbimestreini,        vdbimestrefin,      vvbimestrenome,        vnbimestrenumero,
						vdtrimestreini,       vdtrimestrefin,     vvtrimestrenome,       vntrimestrenumero,
						vdquadrimestreini,    vdquadrimestrefin,  vvquadrimestrenome,    vnquadrimestrenumero,
						vdsemestreini,        vdsemestrefin,      vvsemestrenome,        vnsemestrenumero,
						vdanoini,             vdanofin,           vvanonome,             vnanonumero,
						vvDiaTipo,            vvSemanaTipo,       vvQuinzenaTipo,        vvMesTipo, 
						vvBimestreTipo,       vvTrimestreTipo,    vQuadrimestreTipo,     vvSemestreTipo, 
						vvAnoTipo,            now(),               now());

			vInseridos := vInseridos+1;

			else
				 vposicerro:='Atualizando na tabela ger_per - Tipo Periodo['||pvGerPerTipo||'] Data['||to_char(vdDataIni,'rrrrmmdd')||']';

				 update ger_per set
								data_dia_inicial=vdDataIni,                  data_dia_final=vdDataIni,                   dia_nome=vvdianome,                   dia_numero=vndianumero,
								data_semana_inicial=vdsemanaini,             data_semana_final=vdsemanafin,              semana_nome=vvsemananome,             semana_numero=vnsemananumero,
								data_quinzena_inicial=vdquinzenaini,         data_quinzena_final=vdquinzenafin,          quinzena_nome=vvquinzenanome,         quinzena_numero=vnquinzenanumero,
								data_mes_inicial=vdmesini,                   data_mes_final=vdmesfin,                    mes_nome=vvmesnome,                   mes_numero=vnmesnumero,
								data_bimestre_inicial=vdbimestreini,         data_bimestre_final=vdbimestrefin,          bimestre_nome=vvbimestrenome,         bimestre_numero=vnbimestrenumero,
								data_trimestre_inicial=vdtrimestreini,       data_trimestre_final=vdtrimestrefin,        trimestre_nome=vvtrimestrenome,       trimestre_numero=vntrimestrenumero,
								data_quadrimestre_inicial=vdquadrimestreini, data_quadrimestre_final=vdquadrimestrefin,  quadrimestre_nome=vvquadrimestrenome, quadrimestre_numero=vnquadrimestrenumero,
								data_semestre_inicial=vdsemestreini,         data_semestre_final=vdsemestrefin,          semestre_nome=vvsemestrenome,         semestre_numero=vnsemestrenumero,

								data_ano_inicial=vdanoini,                   data_ano_final=vdanofin,                    ano_nome=vvanonome,                   ano_numero=vnanonumero,
								dia_tipo=vvDiaTipo,
								semana_tipo=vvSemanaTipo,
								quinzena_tipo=vvQuinzenaTipo,
								mes_tipo=vvMesTipo,
								bimestre_tipo=vvBimestreTipo,
								trimestre_tipo=vvTrimestreTipo,
								quadrimestre_tipo=vvQuadrimestreTipo,
								semestre_tipo=vvSemestreTipo,
								ano_tipo=vvAnoTipo,

								log_date_upd=now()
					where data_dia_inicial  = vdDataIni
						and unit_id     = pvUnitId
						and ger_per_tipo_id     = pvGerPerTipo;

					 vAtualizados := vAtualizados+1;

			end if;
			 vdDataIni := vdDataIni + 1;
		end loop;
		
		--==============================
		select json_build_object(
						 'param', vparam,
						 'updated', vAtualizados,
						 'inserted', vInseridos) into vResultData;
	  select fnutil_result_json_create(200,vResultData ,'SUCCESS','Successfully processed') into vResult;
		return vResult;
		
		exception
			 when others then
				 begin
				    --==============================
				 		select json_build_object(
						 'param', vparam) into vResultData;
 					  select fnutil_result_json_create(
						 400,
						 vResultData,
						 'ERROR_PROCESS_BUSINESS',
						 vPosicErro||' - '||sqlerrm) into vResult;
						 return vResult;
				end;
          
end;
$BODY$
LANGUAGE plpgsql VOLATILE;

--================================================================
--Liberar acesso para todos usuários
--================================================================
--admin interno
delete from sys_group_program a where sys_group_id='4218d8f1-8595-4052-aace-ba36f772623e';
insert into sys_group_program(id,sys_group_id,sys_program_id)
select uuid_generate_v4(),'4218d8f1-8595-4052-aace-ba36f772623e', b.id
from sys_program b;
--admin unit
delete from sys_group_program a where sys_group_id='0256e515-51a4-49a2-a8b8-adc36470cd51';
insert into sys_group_program(id,sys_group_id,sys_program_id)
select uuid_generate_v4(),'0256e515-51a4-49a2-a8b8-adc36470cd51', b.id
from sys_program b where b.admin='N';
commit;

               """
    )


def downgrade():
    pass

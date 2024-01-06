package br.com.resultfacil.resultserver.exceptions;

import lombok.Getter;

@Getter
public enum ProblemType {

	INVALID_DATA("/invalid-data", "Dados inválidos"),
	ACCESS_DENIED("/access-denied", "Acesso negado"),
	ERROR_SYSTEM("/error-system", "Erro de sistema"),
	INVALID_PARAMETER("/invalid-parameter", "Parâmetro inválido"),
	INCOMPREHENSIBLE_MESSAGE("/incomprehensible-message", "Mensagem incompreensível"),
	RESOURCE_NOTFOUND("/resource-notfound", "Recurso não encontrado"),
	MODEL_IN_USE("/model-in-use", "Modelo em uso"),
	ERROR_BUSINESS("/error-business", "Violação de regra de negócio"),
	ERROR_DATABASE("/error-database", "Violação de regra de banco de dados"),
	ERROR_STORAGE("/error-storage", "Erro na opera de arquivos para storage"),
	ERROR_OAUTH2("/error-oauth2", "Violação de regra de oauth2"),
	ERROR_LOGIN("/error-login", "Violação de regra de login");
	
	
	private String title;
	private String uri;
	
    //TODO Colocar na properties
	ProblemType(String path, String title) {
		this.uri = "URL_API" + path;
		this.title = title;
	}
	
}

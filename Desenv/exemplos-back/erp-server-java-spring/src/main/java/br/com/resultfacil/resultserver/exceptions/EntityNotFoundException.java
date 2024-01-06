package br.com.resultfacil.resultserver.exceptions;

public class EntityNotFoundException extends BusinessException {

	private static final long serialVersionUID = 1L;

	public EntityNotFoundException(String message) {
		super(message.substring(message.lastIndexOf(".")+1, message.length()) );
	}
	
}
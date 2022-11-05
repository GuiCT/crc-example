# DIvisão modulo-2, utilizando XOR
def mod2div(dividend: int, divisor: int) -> int:
	# [2:] para ignorar o prefixo '0b'
	DIVIDEND_AS_BITS = bin(dividend)[2:]
	DIVISOR_AS_BITS = bin(divisor)[2:]

	# Tamanho do dividendo
	DIVIDEND_SIZE = len(DIVIDEND_AS_BITS)
	# Tamanho do divisor
	DIVISOR_SIZE = len(DIVISOR_AS_BITS)
	# Função que representa inteiro em binário com um digito a menos que o divisor.
	m_bin = lambda number: format(number, f'0{DIVISOR_SIZE - 1}b')
	# Número de digitos comparados depende da posição da divisão
	cursor = DIVISOR_SIZE

	# Cortando a parte importante do dividendo para um determinado passo
	dividend_slice = DIVIDEND_AS_BITS[0 : cursor]

	while cursor < DIVIDEND_SIZE:
		if dividend_slice[0] == '1': # Se o bit mais significativo for 1
			# Reliza XOR e puxa um bit
			dividend_slice = m_bin(divisor ^ int(dividend_slice, base=2)) + DIVIDEND_AS_BITS[cursor]

		else: # Se o bit mais significativo for 0
			# Utiliza uma máscara zerada para o XOR
			dividend_slice = m_bin(int('0'*cursor, base=2) ^ int(dividend_slice, base=2)) + DIVIDEND_AS_BITS[cursor]

		# Incrementando o cursor para o próximo passo
		cursor += 1

	# Tratamento para os últimos bits, para evitar overflow.
	# Não puxa mais 1
	if dividend_slice[0] == '1':
		dividend_slice = m_bin(divisor ^ int(dividend_slice, base=2))
	else:
		dividend_slice = m_bin(int('0'*cursor, base=2) ^ int(dividend_slice, base=2))

	remainder = dividend_slice
	return remainder

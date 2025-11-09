function gerarDigitoVerificador(cpf) {
  let soma1 = 0;
  for (let i = 0; i < 9; i++) {
    soma1 += parseInt(cpf[i]) * (10 - i);
  }

  let digito1 = soma1 % 11;
  if (digito1 === 0 || digito1 === 1) {
    digito1 = 0;
  } else {
    digito1 = 11 - digito1;
  }

  let soma2 = 0;
  for (let i = 0; i < 9; i++) {
    soma2 += parseInt(cpf[i]) * (11 - i);
  }
  soma2 += digito1 * 2;

  let digito2 = soma2 % 11;
  if (digito2 === 0 || digito2 === 1) {
    digito2 = 0;
  } else {
    digito2 = 11 - digito2;
  }

  console.log(
    `O CPF completo é: ${cpf.slice(0, 3)}.${cpf.slice(3, 6)}.${cpf.slice(6, 9)}-${digito1}${digito2}`
  );
  return `${digito1}${digito2}`;
}

function verificarCpf(cpf) {
  let digitoVerificador1 = parseInt(cpf[9]);
  let digitoVerificador2 = parseInt(cpf[10]);
  cpf = cpf.slice(0, 9);

  let soma1 = 0;
  for (let i = 0; i < 9; i++) {
    soma1 += parseInt(cpf[i]) * (10 - i);
  }

  let digito1 = soma1 % 11;
  if (digito1 === 0 || digito1 === 1) {
    digito1 = 0;
  } else {
    digito1 = 11 - digito1;
  }

  let soma2 = 0;
  for (let i = 0; i < 9; i++) {
    soma2 += parseInt(cpf[i]) * (11 - i);
  }
  soma2 += digito1 * 2;

  let digito2 = soma2 % 11;
  if (digito2 === 0 || digito2 === 1) {
    digito2 = 0;
  } else {
    digito2 = 11 - digito2;
  }

  if (digito1 === digitoVerificador1 && digito2 === digitoVerificador2) {
    console.log(
      `O CPF: ${cpf.slice(0, 3)}.${cpf.slice(3, 6)}.${cpf.slice(6, 9)}-${digito1}${digito2} é válido`
    );
    return "Válido";
  } else {
    console.log(
      `O CPF: ${cpf.slice(0, 3)}.${cpf.slice(3, 6)}.${cpf.slice(6, 9)}-${digito1}${digito2} não é válido`
    );
    return "Inválido";
  }
}

function validadorCpf(cpf) {
  // Remove tudo que não é número
  cpf = cpf.replace(/\D/g, "");

  let numeroDigitos = cpf.length;

  if (numeroDigitos < 9 || numeroDigitos > 11) {
    return "Inválido";
  }

  if (numeroDigitos === 9) {
    return gerarDigitoVerificador(cpf);
  }

  if (numeroDigitos === 11) {
    return verificarCpf(cpf);
  }
}

// Programa principal
const entradaUsuario = prompt("Entre com o número do CPF para validar:");
const resultado = validadorCpf(entradaUsuario);
console.log(resultado);

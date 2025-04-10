"""
3. Escreva um programa de autenticação que receba um nome de usuário e senha
( input ) informe se:

   * Autenticação foi bem-sucedida.
    *Se o nome de usuário não existe.
    *Se a senha está incorreta.
    
    Os valores corretos de nome de usuário e senha devem estar armazenados em
    constantes, como no exemplo abaixo:
    USUARIO = "admin"
    SENHA = "123123"
    nome_usuario = input("Digite o nome do usuário: "\n)
...

"""
usuario = 'admin'
senha = '123123'
nome_usuario = input('Digite o nome de usúario: ')
senha_usuario = input('Digite sua senha: ')

if nome_usuario != usuario:
    print('Usúario não existe')
elif senha != senha_usuario:
    print('Senha está incorreta')
else:
    print('Autenticação bem-sucedida!')
    
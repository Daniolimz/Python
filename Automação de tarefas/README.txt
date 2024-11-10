Programa de automação de pesquisa no instagram do pefil Elon Musk

# passo 1: solicitar usuario.
# passo 2: solicitar senha - não aparecer a senha quando estiver digitando
# passo 3: entrar no site do instagram.
# passo 4: fazer login com usuario e senha solicitados.
# passo 5: clicar no agora não salvar informações de login.
# passo 6: mensagem "usuario ou senha incorreto" caso usuario ou senha estejão errados e Loop para solicitar informações novamente até conseguir realizar login com sucesso.
# passo 7: Mensagem "Realizado login com sucesso" quando as informações estiverem corretas.
# passo 8: criptografar e gravar usuario e senha caso informações estejão corretas.
# passo 9: Fechar janela.
# passo 10: Fazer login com usuario e senha gravados
# passo 11: clicar no agora não salvar informações de login.
# passo 12: clicar no agora não da notificação
# passo 13: clicar na barra de pesquisa
# passo 14: digitar elon musk
# passo 15: clicar no perfil  elon musk
# passo 16: Fechar janela.

Principais trechos:
 Ocultação de senha: getpass.getpass() é utilizado para solicitar a senha sem exibi-la no terminal.
 Criptografia: O cryptography.fernet criptografa e armazena as credenciais em um arquivo.
 Login automático e tratamento de erro: O Selenium tenta fazer login, verifica se houve erro e repete a solicitação de credenciais se necessário.
 Navegação e Interações: Após o login, o código interage com os elementos de "Agora não", notificação, pesquisa e perfil.

Lembre-se de substituir webdriver.Chrome() por outro driver compatível, se você estiver usando um navegador diferente
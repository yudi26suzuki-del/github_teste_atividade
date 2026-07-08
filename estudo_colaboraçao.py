/

//==========================================================//
//                        GIT - RESUMO                       //
//==========================================================//

// O que é Git?
// Git é um sistema de controle de versão que permite registrar
// alterações em um projeto, recuperar versões anteriores e
// facilitar o trabalho em equipe.

//==========================================================//
//                  INICIANDO UM PROJETO                    //
//==========================================================//

// Inicializa um repositório Git
git init

// Verifica o estado do projeto
git status

//==========================================================//
//                     ADICIONANDO ARQUIVOS                  //
//==========================================================//

// Adiciona um arquivo específico
git add arquivo.py

// Adiciona todos os arquivos modificados
git add .

//==========================================================//
//                         COMMIT                            //
//==========================================================//

// Salva uma versão do projeto
git commit -m "Mensagem do commit"

// Exemplo
git commit -m "Criando sistema de login"

//==========================================================//
//                     HISTÓRICO                             //
//==========================================================//

// Mostra todos os commits
git log

// Mostra os commits de forma resumida
git log --oneline

//==========================================================//
//                        BRANCHES                           //
//==========================================================//

// Branch = uma linha de desenvolvimento separada da principal.

// Ver todas as branches
git branch

// Criar uma nova branch
git branch nome-da-branch

// Criar e entrar na branch (forma moderna)
git switch -c nome-da-branch

// Criar e entrar na branch (forma antiga)
git checkout -b nome-da-branch

// Trocar de branch
git switch nome-da-branch

// ou
git checkout nome-da-branch

// Voltar para a branch principal
git switch main

//==========================================================//
//                    JUNTANDO BRANCHES                      //
//==========================================================//

// Primeiro entre na branch principal
git switch main

// Junta outra branch na atual
git merge nome-da-branch

//==========================================================//
//                    EXCLUINDO BRANCHES                     //
//==========================================================//

// Exclui uma branch
git branch -d nome-da-branch

// Força a exclusão
git branch -D nome-da-branch

//==========================================================//
//                 REPOSITÓRIO REMOTO (GitHub)               //
//==========================================================//

// Adiciona um repositório remoto
git remote add origin URL_DO_REPOSITORIO

// Verifica os repositórios configurados
git remote -v

//==========================================================//
//                     ENVIANDO PARA O GITHUB                //
//==========================================================//

// Primeiro envio
git push -u origin main

// Explicação:
// git push -> envia os commits
// -u -> cria a ligação entre a branch local e a remota
// origin -> nome do repositório remoto
// main -> branch enviada

// Depois do primeiro envio basta usar
git push

//==========================================================//
//                  BAIXANDO ALTERAÇÕES                      //
//==========================================================//

// Atualiza o projeto com alterações do GitHub
git pull

// Apenas busca as alterações
git fetch

//==========================================================//
//                    CLONANDO UM PROJETO                    //
//==========================================================//

git clone URL_DO_REPOSITORIO

//==========================================================//
//                  VER ALTERAÇÕES                           //
//==========================================================//

// Mostra as diferenças antes do commit
git diff

//==========================================================//
//                 DESFAZENDO ALTERAÇÕES                     //
//==========================================================//

// Descarta alterações de um arquivo
git restore arquivo.py

// Descarta alterações de todos os arquivos
git restore .

// Remove arquivos da área de staging
git restore --staged .

//==========================================================//
//                 FLUXO MAIS UTILIZADO                      //
//==========================================================//

// 1. Verificar alterações
git status

// 2. Adicionar arquivos
git add .

// 3. Criar um commit
git commit -m "Descrição"

// 4. Enviar para o GitHub
git push

//==========================================================//
//              FLUXO UTILIZANDO BRANCHES                    //
//==========================================================//

// Criar uma branch
git switch -c nova-funcionalidade

// Fazer alterações...

// Salvar alterações
git add .
git commit -m "Nova funcionalidade"

// Voltar para a principal
git switch main

// Juntar a branch
git merge nova-funcionalidade

// Enviar para o GitHub
git push

//==========================================================//
//                   COMANDOS MAIS IMPORTANTES               //
//==========================================================//

// git init                 -> Inicializa um repositório
// git status               -> Verifica alterações
// git add .                -> Adiciona todos os arquivos
// git commit -m "msg"      -> Cria um commit
// git log --oneline        -> Histórico resumido
// git branch               -> Lista as branches
// git switch -c nome       -> Cria e entra em uma branch
// git switch nome          -> Troca de branch
// git merge nome           -> Junta branches
// git push                 -> Envia alterações
// git pull                 -> Baixa alterações
// git clone URL            -> Clona um repositório
// git diff                 -> Mostra diferenças
// git restore .            -> Descarta alterações

//==========================================================//
//                         RESUMO                            //
//==========================================================//

// Git controla versões do projeto.
// Commit = salva uma versão.
// Branch = cria uma linha de desenvolvimento separada.
// Merge = junta branches.
// Push = envia para o GitHub.
// Pull = baixa alterações do GitHub.
// Clone = copia um projeto existente.
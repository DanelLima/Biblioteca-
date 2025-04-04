# id
# id_livro
# id_usuario
# data_devolucao
# situacao

class Emprestimo:
    def __init__(self, id, id_livro, id_usuario, data_devolucao, situacao):
        self._id = id # Usar underline para indicar atributo "privado"
        self._id_livro = id_livro 
        self._id_usuario = id_usuario
        self._data_devolucao = data_devolucao
        self._situacao = situacao
        
    def __str__(self):
        return f"ID: {self._id} | Livro: {self._id_livro} | Usuário: {self._id_usuario} | Devolução: {self._data_devolucao} | Situação: {self._situacao}"

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, novo_id):
        self._id = novo_id
                
    @property
    def id_livro(self):
        return self._id_livro

    @id_livro.setter
    def id_livro(self, novo_id_livro):
        self._id_livro = novo_id_livro

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, novo_id_usuario):
        self._id_usuario = novo_id_usuario

    @property
    def data_devolucao(self):
        return self._data_devolucao

    @data_devolucao.setter
    def data_devolucao(self, novo_data_devolucao):
        self._data_devolucao = novo_data_devolucao
        
    @property
    def situacao(self):
        return self._situacao

    @situacao.setter
    def situacao(self, novo_situacao):
        self._situacao = novo_situacao

    def to_string(self):
        # Conversão do emprestimo em string para salvar no txt
        return f"{self._id};{self._id_livro};{self._id_usuario};{self._data_devolucao};{self._situacao}"

    @staticmethod
    def from_string(string):
        # Cria um objeto Emprestimo de uma string
        id, id_livro, id_usuario, data_devolucao, situacao = string.strip().split(";")
        return Emprestimo(id, id_livro, id_usuario, data_devolucao, situacao)

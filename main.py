import cliente_model
from cliente_repository import ClienteRepository

cliente_model = cliente_model.Cliente("Deiva", 45)

ClienteRepository.listar_clientes()
ClienteRepository.inserir_cliente(cliente_model)


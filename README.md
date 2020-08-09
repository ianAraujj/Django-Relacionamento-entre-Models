# Django-Relacionamento-entre-Models
Django: Aplicando todos os tipos de relacionamento nos Models

## Relacionamento 1 para 1:

class Endereco(models.Model):
        # Definimos seus atributos

class Cliente(models.Model):
        # Definimos seus atributos
      endereco = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)
      
O ```OneToOneField``` deve ficar na classe dependente. Ou seja, existe Endereço sem cliente, mas não existe Cliente sem endereço

## Relacionamento 1 para N:

class Pedido(models.Model):
    STATUS_CHOICES = (
        ("P", "Pedido realizado"),
        ("F", "Fazendo"),
        ("E", "Saiu para entrega"),
    )
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE, related_name='pedidos')
    observacoes = models.CharField(max_length=300, null=False, blank=False)
    data_pedido = models.DateTimeField(default=timezone.now)
    valor = models.FloatField(blank=False, null=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=False, null=False)

    def __str__(self):
        return self.cliente.nome

class Cliente(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )

    nome = models.CharField(max_length=100, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    profissao = models.CharField(max_length=50, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
    endereco = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)

O ```ForeignKey``` deve ficar no lado do MUITOS. Ou seja, um cliente tem N pedidos e cada pedido está relacionado por um Cliente.

## Relacionamento N para N

class Produto(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.CharField(max_length=200, null=False, blank=False)
    valor = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    STATUS_CHOICES = (
        ("P", "Pedido realizado"),
        ("F", "Fazendo"),
        ("E", "Saiu para entrega"),
    )
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE, related_name='pedidos')
    observacoes = models.CharField(max_length=300, null=False, blank=False)
    data_pedido = models.DateTimeField(default=timezone.now)
    valor = models.FloatField(blank=False, null=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=False, null=False)
    produtos = models.ManyToManyField(Produto)

    def __str__(self):
        return self.cliente.nome

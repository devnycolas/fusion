import uuid
from django.db import models
from stdimage.models import StdImageField

def get_file_path(_instace, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

# Create your models here.
class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Servico(Base):
    ICONE_CHOISES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descricao', max_length=200)
    icone = models.CharField('Icone', max_length=12, choices=ICONE_CHOISES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico
    

class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo
    

class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models .TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome
    
class Recurso(Base):
    ICONE_CHOISES = (
        ('lni-rocket','Foguete'),
        ('lni-laptop-phone','Laptop'),
        ('lni-cog','Engrenagem'),
        ('lni-leaf','Folha'),
        ('lni-layers','Multi Camadas'),
    )
    recurso = models.CharField('Recurso', max_length=100)
    descricao = models.TextField('Descricao', max_length=200)
    icone = models.CharField('Icone', max_length=20, choices=ICONE_CHOISES)

    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'

    def __str__(self):
        return self.recurso
    

class Plano(Base):
    ICONE_CHOISES = (
        ('lni-package','Caixa'),
        ('lni-drop','Gota de Água'),
        ('lni-star','Estrela'),
    )

    USER_CHOICES = [(str(i), str(i)) for i in range(1, 11)] + [('ilimitado', 'Ilimitado')]
    STORAGE_CHOICES = [(str(i), str(i)) for i in range(10, 51, 10)] + [('ilimitado', 'Ilimitado')]

    icone = models.CharField('Icone', max_length=15, choices=ICONE_CHOISES)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    plano = models.CharField('plano', max_length=100)
    usuarios = models.CharField('Usuários', max_length=10, choices=USER_CHOICES)
    armazenamento = models.CharField('Armazenamento', max_length=10, choices=STORAGE_CHOICES)
    suporte = models.CharField('Suporte', max_length=100)
    atualizacoes = models.CharField('Atualizações', max_length=100)
    

    class Meta:
        verbose_name = "Plano"
        verbose_name_plural = "Planos"
    
    def __str__(self):
        return self.plano
    
class Cliente(Base):
    AVALIACAO_CHOICES = [(i, str(i)) for i in range(1, 6)]

    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    descricao = models.TextField('Descricao', max_length=200)
    avaliacao = models.IntegerField('Avaliação', choices=AVALIACAO_CHOICES)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nome

# coding=utf-8


from django.db import models
from todo_list.managers.item_list_manager import Item_list_manager


class Item_list(models.Model):
    """Model do crud dos itens
        Variavei:
        (1) cod_item: Codigo do item salvo
        (2) nm_item: Nome do item salvo
        (3) sn_ativo: Campo por responsavel por ativar ou desativar a opção de tarefa feita
    """
    cod_item = models.AutoField(primary_key=True)
    nm_item = models.CharField('Nome', max_length=30, null=False)
    descricao = models.TextField('Descricao', max_length=100, null=False)
    sn_feito = models.BooleanField('Feito', default=False)

    objects = Item_list_manager()

    def __unicode__(self):
        return self.nm_item

    class Meta:
        app_label = 'todo_list'
        verbose_name = 'To-Do List'
        verbose_name_plural = 'To-Do List'

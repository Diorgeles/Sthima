# coding: utf-8
from django.db import models


class Item_list_manager(models.Manager):
    """Classe responsavel pelo encapsulamento do Crud"""
    def Inserir(self, nm_item, descricao, sn_feito):
        return self.get_queryset().create(nm_item=nm_item, descricao=descricao, sn_feito=sn_feito)

    def Update(self, cod_item, nm_item, descricao, sn_feito):
        return self.get_queryset().filter(cod_item=cod_item).update(nm_item=nm_item, descricao=descricao, sn_feito=sn_feito)

    def Delete(self, cod_item):
        print(cod_item)
        return self.get_queryset().filter(cod_item=cod_item).delete()
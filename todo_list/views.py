# coding:utf-8
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from todo_list.models.item_list import Item_list


def item_insert(nm_item, descricao):
    """Função responsável por inserir novos items"""
    Item_list.objects.Inserir(nm_item, descricao, False)
    return True


def item_update(cod_item, nm_item, descricao, sn_feito):
    """Função responsável por atualizar as informações dos itens"""
    Item_list.objects.Update(cod_item, nm_item, descricao, sn_feito)
    return True


def item_delete(cod_item):
    """Função responsável por deletar informações"""
    Item_list.objects.Delete(cod_item)
    return True


def todo_list(request):
    """Função responsável por gerenciar a telade itens"""
    itens_list = Item_list.objects.all()
    if request.method == 'POST':
        print(request.POST)
        if 'btn_modal_grupo_novo' in request.POST:
            item_insert(request.POST['nm_item'], request.POST['descricao'])
            return HttpResponseRedirect(reverse('todolist:todo_list'))

        elif 'btn_modal_grupo_edite' in request.POST:
            sn_feito = True if request.POST['sn_feito'] == "1" else False
            item_update(request.POST['cod_item'], request.POST['nm_item'],
                        request.POST['descricao'], sn_feito)
            return HttpResponseRedirect(reverse('todolist:todo_list'))

        elif 'btn_item_delete' in request.POST:
            item_delete(request.POST['cod_item'])
            return HttpResponse(reverse('todolist:todo_list'))
    return render(request, 'todo_list.html', locals())

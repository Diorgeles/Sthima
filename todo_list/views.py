# coding:utf-8
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from todo_list.models.item_list import Item_list
import json


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
    """Função responsável por gerenciar a tela de itens
        Foi usado o cache do navegador para que a aplicação
        funcionasse de forma didatica, vale ressaltar que esta 
        não é a melhor forma de fazer tal ação.

        O cache serve para salvar a posição atual da lista de tarefas,
        como o usuário pode muda-la dinamicamente fiz tal solução 
        para resoler o problema.
    """
    if len(request.session.get('ordem_atual')):
        itens_list = []
        ordem_salva = request.session.get('ordem_atual')        
        for i in ordem_salva:
            for item in Item_list.objects.filter(cod_item=i):
                itens_list.append(
                    {'cod_item': item.cod_item, 'nm_item': item.nm_item, 
                    'descricao': item.descricao, 'sn_feito': item.sn_feito})

    else:
        itens_list = Item_list.objects.all()
    if request.method == 'POST':
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
        else:
            # A cada mudança de ordenação eu mando uma requisição ajax informando 
            # a nova ordem da lista, caso o usuário recarregue a pagina a lista não 
            # perderá a ultima posição
            ordem = []
            if len(json.loads(request.POST['item'])):
                for i in json.loads(request.POST['item']):
                    ordem.append(i["#"])
                request.session['ordem_atual'] = ordem
    return render(request, 'todo_list.html', locals())

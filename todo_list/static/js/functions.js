$(document).ready(function () {
    $( "tbody" ).sortable({
        helper: fixWidthHelper
    }).disableSelection();

    function fixWidthHelper(e, ui) {
        ui.children().each(function() {
            $(this).width($(this).width());
        });
        return ui;
    }
    $('#item_edite').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget);
        var cod_item = button.data('item');
        var nm_item = button.data('nome');
        var descricao = button.data('descricao');
        var sn_feito = button.data('feito');
        var modal = $(this);
        modal.find('#cod_item').val(cod_item);
        modal.find('#nm_item').val(nm_item);
        modal.find('#descricao').val(descricao);
        modal.find('#sn_feito option').removeAttr('selected');
        modal.find('#sn_feito option[value=' + sn_feito + ']').attr('selected', 'selected');
    });


    function msg_erro() {
        BootstrapDialog.show({
            title: "Atenção",
            message: "Ocorreu algum erro durante o processo.",
            buttons: [{
                label: 'OK',
                cssClass: 'btn-danger',
                action: function () {
                    $.each(BootstrapDialog.dialogs, function (id, dialog) {
                        dialog.close();
                    });
                }
            }]
        });
    }

    function msg_delete_item() {
        BootstrapDialog.show({
            title: 'Salvando',
            message: ("<h4 class='text-center'>Excluindo tarefa...</h4>"),
            closable: false,
        })
    }


    $(".delete_item").click(function () {
        $.ajax({
            type: 'POST',
            data: { csrfmiddlewaretoken: $.cookie('csrftoken'), cod_item: $(this).data('item'), btn_item_delete: '' },
            url: "/todolist/delete_item/",
            dataType: "text",
            beforeSend: function () {
                msg_delete_item();
            },
            success: function (data) {                
                location.href = data;
            },
            error: function () {
                msg_erro();
            }
        });
    });
});
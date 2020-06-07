<template>
     <div class="modal fade" id="id_cliente_detail" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Cliente: {{ reserva_open_detail.cliente }}</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <img src="/media/logos/estady.png" width="140px" height="140px" alt="..." class="img-thumbnail">
                <table class="table">
                    <thead>
                        <tr>
                        <th scope="col">#</th>
                        <th scope="col">Hora de ingreso</th>
                        <th scope="col">Ingreso</th>
                        <th scope="col">Salida</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <th scope="row">{{ reserva_open_detail.id }}</th>
                            <th scope="row">{{ reserva_open_detail.hora_ingreso }}</th>
                            <td>{{ reserva_open_detail.fecha_ingreso | format_date }}</td>
                            <td>{{ reserva_open_detail.fecha_salida | format_date }}</td>
                        </tr>
                    </tbody>
                    </table>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal"><i class="fa fa-times"></i></button>
                    <button @click="abrirCobranza(reserva_open_detail.id)" type="button" class="btn btn-primary"><i class="fa fa-usd"></i> </button>
                </div>
                </div>
            </div>
        </div>
</template>

<script>


import {format_date} from '@/libs/filters.js'

export default {
    data(){
        return{
        }
    },
    mounted(){
        
    },
    methods: {
        abrirCobranza(reserva_id){
            window.location.href = '/reservas/cobrar/' + reserva_id
        }
    },
    props: {
        reserva_open_detail:{ //<-- props get reserva 
            required: true 
        }
    },
    filters: {
        format_date
    }
}
</script>
<template>
     <div class="x_panel">
        <div class="x_title">
        <h2>Lista de Pedidos</h2>
        <ul class="nav navbar-right panel_toolbox">
            <li><a class="collapse-link"><i class="fa fa-chevron-up"></i></a>
            </li>
            <li class="dropdown">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false"><i class="fa fa-wrench"></i></a>
            <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                
            </div>
            </li>
            <li><a class="close-link"><i class="fa fa-close"></i></a>
            </li>
        </ul>
        <div class="clearfix"></div>
        </div>
        <div class="x_content">
        <br />
        <table class="table table-striped">
                <thead>
                <tr>
                    <th>Cantidad</th>
                    <th>Descripcion</th>
                    <th>Precio Compra</th>
                    <th>Total</th>
                    <th>Acción</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="(pedido, index) in get_articulos_pedidos" :key="pedido.id">
                    <th scope="row" v-text="pedido.cantidad"></th>
                    <td v-text="pedido.descripcion"></td>
                    <td v-text="'$' + pedido.precio_compra"></td>
                    <td v-text="'$' + pedido.total"></td>
                    <td><button @click="delete_pedidos_articulos(index)" class="btn btn-danger"><i class="fa fa-trash"></i></button></td>
                </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>

import {mapGetters, mapActions} from 'vuex'

export default {
    data(){
        return{

        }
    },
    methods: {
        ...mapActions(['delete_pedidos_articulos'])
    },
    computed: {
        ...mapGetters(['get_articulos_pedidos'])
    }
}
</script>
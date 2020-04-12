<template>
    <div>
        <b-modal id="modalPopover" title="Lista de clientes" hide-footer>
         <input class="form-control" placeholder="buscar un cliente">
         <table class="table table-striped">
                      <thead>
                        <tr>
                          <th>#</th>
                          <th>Nombre</th>
                          <th>Apellido</th>
                          <th>Documento</th>
                        </tr>
                      </thead>
                      <tbody>
                          <template v-for="cliente in get_clientes">
                            <tr :key="cliente.id">
                            <th scope="row" v-text="cliente.id"></th>
                            <td v-text="cliente.nombre"></td>
                            <td v-text="cliente.apellido"></td>
                            <td v-text="cliente.numero_documento"></td>
                            </tr>
                          </template>
                      </tbody>
                    </table>

        </b-modal>
    </div>
</template>

<script>

import {mapActions, mapGetters} from 'vuex'

export default {
    data(){
        return{

        }
    }, 
    methods: {
        ...mapActions(['set_clientes'])
    },
    mounted(){
        this.set_clientes();
    },
    computed: {
        ...mapGetters(['get_clientes'])
    }
}
</script>
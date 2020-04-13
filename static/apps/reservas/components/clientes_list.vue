<template>
    <div>
        <b-modal id="modalPopover" title="Lista de clientes" hide-footer>
            <input v-model="buscador" class="form-control" placeholder="buscar un cliente">
            <template v-if="get_clientes.length == 0">
                <b-alert show variant="error">No existen registros</b-alert>
            </template>
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
                        <tr @click="selected(cliente)" :key="cliente.id">
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
            buscador : ''
        }
    }, 
    methods: {
        ...mapActions(['set_clientes', 'set_buscador']),
        selected(cliente){
            this.$emit('selected', cliente);
            this.$bvModal.hide('modalPopover')	
        }
    },
    mounted(){
        this.set_clientes();
    },
    computed: {
        ...mapGetters(['get_clientes'])
    },
    watch: {
        buscador(value){
            this.set_buscador(value);
        }
    }
}
</script>
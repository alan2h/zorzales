<template>
    <div>
        <b-button v-b-modal.modal-1><i class="fa fa-search"></i></b-button>

        <b-modal id="modal-1" title="BootstrapVue">
            <p class="my-4">Hello from modal!</p>
        </b-modal>
    </div>
</template>

<script>
export default {
    data(){
        return{
            
        }
    }
}
</script>
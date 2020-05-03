<template>
    <div class="col-sm-3" >
        <img src="/media/logos/cabania_ocupada.jpeg" width="240px" height="240px" alt="..." class="img-thumbnail">
        <button class="btn btn-success"><i class="fa fa-search">reserva</i></button>
        <button class="btn btn-success"><i class="fa fa-search">Inventario</i></button>
    </div>
</template>

<script>
export default {
    data(){
        return{

        }
    },
    mounted(){
        console.log(this.cabania)
        
    },
    props: {
        cabania: {
            type: Object,
            required: true
        }
    }
}
</script>
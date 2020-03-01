<template>
     <div class="x_panel">
        <div class="x_title">
        <h2>Precio Total .- </h2>
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
            
             <div class="form-group row">
                <label class="control-label col-md-3" for="first-name">Total a pagar <span class="required">*</span>
                </label>
                <div class="col-md-7">
                    <input v-model="total" type="text" required="required" class="form-control col-md-12 ">
                </div>
            </div>

            <div class="ln_solid"></div>
            <div class="form-group">
              <div class="col-md-9 col-sm-9  offset-md-3">
                <a  href="#" type="button" class="btn btn-primary">Cancelar</a>
                <button type="button" class="btn btn-success">Guardar</button>
              </div>
            </div>

        </div>
    </div>
</template>

<script>

import {mapGetters} from 'vuex'

export default {
    data(){
        return{
            total: 0.0
        }
    },
    computed:{
        ...mapGetters(['get_total'])
    },
    watch: {
        get_total(value){
            this.total = value;
        }
    }
}
</script>
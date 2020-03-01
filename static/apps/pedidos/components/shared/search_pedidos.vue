<template>
    <div class="x_panel">
        <div class="x_title">
        <h2>Buscar Artículos</h2>
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
        
        <form class="form-horizontal form-label-left">
            <div class="form-group row">
            <label class="control-label col-md-3" for="first-name">Código de barras <span class="required">*</span>
            </label>
            <div class="col-md-7">
                <input type="text" id="first-name2" required="required" class="form-control col-md-12 ">
            </div>
            <!-- controles adicionales  -->
            <articulos_list></articulos_list>
            <!-- controles adicionales  -->
            </div>
            
        </form>
        </div>
    </div>
</template>

<script>

import articulos_list from './articulos_list.vue'

export default {
    data(){
        return{

        }
    },
    components: {
        articulos_list
    }
}
</script>
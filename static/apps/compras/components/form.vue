<template>
        <div class="row">
              <div class="col-md-12 col-sm-12 ">
                <div class="x_panel">
                  <div class="x_title">
                    <h2>Cargar una Compra</h2>
                    <ul class="nav navbar-right panel_toolbox">
                      <li><a class="collapse-link"><i class="fa fa-chevron-up"></i></a>
                      </li>
                      <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false"><i class="fa fa-wrench"></i></a>
                       
                      </li>
                      <li><a class="close-link"><i class="fa fa-close"></i></a>
                      </li>
                    </ul>
                    <div class="clearfix"></div>
                  </div>
                  <div class="x_content">
                    <br />
                    <form id="demo-form2" data-parsley-validate class="form-horizontal form-label-left">
                            
                            <!-- controles -->
                              <div class="item form-group">
                                  <label class="col-form-label col-md-3 col-sm-3 label-align" >Pedido <span class="required">*</span>
                                  </label>
                                  <div class="col-md-6 col-sm-6 ">
                                     <select class="form-control">
                                        <option value="">--</option>
                                     </select>
                                  </div>
                              </div>
                            <!-- controles -->

                            <!-- botones -->
                              <div class="ln_solid"></div>
                              <div class="item form-group">
                                  <div class="col-md-6 col-sm-6 offset-md-3">
                                  <button @click="cancelar" class="btn btn-secondary" type="button"><i class="fa fa-times"></i></button>
                                  <button  type="submit" class="btn btn-primary"><i class="fa fa-floppy-o"></i></button>
                                  </div>
                              </div>
                             <!-- botones -->

                    </form>
                  </div>
                </div>
              </div>
            </div>

</template>

<script>

import {mapGetters, mapActions} from 'vuex';

export default {
    data(){
        return{

        }
    },
    methods: {
      cancelar(){
        this.$router.push('/')
      }
    }
}
</script>
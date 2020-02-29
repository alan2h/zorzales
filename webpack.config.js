const path = require('path');
const VueLoaderPlugin = require('vue-loader/lib/plugin')


module.exports = {
    mode: "development",
    entry : {
        pedidos: './static/apps/pedidos/index.js',
      },
      // salidas de mis js
      output: {
        path: path.join(__dirname, "./static/dist/js"),
        filename: '[name].js'
      },
      watch: true,
      module: {
        rules: [
          // ... other rules
          {
            test: /\.vue$/,
            loader: 'vue-loader'
          }
        ]
      },
      plugins: [
        // make sure to include the plugin!
        new VueLoaderPlugin()
      ],
      resolve: {
        alias: {
          'vue$': 'vue/dist/vue.esm.js',
        },
      },
};
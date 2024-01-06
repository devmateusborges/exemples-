const mix = require("laravel-mix");

mix
  .js("resources/js/app.js", "public/js")
  .postCss("resources/css/app.css", "public/css", [
    //
  ]).version()
  .options({
    hmrOptions: {
      host: 'localhost',  // mysite.test is my local domain used for testing
      port: 8080,
    }
  })
  .vue({ version: 3 })
  .alias({ "@": "resources/js" })
  .webpackConfig((webpack) => {
    return {
      plugins: [
        new webpack.DefinePlugin({
          __VUE_OPTIONS_API__: true,
          __VUE_PROD_DEVTOOLS__: false,
        }),
      ],
    };
  });
